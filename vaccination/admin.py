from django.contrib import admin
from vaccination.models import Plasma,Topic,Oxygen,Bed,Location

# Register your models here.

admin.site.register(Plasma)
admin.site.register(Topic)
admin.site.register(Oxygen)
admin.site.register(Bed)
admin.site.register(Location)
