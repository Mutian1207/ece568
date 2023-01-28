from django.shortcuts import render,redirect
from django.views.generic import (TemplateView,ListView,DeleteView,
                                    CreateView,UpdateView,DetailView,RedirectView
                                    )
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView,LogoutView
from .models import Users,Rides,Sharers
from .forms import UserRegisterForm
from django.urls import reverse,reverse_lazy
# Create your views here.
class IndexView(TemplateView):
    template_name = "homepage.html"

#register view
class RegisterView(CreateView):   
    template_name = "register.html"
    form_class = UserRegisterForm
    success_url = reverse_lazy("basicapp:homepage")
  
#login view
class UserLogin(LoginView):
    template_name = "login.html"
    next_page = reverse_lazy("basicapp:homepage")
    
#logout view
class UserLogout(LogoutView):
    next_page = reverse_lazy("basicapp:homepage")

#yourrides view
class UserRides(DetailView):
    model = Rides
    template_name = "userrides.html"

    def get_queryset(self):
        return Rides.objects.filter(status = 'op')




