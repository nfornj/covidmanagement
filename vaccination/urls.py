from django.conf.urls import url
from django.urls import path
from vaccination import views


urlpatterns=[

    path('',views.all_data,name='vaccination'),
    path('', views.index,name='vaccination'),

    url(r'^district$',views.districtdata),

]