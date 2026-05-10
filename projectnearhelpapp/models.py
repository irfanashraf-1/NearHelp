from django.db import models

# Create your models here.
class Client_details(models.Model):
        Fullname = models.CharField(max_length=50)
        Phone_number = models.IntegerField(max_length=10)
        Email = models.CharField()
        Area = models.CharField()
        Town = models.CharField()
        Pin = models.IntegerField(max_length=6)
        Password = models.CharField(max_length=128)

class Helper_details(models.Model):
        Fullname = models.CharField(max_length=50)
        Dob = models.DateField()
        Gender = models.CharField()
        Phone_number = models.IntegerField(max_length=10)
        Email = models.CharField()
        Photo = models.ImageField(upload_to="photos/" , blank=True, null=True)
        Area = models.CharField(max_length=100, null=True, blank=True)
        Town = models.CharField(max_length=100)
        Pin = models.IntegerField(max_length=6)
        Category = models.CharField()
        Availability = models.CharField()
        Password = models.CharField(max_length=128)

