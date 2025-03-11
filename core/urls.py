from django.urls import path
from .views import (RegisterView, LoginView, ListCreateAnnouncementViews, DeleteAnnouncementViews, 
                    ListCreateActivityViews, DeleteActivityViews, ListCreateScheduleViews, DeleteScheduleViews)

urlpatterns = [
  path('register/', RegisterView.as_view(), name='register'),
  path('login/', LoginView.as_view(), name='login'),
  path('list-create-announcement/', ListCreateAnnouncementViews.as_view(), name='list-create-announcement'),
  path('announcement/<str:pk>/delete', DeleteAnnouncementViews.as_view(), name='delete-announcement'),
  path('list-create-activity/', ListCreateActivityViews.as_view(), name='list-create-activity'),
  path('activity/<str:pk>/delete', DeleteActivityViews.as_view(), name='delete-activity'),
  path('list-create-schedules/', ListCreateScheduleViews.as_view(), name='list-create-schedule'),
  path('schedule/<str:pk>/delete', DeleteScheduleViews.as_view(), name='delete-schedule'),
]