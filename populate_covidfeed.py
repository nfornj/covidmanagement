import sys
print (sys.path)
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','covidcryindia.settings')
import django
django.setup()

import random
from covidfeed.models import Plasma,Topic,Oxygen,Bed,Location
from faker import Faker

fakegen = Faker()

Topic_Name = ['Plasma','Oxygen','Bed']

Location_Name = ['Mumbai','Kochi','Chennai','Bangalore']

def add_topic():
    t = Topic.objects.get_or_create(topic_name=random.choice(Topic_Name))[0]
    t.save()
    return t

def add_location():
    t = Location.objects.get_or_create(location_name=random.choice(Location_Name),country="India")[0]
    t.save()
    return t

def populate_data(N=10):

    for entry in range(N):
        # get topic for the entry

        user_name = fakegen.name()
        topic_name = add_topic()
        social_media_content = fakegen.text()
        request_date = fakegen.date() #date created
        user_location = add_location()
        
        if str(topic_name)=="Plasma":
            plasma = Plasma.objects.get_or_create(plasma_topic_name=topic_name,plasma_user_name=user_name,plasma_social_media_content=social_media_content,plasma_request_date=request_date,plasma_user_location=user_location)[0]
        elif str(topic_name)=="Oxygen":
            oxygen = Oxygen.objects.get_or_create(oxygen_topic_name=topic_name,oxygen_user_name=user_name,oxygen_social_media_content=social_media_content,oxygen_request_date=request_date,oxygen_user_location=user_location)[0]
        elif str(topic_name)=="Bed":
            bed = Bed.objects.get_or_create(bed_topic_name=topic_name,bed_user_name=user_name,bed_social_media_content=social_media_content,bed_request_date=request_date,bed_user_location=user_location)[0]
        else:
            continue


if __name__=='__main__':
    print ("Populating Script")
    populate_data(20)