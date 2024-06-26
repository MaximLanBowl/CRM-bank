# Generated by Django 5.0.6 on 2024-06-17 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0008_client_pdf_file_client_word_file_client_xml_file_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='meeting',
            field=models.CharField(blank=True, null=True, verbose_name='Встреча/заседание'),
        ),
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.CharField(verbose_name='Почтовый адрес'),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=models.CharField(max_length=50, verbose_name='Номер телефона'),
        ),
    ]
