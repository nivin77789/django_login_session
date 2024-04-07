from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate
from django.contrib.auth import login 
from django.http import HttpResponse

# Create your views here.
def logins(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        email = request.POST.get('email')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password is incorrect")
    return render(request,'login.html')





def home(request):
    return render(request,'home.html')

def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        email = request.POST.get('email', '')
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1!=password2:
            return HttpResponse("password is not matching")
        else:
            data=User.objects.create_user(username=username,email=email,password=password1)
            data.save()
            return render(request,'login.html')
        
    return render(request,'signup.html')