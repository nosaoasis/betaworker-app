from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class RegisterForm(UserCreationForm):
  firstname = forms.CharField(
    max_length=20, 
    required=True, 
    help_text="Enter First Name", 
    widget=forms.TextInput(
      attrs={'class' : 'form-control border-info', 'placeholder': 'First Name'})
    )
  lastname = forms.CharField(
    max_length=20, 
    required=True, 
    help_text="Enter Last Name", 
    widget=forms.TextInput(
      attrs={'class' : 'form-control border-info', 'placeholder': 'Last Name'})
    )
  username = forms.CharField(
    max_length=20, 
    required=True, 
    help_text="Username", 
    widget=forms.TextInput(
      attrs={'class' : 'form-control border-info', 'placeholder': 'Username'})
    )
  email = forms.EmailField(
    max_length=80, 
    required=True,  
    help_text="Enter Email Address", 
    widget=forms.TextInput(
      attrs={'class' : 'form-control border-info', 'placeholder': 'Email'})
    )
  password = forms.CharField(
    help_text="Enter Password", 
    required=True, 
    widget=forms.PasswordInput(
      attrs={'class' : 'form-control border-info', 'placeholder' : 'Password'})
    )
  password2 = forms.CharField(
    help_text="Confirm Password", 
    required=True, 
    widget=forms.PasswordInput(
      attrs={'class' : 'form-control border-info', 'placeholder' : 'Confirm Password'})
    )
  check_terms = forms.BooleanField(required=True)

  class Meta:
    model = User
    fields = [
      'firstname', 'lastname', 'username', 'email', 'password', 'password2', 'check_terms',
    ]



class LoginForm(UserCreationForm):
  email = forms.EmailField(
    max_length=80, 
    required=True,  
    help_text="Enter Email Address", 
    widget=forms.TextInput(
      attrs={'class' : 'form-control border-info', 'placeholder': 'Email'})
    )
  password = forms.CharField(
    help_text="Enter Password", 
    required=True, 
    widget=forms.PasswordInput(
      attrs={'class' : 'form-control border-info', 'placeholder' : 'Password'})
    )
  remember_me = forms.BooleanField(required=True)

  class Meta:
    model = User
    fields = [
      'email', 'password', 'remember_me',
    ]


 