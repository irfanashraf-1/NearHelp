from django.urls import path 
from projectnearhelpapp import views

urlpatterns = [
    path('',views.Welcomepage,name='Welcomepage'),
    path('Job_signup_page',views.Job_signup_page,name='Job_signup_page'),
    path('Client_signup_page',views.Client_signup_page,name='Client_signup_page'),
    path('Login_page',views.Login_page,name='Login_page'),
]
