from django.conf.urls import url
from vaccination import views


urlpatterns=[

    url(r'^all_data$',views.all_data,name='vaccination'),
    url(r'^plasma$',views.plasma,name='vaccineState'),
    url(r'^oxygen$',views.oxygen,name='vaccinacountry'),
    url(r'^bed$',views.bed,name='vaccinedistrict'),

]