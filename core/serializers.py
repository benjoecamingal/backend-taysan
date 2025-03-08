from rest_framework import serializers
from .models import User 
from rest_framework.authtoken.models import Token


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
    
    Token.objects.get_or_create(user=user)

    return user
  
