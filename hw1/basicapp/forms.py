from django import forms
from .models import Users,Sharers,Rides
from django.contrib.auth.forms import UserCreationForm,UserChangeForm


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = Users
        fields = ('email',)
        widgets ={'email': forms.EmailInput(),
                    }
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['email'].label = "Email"

        # self.fields['password'].label = "Password"    

            

class CreateOrderForm(forms.ModelForm):
    class Meta:
        model = Rides
        fields = ('dest_addr','arr_date_time','party_num','sharable','required_vehic_type','other_reg')
        widgets ={'dest_addr': forms.TextInput(),
                    'arr_date_time':forms.DateTimeInput(),
                    'party_num':forms.NumberInput(),
                    'other_reg':forms.TextInput()}
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['dest_addr'].label = "Destination"
        self.fields['party_num'].label = "Party number"
        self.fields['arr_date_time'].label = "Arrival time"
        self.fields['sharable'].label = "Allow  sharing"
        self.fields['required_vehic_type'].label = "Require vehicle type"
        self.fields['other_reg'].label = "Other requirements" 

class EditOpenRideForm(forms.ModelForm):
    class Meta:
        model = Rides
        fields = ['dest_addr','arr_date_time','party_num','other_reg']
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        #self.fields['owner'].widget.attrs = {"class":"form-control","disabled":"true"}
        self.fields['dest_addr'].widget.attrs = {"class":"form-control"}
        self.fields['dest_addr'].label = "Destination"
        self.fields['arr_date_time'].widget.attrs = {"class":"form-control"}
        self.fields['arr_date_time'].label = "Arrival time"
        self.fields['party_num'].widget.attrs = {"class":"form-control"}
        self.fields['party_num'].label = "Party number"
        #self.fields['sharable'].widget.attrs = {"class":"form-control","readonly":"true"}
        #self.fields['status'].widget.attrs = {"class":"form-control","readonly":"true"}
        #self.fields['driver_acc'].widget.attrs = {"class":"form-control","readonly":"true"}
        #self.fields['required_vehic_type'].widget.attrs = {"class":"form-control","readonly":"true"}
        self.fields['other_reg'].widget.attrs = {"class":"form-control"}
        self.fields['other_reg'].label = "Other requirements" 

