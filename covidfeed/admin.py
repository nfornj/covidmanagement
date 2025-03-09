from django.contrib import admin
from .models import Topic, Location, ResourceRequest

# Register your models here.

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'state', 'country')
    list_filter = ('country', 'state')
    search_fields = ('name', 'city', 'state')

@admin.register(ResourceRequest)
class ResourceRequestAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'resource_type', 'topic', 'request_date', 'status')
    list_filter = ('resource_type', 'status', 'request_date')
    search_fields = ('user_name', 'content')
    date_hierarchy = 'request_date'
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('User Information', {
            'fields': ('user_name', 'contact_info')
        }),
        ('Request Details', {
            'fields': ('resource_type', 'topic', 'content', 'request_date', 'status')
        }),
        ('Location', {
            'fields': ('location',)
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )



