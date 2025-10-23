from django.shortcuts import render
from .models import Journey, AboutMe

# Create your views here.

def index(request):
    journeys = Journey.objects.all().order_by('number')
    return render(request, 'index.html', {'journeys': journeys})

def about_me(request):
    about = AboutMe.objects.first()
    return render(request, 'aboutMe.html', {'about': about})
