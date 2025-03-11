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
  

class Announcements(models.Model):
  title = models.CharField(max_length=225)
  content = models.TextField()
  created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='announcements')
  timestamp = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title
  

class Activities(models.Model):
  title = models.CharField(max_length=225)
  content = models.TextField()
  place = models.CharField(max_length=500)
  date = models.DateField()
  time = models.TimeField()
  created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
  timestamp = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title
  

class Schedules(models.Model):
  title = models.CharField(max_length=225)
  content = models.TextField()
  barangay = models.CharField(max_length=225)
  date = models.DateField()
  time = models.TimeField()
  timestamp = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title