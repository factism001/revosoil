from django.contrib import admin
from .models import Profile, SoilData

# Register your models here.

admin.site.register(SoilData)
admin.site.register(Profile)
