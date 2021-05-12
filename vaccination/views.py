from django.shortcuts import render
from django.http import HttpResponse
from covidfeed.models import Topic,Plasma,Oxygen,Bed,Location
from datetime import datetime, timedelta
from django.db.models import Q
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

    return render(request, 'vaccination/index.html',context=data)

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
