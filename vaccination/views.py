from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q, Count
from datetime import datetime, timedelta

from covidfeed.models import ResourceRequest
from .models import State, District, VaccinationCenter, VaccinationSession

# Create your views here.

def index(request):
    """
    Main view for the vaccination app showing vaccination centers and availability.
    """
    # Get filter parameters
    state_id = request.GET.get('state_id')
    district_id = request.GET.get('district_id')
    date_from = request.GET.get('date_from', datetime.now().date().strftime('%Y-%m-%d'))
    vaccine = request.GET.get('vaccine')
    
    # Base queryset
    queryset = VaccinationSession.objects.select_related('center', 'center__district', 'center__district__state')
    
    # Apply filters
    if state_id:
        queryset = queryset.filter(center__district__state__state_id=state_id)
    
    if district_id:
        queryset = queryset.filter(center__district__district_id=district_id)
    
    if date_from:
        try:
            date_obj = datetime.strptime(date_from, '%Y-%m-%d').date()
            queryset = queryset.filter(date__gte=date_obj)
        except ValueError:
            # Invalid date format, ignore filter
            pass
    
    if vaccine:
        queryset = queryset.filter(vaccine__icontains=vaccine)
    
    # Get resource request counts for sidebar
    oxygen_count = ResourceRequest.objects.filter(resource_type='OXYGEN').count()
    plasma_count = ResourceRequest.objects.filter(resource_type='PLASMA').count()
    bed_count = ResourceRequest.objects.filter(resource_type='BED').count()
    
    # Get states and districts for filters
    states = State.objects.all().order_by('name')
    districts = District.objects.all().order_by('name')
    if state_id:
        districts = districts.filter(state__state_id=state_id)
    
    context = {
        'vaccination_sessions': queryset.order_by('date'),
        'states': states,
        'districts': districts,
        'selected_state_id': state_id,
        'selected_district_id': district_id,
        'date_from': date_from,
        'selected_vaccine': vaccine,
        'oxygen_count': oxygen_count,
        'plasma_count': plasma_count,
        'bed_count': bed_count,
    }
    
    return render(request, 'vaccination/index.html', context=context)

def get_districts_by_state(request, state_id):
    """API endpoint to get districts for a state."""
    districts = District.objects.filter(state__state_id=state_id).values('district_id', 'name')
    return JsonResponse(list(districts), safe=False)

class VaccinationSessionListView(ListView):
    """Class-based view for listing vaccination sessions with filtering."""
    model = VaccinationSession
    template_name = 'vaccination/index.html'
    context_object_name = 'vaccination_sessions'
    paginate_by = 20
    
    def get_queryset(self):
        queryset = super().get_queryset().select_related(
            'center', 'center__district', 'center__district__state'
        )
        
        # Apply filters from request parameters
        state_id = self.request.GET.get('state_id')
        district_id = self.request.GET.get('district_id')
        date_from = self.request.GET.get('date_from')
        vaccine = self.request.GET.get('vaccine')
        
        if state_id:
            queryset = queryset.filter(center__district__state__state_id=state_id)
        
        if district_id:
            queryset = queryset.filter(center__district__district_id=district_id)
        
        if date_from:
            try:
                date_obj = datetime.strptime(date_from, '%Y-%m-%d').date()
                queryset = queryset.filter(date__gte=date_obj)
            except ValueError:
                # Invalid date format, ignore filter
                pass
        
        if vaccine:
            queryset = queryset.filter(vaccine__icontains=vaccine)
        
        return queryset.order_by('date')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Add resource request counts for sidebar
        context['oxygen_count'] = ResourceRequest.objects.filter(resource_type='OXYGEN').count()
        context['plasma_count'] = ResourceRequest.objects.filter(resource_type='PLASMA').count()
        context['bed_count'] = ResourceRequest.objects.filter(resource_type='BED').count()
        
        # Add states and districts for filters
        context['states'] = State.objects.all().order_by('name')
        
        state_id = self.request.GET.get('state_id')
        if state_id:
            context['districts'] = District.objects.filter(
                state__state_id=state_id
            ).order_by('name')
        else:
            context['districts'] = District.objects.all().order_by('name')
        
        # Add filter parameters to context
        context['selected_state_id'] = self.request.GET.get('state_id')
        context['selected_district_id'] = self.request.GET.get('district_id')
        context['date_from'] = self.request.GET.get('date_from', 
                                                  datetime.now().date().strftime('%Y-%m-%d'))
        context['selected_vaccine'] = self.request.GET.get('vaccine')
        
        return context
