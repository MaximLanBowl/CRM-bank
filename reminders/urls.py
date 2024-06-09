from django.urls import path

from clients import views
from reminders.views import (
    ReminderListView,
    ReminderCreateView,
    ReminderDeleteView,
    ReminderDetailView,
    ReminderUpdateView

)

app_name = "reminders"

urlpatterns = [
    path('', ReminderListView.as_view(), name='reminder_list'),
    path('create/', ReminderCreateView.as_view(), name='reminder_create'),
    path('<int:pk>/', ReminderDetailView.as_view(), name='reminder_detail'),
    path('<int:pk>/update/', ReminderUpdateView.as_view(), name='reminder_update'),
    path('<int:pk>/delete/', ReminderDeleteView.as_view(), name='reminder_delete'),

]
