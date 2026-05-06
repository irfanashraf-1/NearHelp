from django.shortcuts import render

# Create your views here.
def Welcomepage(request):
    return render(request,'welcome.html')
def Job_signup(request):
    return render(request,'job_signup_form.html')