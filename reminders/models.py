from django.db import models

from clients.models import Client


class Reminder(models.Model):
    title = models.CharField(max_length=300, verbose_name='Напоминание', blank=True)
    date = models.DateField(verbose_name='Дата')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='reminders', verbose_name='Клиент')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

