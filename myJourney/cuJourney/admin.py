from django.contrib import admin
from .models import Journey, AboutMe

# Register your models here.

@admin.register(Journey)
class JourneyAdmin(admin.ModelAdmin):
    list_display = ('number', 'topic', 'description')

@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ('name', 'education', 'college', 'place')
