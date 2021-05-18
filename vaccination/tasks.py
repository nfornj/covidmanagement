from celery import shared_task
import requests
import json
import time
from datetime import datetime, timedelta
#from celery import vaccination
from django.apps import apps
from vaccination.modules.utils.sendemail import sendemail
import asyncio
import aiohttp
from cffi.backend_ctypes import xrange
from asgiref.sync import sync_to_async
import redis
import pandas as pd
pd.set_option('display.max_columns', 500)

from .modules.config.tableobjects import stateobject,districtobject


def populate_vaccination_state(df):

    for index, row in df.iterrows():
        print(row['state_id'], row['state_name'])

        plasma = States.objects.get_or_create(state_id=row['state_id'],state_name=row['state_name'])[0]
       
        # get topic for the entry


@sync_to_async
def iterate_json(result,states_object):

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
                 'date', 'available_capacity'])

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

            centers = json.loads(centers)

            

            for key in centers["centers"]:
                result_data=[]
                #print (key)
                for session in key["sessions"]:
         
                    district=await get_district_id(Districts,key['district_name'])

                    for id in district:
                        district_id=district_id
                        if str(id[0]) in list(district_id):
                            dis_id=id[0]
                        else:
                            print ("Not valid")
                            dis_id=9999999

                    df_hospital_list = df_hospital_list.append({
                                                        'state_name': key['state_name'],
                                                        'district_name': key["district_name"],
                                                        'district_id':dis_id,
                                                        'name' : key["name"],
                                                        'vaccine' : session["vaccine"],
                                                        'date' : session["date"],
                                                        'available_capacity' : session["available_capacity"],
                                                        'status' : 'New'
                                                       },ignore_index=True)

                df_hospital_list = df_hospital_list.groupby(['name','district_name'],as_index=False).agg(
                    {
                       
                        'available_capacity':'sum',
                        'district_id': 'first',
                        'vaccine':'first',
                        'state_name':'first',
                        'date':'first',
                        'status' : 'first'
                        
                        })

                response = redis.Redis(host='redis', port=6379, db=0)

                for x in df_hospital_list.to_json(orient='records', lines=True).split('\n'):

                    if x != '':
                        response.publish('response', str(x))

                #await iterate_json(result,stateobject(statename))

        #result_data='\n'.join(map(str, result_data))

            if result_data:
                print ("Vaccine Available")
                #sendemail(result_data)
            else:
                print ("No Vaccination Available")


@shared_task
def download_task():

    from .models import States,Districts

    request_date = datetime.today().strftime('%d-%m-%y')

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    
    ## IMPLEMENT QUEUE HERE
    for e in States.objects.all():
        if e.state_id == 2 or e.state_id == 1 or e.state_id == 3:
            state_name=e.state_name
            district_ids = list(Districts.objects.filter(state_id=e.state_id).values_list('district_id'))
            
            urls = []

            celery= redis.StrictRedis('redis', 6379, charset="utf-8", decode_responses=True)
            p = celery.pubsub()
            p.psubscribe('URL')
            count = 0
            for new_message in p.listen():
                id=new_message['data']
                d_id = []
        
                d_id.append("https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id="+str(id)+"&date="+request_date)
                d_id.append(id)
                
                urls.append(d_id)

                count += 1
                if count==20:
                    batchsize = 20
                    y=0
                    d_list=[d[1] for d in urls]
                    d_list.pop(0)
                    for i in xrange(0, len(urls), batchsize):
                        batch = urls[i:i+batchsize]
                        #print (batch)
                        asyncio.run(fetch_concurrent(batch,y,d_list))
                        y = y + 1
                    count=0
                    time.sleep(60)

@shared_task
def upload_task():

    from .models import States,Districts

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    
    ## IMPLEMENT QUEUE HERE
    for e in States.objects.all():

            state_name=e.state_name
            district_ids = list(Districts.objects.filter(state_id=e.state_id).values_list('district_id'))

            URL = redis.Redis(host='redis', port=6379, db=0)

            for district_id in district_ids:
                URL.publish('URL', str(district_id[0]))



@shared_task
def delete_records():

    from .models import States,Districts,Andaman_and_nicobar_islands,Arunachal_Pradesh,Andhra_Pradesh

    Andaman_and_nicobar_islands.objects.filter(vaccine_date__lte=datetime.now() - timedelta(days=1)).delete()

    return "Hello"







