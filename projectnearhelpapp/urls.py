from django.urls import path 
from projectnearhelpapp import views

urlpatterns = [
    path('',views.Welcomepage,name='Welcomepage'),

    #Signup login and logout pages
    path('Helper_signup_page',views.Helper_signup_page,name='Helper_signup_page'),
    path('Client_signup_page',views.Client_signup_page,name='Client_signup_page'),

    path('Login_page',views.Login_page,name='Login_page'),
    path('logout/', views.Logout, name='Logout'),

    #Home pages
    path('Home_helper',views.Home_helper,name='Home_helper'),
    path('Home_client',views.Home_client,name='Home_client'),

    path('Job_posting_form',views.Job_posting_form,name='Job_posting_form'),
    
    #Admin pages
    path('Admin_dashboard',views.Admin_dashboard,name='Admin_dashboard'),

    #Helper Data Table
    path('Helper_data_table',views.Helper_data_table,name='Helper_data_table'),
    path('Edit_helper_data_table/<int:pk>/',views.Edit_helper_data_table,name='Edit_helper_data_table'),
    path('Update_helper_data_table/<int:pk>/',views.Update_helper_data_table,name='Update_helper_data_table'),
    path('Delete_helper_data_table/<int:pk>/',views.Delete_helper_data_table,name='Delete_helper_data_table'),
    
    #Client Data Table
    path('Client_data_table',views.Client_data_table,name='Client_data_table'),
    path('Edit_client_data_table/<int:pk>/',views.Edit_client_data_table,name='Edit_client_data_table'),
    path('Update_client_data_table/<int:pk>/',views.Update_client_data_table,name='Update_client_data_table'),
    path('Delete_client_data_table/<int:pk>/',views.Delete_client_data_table,name='Delete_client_data_table'),

    #User Data Table
    path('User_data_table',views.User_data_table,name='User_data_table'),
    path('Delete_user_data_table/<int:pk>/',views.Delete_user_data_table,name='Delete_user_data_table'),

    path('Save_client_data',views.Save_client_data,name='Save_client_data'),
    path('Save_helper_data',views.Save_helper_data,name='Save_helper_data'),
    path('Save_job_posting',views.Save_job_posting,name='Save_job_posting'),
    path('Login',views.Login,name='Login'),

    #Profile pages
    path('Profile_client',views.Profile_client,name='Profile_client'),
    # path('Profile_helper',views.Profile_helper,name='Profile_helper'),

    # path('Profile_dashboard_view',views.Profile_dashboard_view,name='Profile_dashboard_view'),
    # path('Profile_view',views.Profile_view,name='Profile_view')

    #Category pages
    path('Carpentry_page',views.Carpentry_page,name='Carpentry_page'),
    path('Moving_page',views.Moving_page,name='Moving_page'),
    path('Gardening_page',views.Gardening_page,name='Gardening_page'),
    path('Techhelp_page',views.Techhelp_page,name='Techhelp_page'),
    path('Cleaning_page',views.Cleaning_page,name='Cleaning_page'),
    path('Painting_page',views.Painting_page,name='Painting_page'),
    path('Plumbing_page',views.Plumbing_page,name='Plumbing_page'),
    path('Electrical_page',views.Electrical_page,name='Electrical_page'),

    
    # Client: full job detail + helper requests
    path('jobs/<int:job_id>/detail/',         views.job_detail_client,  name='Job_detail_client'),
 
    # Helper: press "Accept" on a listing → creates JobRequest
    path('jobs/<int:job_id>/accept/',         views.helper_accept_job,  name='Helper_accept_job'),
 
    # Client: press "Hire" on a specific request
    path('requests/<int:request_id>/accept/', views.accept_request,      name='Accept_request'),
 
    # Client: toggle job open ↔ closed
    path('jobs/<int:job_id>/toggle-status/',  views.toggle_job_status,  name='Toggle_job_status'),
 
    # Client: delete a job
    path('jobs/<int:job_id>/delete/',         views.delete_job,         name='Delete_job'),


    path('helper/profile/',         views.Profile_helper,   name='Profile_helper'),
    path('request/<int:request_id>/accept/', views.Accept_request, name='Accept_request'),
]
