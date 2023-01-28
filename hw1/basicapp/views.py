from django.shortcuts import render,redirect
from django.views.generic import (TemplateView,ListView,DeleteView,
                                    CreateView,UpdateView,DetailView,RedirectView
                                    )
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView,LogoutView
from .models import Users,Rides,Sharers
from .forms import UserRegisterForm,CreateOrderForm,EditOpenRideForm
from django.urls import reverse,reverse_lazy
# Create your views here.
class IndexView(TemplateView):
    template_name = "homepage.html"

#register view
class RegisterView(CreateView):
    model = Users
    template_name = "register.html"
    form_class = UserRegisterForm
    success_url = reverse_lazy("basicapp:homepage")
  
#login view
class UserLoginView(LoginView):
    template_name = "login.html"
    next_page = reverse_lazy("basicapp:homepage")
    
#logout view
class UserLogoutView(LogoutView):
    next_page = '/'
    template_name="base.html"

#openrides view
class UserOpenRidesView(ListView):
    model = Rides
    context_object_name = "open_ride_list"
    template_name = "userrides.html"

#sharerides view
class UserShareRidesView(ListView):
    context_object_name = "share_ride_list"
    template_name = "userrides.html"

    def get_queryset(self):
        return Sharers.objects.all()

#create order view
class CreateOrderView(CreateView):
    template_name = "homepage.html"
    form_class = CreateOrderForm

    success_url = reverse_lazy("basicapp:ordersuccess")
 
    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user.pk
        self.object.sharable = True
        self.object.status = 'op'
        self.object.save()
        return super().form_valid(form)

#order success view
class OrderSuccessView(TemplateView):
    template_name = "ordersuccess.html"


#personal info view
class PersonalInfoView(LoginRequiredMixin,DetailView):
    model = Users
    template_name = "personalinfo.html"

#update personal info view
class UpdateInfoView(LoginRequiredMixin,UpdateView):
    model = Users
    template_name="updateinfo.html"

    fields = ['is_driver','vehic_type','lice_plate_number','max_pass_num','other_reg']
    success_url = '/'
    
class EditOpenRideView(UpdateView):
    model = Rides
    form_class = EditOpenRideForm
    template_name = "editrides.html"
    pass

         
