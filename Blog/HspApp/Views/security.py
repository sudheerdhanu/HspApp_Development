from django.contrib import messages
from django.contrib.auth import authenticate, login

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .EmailBackend import CustomBackend
from ..models import Profile

def sign_up(request):

    if request.user.is_authenticated:
        return redirect('home_page')
    else:
        if request.method=='POST':
            try:
                print("Post data", request.POST)
                first_name = request.POST.get('first_name')
                last_name = request.POST.get('last_name')
                email = request.POST.get('email')
                username = request.POST.get('username')
                address = request.POST.get('address')
                password = request.POST.get('password')
                mobile = request.POST.get('mobile')
                user = User.objects.create_user(first_name=first_name, last_name=last_name,email=email,
                                           username=username, password=password)
                user.profile.address = address
                user.profile.email = email
                user.profile.mobile = mobile
                user.profile.active = True
                user.is_staff = True
                user.save()
                messages.success(request, 'Form submission successful')
                user1=authenticate(request, username=user, password=password)
                print(user1)

                if user1 is not None:
                    login(request, user1)
                    messages.info(request, f"You are now logged in as {username}")
                    return redirect('home_page')

                return HttpResponse('invalid')



            except Exception as e:
                return HttpResponse(e.__repr__())


        return render(request,'security/register.html')



def login1(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        user = authenticate(request,username=username, password=password)
        print(user)

        if user is not None:
            login(request, user)
            messages.info(request, f"You are now logged in as {username}")
            return redirect('home')

        else:
            messages.error(request, "Invalid username or password.")
            return HttpResponse("Invalid")

    return render(request,'registration/login.html')

