from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
  class Mata:
    model = User
    fields = ['username', 'email', 'password', 'password2']
