from django.db import models

# Create your models here.
class Country(models.Model):
    countryName = models.CharField(max_length=100, unique=True, blank=False, null=False)

class State(models.Model):
    stateName = models.CharField(max_length=100, blank=False, null=False)
    country = models.ForeignKey(Country, related_name="country", on_delete=models.CASCADE)  

class City(models.Model):
    cityName = models.CharField(max_length=100, blank=False, null=False)
    state = models.ForeignKey(State, related_name="state", on_delete=models.CASCADE)

