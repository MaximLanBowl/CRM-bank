from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.CharField(verbose_name='Почтовый адрес')
    phone = models.CharField(max_length=50, verbose_name='Номер телефона')
    notes = models.TextField(blank=True, null=True, verbose_name='Дополнительная информация')
    pdf_file = models.FileField(upload_to='client_files/pdf', null=True, blank=True, verbose_name='PDF файл')
    xml_file = models.FileField(upload_to='client_files/xml', null=True, blank=True, verbose_name='XML файл')
    word_file = models.FileField(upload_to='client_files/word', null=True, blank=True, verbose_name='Word файл')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name