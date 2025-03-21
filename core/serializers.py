from rest_framework import serializers
from .models import User, Announcements, Activities, Schedules, HealthInfo, Message
from django.utils import timezone


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['id', 'first_name', 'last_name', 'username', 'email', 'password', 'role']
    extra_kwargs = {'password':{'write_only': True}}

  def create(self, validated_data):
    user = User.objects.create_user(
      first_name=validated_data['first_name'],
      last_name=validated_data['last_name'],
      username=validated_data['username'],
      email=validated_data['email'],
      password=validated_data['password'],
      role=validated_data['role']
    )

    return user
  

class EncoderSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['id', 'first_name', 'last_name', 'username', 'email', 'password', 'role',
              'medical_role']
    extra_kwargs = {
      'password': {'write_only': True},
    }

  def create(self, validated_data):
    print(validated_data)
    user = User.objects.create_user(
      first_name = validated_data['first_name'],
      last_name = validated_data['last_name'],
      username = validated_data['username'],
      email = validated_data['email'],
      password = validated_data['password'],
      role = 'encoder',
      medical_role = validated_data['medical_role'],
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
  year = serializers.SerializerMethodField()
  month = serializers.SerializerMethodField()
  day = serializers.SerializerMethodField()

  class Meta:
    model = Schedules
    fields = ['id', 'title', 'content', 'barangay', 'date', 'time', 'datepht', 
              'timepht', 'timestamp', 'year', 'month', 'day']
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
  
  def get_year(self, obj):
    return obj.date.strftime('%Y')
  
  def get_month(self, obj):
    return obj.date.strftime('%B')
  
  def get_day(self, obj):
    return obj.date.strftime('%d').lstrip('0')


class HealthInfoSerializer(serializers.ModelSerializer):
  datepht = serializers.SerializerMethodField()
  timepht = serializers.SerializerMethodField()
  name = serializers.SerializerMethodField()
  creator_name = serializers.SerializerMethodField()
  creator_medical_role = serializers.SerializerMethodField()

  class Meta:
    model = HealthInfo
    fields = ['id', 'created_by', 'created_for', 'consultation_type', 'consultation_date',
               'consultation_time', 'age', 'gender', 'symptoms', 'medical_history', 'diagnosis', 'datepht', 
               'name', 'timepht', 'creator_name', 'creator_medical_role']
    extra_kwargs = {
      'id': {'read_only': True},
      'created_by': {'read_only': True},
      'consultation_date': {'write_only': True},
      'consultation_time': {'write_only': True}
    }

  def get_datepht(self, obj):
    return obj.consultation_date.strftime('%d %B %Y')
  
  def get_timepht(self, obj):
    return obj.consultation_time.strftime('%I:%M %p')
  
  def get_name(self, obj):
    first_name = obj.created_for.first_name
    last_name = obj.created_for.last_name
    return f"{first_name} {last_name}"
  
  def get_creator_name(self, obj):
    user = User.objects.get(id=obj.created_by.id)
    return f"{user.first_name} {user.last_name}"
  
  def get_creator_medical_role(self, obj):
    user = User.objects.get(id=obj.created_by.id)
    return user.medical_role
  

class MessageSerializer(serializers.ModelSerializer):
  date_time = serializers.SerializerMethodField()
  
  class Meta:
    model = Message
    fields = ['id', 'sender', 'receiver', 'content', 'date_time']

    extra_kwargs = {
      'id': {'read_only': True},
      'sender': {'read_only': True},
    }

  def get_date_time(self, obj):
    local_time = timezone.localtime(obj.timestamp)
    return local_time.strftime('%d %B %Y - %I:%M %p')
    
