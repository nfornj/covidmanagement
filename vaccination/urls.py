from django.conf.urls import url
from vaccination import views


urlpatterns=[

    url(r'^$',views.index,name='vaccination'),
    url(r'^plasma$',views.plasma,name='vaccineState'),
    url(r'^oxygen$',views.oxygen,name='vaccinacountry'),
    url(r'^bed$',views.bed,name='vaccinedistrict'),

]