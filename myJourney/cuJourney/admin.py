from django.contrib import admin
from .models import Journey, AboutMe
# Import the Django admin module and the models created in models.py


# ===================== Journey Model Registration =====================
@admin.register(Journey)
class JourneyAdmin(admin.ModelAdmin):
    """
    Customizes how the Journey model appears in the Django Admin panel.
    """
    list_display = ('number', 'topic', 'description')  
    # Displays these fields as columns in the admin list view


# ===================== AboutMe Model Registration =====================
@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    """
    Customizes how the AboutMe model appears in the Django Admin panel.
    """
    list_display = ('name', 'education', 'college', 'place')  
    # Displays these fields as columns in the admin list view
