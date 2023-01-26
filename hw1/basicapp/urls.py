from django.urls import path
from django.contrib import admin

from . import views
app_name = "basicapp"
urlpatterns = [
    path('', views.IndexView.as_view(), name="homepage"),
    path('register/',views.RegisterView.as_view(),name = "register"),
    path('login/',views.UserLogin.as_view(),name = "login"),
    path('logout/',views.UserLogout.as_view(),name = "logout"),
    
]