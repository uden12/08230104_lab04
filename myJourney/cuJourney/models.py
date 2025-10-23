from django.db import models

# Create your models here.
class Journey(models.Model):
    number = models.PositiveIntegerField()
    topic = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.number}. {self.topic}"


class AboutMe(models.Model):
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=200)
    education = models.CharField(max_length=200)
    college = models.CharField(max_length=200)
    interests = models.TextField()

    def __str__(self):
        return self.name
