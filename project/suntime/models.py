from django.db import models

class Country(models.Model):
    name = models.TextField()
    lat = models.FloatField()
    long = models.FloatField()