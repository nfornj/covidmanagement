from django.shortcuts import render
from django.http import HttpResponse
from covidfeed.models import Topic,Plasma,Oxygen,Bed,Location
from datetime import datetime, timedelta
from django.db.models import Q
from .modules.config.tableobjects import stateobject
from .models import States,Districts
from django.db.models import Sum,Min
import json

from vaccination.forms import UserBaseForm


# Create your views here.

d = datetime.today() - timedelta(days=1200)

d= d.date()


def index(request):

    districts = Districts.objects.all()

    return render(request,'vaccination/posts.html',context={"district_list":districts})


def all_data(request):

    state_list=[]

    state_count={}


    districts = Districts.objects.all()

    for e in States.objects.all():


        state_availability = stateobject(e.state_name).objects.aggregate(Sum('available_capacity'))
        earliest = stateobject(e.state_name).objects.values('vaccine_date').annotate(min=Min('vaccine_date')).first()

        
        if earliest is not None:

            state_count['state_id']=e.state_id
            state_count['state_name']=e.state_name
            state_count['available_capacity']=state_availability['available_capacity__sum']
            state_count['available_date']=earliest['min'].strftime('%Y-%m-%d')
            

        else:
             state_count['state_id']=e.state_id
             state_count['state_name']=e.state_name
             state_count['available_capacity']=state_availability['available_capacity__sum']
             state_count['available_date']="No Data"
            
        state_list.append(json.loads(json.dumps(state_count)))

    data = {

        "total_state_availability": state_list,
        "district_list":districts

    }

    return render(request, 'vaccination/posts.html',context=data)



def districtdata(request):

    districts = Districts.objects.all()

    district_id=request.GET.get('district_id')

    district_name = Districts.objects.get(district_id=district_id)
    state_name = States.objects.get(state_id=district_name.state_id)

    data= stateobject(state_name.state_name).objects.filter(district_id=district_id).values('district_name','name','vaccine').annotate(Sum('available_capacity'),min=Min('vaccine_date'))

    return render(request,'vaccination/posts.html',context={
        
        "hospital_list":data,
        "state_name" : state_name.state_name,
        "district_list":districts
    
    })

def statedata(request):

    districts = Districts.objects.all()

    state_id=request.GET.get('state_id')

    state_name = States.objects.get(state_id=state_id)

    data = stateobject(state_name.state_name).objects.values('district_name','district_id').annotate(Sum('available_capacity'),min=Min('vaccine_date'))

    print(data)

    return render(request,'vaccination/posts.html',context={
        
        "district_details":data,
        "state_name" : state_name.state_name,
        "district_list":districts
    
    })


def userdetails(request):

    form = UserBaseForm()

    if request.method == 'POST':

        form = UserBaseForm(request.POST)

        if form.is_valid():

            form.save(commit=True)

            return (districtdata(request))
        else:
            print ("Error Form is invalid")

    
    return render(request,'vaccination/posts.html', {'form':form})