from django.conf.urls import include, url
from django.urls import path
from . import views
from spirit.views import dashboard, spiritWeek, flappyEagle, brickBreaker, brickBreakerScoreUpdate, flappyEagleScoreUpdate, airHockeyScoreUpdate
from spirit.views import profile_upload
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="home"),
    path('accounts/register/',views.register, name="register"),
    path('accounts/', include('django.contrib.auth.urls')),
    url(r"^dashboard/", dashboard, name="dashboard"),
    url(r"^spiritWeek/", spiritWeek, name="spiritWeek"),
    
    url(r"^flappyEagle/", flappyEagle, name="flappyEagle"),
    url(r"^flappyEagleScoreUpdate/", flappyEagleScoreUpdate, name="flappyEagleScoreUpdate"),
    url(r"^brickBreaker/", brickBreaker, name="brickBreaker"),
    url(r"^brickBreakerScoreUpdate/", brickBreakerScoreUpdate, name="brickBreakerScoreUpdate"),
    url(r"^airHockeyScoreUpdate/", airHockeyScoreUpdate, name="airHockeyScoreUpdate"),

    #Score Updates
    
    path('upload-csv/', profile_upload, name="profile_upload"),
]