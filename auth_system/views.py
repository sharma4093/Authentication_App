from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def LOGIN(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password = password)
        if user is not None:
            login(request,user)
            return redirect('home')
            messages.success(request,'Successfully logged in!')
        elif user is None:
            messages.error(request,'Please enter email and password! ')
            return redirect('login_page')
        else:
            message.error(request,'Invalid email or password!')
    return render(request, 'login.html')


def REGISTRATION(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        mobile_no = request.POST.get('mobile_no')
        address = request.POST.get('address')
        
        if User.objects.filter(username=username).exists():
            messages.warning(request,'Username already exists! ')
            return render(request,'registration_page.html')
        if User.objects.filter(email=email).exists():
            messages.warning(request,'Email already exists! ')
            return render(request,'registration_page.html')
        else:
             new_user = User.objects.create_user(username, email, password )
             new_user.first_name=first_name
             new_user.last_name=last_name
             new_user.mobile_no = mobile_no
             new_user.address = address
       
             new_user.save()
             return redirect('login_page')
    return render(request, 'registration_page.html')



def F_PASSWORD(request): 
    return render(request, 'forgot_password.html')

@login_required
def HOME(request):

    return render(request, 'home.html')

@login_required
def logOut(request):
    logout(request)
    return redirect('login_page')