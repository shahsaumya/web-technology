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
import requests, json

def index(request):
    return render(request,'index.html', {'view_is_index': True})

def dashboard(request):
    current_user = request.user
    user_id=current_user.id
    movies=[]
    posters=[]
    recommended = client.send(UserBasedRecommendation(user_id,'5'))
    print(recommended)
    for choice in recommended:
        add=""
        travel = Movies.objects.filter(movieId__icontains=choice)
        movies.append(travel)
        name = travel.values_list("title", flat=True).first()
        print(name)
        splitted = name.split(' ')
        if(len(splitted)==1):
            url = "https://api.themoviedb.org/3/search/movie?api_key=b2ab260c085a2d708971348fc410b93c&language=en-US&query="+name+"&page=1&include_adult=false"
            r = requests.get(url)
        else:
            for i in range(0, len(splitted)-1):
                add=add+splitted[i]+"%20"
            url = "https://api.themoviedb.org/3/search/movie?api_key=b2ab260c085a2d708971348fc410b93c&language=en-US&query="+add+"&page=1&include_adult=false"
            r = requests.get(url)
        poster = "https://image.tmdb.org/t/p/w300_and_h450_bestv2" + json.loads(r.content)["results"][0]["poster_path"]
        print(poster)
        posters.append(poster)
    return render(request,'dashboard.html',{'posters':posters})

def movieDesc(request):
    return render(request,'movieDesc.html')

def mdB(request):
    return render(request,'mdB.html')

@csrf_protect
@csrf_exempt
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

def send_choices(request):
    current_user = request.user
    ratings = []
    final=[]
    print(current_user.id)
    user_id = current_user.id;
    choices = request.GET.get('pp')
    print(choices)
    if(choices):
        final.append(choices)
    choices = request.GET.get('is')
    if(choices):
        final.append(choices)
    choices = request.GET.get('pom')
    if(choices):
        final.append(choices)
    choices = request.GET.get('tfios')
    print(choices)
    if(choices):
        final.append(choices)
    choices = request.GET.get('whms')
    if(choices):
        final.append(choices)
    choices = request.GET.get('sp')
    if(choices):
        final.append(choices)
    choices = request.GET.get('dp')
    if(choices):
        final.append(choices)
    choices = request.GET.get('gb')
    if(choices):
        final.append(choices)
    choices = request.GET.get('spectre')
    if(choices):
        final.append(choices)
    print(final)
    for choice in final:
        interaction = AddDetailView(user_id, choice,
                    #optional parameters:
                cascade_create=True
                )
        ratings.append(interaction)

    try:
        print('sending')
        client.send(Batch(ratings))
        print('Send')
        return redirect(reverse('dashboard'))

    except APIException as e:
        print(e)
        return redirect(reverse('gtky'))

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
