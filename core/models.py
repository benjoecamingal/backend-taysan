from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  ROLE_CHOICES = (
    ('admin', 'Admin'),
    ('encoder', 'Encoder'),
    ('citizen', 'Citizen')
  )

  MEDICAL_ROLE_CHOICES = (
    ('nurse', 'Nurse'),
    ('doctor', 'Doctor')
  )
  role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='citizen')
  medical_role = models.CharField(max_length=225, choices=MEDICAL_ROLE_CHOICES, null=True, blank=True)

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
  

class HealthInfo(models.Model):
  created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_health_info')
  created_for = models.ForeignKey(User, on_delete=models.CASCADE, related_name='health_info')
  consultation_type = models.CharField(max_length=225)
  consultation_date = models.DateField()
  consultation_time = models.TimeField()
  age = models.IntegerField()
  gender = models.CharField(max_length=225)
  symptoms = models.TextField()
  medical_history = models.TextField()
  diagnosis = models.TextField()

  def __str__(self):
    return str(self.created_for) + ' - ' + str(self.consultation_type)
  

class Message(models.Model):
  sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_message')
  receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_message')
  content = models.TextField()
  timestamp = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"{self.sender} -> {self.receiver}"