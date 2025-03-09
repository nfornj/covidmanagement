from celery import shared_task
import requests
import json
import time
import datetime
import logging
import asyncio
import aiohttp
from asgiref.sync import sync_to_async
from django.conf import settings

from .models import State, District, VaccinationCenter, VaccinationSession

# Configure logging
logger = logging.getLogger(__name__)

@shared_task
def populate_states_and_districts():
    """
    Task to populate states and districts from the CoWIN API.
    """
    try:
        # API endpoints
        states_url = "https://cdn-api.co-vin.in/api/v2/admin/location/states"
        
        # Headers to mimic a browser request
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
        }
        
        # Get states
        states_response = requests.get(states_url, headers=headers)
        states_data = states_response.json()
        
        # Process states
        for state in states_data.get('states', []):
            state_obj, created = State.objects.update_or_create(
                state_id=state['state_id'],
                defaults={'name': state['state_name']}
            )
            
            # Get districts for this state
            districts_url = f"https://cdn-api.co-vin.in/api/v2/admin/location/districts/{state['state_id']}"
            districts_response = requests.get(districts_url, headers=headers)
            districts_data = districts_response.json()
            
            # Process districts
            for district in districts_data.get('districts', []):
                District.objects.update_or_create(
                    district_id=district['district_id'],
                    state=state_obj,
                    defaults={'name': district['district_name']}
                )
            
            # Sleep to avoid rate limiting
            time.sleep(0.5)
        
        return f"Successfully populated {State.objects.count()} states and {District.objects.count()} districts"
    
    except Exception as e:
        logger.error(f"Error in populate_states_and_districts: {str(e)}")
        return f"Error: {str(e)}"

async def fetch_vaccination_data(session, url, district_id):
    """
    Fetch vaccination data for a district from the CoWIN API.
    """
    try:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                return data, district_id
            else:
                logger.warning(f"Failed to fetch data for district {district_id}: {response.status}")
                return None, district_id
    except Exception as e:
        logger.error(f"Error fetching data for district {district_id}: {str(e)}")
        return None, district_id

@sync_to_async
def process_vaccination_data(data, district_id):
    """
    Process vaccination data and save to database.
    """
    if not data or 'centers' not in data:
        return 0
    
    try:
        district = District.objects.get(district_id=district_id)
        count = 0
        
        for center in data['centers']:
            # Create or update vaccination center
            center_obj, _ = VaccinationCenter.objects.update_or_create(
                name=center['name'],
                district=district,
                defaults={
                    'address': center.get('address', ''),
                    'pincode': center.get('pincode', '')
                }
            )
            
            # Process sessions
            for session in center.get('sessions', []):
                try:
                    session_date = datetime.datetime.strptime(session['date'], '%d-%m-%Y').date()
                    
                    # Determine status based on capacity
                    if session['available_capacity'] > 0:
                        status = 'AVAILABLE'
                    else:
                        status = 'BOOKED'
                    
                    # Create or update vaccination session
                    VaccinationSession.objects.update_or_create(
                        center=center_obj,
                        date=session_date,
                        vaccine=session['vaccine'],
                        min_age_limit=session.get('min_age_limit', 18),
                        defaults={
                            'available_capacity': session['available_capacity'],
                            'status': status
                        }
                    )
                    count += 1
                except Exception as e:
                    logger.error(f"Error processing session: {str(e)}")
        
        return count
    except District.DoesNotExist:
        logger.error(f"District with ID {district_id} does not exist")
        return 0
    except Exception as e:
        logger.error(f"Error processing data for district {district_id}: {str(e)}")
        return 0

async def fetch_all_districts(districts, date_str):
    """
    Fetch vaccination data for all districts concurrently.
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
    }
    
    async with aiohttp.ClientSession(headers=headers) as session:
        tasks = []
        for district in districts:
            url = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={district.district_id}&date={date_str}"
            tasks.append(fetch_vaccination_data(session, url, district.district_id))
        
        results = await asyncio.gather(*tasks)
        
        # Process results
        processing_tasks = []
        for data, district_id in results:
            if data:
                processing_tasks.append(process_vaccination_data(data, district_id))
        
        processed_counts = await asyncio.gather(*processing_tasks)
        return sum(processed_counts)

@shared_task
def download_vaccination_data():
    """
    Main task to download vaccination data for all districts.
    """
    try:
        # Get all districts or a subset if needed
        districts = District.objects.all()
        
        # Format date for API (DD-MM-YYYY)
        today = datetime.datetime.now().strftime('%d-%m-%Y')
        
        # Run the async function
        result = asyncio.run(fetch_all_districts(districts, today))
        
        return f"Successfully processed {result} vaccination sessions"
    
    except Exception as e:
        logger.error(f"Error in download_vaccination_data: {str(e)}")
        return f"Error: {str(e)}"