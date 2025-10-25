from django.urls import path
from . import views
# Import path for URL routing and import views from the current app


# ===================== URL Configuration =====================
urlpatterns = [
    # Home page route – connects the root URL ('') to the index view
    path('', views.index, name='index'),

    # About Me page route – connects '/about/' URL to the about_me view
    path('about/', views.about_me, name='about_me'),
]
