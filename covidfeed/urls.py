from django.conf.urls import url
from covidfeed import views


urlpatterns=[

    url(r'^$',views.index,name='covidfeed'),
    url(r'^plasma$',views.plasma,name='plasma'),
    url(r'^oxygen$',views.oxygen,name='oxygen'),
    url(r'^bed$',views.bed,name='bed'),

]