from django.urls import path
from django.contrib import admin
from django.urls import re_path
from . import views
app_name = "basicapp"
urlpatterns = [
    path('', views.CreateOrderView.as_view(), name="homepage"),
    path('register/',views.RegisterView.as_view(),name = "register"),
    path('login/',views.UserLoginView.as_view(),name = "login"),
    path('logout/',views.UserLogoutView.as_view(),name = "logout"),
    path('success/',views.OrderSuccessView.as_view(),name = "ordersuccess"),
    re_path(r'^/(?P<pk>\d+)/$',views.PersonalInfoView.as_view(),name = "personalinfo"),
    re_path(r'^rides/(?P<pk>\d+)/$',views.UserRidesView.as_view(),name = "rides"),
]