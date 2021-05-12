from django.contrib import admin
from vaccination.models import Andaman_and_nicobar_islands,States,Districts,Andhra_Pradesh,Arunachal_Pradesh

# Register your models here.

admin.site.register(States)
admin.site.register(Districts)

admin.site.register(Andaman_and_nicobar_islands)
admin.site.register(Andhra_Pradesh)
admin.site.register(Arunachal_Pradesh)

