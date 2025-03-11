from django.contrib import admin
from .models import User, Announcements, Activities, Schedules

admin.site.register(User)
admin.site.register(Announcements)
admin.site.register(Activities)
admin.site.register(Schedules)