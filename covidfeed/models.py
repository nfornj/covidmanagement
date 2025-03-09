from django.db import models

# Create your models here.

class Topic(models.Model):
    """Model representing a resource topic category."""
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name

class Location(models.Model):
    """Model representing a location with country information."""
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50, default='India')
    state = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    
    def __str__(self):
        return f"{self.name}, {self.country}"

class ResourceRequest(models.Model):
    """
    Model representing a resource request (Plasma, Oxygen, Bed, etc.)
    This replaces the separate models for each resource type.
    """
    RESOURCE_TYPES = [
        ('PLASMA', 'Plasma'),
        ('OXYGEN', 'Oxygen'),
        ('BED', 'Hospital Bed'),
        ('MEDICINE', 'Medicine'),
        ('OTHER', 'Other'),
    ]
    
    STATUS_CHOICES = [
        ('NEW', 'New'),
        ('IN_PROGRESS', 'In Progress'),
        ('FULFILLED', 'Fulfilled'),
        ('CLOSED', 'Closed'),
    ]
    
    user_name = models.CharField(max_length=100)
    resource_type = models.CharField(max_length=20, choices=RESOURCE_TYPES)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='resource_requests')
    content = models.TextField()
    request_date = models.DateField(auto_now_add=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True, related_name='resource_requests')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='NEW')
    contact_info = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.get_resource_type_display()} request by {self.user_name} ({self.get_status_display()})"






