from django import forms
from scramble.models import UserProfile
from django.contrib.auth.models import User
from django.forms import ModelForm, PasswordInput

class UserForm(forms.ModelForm):
    username = forms.CharField(help_text="Please enter a username.")
    email = forms.CharField(help_text="Please enter an email address.")
    password = forms.CharField(widget=forms.PasswordInput(), help_text="Please enter a password.")
    
    class Meta:
        model = User
        fields = ('username','email','password')