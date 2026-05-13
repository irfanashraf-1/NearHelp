from django.shortcuts import render ,redirect
from projectnearhelpapp.models import Client_details , Helper_details
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
def Home(request):
    return render(request,'home.html')
def Job_posting_form(request):
    return render(request,'job_posting_form.html')

def Admin_dashboard(request):
    return render(request,'admin_dashboard.html')
def Helper_data_table(request):
    return render(request,'helper_data_table.html')
def Client_data_table(request):
    return render(request,'client_data_table.html')
def Users_data_table(request):
    return render(request,'users_data_table.html')


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

        if password == confirm_passsword :
            if User.objects.filter(username = phone_number).exists():
                messages.info(request,'This phone number already has an account.')
                return redirect('Client_signup_page')
            else:
                user = User.objects.create_user(first_name= fullname , username= phone_number , email= email , password= password)
                user.save()

                client_data = Client_details(  Fullname = fullname,
                                            Phone_number = phone_number,
                                            Email = email,
                                            Area = area,
                                            Town = town,
                                            Pin = pin,
                                            Password = password )
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
                                                Password = password )
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
                return redirect('Home')
        else:
            messages.info(request,'invalid username or password')
            return redirect('Login_page')

