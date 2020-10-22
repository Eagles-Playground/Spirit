from django.conf.urls import include, url
from django.urls import path
from . import views
from spirit.views import dashboard, flappyEagle, brickBreaker, brickBreakerScoreUpdate, flappyEagleScoreUpdate, airHockeyScoreUpdate, airHockey, leaderboard, runawayStudents
from spirit.views import profile_upload
from django.contrib import admin

urlpatterns = [

    #basic url
    path('admin/', admin.site.urls),
    path('', views.index,name="home"),

    #account related urls
    path('accounts/register/',views.register, name="register"),
    path('accounts/', include('django.contrib.auth.urls')),
    url(r"^dashboard/", dashboard, name="dashboard"),
    url(r"^leaderboard/", leaderboard, name="leaderboard"),
    
    #Game Related Urls
    url(r"^flappyEagle/", flappyEagle, name="flappyEagle"),
    url(r"^flappyEagleScoreUpdate/", flappyEagleScoreUpdate, name="flappyEagleScoreUpdate"),
    url(r"^brickBreaker/", brickBreaker, name="brickBreaker"),
    url(r"^airHockey/", airHockey, name="airHockeyr"),
    url(r"^runawayStudents/", runawayStudents, name="runawayStudents"),
    url(r"^brickBreakerScoreUpdate/", brickBreakerScoreUpdate, name="brickBreakerScoreUpdate"),
    url(r"^airHockeyScoreUpdate/", airHockeyScoreUpdate, name="airHockeyScoreUpdate"),
  
    #Mass User upload url
    path('upload-csv/', profile_upload, name="profile_upload"),
]