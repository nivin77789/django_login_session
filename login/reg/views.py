from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate
from django.contrib.auth import login ,logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control,never_cache
from django.contrib import messages

# Create your views here.


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@never_cache
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
            messages.error(request, "Username or Password is incorrect")
    return render(request,'login.html')




@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@never_cache
@login_required(login_url='logins')
def home(request):
    return render(request,'home.html')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@never_cache
def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        email = request.POST.get('email', '')
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1!=password2:
            messages.error(request, "Password is mismatching")
        else:
            data=User.objects.create_user(username=username,email=email,password=password1)
            data.save()
            return redirect('logins')
        
    return render(request,'signup.html')



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@never_cache
def LogoutPage(request):
    logout(request)
    return redirect('logins') 