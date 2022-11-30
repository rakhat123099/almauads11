from django.db import models
from datetime import datetime

# Create your models here.
class Ad(models.Model):

    class Categories(models.TextChoices):
        LOST = 'Lost'
        ROOMMATES = 'Roommates'
        JOB = 'Job'
        VACANCIES = 'Vacancies'
        EVENTS = 'Events'
        SERVICES = 'Services'
        GARAGESALE = 'Garagesale'
        OTHER = 'Other'

    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    created = models.DateTimeField(default=datetime.now)
    postdate = models.DateField(default=datetime.now)
    posttime = models.TimeField(default=datetime.now)
    text = models.CharField(max_length=5000)
    category = models.CharField(
        max_length=255,
        choices=Categories.choices,
        default=Categories.OTHER
    )