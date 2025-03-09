from django.urls import path
from . import views

app_name = 'covidfeed'

urlpatterns = [
    path('', views.ResourceRequestListView.as_view(), name='index'),
    path('plasma/', views.ResourceRequestListView.as_view(initial={'resource_type': 'PLASMA'}), name='plasma'),
    path('oxygen/', views.ResourceRequestListView.as_view(initial={'resource_type': 'OXYGEN'}), name='oxygen'),
    path('bed/', views.ResourceRequestListView.as_view(initial={'resource_type': 'BED'}), name='bed'),
    # Legacy function-based views for backward compatibility
    path('legacy/', views.index, name='legacy_index'),
    path('legacy/plasma/', views.plasma, name='legacy_plasma'),
    path('legacy/oxygen/', views.oxygen, name='legacy_oxygen'),
    path('legacy/bed/', views.bed, name='legacy_bed'),
]