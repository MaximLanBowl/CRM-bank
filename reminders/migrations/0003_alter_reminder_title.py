# Generated by Django 5.0.6 on 2024-06-06 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reminders', '0002_remove_reminder_time_alter_reminder_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reminder',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Описание'),
        ),
    ]
