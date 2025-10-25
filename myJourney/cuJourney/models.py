from django.db import models
# Import Django's built-in models module to create database models


# ===================== Journey Model =====================
class Journey(models.Model):
    """
    The Journey model stores information about each step or topic
    in the user's learning journey.
    """
    number = models.PositiveIntegerField()  # Serial number for the topic (must be positive)
    topic = models.CharField(max_length=100)  # Short title or name of the learning topic
    description = models.TextField()  # Detailed explanation or reflection on the topic

    def __str__(self):
        """
        Returns a readable string representation for the admin panel.
        Example: '1. HTML Basics'
        """
        return f"{self.number}. {self.topic}"


# ===================== AboutMe Model =====================
class AboutMe(models.Model):
    """
    The AboutMe model stores personal details of the user,
    which are displayed on the 'About Me' page.
    """
    name = models.CharField(max_length=100)  # User's full name
    place = models.CharField(max_length=200)  # Hometown or location
    education = models.CharField(max_length=200)  # Current education level or degree
    college = models.CharField(max_length=200)  # Name of the college or institution
    interests = models.TextField()  # User’s hobbies, skills, or interests

    def __str__(self):
        """
        Returns the user's name as the display label in the admin panel.
        """
        return self.name
