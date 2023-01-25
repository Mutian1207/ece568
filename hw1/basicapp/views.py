from django.shortcuts import render,redirect
from django.views.generic import (TemplateView,ListView,DeleteView,
                                    CreateView,UpdateView,DetailView,RedirectView
                                    )
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView,LogoutView
from .models import Users,Rides,Sharers
from .forms import UserRegisterForm
# Create your views here.
class IndexView(TemplateView):
    template_name = "homepage.html"

#register view
class RegisterView(CreateView):   
    template_name = "register.html"
    form_class = UserRegisterForm

    def get_success_url(self,request):
        return rediect(reverse('basicapp:homepage'))
        

#login view
class UserLogin(LoginView):
    template_name = "login.html"
#logout view
class UserLogout(LogoutView):
    pass




