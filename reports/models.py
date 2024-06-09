from django.db import models
from clients.models import Client


class Report(models.Model):
    title = models.CharField(max_length=100, verbose_name='Описание')
    date = models.DateField(verbose_name='Дата')
    content = models.TextField(verbose_name='Контент')
    clients = models.ManyToManyField(Client, related_name='reports', verbose_name='Клиенты')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)