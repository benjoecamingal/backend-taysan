from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  ROLE_CHOICES = (
    ('admin', 'Admin'),
    ('encoder', 'Encoder'),
    ('citizen', 'Citizen')
  )
  role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='citizen')

  def __str__(self):
    return self.username
  

