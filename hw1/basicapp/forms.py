from django import forms
from .models import Users,Sharers,Rides
from django.contrib.auth.forms import UserCreationForm,UserChangeForm


class UserRegisterForm(forms.ModelForm):

    class Meta():
        model = Users
        fields = ('username','email','password')
        widgets ={'username':forms.TextInput(),'email': forms.EmailInput(),
                    'password':forms.PasswordInput(),}
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['email'].label = "Email"
        self.fields['password'].label = "Password"    