from django.urls import path
from .views import (RegisterView, LoginView, ListCreateAnnouncementViews, DeleteAnnouncementViews, 
                    ListCreateActivityViews, DeleteActivityViews, ListCreateScheduleViews, DeleteScheduleViews,
                    ListCreateEncoderViews, ListCitizenView, ListCreateHealthInfoViews, GetHealthInfoViews,
                    ListUserHealthInfoViews, ListEncoderView, CreateMessageViews, ListMessageViews)

urlpatterns = [
  path('register/', RegisterView.as_view(), name='register'),
  path('login/', LoginView.as_view(), name='login'),
  path('list-create-encoder/', ListCreateEncoderViews.as_view(), name='create-encoder'),
  path('list-create-announcement/', ListCreateAnnouncementViews.as_view(), name='list-create-announcement'),
  path('announcement/<str:pk>/delete', DeleteAnnouncementViews.as_view(), name='delete-announcement'),
  path('list-create-activity/', ListCreateActivityViews.as_view(), name='list-create-activity'),
  path('activity/<str:pk>/delete', DeleteActivityViews.as_view(), name='delete-activity'),
  path('list-create-schedules/', ListCreateScheduleViews.as_view(), name='list-create-schedule'),
  path('schedule/<str:pk>/delete', DeleteScheduleViews.as_view(), name='delete-schedule'),
  path('list-citizen/', ListCitizenView.as_view(), name='list-citizen'),
  path('list-encoder/', ListEncoderView.as_view(), name='list-encoder'),
  path('list-create-health-info/', ListCreateHealthInfoViews.as_view(), name='list-create-health-info'),
  path('get-health-info/<str:pk>/', GetHealthInfoViews.as_view(), name='get-health-info'),
  path('list-health-info/', ListUserHealthInfoViews.as_view(), name='list-health-info'),
  path('create-message/', CreateMessageViews.as_view(), name='create-message'),
  path('list-message/<str:pk>', ListMessageViews.as_view(), name='list-message'),
]