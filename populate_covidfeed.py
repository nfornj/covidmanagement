import sys
print (sys.path)
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','covidcryindia.settings')
import django
django.setup()
import random
from covidfeed.models import Plasma,Topic,Oxygen,Bed,Location
from vaccination.models import States,Districts,Arunachal_Pradesh,Andhra_Pradesh,Andaman_and_nicobar_islands
from faker import Faker
import pandas as pd

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
            plasma = Plasma.objects.get_or_create(topic_name=topic_name,user_name=user_name,social_media_content=social_media_content,request_date=request_date,user_location=user_location)[0]
        elif str(topic_name)=="Oxygen":
            oxygen = Oxygen.objects.get_or_create(topic_name=topic_name,user_name=user_name,social_media_content=social_media_content,request_date=request_date,user_location=user_location)[0]
        elif str(topic_name)=="Bed":
            bed = Bed.objects.get_or_create(topic_name=topic_name,user_name=user_name,social_media_content=social_media_content,request_date=request_date,user_location=user_location)[0]
        else:
            continue


def populate_vaccination_state(df):

    for index, row in df.iterrows():
        print(row['state_id'], row['state_name'])

        plasma = States.objects.get_or_create(state_id=row['state_id'],state_name=row['state_name'])[0]
       
        # get topic for the entry


def populate_vaccination_district(df):

    for index, row in df.iterrows():
        print(row['state_id'], row['district_name'],row['district_id'])

        plasma = Districts.objects.get_or_create(state_id=row['state_id'],district_name=row['district_name'],district_id=row['district_id'])[0]
       
        # get topic for the entry

def delete_table_data():


    Andhra_Pradesh().objects.all().delete()



if __name__=='__main__':


    print ("Populating Script")



    #populate_data(2000)


    df = pd.read_csv('/code/vaccination/data/states.csv')

    print (df)

    populate_vaccination_state(df)


    df = pd.read_csv('/code/vaccination/data/states_district.csv')

    populate_vaccination_district(df)

    #delete_table_data()