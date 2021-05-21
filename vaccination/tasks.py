from vaccination.modules.utils.duplicates import removeDuplicates
from celery import shared_task
import requests
import json
import time
from datetime import datetime, timedelta
#from celery import vaccination
from django.apps import apps
from vaccination.modules.utils.sendemail import sendemail
from django.db.models import Count, Max
import asyncio
import aiohttp
from cffi.backend_ctypes import xrange
from asgiref.sync import sync_to_async
import redis
import pandas as pd
pd.set_option('display.max_columns', 500)

from .modules.config.tableobjects import stateobject


def populate_vaccination_state(df):

    for index, row in df.iterrows():
        print(row['state_id'], row['state_name'])

        plasma = States.objects.get_or_create(state_id=row['state_id'],state_name=row['state_name'])[0]
       
        # get topic for the entry


@sync_to_async
def iterate_json(result,states_object):

    print (result)

    for k, v in result.items():
        setattr(states_object, k, v)
    #arunachal_Pradesh=iterate_json(result,arunachal_Pradesh)

    states_object.save()


@sync_to_async
def get_district_id(Districts,district_name):

    return list(Districts.objects.filter(district_name=district_name).values_list('district_id'))
                    

async def fetch(session, url):
    async with session.get(url) as resp:
        return await resp.read()
        # Catch HTTP errors/exceptions here


async def fetch_concurrent(urls,y,district_id):

    from .models import Andaman_and_nicobar_islands,States,Districts,Andhra_Pradesh,Arunachal_Pradesh


    df_hospital_list = pd.DataFrame(
        columns=['state_name', 'district_name', 'district_id', 'name', 'vaccine',
                 'vaccine_date', 'available_capacity'])



    print (district_id)

    loop = asyncio.get_event_loop()
    async with aiohttp.ClientSession(headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}) as session:
        
        tasks = []
        
        for u in urls:
            tasks.append(loop.create_task(fetch(session, u[0]),name=str(u[1])))

        for result in asyncio.as_completed(tasks):

            #print('Active tasks count: ', [task.get_name() for task in asyncio.all_tasks()])

            centers = await result

            #Do whatever you want with results

            try:

                centers = json.loads(centers)
            
                for key in centers["centers"]:

                    for session in key["sessions"]:

                        df_hospital_list = pd.DataFrame(
                            columns=['state_name', 'district_name', 'district_id', 'name', 'vaccine',
                            'vaccine_date', 'available_capacity'])


                        dis_id=9999999
         
                        district=await get_district_id(Districts,key['district_name'])

                        for id in district:
                            if str(id[0]) in list(district_id):
                                dis_id=id[0]
                                df_hospital_list = df_hospital_list.append({
                                                        'state_name': key['state_name'],
                                                        'district_name': key["district_name"],
                                                        'district_id':dis_id,
                                                        'name' : key["name"],
                                                        'vaccine' : session["vaccine"],
                                                        'vaccine_date' : datetime.strptime(str(session["date"]),"%d-%m-%Y").strftime('%Y-%m-%d'),
                                                        'available_capacity' : session["available_capacity"],
                                                        'status' : 'New'
                                                       },ignore_index=True)
                            else:
                                print ("Not valid : "+str(id[0]))
                                print ("ID LIST : "+str(district_id))
                                continue

                
                    if not df_hospital_list.empty:
                        df_hospital_list = df_hospital_list.groupby(['name','district_name','district_id'],as_index=False).agg({
                       
                            'available_capacity':'sum',
                            'vaccine':'first',
                            'state_name':'first',
                            'vaccine_date':'first',
                            'status' : 'first',
                
                            })

                        response = redis.Redis(host='redis', port=6379, db=0)

                        for x in df_hospital_list.to_json(orient='records', lines=True).split('\n'):

                            if x != '':

                                y = json.loads(x)
                        
                                response.publish('response', str(x))
                        
                                await iterate_json(y,stateobject(y['state_name']))

                        del df_hospital_list
            
            except Exception as e:
                print (e)
                pass



@shared_task
def download_task():

    from .models import States,Districts

    request_date = datetime.today().strftime('%d-%m-%y')
    celery= redis.StrictRedis('redis', 6379, charset="utf-8", decode_responses=True)
          
    p = celery.pubsub()
    p.psubscribe('URL')
    
    ## IMPLEMENT QUEUE HERE
 
     
    urls = []
    d_list = []
  
    count = 0
    for new_message in p.listen():
        id=new_message['data']

        print ("District ID : "+str(id))

        d_id = []

        d_id.append("https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id="+str(id)+"&date="+request_date)
        d_id.append(id)
        d_list.append(id)
        urls.append(d_id)

        count += 1
        if count>=20:
            batchsize = 20
            y=0
            for i in xrange(0, len(urls), batchsize):
                batch = urls[i:i+batchsize]
                print (batch)
                asyncio.run(fetch_concurrent(batch,y,d_list))
                time.sleep(60)
                y = y + 1
                count=0
            urls = []
            d_list = []
                    

@shared_task
def upload_task():

    from .models import States,Districts

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    
    ## IMPLEMENT QUEUE HERE
    for e in States.objects.all():

        print ("UPLOADING STATE: "+str(e.state_name))


        if e.state_id>=1:
            state_name=e.state_name
            district_ids = list(Districts.objects.filter(state_id=e.state_id).values_list('district_id'))

            print (district_ids)

            URL = redis.Redis(host='redis', port=6379, db=0)

            for district_id in district_ids:
                URL.publish('URL', str(district_id[0]))



@shared_task
def delete_task():

    from .models import States,Districts

    from vaccination.models import Andaman_and_nicobar_islands
    from vaccination.models import Andhra_Pradesh
    from vaccination.models import Arunachal_Pradesh
    from vaccination.models import Assam
    from vaccination.models import Bihar
    from vaccination.models import Chandigarh
    from vaccination.models import Chhattisgarh
    from vaccination.models import Dadra_and_nagar_haveli
    from vaccination.models import Daman_and_diu
    from vaccination.models import Delhi
    from vaccination.models import Goa
    from vaccination.models import Gujarat
    from vaccination.models import Haryana
    from vaccination.models import Himachal_pradesh
    from vaccination.models import Jammu_and_kashmir
    from vaccination.models import Jharkhand
    from vaccination.models import Karnataka
    from vaccination.models import Kerala
    from vaccination.models import Ladakh
    from vaccination.models import Lakshadweep
    from vaccination.models import Madhya_pradesh
    from vaccination.models import Maharashtra
    from vaccination.models import Manipur
    from vaccination.models import Meghalaya
    from vaccination.models import Mizoram
    from vaccination.models import Nagaland
    from vaccination.models import Odisha
    from vaccination.models import Puducherry
    from vaccination.models import Punjab
    from vaccination.models import Rajasthan
    from vaccination.models import Sikkim
    from vaccination.models import Tamil_nadu
    from vaccination.models import Telangana
    from vaccination.models import Tripura
    from vaccination.models import Uttar_pradesh
    from vaccination.models import Uttarakhand
    from vaccination.models import West_bengal



    Andaman_and_nicobar_islands.objects.filter(vaccine_date__lte=datetime.now() - timedelta(days=1)).delete()
    
    Andhra_Pradesh.objects.filter(vaccine_date__lte=datetime.now() - timedelta(days=1)).delete()
    
    Arunachal_Pradesh.objects.filter(vaccine_date__lte=datetime.now() - timedelta(days=1)).delete()
    
    Assam.objects.filter(vaccine_date__lte=datetime.now() - timedelta(days=1)).delete()
    
    Bihar.objects.filter(vaccine_date__lte=datetime.now() - timedelta(days=1)).delete()
    
    Chandigarh.objects.filter(vaccine_date__lte=datetime.now() - timedelta(days=1)).delete()
    
    Chhattisgarh.objects.filter(vaccine_date__lte=datetime.now() - timedelta(days=1)).delete()
    
    Dadra_and_nagar_haveli.objects.filter(vaccine_date__lte=datetime.now() - timedelta(days=1)).delete()
    
    Daman_and_diu.objects.filter(vaccine_date__lte=datetime.now() - timedelta(days=1)).delete()
    
    Delhi.objects.filter(vaccine_date__lte=datetime.now() - timedelta(days=1)).delete()
    
    Goa.objects.filter(vaccine_date__lte=datetime.now() - timedelta(days=1)).delete()
    
    Gujarat.objects.filter(vaccine_date__lte=datetime.now() - timedelta(days=1)).delete()
    
    Haryana.objects.filter(vaccine_date__lte=datetime.now() - timedelta(days=1)).delete()
    
    Himachal_pradesh.objects.filter(vaccine_date__lte=datetime.now() - timedelta(days=1)).delete()
    
    Jammu_and_kashmir.objects.filter(vaccine_date__lte=datetime.now() - timedelta(days=1)).delete()
    
    Jharkhand.objects.filter(vaccine_date__lte=datetime.now() - timedelta(days=1)).delete()
    
    Karnataka.objects.filter(vaccine_date__lte=datetime.now() - timedelta(days=1)).delete()
    
    Kerala.objects.filter(vaccine_date__lte=datetime.now() - timedelta(days=1)).delete()
    
    Ladakh.objects.filter(vaccine_date__lte=datetime.now() - timedelta(days=1)).delete()
    
    Lakshadweep.objects.filter(vaccine_date__lte=datetime.now() - timedelta(days=1)).delete()
    
    Madhya_pradesh.objects.filter(vaccine_date__lte=datetime.now() - timedelta(days=1)).delete()
    
    Maharashtra.objects.filter(vaccine_date__lte=datetime.now() - timedelta(days=1)).delete()
    
    Manipur.objects.filter(vaccine_date__lte=datetime.now() - timedelta(days=1)).delete()
    
    Meghalaya.objects.filter(vaccine_date__lte=datetime.now() - timedelta(days=1)).delete()
    
    Mizoram.objects.filter(vaccine_date__lte=datetime.now() - timedelta(days=1)).delete()
    
    Nagaland.objects.filter(vaccine_date__lte=datetime.now() - timedelta(days=1)).delete()
    
    Odisha.objects.filter(vaccine_date__lte=datetime.now() - timedelta(days=1)).delete()
    
    Puducherry.objects.filter(vaccine_date__lte=datetime.now() - timedelta(days=1)).delete()
    
    Punjab.objects.filter(vaccine_date__lte=datetime.now() - timedelta(days=1)).delete()
    
    Rajasthan.objects.filter(vaccine_date__lte=datetime.now() - timedelta(days=1)).delete()
    
    Sikkim.objects.filter(vaccine_date__lte=datetime.now() - timedelta(days=1)).delete()
    
    Tamil_nadu.objects.filter(vaccine_date__lte=datetime.now() - timedelta(days=1)).delete()
    
    Telangana.objects.filter(vaccine_date__lte=datetime.now() - timedelta(days=1)).delete()
    
    Tripura.objects.filter(vaccine_date__lte=datetime.now() - timedelta(days=1)).delete()
    
    Uttar_pradesh.objects.filter(vaccine_date__lte=datetime.now() - timedelta(days=1)).delete()
    
    Uttarakhand.objects.filter(vaccine_date__lte=datetime.now() - timedelta(days=1)).delete()
    
    West_bengal.objects.filter(vaccine_date__lte=datetime.now() - timedelta(days=1)).delete()


    return "Successfully Deleted "

@shared_task
def remove_duplicated_records():

    from vaccination.models import Andaman_and_nicobar_islands
    from vaccination.models import Andhra_Pradesh
    from vaccination.models import Arunachal_Pradesh
    from vaccination.models import Assam
    from vaccination.models import Bihar
    from vaccination.models import Chandigarh
    from vaccination.models import Chhattisgarh
    from vaccination.models import Dadra_and_nagar_haveli
    from vaccination.models import Daman_and_diu
    from vaccination.models import Delhi
    from vaccination.models import Goa
    from vaccination.models import Gujarat
    from vaccination.models import Haryana
    from vaccination.models import Himachal_pradesh
    from vaccination.models import Jammu_and_kashmir
    from vaccination.models import Jharkhand
    from vaccination.models import Karnataka
    from vaccination.models import Kerala
    from vaccination.models import Ladakh
    from vaccination.models import Lakshadweep
    from vaccination.models import Madhya_pradesh
    from vaccination.models import Maharashtra
    from vaccination.models import Manipur
    from vaccination.models import Meghalaya
    from vaccination.models import Mizoram
    from vaccination.models import Nagaland
    from vaccination.models import Odisha
    from vaccination.models import Puducherry
    from vaccination.models import Punjab
    from vaccination.models import Rajasthan
    from vaccination.models import Sikkim
    from vaccination.models import Tamil_nadu
    from vaccination.models import Telangana
    from vaccination.models import Tripura
    from vaccination.models import Uttar_pradesh
    from vaccination.models import Uttarakhand
    from vaccination.models import West_bengal

 

    removeDuplicates(Andaman_and_nicobar_islands)
    removeDuplicates(Andhra_Pradesh)
    removeDuplicates(Arunachal_Pradesh)
    removeDuplicates(Assam)
    removeDuplicates(Bihar)
    removeDuplicates(Chandigarh)
    removeDuplicates(Chhattisgarh)
    removeDuplicates(Dadra_and_nagar_haveli)
    removeDuplicates(Daman_and_diu)
    removeDuplicates(Delhi)
    removeDuplicates(Goa)
    removeDuplicates(Gujarat)
    removeDuplicates(Haryana)
    removeDuplicates(Himachal_pradesh)
    removeDuplicates(Jammu_and_kashmir)
    removeDuplicates(Jharkhand)
    removeDuplicates(Karnataka)
    removeDuplicates(Kerala)
    removeDuplicates(Ladakh)
    removeDuplicates(Lakshadweep)
    removeDuplicates(Madhya_pradesh)
    removeDuplicates(Maharashtra)
    removeDuplicates(Manipur)
    removeDuplicates(Meghalaya)
    removeDuplicates(Mizoram)
    removeDuplicates(Nagaland)
    removeDuplicates(Odisha)
    removeDuplicates(Puducherry)
    removeDuplicates(Punjab)
    removeDuplicates(Rajasthan)
    removeDuplicates(Sikkim)
    removeDuplicates(Tamil_nadu)
    removeDuplicates(Telangana)
    removeDuplicates(Tripura)
    removeDuplicates(Uttar_pradesh)
    removeDuplicates(Uttarakhand)
    removeDuplicates(West_bengal)












