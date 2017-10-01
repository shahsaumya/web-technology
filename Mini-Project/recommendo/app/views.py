from app.models import UserProfile
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from app.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect, csrf_exempt

from app.models import Movies
import csv

def index(request):
    # reader = csv.reader(open("/home/saumya/Desktop/WT/Mini-Project/ml-latest-small/combined.csv"))

    # for row in reader:
    #     mid = row[0]
    #     title = row[1]
    #     genre = row[2]
    #     imdb = row[3]
    #     tmdb = row[4]
    #     Movies.objects.get_or_create(movieId = mid,title = title,genres = genre,imdbId = imdb,tmdbId = tmdb)

    return render(request,'index.html', {'view_is_index': True})

def home(request):
    if request.user.is_authenticated():
        return redirect(reverse('index'))
    return render(request,'home.html')


def signupLogin(request):
    return render(request,'signupLogin.html')

def register(request):
    registered = False

    user_form = UserForm()
    profile_form = UserProfileForm()

    # Prevent logged in users from registering again
    if request.user.is_authenticated():
       return redirect(reverse('index'))

    else:
        return render(request, 'register.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


@csrf_protect
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('index'))
            else:
                return HttpResponse("Your account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print ("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    elif request.method == 'GET':
        print(request.user)
        if request.user.is_authenticated:
             return redirect(reverse('index'))
        else:
            return render(request, 'sign-in.html', {})


def add_user(request):
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            try:
                user.set_password(user.password)
                user.save()

                profile = profile_form.save(commit=False)
                profile.user = user

                profile.save()
                registered = True
                return redirect(reverse('sign-in'))

            except:
                return redirect(reverse('sign-in'))

        else:
            print (user_form.errors, profile_form.errors)
            return redirect(reverse('register'))
    else:
        return redirect(reverse('sign-in'))

@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)
    # Take the user back to the homepage.
    return HttpResponseRedirect(reverse('home'))
