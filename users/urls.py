
from django.conf.urls import include, url
from users.views import dashboard, register, login, logout, password_change, password_reset

urlpatterns = [
    url(r"^login/", login, name="login"),
    url(r"^logout/", logout, name="logout"),
    url(r"^password_change/", password_change, name="password_change"),
    url(r"^password_reset/", password_reset, name="password_reset"),
    url(r"^dashboard/", dashboard, name="dashboard"),
    url(r"^register/", register, name="register"),
]