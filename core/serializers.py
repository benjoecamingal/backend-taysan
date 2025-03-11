from rest_framework import serializers
from .models import User, Announcements, Activities, Schedules
from django.utils import timezone




class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['username', 'email', 'password', 'role']
    extra_kwargs = {'password':{'write_only': True}}

  def create(self, validated_data):
    user = User.objects.create_user(
      username=validated_data['username'],
      email=validated_data['email'],
      password=validated_data['password'],
      role=validated_data['role']
    )

    return user
  

class AnnouncementsSerializer(serializers.ModelSerializer):
  username = serializers.SerializerMethodField()
  timestamp = serializers.SerializerMethodField()
  class Meta:
    model = Announcements
    fields = ['id', 'title', 'content', 'timestamp', 'username']
    extra_kwargs = {'id':{'read_only':True}}

  def get_username(self, obj):
    return obj.created_by.username
  
  def get_timestamp(self, obj):
    local_time = timezone.localtime(obj.timestamp)
    return local_time.strftime('%d %B %Y - %I:%M %p')


class ActivitiesSerializer(serializers.ModelSerializer):
  username = serializers.SerializerMethodField()
  timestamp = serializers.SerializerMethodField()
  datepht = serializers.SerializerMethodField()
  timepht = serializers.SerializerMethodField()

  class Meta:
    model = Activities
    fields = ['id', 'title', 'content', 'place', 'date', 'time', 'datepht', 'timepht', 
              'username', 'timestamp']
    extra_kwargs = {
      'id': {'read_only': True},
      'date': {'write_only': True},
      'time': {'write_only': True},
    }

  def get_username(self, obj):
    return obj.created_by.username
  
  def get_timestamp(self, obj):
    local_time = timezone.localtime(obj.timestamp)
    return local_time.strftime('%d %B %Y - %I:%M %p')
    
  def get_datepht(self, obj):
    return obj.date.strftime('%d %B %Y')
  
  def get_timepht(self, obj):
    return obj.time.strftime('%I:%M %p')
  

class SchedulesSerializer(serializers.ModelSerializer):
  timestamp = serializers.SerializerMethodField()
  datepht = serializers.SerializerMethodField()
  timepht = serializers.SerializerMethodField()

  class Meta:
    model = Schedules
    fields = ['id', 'title', 'content', 'barangay', 'date', 'time', 'datepht', 
              'timepht', 'timestamp']
    extra_kwargs = {
      'id': {'read_only': True},
      'date': {'write_only': True},
      'time': {'write_only': True}
    }

  def get_timestamp(self, obj):
    local_time = timezone.localtime(obj.timestamp)
    return local_time.strftime('%d %B %Y - %I:%M %p')
  
  def get_datepht(self, obj):
    return obj.date.strftime('%d %B %Y')
  
  def get_timepht(self, obj):
    return obj.time.strftime('%I:%M %p')
