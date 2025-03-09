from django.urls import path
from . import views

app_name = 'vaccination'

urlpatterns = [
    path('', views.VaccinationSessionListView.as_view(), name='index'),
    # Legacy function-based view for backward compatibility
    path('legacy/', views.index, name='legacy_index'),
    # API endpoints for AJAX requests
    path('api/districts/<int:state_id>/', views.get_districts_by_state, name='api_districts_by_state'),
]

# Add a view for the API endpoint
from django.http import JsonResponse

def get_districts_by_state(request, state_id):
    """API endpoint to get districts for a state."""
    from .models import District
    districts = District.objects.filter(state__state_id=state_id).values('district_id', 'name')
    return JsonResponse(list(districts), safe=False)