
from django.conf.urls import include, url

from users.views import dashboard, register, flappyEagle, brickBreaker

from users.views import dashboard, register


urlpatterns = [
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"^dashboard/", dashboard, name="dashboard"),
    url(r"^register/", register, name="register"),
    url(r"^flappyEagle/", flappyEagle, name="flappyEagle"),
    url(r"^brickBreaker/", brickBreaker, name="brickBreaker"),
]