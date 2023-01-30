from django.shortcuts import render,redirect
from django.views.generic import (TemplateView,ListView,DeleteView,
                                    CreateView,UpdateView,DetailView,RedirectView,
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
    model = Sharers
    context_object_name = "open_ride_list"
    template_name = "userrides.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        user_pk = str(self.request.user.pk)
        sql1 = 'SELECT * FROM basicapp_sharers a' 
        sql2 = ' inner join basicapp_rides b on a.share_id_id=b.ride_id and a.sharer_id_id=' + user_pk
        sql3 = ' inner join basicapp_users c on c.id=b.owner_id'
        data['share_ride_list'] = Sharers.objects.raw(sql1 + sql2 + sql3)
        data['is_driver'] = Users.objects.get(id=self.request.user.pk).is_driver
        if(Users.objects.get(id=self.request.user.pk).is_driver):
            selectitems = 'SELECT * FROM basicapp_users a'
            jointable1 = ' inner join basicapp_rides b on b.driver_acc_id=' + user_pk + 'and a.id=' + user_pk
            #jointable2 = ' inner join basicapp_shares c on b.ride_id=c.share_id_id'
            res = Rides.objects.raw(selectitems + jointable1)
            share_list = {}
            for item in res:
                print(item.ride_id)
                print(Sharers.objects.filter(share_id=item.ride_id))
                ride_id = item.email
                share_list[ride_id] = Sharers.objects.filter(share_id=item.ride_id)
                print(share_list)
            data['drive_ride_list'] = res
            data['sharers_list'] = share_list
        return data

    def get_queryset(self):
        return Rides.objects.filter(owner=self.request.user).order_by('-arr_date_time')

#create order view
class CreateOrderView(CreateView):
    template_name = "homepage.html"
    form_class = CreateOrderForm

    success_url = reverse_lazy("basicapp:ordersuccess")
 
    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user

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

    fields = ['is_driver','vehic_type','name','lice_plate_number','max_pass_num','other_reg']
    success_url = '/'
#edit open ride
class EditOpenRideView(UpdateView):
    model = Rides
    form_class = EditOpenRideForm
    template_name = "editrides.html"
    pass


# To Drive(driver registered)
class ToDriveView(ListView):
    model = Rides
    template_name ="todrive.html"
    context_object_name = "open_ride_list"
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        all_shares = Sharers.objects.all()
        context['all_shares'] = all_shares
        counter = {i :i.party_num for i in context['open_ride_list']}
        
        for share in all_shares:
            counter[share.share_id] +=share.share_party_num
        
        max_pass_num = self.request.user.max_pass_num
        vehic_type = self.request.user.vehic_type
        context['open_ride_list'] = list(filter(lambda key: (counter[key]<=max_pass_num and 
                                                            #total party number limit
                                                            (key.required_vehic_type==vehic_type or 
                                                            key.required_vehic_type=='al')) and 
                                                            #vehicle type match
                                                            key.owner!=self.request.user and 
                                                            #driver cannot drive a ride whose owner is himself
                                                            (key not in [ share.share_id for share in all_shares.filter(sharer_id=self.request.user)]) 
                                                            # drive cannot todrive a ride including himself in sharers
                                                            , context['open_ride_list']))
        
        return context
    
        

# confirm drive
class ConfirmDriveView(View):
    model = Rides
    
    success_url = "/"
    
        
    def get(self, request,**kwargs):
        pk_ride = self.kwargs["pk"]
 
        self.object = self.model.objects.get(pk=pk_ride)
        self.object.status = 'cf'
        self.object.driver_acc = self.request.user
        self.object.save()

        return render(request,"confirmdrive.html")

# to share ride
class JoinShareView(ListView):
    model = Rides
    context_object_name = "sharablerides"
    template_name = "joinshare.html"
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)

        context['sharablerides'] = context['sharablerides'].filter(sharable=True)
        context['sharablerides'] = context['sharablerides'].filter(status='op')
        all_shares = Sharers.objects.all()
        context['all_shares'] = all_shares

        return context
    def post(self,request,**kwargs):
       
        if self.request.method=='POST':
            dest = self.request.POST['destination']
            e_time = self.request.POST['early_time']
            l_time = self.request.POST['late_time']
           
            sharablerides = Rides.objects.all().filter(sharable=True).filter(status='op')
            if dest: 
                sharablerides = sharablerides.filter(dest_addr=dest)
            if e_time:
                sharablerides = sharablerides.filter(arr_date_time__gte = e_time)
            if l_time:
                sharablerides = sharablerides.filter(arr_date_time__lte =l_time)
            all_shares = Sharers.objects.all()
        return render(request,"joinshare.html",{'sharablerides':sharablerides ,'all_shares':all_shares})


# edit join info 
class JoinInfoView(CreateView):
    model = Sharers
    fields = ['share_party_num']
    template_name="editjoininfo.html"
    success_url = '/'
    def form_valid(self,form):
        pk = self.kwargs['pk']
        self.object = form.save(commit=False)
   
        self.object.share_id = Rides.objects.get(pk=pk)
        self.object.sharer_id = self.request.user
        print(self.object)
        self.object.save()

        return super().form_valid(form)
   
