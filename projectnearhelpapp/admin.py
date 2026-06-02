from django.contrib import admin
from projectnearhelpapp.models import Client_details , Helper_details , Job_postings
# Register your models here.

@admin.register(Client_details)
class Client_details_admin(admin.ModelAdmin):
    list_display =['id',
                    'Fullname',
                    'Phone_number',
                    'Email',
                    'Area',
                    'Town',
                    'Pin',
                    'Password']
    
@admin.register(Helper_details)
class Helper_details_admin(admin.ModelAdmin):
    list_display =[ 
                    'id',
                    'Fullname',
                    'Dob',
                    'Gender',
                    'Phone_number', 
                    'Email', 
                    'Photo', 
                    'Area', 
                    'Town', 
                    'Pin', 
                    'Category', 
                    'Availability', 
                    'Password']
    
@admin.register(Job_postings)
class Job_postings_admin(admin.ModelAdmin):
    list_display =[
                    'id',
                    'Client',
                    'Title',
                    'Category',
                    'Description',
                    'Photos',
                    'Budget_min',
                    'Budget_max',
                    'Duration',
                    'Urgency',    
                    'Area',
                    'Town',
                    'Pin',
                    'Date_posted',
                    'Status']