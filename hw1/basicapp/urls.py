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
<<<<<<< HEAD
    re_path(r'^/(?P<pk>\d+)/$',views.PersonalInfoView.as_view(),name = "personalinfo"),
<<<<<<< HEAD
    re_path(r'^rides/(?P<pk>\d+)/$',views.UserRidesView.as_view(),name = "rides"),
=======
    re_path(r'^info/(?P<pk>\d+)/$',views.PersonalInfoView.as_view(),name = "personalinfo"),
    re_path(r'^updateinfo/(?P<pk>\d+)/$',views.UpdateInfoView.as_view(),name = "updateinfo"),
    re_path(r'^rides/(?P<pk>\d+)/$',views.UserRidesView.as_view(),name = "rides"),


    
>>>>>>> e94d2f59f8ec495c1fb1d72f4c910a59ca0c01b5
=======
    re_path(r'^rides/(?P<pk>\d+)/$',views.UserOpenRidesView.as_view(),name = "rides"),
>>>>>>> kirk
]