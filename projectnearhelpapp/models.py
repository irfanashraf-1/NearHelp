from django.conf import settings
from django.db import models


# Create your models here.
class Client_details(models.Model):
        user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE , related_name='client_details' , null=True, blank=True)
        Fullname = models.CharField(max_length=50)
        Phone_number = models.CharField()
        Email = models.CharField()
        Area = models.CharField()
        Town = models.CharField()
        Pin = models.IntegerField()
        Password = models.CharField(max_length=128)
        Preferred_language = models.CharField(max_length=50 , null=True, blank=True)
        Preferred_contact_method = models.CharField(max_length=50 , null=True, blank=True)
        Photo = models.ImageField(upload_to="photos/client_photos/" , blank=True, null=True)

        # def __str__(self):
        #         return f"Client: {self.user.username}"

class Helper_details(models.Model):
        user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE , related_name='helper_details', null=True, blank=True)
        Fullname = models.CharField(max_length=50)
        Dob = models.DateField()
        Gender = models.CharField()
        Phone_number = models.CharField()
        Email = models.CharField()
        Photo = models.ImageField(upload_to="photos/" , blank=True, null=True)
        Area = models.CharField(max_length=100, null=True, blank=True)
        Town = models.CharField(max_length=100)
        Pin = models.IntegerField()
        Category = models.CharField()
        Availability = models.CharField()
        Password = models.CharField(max_length=128)

        # def __str__(self):
        #         return f"Helper: {self.user.username}"

class Job_postings(models.Model):
        Client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
        Title = models.CharField(max_length=80)
        Category = models.CharField()
        Description = models.TextField(max_length=500)
        Photos = models.ImageField(upload_to="job_photos/" , blank=True, null=True)
        Budget_min = models.IntegerField(blank=True, null=True)
        Budget_max = models.IntegerField(blank=True, null=True)
        Duration = models.CharField()
        Urgency = models.CharField()    
        Area = models.CharField(max_length=100)
        Town = models.CharField(max_length=100)
        Pin = models.IntegerField(max_length=6)
        Date_posted = models.DateTimeField(auto_now_add=True)
        Status = models.CharField(max_length=20, default='open') 

        # def __str__(self):
        #         return f"Order by {self.client.username} "
