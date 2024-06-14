from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from .models import Client


class ClientListView(ListView):
    model = Client
    template_name = 'clients/client_list.html'
    context_object_name = 'clients'

    def get_queryset(self):
        return Client.objects.all()


class ClientCreateView(CreateView):
    model = Client
    fields = ['name', 'email', 'phone', 'notes']
    success_url = reverse_lazy('clients:client_list')


class ClientDetailView(DetailView):
    model = Client
    template_name = 'clients/client_detail.html'


class ClientUpdateView(UpdateView):
    model = Client
    fields = ['name', 'email', 'phone', 'notes']
    success_url = reverse_lazy('clients:client_list')


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('clients:client_list')


def client_files(request, client_id):
    object = Client.objects.get(pk=client_id)
    if request.method == 'POST':
        object.pdf_file = request.FILES.get('pdf_file')
        object.xml_file = request.FILES.get('xml_file')
        object.word_file = request.FILES.get('word_file')
        object.save()
        return redirect('clients:client_files', client_id=object.pk)
    return render(request, 'clients/client_files.html', {'client': object})
