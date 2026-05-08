from django.shortcuts import render

# Create your views here.
def Welcomepage(request):
    return render(request,'welcome.html')
def Job_signup_page(request):
    return render(request,'job_signup_form.html')
def Client_signup_page(request):
    return render(request,'client_signup_page.html')
def Login_page(request):
    return render(request,'login_page.html')