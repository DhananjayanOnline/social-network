from django import forms
from api.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'email'
        ]


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = [
            'title',
            'image',
        ]

        widgets = {
            'title':forms.TextInput(attrs={"class":"form-control"}),
            'image':forms.FileInput(attrs={"class":"form-control"}),
        }