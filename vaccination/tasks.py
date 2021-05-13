from celery import shared_task
import requests
import json
import time
import datetime
#from celery import vaccination
from django.apps import apps
from vaccination.modules.utils.sendemail import sendemail
import asyncio
import aiohttp
from cffi.backend_ctypes import xrange
from asgiref.sync import sync_to_async
import redis

from .modules.config.tableobjects import tableobject


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
                    

async def fetch(session, url):
    async with session.get(url) as resp:
        return await resp.read()
        # Catch HTTP errors/exceptions here


async def fetch_concurrent(urls,y,district_id):

    from .models import Andaman_and_nicobar_islands,States,Districts,Andhra_Pradesh,Arunachal_Pradesh

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
            result_data=[]

            for key in centers["centers"]:
                #print (key)
                for session in key["sessions"]:
                    result = {}
                    result["name"]=key["name"]
                    result["district_name"]=key['district_name']
                    print (key['district_name'])
                    district=list(Districts.objects.filter(district_name=key['district_name'].values_list('district_id')))

                    for id in district:
                        if district_id==id:
                            result["district_id"]=id
                        else:
                            result["district_id"]=9999999

                    result["available_capacity"]=session["available_capacity"]
                    result["vaccine_date"]=datetime.datetime.strptime(session["date"], "%d-%m-%Y").strftime("%Y-%m-%d")
                    result["vaccine"]=session["vaccine"]
                    result["status"]="New"

                    #print(json.dumps(result))

                    result_data.append(json.dumps(result))

                    #print (result)

                    response = redis.Redis(host='redis', port=6379, db=0)

                    response.publish('response', str(result))



                    #await iterate_json(result,tableobject(statename))

        #result_data='\n'.join(map(str, result_data))

            if result_data:
                print ("Vaccine Available")
                #sendemail(result_data)
            else:
                print ("No Vaccination Available")


@shared_task
def download_task():

    from .models import States,Districts

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
        
                d_id.append("https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id="+str(id)+"&date=12-05-2021")
                d_id.append(id)
                
                urls.append(d_id)

                count += 1
                if count==20:
                    batchsize = 20
                    y=0
                    for i in xrange(0, len(urls), batchsize):
                        batch = urls[i:i+batchsize]
                        #print (batch)
                        asyncio.run(fetch_concurrent(batch,y,d_id[1]))
                        y = y + 1
                    count=0
                    time.sleep(60)

@shared_task
def upload_task():

    from .models import States,Districts

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    
    ## IMPLEMENT QUEUE HERE
    for e in States.objects.all():

        if e.state_id == 2 or e.state_id == 1 or e.state_id == 3:

            state_name=e.state_name
            district_ids = list(Districts.objects.filter(state_id=e.state_id).values_list('district_id'))

            URL = redis.Redis(host='redis', port=6379, db=0)

            for district_id in district_ids:
                URL.publish('URL', str(district_id[0]))



