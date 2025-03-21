from .serializers import (UserSerializer, AnnouncementsSerializer, ActivitiesSerializer, SchedulesSerializer,
                          EncoderSerializer, HealthInfoSerializer, MessageSerializer)
from rest_framework import generics, permissions
from .models import User, Announcements, Activities, Schedules, HealthInfo, Message
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q

class RegisterView(generics.CreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = [permissions.AllowAny]

  def create(self, request, *args, **kwargs):
    response = super().create(request, *args, **kwargs)
    user = User.objects.get(username=response.data['username'])
    medical_role = user.medical_role
    token, _ = Token.objects.get_or_create(user=user)
    response.data['token'] = token.key
    response.data['medical_role'] = medical_role
    return response
  

class LoginView(ObtainAuthToken):
  def post(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    # user = serializer.validated_data['user']
    user = User.objects.get(username=serializer.validated_data['username'])
    token, _ = Token.objects.get_or_create(user=user)

    response = {
      'first_name': user.first_name,
      'last_name': user.last_name,
      'username': user.username,
      'email': user.email,
      'role': user.role,
      'token': token.key,
      'medical_role': user.medical_role
    }

    return Response(response, status=status.HTTP_200_OK)
  

class ListCitizenView(generics.ListAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = [permissions.IsAuthenticated]

  def get_queryset(self):
    return User.objects.filter(role='citizen')
  

class ListEncoderView(generics.ListAPIView):
  queryset = User.objects.all()
  serializer_class = EncoderSerializer
  permission_classes = [permissions.IsAuthenticated]

  def get_queryset(self):
    return User.objects.filter(role='encoder')
  

class ListCreateEncoderViews(generics.ListCreateAPIView):
  queryset = User.objects.all()
  serializer_class = EncoderSerializer
  permission_classes = [permissions.IsAuthenticated]

  def get_queryset(self):
    return User.objects.filter(role='encoder')
    

class ListCreateAnnouncementViews(generics.ListCreateAPIView):
  queryset = Announcements.objects.all()
  serializer_class = AnnouncementsSerializer
  permission_classes = [permissions.IsAuthenticated]
  
  def get_queryset(self):
    return Announcements.objects.order_by('-timestamp')

  def perform_create(self, serializer):
    serializer.save(created_by=self.request.user)


class DeleteAnnouncementViews(generics.DestroyAPIView):
  queryset = Announcements.objects.all()
  serializer_class = AnnouncementsSerializer
  permission_classes = [permissions.IsAuthenticated]


class ListCreateActivityViews(generics.ListCreateAPIView):
  queryset = Activities.objects.all()
  serializer_class = ActivitiesSerializer
  permission_classes = [permissions.IsAuthenticated]

  def get_queryset(self):
    return Activities.objects.order_by('-timestamp')
  
  def perform_create(self, serializer):
    return serializer.save(created_by=self.request.user)
  

class DeleteActivityViews(generics.DestroyAPIView):
  queryset = Activities.objects.all()
  serializer_class = ActivitiesSerializer
  permission_classes = [permissions.IsAuthenticated]


class ListCreateScheduleViews(generics.ListCreateAPIView):
  queryset = Schedules.objects.all()
  serializer_class = SchedulesSerializer
  permission_classes = [permissions.IsAuthenticated]

  def get_queryset(self):
    return Schedules.objects.order_by('-timestamp')
  

class DeleteScheduleViews(generics.DestroyAPIView):
  queryset = Schedules.objects.all()
  serializer_class = SchedulesSerializer
  permission_classes = [permissions.IsAuthenticated]


class ListCreateHealthInfoViews(generics.ListCreateAPIView):
  queryset = HealthInfo.objects.all()
  serializer_class = HealthInfoSerializer
  permission_classes = [permissions.IsAuthenticated]

  def get_queryset(self):
    return self.request.user.created_health_info.all()

  def perform_create(self, serializer):
    return serializer.save(created_by=self.request.user)
  

class ListUserHealthInfoViews(generics.ListAPIView):
  queryset = HealthInfo.objects.all()
  serializer_class = HealthInfoSerializer
  permission_classes = [permissions.IsAuthenticated]

  def get_queryset(self):
    return self.request.user.health_info.all()
  
  
class GetHealthInfoViews(generics.RetrieveAPIView):
  queryset = HealthInfo.objects.all()
  serializer_class = HealthInfoSerializer
  permission_classes = [permissions.IsAuthenticated]


class CreateMessageViews(generics.CreateAPIView):
  queryset = Message.objects.all()
  serializer_class = MessageSerializer
  permission_classes = [permissions.IsAuthenticated]

  def get_queryset(self):
    id = self.kwargs['pk']
    user1_id = self.request.user.id
    user2_id = User.objects.get(id=id).id

    return Message.objects.filter(
      Q(sender=user1_id, receiver=user2_id) |
      Q(sender=user2_id, receiver=user1_id)
    ).order_by('-timestamp')
  
  def perform_create(self, serializer):
    return serializer.save(sender=self.request.user)
  

class ListMessageViews(generics.ListAPIView):
  queryset = Message.objects.all()
  serializer_class = MessageSerializer
  permission_classes = [permissions.IsAuthenticated]

  def get_queryset(self):
    id = self.kwargs['pk']
    user1_id = self.request.user.id
    user2_id = User.objects.get(id=id).id

    return Message.objects.filter(
      Q(sender=user1_id, receiver=user2_id) |
      Q(sender=user2_id, receiver=user1_id)
    ).order_by('timestamp')
