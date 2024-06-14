from django.contrib import admin

from clients.models import Client
from reminders.models import Reminder
from reports.models import Report
from .models import CustomUser


admin.site.register(Reminder)
admin.site.register(Client)
admin.site.register(Report)

admin.site.register(CustomUser)
