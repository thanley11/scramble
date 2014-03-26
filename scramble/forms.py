from django import forms
from scramble.models import UserProfile, Course
from django.contrib.auth.models import User
from django.forms import ModelForm, PasswordInput

class UserForm(forms.ModelForm):
    username = forms.CharField(help_text="Please enter a username.")
    email = forms.CharField(help_text="Please enter an email address.")
    password = forms.CharField(widget=forms.PasswordInput(), help_text="Please enter a password.")
    
    class Meta:
        model = User
        fields = ('username','email','password')
  
class CourseForm(forms.ModelForm):
    name = forms.CharField(label='name',
                            widget=forms.TextInput(attrs={'placeholder': 'Name of Scramble'}))
    par = forms.IntegerField(label='par',
                            widget=forms.TextInput(attrs={'placeholder': 'Enter a par here'}))
    handicap = forms.IntegerField(label='handicap',
                            widget=forms.TextInput(attrs={'placeholder': 'Enter a handicap here'}))
    location = forms.CharField(label='location',
                            widget=forms.TextInput(attrs={'placeholder': 'Enter a course location here'}))
    
    class Meta:
        model = Course
        fields = ('name','par','handicap','location') 