# Generated by Django 5.0.6 on 2024-06-08 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0005_client_pdf_file_client_xml_file_clientpdfview_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientxmlview',
            name='client',
        ),
        migrations.RemoveField(
            model_name='client',
            name='pdf_file',
        ),
        migrations.RemoveField(
            model_name='client',
            name='website',
        ),
        migrations.RemoveField(
            model_name='client',
            name='xml_file',
        ),
        migrations.DeleteModel(
            name='ClientPDFView',
        ),
        migrations.DeleteModel(
            name='ClientXMLView',
        ),
    ]