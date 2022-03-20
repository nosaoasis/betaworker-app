from django.urls import path
from .views import home

app_name = 'jobs'

urlpatterns = [
  path('', home, name='home'),
]


