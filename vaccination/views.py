from django.shortcuts import render
from django.http import HttpResponse
from covidfeed.models import Topic,Plasma,Oxygen,Bed,Location
from datetime import datetime, timedelta
from django.db.models import Q
from .modules.config.tableobjects import stateobject
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

# Create your views here.

d = datetime.today() - timedelta(days=1200)

d= d.date()





def index(request):

    oxygen = Oxygen.objects.filter(Q(request_date__gte=d)).reverse()

    bed = Bed.objects.filter(Q(request_date__gte=d)).reverse()

    plasma = Plasma.objects.filter(Q(request_date__gte=d)).reverse()

    all_data=plasma.union(oxygen,bed)

    data = {

    "all_data": all_data.order_by('request_date'),
    "oxygen_count": oxygen.count(),
    "plasma_count": plasma.count(),
    "bed_count": bed.count()

    }

    return render(request, 'vaccination/posts.html',context=data)


def all_data(request):

    for e in States.objects.all():

        total_state_availability = stateobject(e.state_name).objects.aggregate('available_capacity')

        print (total_state_availability)

        data = {

        "total_state_availability": total_state_availability.count(),

        }

    return render(request, 'vaccination/posts.html',context=data)


    


    

def plasma(request):

    oxygen = Oxygen.objects.filter(Q(request_date__gte=d)).reverse()

    bed = Bed.objects.filter(Q(request_date__gte=d)).reverse()

    plasma = Plasma.objects.filter(Q(request_date__gte=d)).reverse()


    data = {

    "all_data": plasma.order_by('request_date'),
    "oxygen_count": oxygen.count(),
    "plasma_count": plasma.count(),
    "bed_count": bed.count()

    }

    return render(request, 'vaccination/posts.html',context=data)

def oxygen(request):

    oxygen = Oxygen.objects.filter(Q(request_date__gte=d)).reverse()

    bed = Bed.objects.filter(Q(request_date__gte=d)).reverse()

    plasma = Plasma.objects.filter(Q(request_date__gte=d)).reverse()

    data = {

    "all_data": oxygen.order_by('request_date'),
    "oxygen_count": oxygen.count(),
    "plasma_count": plasma.count(),
    "bed_count": bed.count()

    }

    return render(request, 'vaccination/posts.html',context=data)

def bed(request):

    oxygen = Oxygen.objects.filter(Q(request_date__gte=d)).reverse()

    bed = Bed.objects.filter(Q(request_date__gte=d)).reverse()

    plasma = Plasma.objects.filter(Q(request_date__gte=d)).reverse()

    data = {

    "all_data": bed.order_by('request_date'),
    "oxygen_count": oxygen.count(),
    "plasma_count": plasma.count(),
    "bed_count": bed.count()

    }

    return render(request, 'vaccination/posts.html',context=data)
