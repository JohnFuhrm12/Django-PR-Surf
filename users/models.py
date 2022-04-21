from django.db import models
from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class':'validate','placeholder': 'Username'}))
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder':'Password'}))

class Link(models.Model):
    title = models.CharField(max_length=200, unique=True)
    url_field = models.URLField(max_length = 200, default=None, blank=True)
    favorites = models.ManyToManyField(User, related_name='favorite', default=None, blank=True)

    def __str__(self):
        return self.title