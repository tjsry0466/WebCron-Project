from django.db import models
from django.conf import settings

class Schedule(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fieldir = models.CharField(max_length=100)
    second = models.CharField(max_length=2)
    minute =  models.CharField(max_length=2)
    day = models.CharField(max_length=2)
    week = models.CharField(max_length=2)
    month = models.CharField(max_length=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

