from django.shortcuts import render ,redirect
from projectnearhelpapp.models import Client_details , Helper_details, Job_postings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User , auth
from django.contrib import messages
from django.contrib.auth import login


# Create your views here.
def Welcomepage(request):
    return render(request,'welcome.html')
def Helper_signup_page(request):
    return render(request,'helper_signup_page.html')
def Client_signup_page(request):
    return render(request,'client_signup_page.html')
def Login_page(request):
    return render(request,'login_page.html')

@login_required
def Home_helper(request):
    return render(request,'home_helper.html')

@login_required
def Home_client(request):
    return render(request,'home_client.html')

def Job_posting_form(request):
    return render(request,'job_posting_form.html')

@login_required
def Admin_dashboard(request):
    return render(request,'admin_dashboard.html')
def Helper_data_table(request):
    return render(request,'admin_dashboard/helper_data_table.html')
def Client_data_table(request):
    return render(request,'admin_dashboard/client_data_table.html')
def User_data_table(request):
    return render(request,'admin_dashboard/user_data_table.html')

# Profile pages
def Profile_client(request):
    return render(request,'profile_client.html')
def Profile_helper(request):
    return render(request,'profile_helper.html')

#Category pages
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

                client_data = Client_details(   Fullname = fullname,
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
        budget = request.POST.get('budget')
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
                                    Budget = budget,
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
