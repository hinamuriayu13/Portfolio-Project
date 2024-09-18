from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Registration Form
class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Login Form
class UserLoginForm(AuthenticationForm):
    username = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)