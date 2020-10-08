# users/views.py

from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.hashers import make_password, check_password

from users.forms import RegisterForm

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
        return render(request, "users/register.html", {"form": RegisterForm})