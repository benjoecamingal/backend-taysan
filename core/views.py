from .serializers import UserSerializer, AnnouncementsSerializer, ActivitiesSerializer, SchedulesSerializer
from rest_framework import generics, permissions
from .models import User, Announcements, Activities, Schedules
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework import status

class RegisterView(generics.CreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = [permissions.AllowAny]

  def create(self, request, *args, **kwargs):
    response = super().create(request, *args, **kwargs)
    user = User.objects.get(username=response.data['username'])
    token, _ = Token.objects.get_or_create(user=user)
    response.data['token'] = token.key
    return response
  

class LoginView(ObtainAuthToken):
  def post(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    token, _ = Token.objects.get_or_create(user=user)

    response = {
      'username': user.username,
      'email': user.email,
      'role': user.role,
      'token': token.key
    }

    return Response(response, status=status.HTTP_200_OK)
  

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


