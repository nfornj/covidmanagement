from django.contrib import admin
from .models import State, District, VaccinationCenter, VaccinationSession

# Register your models here.

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'state_id')
    search_fields = ('name',)

@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('name', 'district_id', 'state')
    list_filter = ('state',)
    search_fields = ('name',)

@admin.register(VaccinationCenter)
class VaccinationCenterAdmin(admin.ModelAdmin):
    list_display = ('name', 'district', 'pincode')
    list_filter = ('district__state', 'district')
    search_fields = ('name', 'address', 'pincode')

@admin.register(VaccinationSession)
class VaccinationSessionAdmin(admin.ModelAdmin):
    list_display = ('center', 'date', 'vaccine', 'available_capacity', 'status')
    list_filter = ('status', 'vaccine', 'date', 'center__district__state', 'center__district')
    search_fields = ('center__name', 'vaccine')
    date_hierarchy = 'date'
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Center Information', {
            'fields': ('center',)
        }),
        ('Session Details', {
            'fields': ('date', 'vaccine', 'available_capacity', 'min_age_limit', 'status')
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

