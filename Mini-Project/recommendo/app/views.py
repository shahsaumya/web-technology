from app.models import UserProfile
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from app.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from recombee_api_client.api_client import RecombeeClient
from recombee_api_client.api_requests import *
client = RecombeeClient('sns', 'cqLZqZnboKlyVKS7EhhYYyM8BflGRDlizngZbljA3kp67tjd1FKfH3WaXLNSXl7F')
from app.models import Movies
import csv

def index(request):
    return render(request,'index.html', {'view_is_index': True})

def dashboard(request):
    return render(request,'dashboard.html')

def movieDesc(request):
    return render(request,'movieDesc.html')

def mdB(request):
    return render(request,'mdB.html')

def ff(request):
    return render(request,'ff.html')

def mdS(request):
    return render(request,'mdS.html')

def gtky(request):
    return render(request,'gtky.html')

def gallery(request):
    return render(request,'gallery.html')

def todo_list(request):
    return render(request,'todo_list.html')

def profile(request):
    return render(request,'profile.html')

def prof(request):
    return render(request,'prof.html')

def home(request):
    if request.user.is_authenticated():
        return redirect(reverse('index'))
    return render(request,'dashboard.html')

def register(request):
    registered = False

    user_form = UserForm()
    profile_form = UserProfileForm()

    # Prevent logged in users from registering again
    if request.user.is_authenticated():
       return redirect(reverse('index'))

    else:
        return render(request, 'signup.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

@csrf_protect
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        print(username)
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                auth_login(request, user)
                return redirect(reverse('gtky'))
            else:
                return HttpResponse("Your account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print ("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    elif request.method == 'GET':
        print(request.user)
        if request.user.is_authenticated:
             return redirect(reverse('gtky'))
        else:
            return render(request, 'login.html', {})

def add_user(request):
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            try:
                user.set_password(user.password)
                user.save()
                print(user)
                print(type(user.id))
                user_id = user.id
                profile = profile_form.save(commit=False)
                profile.user = user

                profile.save()
                registered = True

                try:
                    print('Sending')
                    request_user = AddUser(str(user_id))
                    client.send(request_user)
                    print('Sent')

                except:
                    print('Not sent')

                return redirect(reverse('login'))

            except:
                return redirect(reverse('login'))


        else:
            print (user_form.errors, profile_form.errors)
            return redirect(reverse('register'))
    else:
        return redirect(reverse('login'))

@login_required
def logout(request):
    # Since we know the user is logged in, we can now just log them out.
    auth_logout(request)
    # Take the user back to the homepage.
    return HttpResponseRedirect('/login/')
