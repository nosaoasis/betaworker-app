from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User


# Create your views here.
def register(request):
  page_title = "Register"
  if request.method == 'GET':
    form = RegisterForm()
    context = {
      'form' : form,
      'page_title' : page_title
    }
    return render(request, 'users_app/register.html', context)
  
  if request.method == "POST":
    form = RegisterForm(request.POST or None)
    firstname = request.POST.get('firstname')
    lastname = request.POST.get('lastname')
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    password = request.POST.get('password')
    password2 = request.POST.get('password2')
    print(firstname, lastname, username, email, password, password2)
    if form.is_valid():
      form.save()
      firstname = form.cleaned_data.get('firstname')
      messages.success(request, f'Account was created successfuly for {firstname}')
      return redirect('home')
    else:
      print('Invalid form entries.')
      messages.error(request, 'Error processing your request')
      context = {
        'form' : form,
        'page_title' : page_title
      } 
      return render(request, 'users_app/register.html', context)
  return render(request, 'users_app/register.html', context)


def login(request, *args, **kwargs):
  page_title = "Login"
  # form = LoginForm()
  # if request.method == "GET":
  #   form = RegisterForm()
  #   context = {
  #     'form' : form,
  #     'page_title' : page_title
  #   }
  #   return render(request, 'users_app/login.html', context)

  # if request.method == "POST":
  #   form = LoginForm(request.POST)
  #   qs = User.objects.get()
  context = {
    'page_title' : page_title
  }
  return render(request, 'users_app/login.html', context)