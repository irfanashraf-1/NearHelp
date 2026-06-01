from django.contrib import admin
from projectnearhelpapp.models import Client_details , Helper_details
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
    

