from django import forms
from .models import Users,Sharers,Rides
from django.contrib.auth.forms import UserCreationForm,UserChangeForm


class UserRegisterForm(forms.ModelForm):

    class Meta():
        model = Users
        fields = ('user_id','user_pwd')
        widgets ={'user_id': forms.EmailInput(),
                    'user_pwd':forms.PasswordInput(),}
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['user_id'].label = "Email"
        self.fields['user_pwd'].label = "Password"    