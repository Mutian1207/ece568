from django.shortcuts import render,redirect
from django.views.generic import (TemplateView,ListView,DeleteView,
                                    CreateView,UpdateView,DetailView,RedirectView
                                    )
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView,LogoutView
from .models import Users,Rides,Sharers
from .forms import UserRegisterForm,CreateOrderForm
from django.urls import reverse_lazy
# Create your views here.
class IndexView(TemplateView):
    template_name = "homepage.html"

#register view
class RegisterView(CreateView):   
    template_name = "register.html"
    form_class = UserRegisterForm
    success_url = reverse_lazy("basicapp:homepage")
  
        

#login view
class UserLoginView(LoginView):
    template_name = "login.html"
    next_page = '/'
    
#logout view
class UserLogoutView(LogoutView):
    next_page = '/'
    template_name="base.html"

#create order view
class CreateOrderView(CreateView):
    template_name = "homepage.html"
    form_class = CreateOrderForm

    success_url = reverse_lazy("basicapp:ordersuccess")
#order success view
class OrderSuccessView(TemplateView):
    template_name = "ordersuccess.html"



#personal info view
class PersonalInfoView(LoginRequiredMixin,DetailView):
    model = Users
    template_name = "personalinfo.html"


         
        