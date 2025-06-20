from django.db import models

class Register(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=100)
    mobilenumber = models.CharField(max_length=20, null=True, blank=True)

    propertyName = models.CharField(max_length=100)

class Property(models.Model):
    propertytype = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    price = models.IntegerField(null=True, blank=True)
    area_sqft = models.IntegerField(null=True, blank=True)
    dwellingplace = models.CharField(max_length=100)