from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):

    print (request)

    data = {"insert_me":"Home Value UVAA PINNE PRAANTHU"}
    return render(request, 'covidfeed/index.html',context=data)
