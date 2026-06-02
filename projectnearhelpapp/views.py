from django.shortcuts import render ,redirect
from projectnearhelpapp.models import Client_details , Helper_details, Job_postings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User , auth
from django.contrib import messages
from django.contrib.auth import login
from datetime import datetime




def Welcomepage(request):
    return render(request,'welcome.html')
#Login & Signup 
def Helper_signup_page(request):
    return render(request,'login_signup/helper_signup_page.html')
def Client_signup_page(request):
    return render(request,'login_signup/client_signup_page.html')
def Login_page(request):
    return render(request,'login_signup/login_page.html')

#Home page
@login_required
def Home_helper(request):
    return render(request,'home_helper.html')

@login_required
def Home_client(request):
    client = request.user.client_details  
    client_jobs = Job_postings.objects.filter(Client=request.user)
    context = {
        'client': client,
        'client_jobs': client_jobs,
        'total_jobs': client_jobs.count(),
        'open_jobs': client_jobs.filter(Status='open').count(),     
        'completed_jobs': client_jobs.filter(Status='closed').count(),
    }
    return render(request,'home_client.html', context)

#job posting form
def Job_posting_form(request):
    return render(request,'job_posting_form.html')

#Admin page
@login_required
def Admin_dashboard(request):
    return render(request,'admin_dashboard/admin_dashboard.html')

# Profile 
def Profile_client(request):
    client = request.user.client_details  
    client_jobs = Job_postings.objects.filter(Client=request.user)
    context = {
        'client': client,
        'client_jobs': client_jobs,
        'total_jobs': client_jobs.count(),
        'open_jobs': client_jobs.filter(Status='open').count(),     
        'completed_jobs': client_jobs.filter(Status='closed').count(),
    }
    return render(request,'profile_pages/profile_client.html', context)

def Profile_helper(request):
    return render(request,'profile_pages/profile_helper.html')

#Categories
def Carpentry_page(request):
    return render(request,'category/carpentry_cat_page.html')
def Plumbing_page(request):
    return render(request,'category/plumbing_cat_page.html')
def Electrical_page(request):
    return render(request,'category/electrical_cat_page.html')
def Cleaning_page(request):
    return render(request,'category/cleaning_cat_page.html')
def Painting_page(request):
    return render(request,'category/painting_cat_page.html')
def Moving_page(request):
    return render(request,'category/moving_cat_page.html')
def Gardening_page(request):
    return render(request,'category/gardening_cat_page.html')
def Techhelp_page(request):
    return render(request,'category/techhelp_cat_page.html')


def Save_client_data(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        area = request.POST.get('area')
        town = request.POST.get('town')
        pin = request.POST.get('pin')
        password = request.POST.get('password')
        confirm_passsword = request.POST.get('confirm_passsword')
        preferred_language = request.POST.get('language')
        preferred_contact_method = request.POST.get('contact_preference')

        if password == confirm_passsword :
            if User.objects.filter(username = phone_number).exists():
                messages.info(request,'This phone number already has an account.')
                return redirect('Client_signup_page')
            else:
                user = User.objects.create_user(first_name= fullname , username= phone_number , email= email , password= password)
                user.save()

                client_data = Client_details(   
                                                user=user,
                                                Fullname = fullname,
                                                Phone_number = phone_number,
                                                Email = email,
                                                Area = area,
                                                Town = town,
                                                Pin = pin,
                                                Password = password,
                                                Preferred_language = preferred_language,
                                                Preferred_contact_method = preferred_contact_method )
                client_data.save()

                return redirect('Login_page')
            

def Save_helper_data(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        phone_number = request.POST.get('phone')
        email = request.POST.get('email')
        photo = request.FILES.get('photo')
        area = request.POST.get('area')
        town = request.POST.get('town')
        pin = request.POST.get('pin')
        category = request.POST.get('category')
        availability = request.POST.get('availability')
        password = request.POST.get('password')
        confirm_passsword = request.POST.get('confirm_passsword')
        

        if password == confirm_passsword :
            if User.objects.filter(username = phone_number).exists():
                messages.info(request,'This phone number already has an account.')
                return redirect('Helper_signup_page')
            else:
                user = User.objects.create_user(first_name= fullname , username= phone_number , email= email , password= password)
                user.save()

                helper_data = Helper_details(   Fullname = fullname,
                                                Dob = dob,
                                                Gender = gender,
                                                Phone_number = phone_number,
                                                Email = email,
                                                Photo = photo,
                                                Area = area,
                                                Town = town,
                                                Pin = pin,
                                                Category = category,
                                                Availability = availability,
                                                Password = password  )
                                            
                helper_data.save()
                
                return redirect('Login_page')
            
def Login(request):
    if request.method == 'POST':
        
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')

        user = auth.authenticate(username =  phone_number, password = password)

        if user is not None :
            if user.is_staff:
                login(request,user)
                return redirect('Admin_dashboard')
            else:
                auth.login(request,user)
                user = request.user
                if Client_details.objects.filter(Phone_number = phone_number).exists():
                    if hasattr(user, 'client_details'):
                        context = {
                            'role': 'Client',
                            'profile': user.client_details, 
                        }
                    return redirect('Home_client')
                elif Helper_details.objects.filter(Phone_number = phone_number).exists():
                    if hasattr(user, 'helper_details'):
                        context = {
                            'role': 'Helper',
                            'profile': user.helper_details, 
                        }
                    return redirect('Home_helper')
        else:
            messages.info(request,'invalid username or password')
            return redirect('Login_page')

    # if request.method == 'POST':
        
    #     phone_number = request.POST.get('phone_number')
    #     password = request.POST.get('password')
    #     user = auth.authenticate(username =  phone_number, password = password)

    #     if user is not None :
    #         if user.is_staff:
    #             login(request,user)
    #             return redirect('Admin_dashboard')
    #         else:
    #             client = Client_details.objects.filter(Phone_number = phone_number).first()
    #             helper = Helper_details.objects.filter(Phone_number = phone_number).first()
    #             if client and client.password == password:
    #                 request.session['user_id'] = client.id
    #                 request.session['user_type'] = 'client'
    #                 return redirect('Client_profile')

    #             elif helper and helper.password == password:
    #                 request.session['user_id'] = helper.id
    #                 request.session['user_type'] = 'helper'
    #                 return redirect('Helper_profile')
    #     else:
    #         messages.info(request,'invalid username or password')
    #         return redirect('Login_page')
        
# def Profile_view(request):
#     user_type = request.session.get('user_type')

#     if user_type == 'client':
#         client = Client_details.objects.get(id=request.session['user_id'])
#         return render(request, 'client_profile.html', {'client': client})

#     elif user_type == 'helper':
#         helper = Helper_details.objects.get(id=request.session['user_id'])
#         return render(request, 'helper_profile.html', {'helper': helper})

#     else:
#         return redirect('Login_page')

# Job details posted by client
def Save_job_posting(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        category = request.POST.get('category')
        description = request.POST.get('description')
        photos = request.FILES.get('photos')
        budget_min = request.POST.get('budget_min')
        budget_max = request.POST.get('budget_max')
        duration = request.POST.get('duration')
        urgency = request.POST.get('urgency')
        area = request.POST.get('area')
        town = request.POST.get('town')
        pin = request.POST.get('pin')

        job_postings = Job_postings(
                                    Client = request.user,
                                    Title = title,
                                    Category = category,
                                    Description = description,
                                    Photos = photos,
                                    Budget_min = budget_min,
                                    Budget_max = budget_max,
                                    Duration = duration,
                                    Urgency = urgency,
                                    Area = area,
                                    Town = town,
                                    Pin = pin)
        job_postings.save()
        return redirect('Home_client')
    
    # def Show_job_postings(request):
    #     job_posting = Job_postings.objects.all()
    #     return render(request, 'job_postings.html', {'job_postings': job_postings})

    

# @login_required
# def Profile_dashboard_view(request):
#     user = request.user
    
#     # Check if the logged-in user is a Client
#     if hasattr(user, 'client_details'):
#         context = {
#             'role': 'Client',
#             'profile': user.client_details, 
#         }
#         return render(request, 'profile_client.html', context)
        
#     # Check if the logged-in user is a Worker
#     elif hasattr(user, 'helper_details'):
#         context = {
#             'role': 'Helper',
#             'profile': user.helper_details, 
#         }
#         return render(request, 'profile_helper.html', context)
    
#     return redirect('Login_page')

#Helper signup data table in admin dashboard 
def Helper_data_table(request):
    alldata = Helper_details.objects.all()
    return render(request,'admin_dashboard/helper_data_table.html',{'helperdata':alldata})

def Edit_helper_data_table(request, pk):
    selected_helper = Helper_details.objects.get(id=pk)
    return render(request,'admin_dashboard/edit_helper_data_admin.html',{'selected_helper':selected_helper})

def Update_helper_data_table(request, pk):
    if request.method == 'POST':
        modified = Helper_details.objects.get(id=pk)
        modified.Fullname = request.POST.get('fullname')
        modified.Dob = request.POST.get('dob')
        modified.Gender = request.POST.get('gender')
        modified.Phone_number = request.POST.get('phone')
        modified.Email = request.POST.get('email')
        if request.FILES.get('photo'):
            modified.Photo = request.FILES.get('photo')
        modified.Area = request.POST.get('area')
        modified.Town = request.POST.get('town')
        modified.Pin = request.POST.get('pin')
        modified.Category = request.POST.get('category')
        modified.Availability = request.POST.get('availability')
        modified.save()
        return redirect('Helper_data_table')
    
def Delete_helper_data_table(request, pk):
        deleted = Helper_details.objects.get(id=pk)
        deleted.delete()
        return redirect('Helper_data_table')

#Client signup data table in admin dashboard
def Client_data_table(request):
    alldata = Client_details.objects.all()
    return render(request,'admin_dashboard/client_data_table.html',{'clientdata':alldata})

def Edit_client_data_table(request, pk):
    selected_client = Client_details.objects.get(id=pk)
    return render(request,'admin_dashboard/edit_client_data_admin.html',{'selected_client':selected_client})

def Update_client_data_table(request, pk):
    if request.method == 'POST':
        modified = Client_details.objects.get(id=pk)
        modified.Fullname = request.POST.get('fullname')
        modified.Phone_number = request.POST.get('phone_number')
        modified.Email = request.POST.get('email')
        modified.Area = request.POST.get('area')
        modified.Town = request.POST.get('town')
        modified.Pin = request.POST.get('pin')
        modified.Preferred_language = request.POST.get('language')
        modified.Preferred_contact_method = request.POST.get('contact_preference')
        modified.save()
        return redirect('Client_data_table')

def Delete_client_data_table(request, pk):
        deleted = Client_details.objects.get(id=pk)
        deleted.delete()
        return redirect('Client_data_table')    

#User data table in admin dashboard
def User_data_table(request):
    userdata = User.objects.all()
    return render(request,'admin_dashboard/user_data_table.html',{'userdata':userdata})

def Delete_user_data_table(request, pk):
        deleted = User.objects.get(id=pk)
        deleted.delete()
        return redirect('User_data_table')