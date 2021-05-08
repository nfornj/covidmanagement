from django.shortcuts import render
from django.http import HttpResponse
from covidfeed.models import Topic,Plasma,Oxygen,Bed,Location
# Create your views here.


def index(request):

    oxygen_list = Oxygen.objects.order_by('oxygen_request_date')

    data = {"oxygen":oxygen_list}
    
    return render(request, 'covidfeed/index.html',context=data)
