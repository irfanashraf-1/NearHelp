from django.urls import path 
from projectnearhelpapp import views

urlpatterns = [
    path('',views.Welcomepage,name='Welcomepage'),
    path('Helper_signup_page',views.Helper_signup_page,name='Helper_signup_page'),
    path('Client_signup_page',views.Client_signup_page,name='Client_signup_page'),
    path('Login_page',views.Login_page,name='Login_page'),
    path('Home',views.Home,name='Home'),

    path('Admin_dashboard',views.Admin_dashboard,name='Admin_dashboard'),
    path('Helper_data_table',views.Helper_data_table,name='Helper_data_table'),
    path('Client_data_table',views.Client_data_table,name='Client_data_table'),
    path('Users_data_table',views.Users_data_table,name='Users_data_table'),
    

    path('Save_client_data',views.Save_client_data,name='Save_client_data'),
    path('Save_helper_data',views.Save_helper_data,name='Save_helper_data'),
    path('Login',views.Login,name='Login'),



]
