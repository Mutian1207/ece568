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
    re_path(r'^info/(?P<pk>\d+)/$',views.PersonalInfoView.as_view(),name = "personalinfo"), # personal info view
    re_path(r'^updateinfo/(?P<pk>\d+)/$',views.UpdateInfoView.as_view(),name = "updateinfo"), # update personal info view
    re_path(r'^myrides/(?P<pk>\d+)/$',views.UserOpenRidesView.as_view(),name = "rides"),# my rides view
    re_path(r'^todrive/(?P<pk>\d+)/$',views.ToDriveView.as_view(),name = "todrive"),# To drive view
    re_path(r'^driveconfirm/(?P<pk>\d+)/$',views.ConfirmDriveView.as_view(),name="confirmdrive"),# Driver confirm drive
    re_path(r'^joinshare/(?P<pk>\d+)/$',views.JoinShareView.as_view(),name="joinshare"), # all sharable orders suitable
    re_path(r'^joininfo/(?P<pk>\d+)/$',views.JoinInfoView.as_view(),name="editjoininfo"),# edit join share info
    re_path(r'^editopenride/(?P<pk>\d+)/$',views.EditOpenRideView.as_view(),name="editride"),# edit open ride info 
    re_path(r'^sharesearch/(?P<pk>\d+)/$',views.ShareSearchView.as_view(),name="shareforsearch"), # share search
    re_path(r'^myrideinfo/(?P<pk>\d+)/$',views.RideDetailView.as_view(),name="rideinfo"), #view ride detail
    re_path(r'^myshareinfo/(?P<pk>\d+)/$',views.ShareDetailView.as_view(),name="sharerideinfo"), #view share detail
    re_path(r'^deleteride/(?P<pk>\d+)/$',views.RideDeleteView.as_view(),name="deleteride"), #delete open detail
    re_path(r'^deleteshare/(?P<pk>\d+)/$',views.ShareDeleteView.as_view(),name="deleteshare"), #delete share info
    re_path(r'^mydriveinfo/(?P<pk>\d+)/$',views.DriveDetailView.as_view(),name="driveinfo") #view drive detail
]