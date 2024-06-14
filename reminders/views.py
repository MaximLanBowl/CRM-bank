from datetime import timedelta

from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView
from django.views.generic import ListView, UpdateView, DetailView, DeleteView

from reminders.models import Reminder


class ReminderListView(ListView):
    model = Reminder
    template_name = 'reminders/reminder_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reminders'] = self.get_queryset()
        return context



class ReminderCreateView(CreateView):
    model = Reminder
    fields = "__all__"
    success_url = reverse_lazy('reminders:reminder_list')


class ReminderDetailView(DetailView):
    model = Reminder
    template_name = 'reminders/reminder_detail.html'


class ReminderUpdateView(UpdateView):
    model = Reminder
    fields = ['title', 'date', 'client']
    success_url = reverse_lazy('reminders:reminder_list')


class ReminderDeleteView(DeleteView):
    model = Reminder
    success_url = reverse_lazy('reminders:reminder_list')
