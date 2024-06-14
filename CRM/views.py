from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .models import CustomUser


class RegisterView(CreateView):
    model = CustomUser
    fields = ['username', 'email', 'password']
    template_name = 'CRM/register.html'
    success_url = reverse_lazy('login')


class CustomLoginView(LoginView):
    template_name = 'CRM/login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('client_list')


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')
