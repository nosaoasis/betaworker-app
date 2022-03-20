from django.shortcuts import render
from .models import Jobs

# Create your views here.
def home(request, *args, **kwargs):
  data = Jobs.objects.all()
  context = {
    "jobs" : data
  }
  return render(request, 'jobs_app/home.html', context)
