# users/views.py

from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse

from users.forms import CustomUserCreationForm
from django.contrib.auth.hashers import make_password, check_password
from users.forms import RegisterForm

def dashboard(request):
    return render(request, "users/dashboard.html")

def flappyEagle(request):
    return render(request, "users/flappyEagle.html")

def brickBreaker(request):
    return render(request, "users/brickBreaker.html")

def register(request):
    if request.method == "GET":
        return render(
            request, "users/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("dashboard"))