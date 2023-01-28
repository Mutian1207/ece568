from django import forms
from .models import Users,Sharers,Rides
from django.contrib.auth.forms import UserCreationForm,UserChangeForm


class UserRegisterForm(forms.ModelForm):

    class Meta():
        model = Users
        fields = ('email','password')
        widgets ={'email': forms.EmailInput(),
                    'password':forms.PasswordInput(),}
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['email'].label = "Email"
        self.fields['password'].label = "Password"
            
class CreateOrderForm(forms.ModelForm):
    class Meta():
        model = Rides
        fields = ('dest_addr','arr_date_time','party_num','other_reg')
        widgets ={'dest_addr': forms.TextInput(),
                    'arr_date_time':forms.DateTimeInput(),
                    'party_num':forms.NumberInput(),
                    'other_reg':forms.TextInput()}
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['dest_addr'].label = "Destination"
        self.fields['party_num'].label = "Party number"
        self.fields['arr_date_time'].label = "Arrival time"
        self.fields['other_reg'].label = "Other requirements" 

class EditOpenRideForm(forms.ModelForm):
    pass  
