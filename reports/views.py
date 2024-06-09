from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import ListView, DetailView, UpdateView, DeleteView

from reports.models import Report


class ReportListView(ListView):
    model = Report
    template_name = 'reports/report_list.html'
    context_object_name = 'reports'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_reports'] = self.model.objects.count()
        context['total_clients'] = self.model.objects.values_list('clients', flat=True).distinct().count()
        return context


class ReportDetailView(DetailView):
    model = Report
    template_name = 'reports/report_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_reports'] = self.model.objects.filter(clients__in=self.object.clients.all()).exclude(
            pk=self.object.pk)
        return context


class ReportCreateView(CreateView):
    model = Report
    fields = ['title', 'date', 'content', 'clients']
    template_name = 'reports/report_form.html'
    success_url = reverse_lazy('reports:report_list')


class ReportUpdateView(UpdateView):
    model = Report
    fields = ['title', 'date', 'content', 'clients']
    template_name = 'reports/report_form.html'
    success_url = reverse_lazy('reports:report_list')


class ReportDeleteView(DeleteView):
    model = Report
    template_name = 'reports/report_confirm_delete.html'
    success_url = reverse_lazy('reports:report_list')

