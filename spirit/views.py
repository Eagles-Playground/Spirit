from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from spirit.forms import (RegistrationForm, EditProfileForm)
import csv, io
from django.contrib import messages
from spirit.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.http import HttpResponse

from spirit.models import UserProfile

def register(request):
    context = {}
    form = RegistrationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request,user)
            return render(request,'users/dashboard.html')
    context['form']=form
    return render(request,'users/dashboard.html',context)

def dashboard(request):
    scores1 = UserProfile.objects.order_by("-score1")[:5]
    scores2 = UserProfile.objects.order_by("-score2")[:5]
    scores3 = UserProfile.objects.order_by("-score3")[:5]
    args = {'user': request.user, "scores1": scores1, "scores2": scores2, "scores3": scores3,}
    return render(request, "users/dashboard.html", args)

def spiritWeek(request):
    return render(request, "users/spiritWeek.html")

def flappyEagle(request):
    args = {'user': request.user}
    return render(request, "users/flappyEagle.html", args)

def brickBreaker(request):
    args = {'user': request.user}
    return render(request, "users/brickBreaker.html", args)

def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'users/dashboard.html', args)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('users:view_profile'))
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'users/edit_profile.html', args)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('users:view_profile'))
        else:
            return redirect(reverse('users:change_password'))
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'users/change_password.html', args)

def profile_upload(request): #Mack's Don't touch
    template = "profile_upload.html"
    data = userProfile.objects.all()
    prompt = {
        'order': 'Order of the CSV should be email, first name, last name, grade, scores',
        'profiles': data    
              }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')
    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = User.objects.update_or_create(
            id=column[0],
            password=column[1],
            last_login=column[2],
            is_superuser=column[3],
            email=column[4],
            first_name=column[5],
            last_name=column[6],
            is_active=column[7],
            is_staff=column[8],
            date_joined=column[9],
            grade=column[10],
            score1=column[11],
            score2=column[12],
            score3=column[13]
        )
    context = {}
    return render(request, template, context)

#AJAX routes:
def flappyEagleScoreUpdate(request):
  if request.method == 'POST':
    print(request.headers["score"])
    #checks for user
    if not request.user.is_authenticated:
      return redirect("register")
    if request.user.score1 < int(request.headers["score"]):
      request.user.score1 = int(request.headers["score"])
      request.user.save()
      return HttpResponse("True")
    return HttpResponse("False")

  #in case someone goes to the url
  if request.method == 'GET':
    return redirect("flappyEagle")

def brickBreakerScoreUpdate(request):
  if request.method == 'POST':
    print("hi!")
    #checks for user
    if not request.user.is_authenticated:
      return redirect("register")

    print(request.user.score)
    print(int(request.headers["score"]))
    if request.user.score2 < int(request.headers["score"]):
      request.user.score2 = int(request.headers["score"])
      request.user.save()
      return render(request, "users/brickBreak.html", {"form": form})
    return render(request, "users/brickBreak.html")

  #in case someone goes to the url
  if request.method == 'GET':
    return redirect("brickBreaker")

def airHockeyScoreUpdate(request):
  if request.method == 'POST':
    #checks for user
    if not request.user.is_authenticated:
      return redirect("register")
    if request.user.score3 < int(request.headers["score"]):
      request.user.score3 = int(request.headers["score"])
      request.user.save()
      return HttpResponse("True")
    return HttpResponse("False")

  #in case someone goes to the url
  if request.method == 'GET':
    return redirect("dashboard")

  def leaderboard (request):
    Entry.objects.filter(score1 = 0).order_by('-score1', 'Leaders')
    #remember to do the stuff in the shell     // https://docs.djangoproject.com/en/3.1/ref/models/querysets/