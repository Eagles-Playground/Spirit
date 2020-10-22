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
    if request.user.is_authenticated:
      return redirect("dashboard")
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

def leaderboard(request):
    #gets students by grade
    #freshmen
    try:
      freshmen = UserProfile.objects.filter(grade=9)
    except:
      freshmen = None
    #sophmore
    try:
      sophomore = UserProfile.objects.filter(grade=10)
    except:
      sophomore = None
    #junior
    try:
      junior = UserProfile.objects.filter(grade=11)
    except:
      junior = None
    #senior
    try:
      senior = UserProfile.objects.filter(grade=12)
    except:
     senior = None
    #filter data for template
    scorearr9 = []
    scorearr10 = []
    scorearr11 = []
    scorearr12 = []
    #freshman
    f_total = 0
    soph_total = 0
    j_total = 0
    s_total = 0
    for student in freshmen:
      highscore = student.score1 + student.score2 + student.score3
      scorearr9.append({"name": student.first_name, "score": highscore})
      f_total = f_total + highscore
    #sophomore
    for student in sophomore:
      highscore = student.score1 + student.score2 + student.score3
      scorearr10.append({"name": student.first_name, "score": highscore})
      soph_total = soph_total + highscore
    #junior
    for student in junior:
      highscore = student.score1 + student.score2 + student.score3
      scorearr11.append({"name": student.first_name, "score": highscore})
      j_total = j_total + highscore
    #senior
    for student in senior:
      highscore = student.score1 + student.score2 + student.score3
      scorearr12.append({"name": student.first_name, "score": highscore})
      s_total = s_total + highscore

    #sort data by score
    scorearr9 = sorted(scorearr9, key = lambda i: i['score'], reverse=True)
    scorearr10 = sorted(scorearr10, key = lambda i: i['score'], reverse=True)
    scorearr11 = sorted(scorearr11, key = lambda i: i['score'], reverse=True)
    scorearr12 = sorted(scorearr12, key = lambda i: i['score'], reverse=True)
    args = {'user': request.user, "freshmen": scorearr9, "sophomore": scorearr10, "junior": scorearr11, "senior": scorearr12, "fhigh":f_total, "sophHigh":soph_total, "jHigh": j_total, "senHigh": s_total}
    return render(request, "users/leaderboard.html", args)

def flappyEagle(request):
    args = {'user': request.user}
    return render(request, "users/flappyEagle.html", args)

def runawayStudents(request):
    args = {'user': request.user}
    return render(request, "users/flappyEagle.html", args)

def brickBreaker(request):
    args = {'user': request.user}
    return render(request, "users/brickBreaker.html", args)

def airHockey(request):
    args = {'user': request.user}
    return render(request, "users/airHockey.html", args)

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
      return HttpResponse("False")
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
    #checks for user
    if not request.user.is_authenticated:
      return redirect("register")
    if request.user.score2 < int(request.headers["score"]):
      request.user.score2 = int(request.headers["score"])
      request.user.save()
      return HttpResponse("True")
    return HttpResponse("False")

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

