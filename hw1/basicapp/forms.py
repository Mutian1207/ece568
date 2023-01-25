from django import forms
from .models import Users,Sharers,Rides
from django.contrib.auth.forms import UserCreationForm,UserChangeForm


class UserRegisterForm(forms.ModelForm):

    class Meta():
        model = Users
        fields = ('','','')
        
        