
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

from django import forms

from django.forms.widgets import PasswordInput, TextInput





# - Register/create a user

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', '<password1>', '<password2>']

# - Login a User
class LoginForm(AuthenticationForm):
    class Meta:
      username = forms.CharField(widget=forms.TextInput())
      password = forms.CharField(widget=forms.PasswordInput())












