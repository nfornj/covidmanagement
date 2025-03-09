from django.db import models

# Create your models here.

class State(models.Model):
    """Model representing a state/union territory in India."""
    name = models.CharField(max_length=100)
    state_id = models.IntegerField(unique=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "States"

class District(models.Model):
    """Model representing a district within a state."""
    name = models.CharField(max_length=100)
    district_id = models.IntegerField(unique=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='districts')
    
    def __str__(self):
        return f"{self.name}, {self.state.name}"
    
    class Meta:
        verbose_name_plural = "Districts"
        unique_together = ('district_id', 'state')

class VaccinationCenter(models.Model):
    """Model representing a vaccination center with availability information."""
    name = models.CharField(max_length=255)
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='vaccination_centers')
    address = models.TextField(blank=True, null=True)
    pincode = models.CharField(max_length=10, blank=True, null=True)
    
    def __str__(self):
        return f"{self.name} - {self.district.name}"

class VaccinationSession(models.Model):
    """Model representing a vaccination session at a center on a specific date."""
    center = models.ForeignKey(VaccinationCenter, on_delete=models.CASCADE, related_name='sessions')
    date = models.DateField()
    vaccine = models.CharField(max_length=50)
    available_capacity = models.IntegerField(default=0)
    min_age_limit = models.IntegerField(default=18)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    STATUS_CHOICES = [
        ('AVAILABLE', 'Available'),
        ('BOOKED', 'Fully Booked'),
        ('UNAVAILABLE', 'Unavailable'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='UNAVAILABLE')
    
    class Meta:
        unique_together = ('center', 'date', 'vaccine', 'min_age_limit')
        
    def __str__(self):
        return f"{self.center.name} - {self.date} - {self.vaccine} ({self.available_capacity})"