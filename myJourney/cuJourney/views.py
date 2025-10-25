from django.shortcuts import render
from .models import Journey, AboutMe
# Import render to display templates and import the models used in this app


# ===================== INDEX VIEW =====================
def index(request):
    """
    Renders the home page (index.html) and displays all learning journey topics.
    """
    # Retrieve all Journey records from the database, ordered by 'number'
    journeys = Journey.objects.all().order_by('number')
    
    # Render the 'index.html' template with the list of journeys as context data
    return render(request, 'index.html', {'journeys': journeys})


# ===================== ABOUT ME VIEW =====================
def about_me(request):
    """
    Renders the About Me page (aboutMe.html) with personal information.
    """
    # Retrieve the first AboutMe record from the database
    # (Assumes only one record is used for the personal profile)
    about = AboutMe.objects.first()
    
    # Render the 'aboutMe.html' template with the AboutMe data as context
    return render(request, 'aboutMe.html', {'about': about})
