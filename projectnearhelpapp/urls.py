from django.urls import path 
from projectnearhelpapp import views

urlpatterns = [
    path('',views.Welcomepage,name='Welcomepage'),
    path('Job_signup',views.Job_signup,name='Job_signup'),
]
