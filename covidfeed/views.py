from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q, Count
from datetime import datetime, timedelta

from .models import Topic, ResourceRequest, Location

# Create your views here.

def index(request):
    """
    Main view for the covidfeed app showing all resource requests
    with filtering options.
    """
    # Get filter parameters from request
    resource_type = request.GET.get('resource_type', None)
    days = int(request.GET.get('days', 30))  # Default to 30 days
    status = request.GET.get('status', None)
    
    # Base queryset
    queryset = ResourceRequest.objects.all()
    
    # Apply filters
    if resource_type:
        queryset = queryset.filter(resource_type=resource_type)
    
    if status:
        queryset = queryset.filter(status=status)
    
    # Filter by date
    date_threshold = datetime.now().date() - timedelta(days=days)
    queryset = queryset.filter(request_date__gte=date_threshold)
    
    # Get counts for each resource type
    plasma_count = ResourceRequest.objects.filter(resource_type='PLASMA').count()
    oxygen_count = ResourceRequest.objects.filter(resource_type='OXYGEN').count()
    bed_count = ResourceRequest.objects.filter(resource_type='BED').count()
    
    # Prepare context data
    context = {
        'all_data': queryset.order_by('-request_date'),
        'plasma_count': plasma_count,
        'oxygen_count': oxygen_count,
        'bed_count': bed_count,
        'resource_type': resource_type,
        'days': days,
        'status': status,
    }
    
    return render(request, 'covidfeed/index.html', context=context)

def plasma(request):
    """View for plasma resource requests."""
    return index(request._replace(GET=request.GET.copy().update({'resource_type': 'PLASMA'})))

def oxygen(request):
    """View for oxygen resource requests."""
    return index(request._replace(GET=request.GET.copy().update({'resource_type': 'OXYGEN'})))

def bed(request):
    """View for hospital bed resource requests."""
    return index(request._replace(GET=request.GET.copy().update({'resource_type': 'BED'})))

class ResourceRequestListView(ListView):
    """Class-based view for listing resource requests with filtering."""
    model = ResourceRequest
    template_name = 'covidfeed/index.html'
    context_object_name = 'all_data'
    paginate_by = 20
    
    def get_queryset(self):
        queryset = super().get_queryset()
        
        # Apply filters from request parameters
        resource_type = self.request.GET.get('resource_type')
        status = self.request.GET.get('status')
        days = int(self.request.GET.get('days', 30))
        
        if resource_type:
            queryset = queryset.filter(resource_type=resource_type)
        
        if status:
            queryset = queryset.filter(status=status)
        
        # Filter by date
        date_threshold = datetime.now().date() - timedelta(days=days)
        queryset = queryset.filter(request_date__gte=date_threshold)
        
        return queryset.order_by('-request_date')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Add resource type counts to context
        context['plasma_count'] = ResourceRequest.objects.filter(resource_type='PLASMA').count()
        context['oxygen_count'] = ResourceRequest.objects.filter(resource_type='OXYGEN').count()
        context['bed_count'] = ResourceRequest.objects.filter(resource_type='BED').count()
        
        # Add filter parameters to context
        context['resource_type'] = self.request.GET.get('resource_type')
        context['status'] = self.request.GET.get('status')
        context['days'] = int(self.request.GET.get('days', 30))
        
        return context
