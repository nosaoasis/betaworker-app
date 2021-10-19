from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Jobs(models.Model):
  FULL_TIME = 'FT'
  PART_TIME = 'PT'
  REMOTE = 'RT'
  TIER1 = 't1'
  TIER2 = 't2'
  TIER3 = 't3'
  TIER4 = 't4'
  TIER5 = 't5'



  TYPE_CHOICES = [
    (FULL_TIME, 'Full Time'),
    (PART_TIME, 'Part Time'),
    (REMOTE, 'Remote'),
  ]

  EXP_CHOICES = [
    (TIER1, 'Less than 2 years'),
    (TIER2, '2 years - 5 years'),
    (TIER3, '5 years - 10 years'),
    (TIER4, '10 years - 15 years'),
    (TIER5, 'More than 15 years'),
  ]

  title = models.CharField(max_length=100)
  company = models.CharField(max_length=100)
  location = models.CharField(max_length=100)
  salary = models.CharField(max_length=100)
  job_type = models.CharField(max_length=10, choices=TYPE_CHOICES, default=FULL_TIME)
  experience = models.CharField(max_length=10, choices=EXP_CHOICES, default=TIER1)
  summary = models.TextField()
  description = models.TextField()
  requirements = models.TextField()
  logo = models.ImageField(default='default.png', upload_to='upload_images')
  date_created = models.DateTimeField(default=timezone.now)
  owner = models.ForeignKey(User, on_delete=models.CASCADE)


  def __str__(self):
    return '{} looking for {}'.format(self.company, self.title)