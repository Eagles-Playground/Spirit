# users/views.py

from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.hashers import make_password, check_password

from users.forms import RegisterForm, LoginForm
from users.models import Student

def dashboard(request):
    return render(request, "users/dashboard.html")

def register(request):
    if request.method == "GET":
        return render(
            request, "users/register.html",
            {"form": RegisterForm}
        )
    elif request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            #saves user to database
            #not the most efficient way to do it,
            #but the right way was giving me lots of bugs
            user = form.save()
            user.password = make_password(user.password)
            user.save()
            #logs user in
            request.session["id"] = user.id
            request.session["name"] = user.username
            return redirect(reverse("dashboard"))
        print(form.errors)
        return render(request, "users/register.html", {"form": form})

def login(request):
    if request.method == "GET":
        return render(
            request, "registration/login.html",
            {"form": LoginForm}
        )
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = Student.objects.get(username=form.cleaned_data.get("username"))
            request.session["id"] = user.id
            request.session["name"] = user.username
            return redirect(reverse("dashboard"))
    return render(request, "users/login.html", {"form": form})

def logout(request):
    request.session.clear()
    return redirect(reverse("dashboard"))

#TODO
def password_change(request):
    return redirect(reverse("dashboard"))

def password_reset(request):
    return redirect(reverse("dashboard"))