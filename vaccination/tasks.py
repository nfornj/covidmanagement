from celery import shared_task
import requests
import json
import time
import smtplib , ssl
from smtplib import SMTP
import datetime

from vaccination.modules.sendemail import sendemail



@shared_task
def download_task():
    
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    r= requests.get("https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=307&date=11-05-2021",headers=headers)

    print (r)

    centers = json.loads(r.text)

    hospital_name_list=[]

    result_data=[]

    for key in centers["centers"]:
        print (key)
        for session in key["sessions"]:
            if session["available_capacity"]>0:
                result = {}
                result["Hospital Name"]=key["name"]
                result["Address"]=key["address"]
                result["Slots Available"]=session["available_capacity"]
                result["Available Date"]=session["date"]
                result["Vaccine"]=session["vaccine"]
                print(json.dumps(result))

                result_data.append(json.dumps(result))


    print (result_data)

    result_data='\n'.join(map(str, result_data))

    if result_data:
        sendemail(result_data)
    else:
        print ("No Vaccination Available")