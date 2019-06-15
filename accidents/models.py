from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

import datetime

# Create your models here.
class Accident(models.Model):
    longitude = models.DecimalField(max_digits=10 , decimal_places=6)
    latitude = models.DecimalField(max_digits=10, decimal_places=6)
    accident_catagory = models.CharField(max_length=100)
    municipality = models.CharField(max_length = 100)
    urban_or_not = models.BooleanField()
    scene_description = models.CharField(max_length=100)
    cause_of_accident = models.CharField(max_length=100)
    accident_type = models.CharField(max_length=100)
    traffic_condition = models.CharField(max_length=100)
    date = models.DateField(default = datetime.date.today)
    day_of_week = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(7)])
    time = models.DateTimeField(blank = False)
    road_type = models.CharField(max_length = 100)
    weather_condition = models.CharField(max_length = 100)
    road_surface_condition = models.CharField(max_length = 100 )

class Victim(models.Model):
    caused_the_accident = models.BooleanField()
    age = models.IntegerField(null = False)
    sex = models.BooleanField(null=True)
    municipality = models.CharField(max_length= 100)
    citizenship = models.CharField(max_length = 100)
    injury = models.CharField(max_length = 100)
    type_of_person = models.CharField(max_length=100) #how was the person involved in the accident, e.g.,pedestrian
    safety_belt_or_helmet = models.BooleanField(null = False)
    years_of_driving = models.IntegerField()
    age_discrete = models.IntegerField()

class Municipality(models.Model):
    municipality_name = models.CharField(max_length=100)
    no_of_inhabitants = models.IntegerField()
    area_size = models.DecimalField(max_digits = 20 , decimal_places= 10)