from django.urls import path
from reports.views import (
    ReportCreateView,
    ReportUpdateView,
    ReportListView,
    ReportDetailView,
    ReportDeleteView
)

app_name="reports"

urlpatterns = [
    path('', ReportListView.as_view(), name='report_list'),
    path('create/', ReportCreateView.as_view(), name='report_create'),
    path('<int:pk>/', ReportDetailView.as_view(), name='report_detail'),
    path('<int:pk>/update/', ReportUpdateView.as_view(), name='report_update'),
    path('<int:pk>/delete/', ReportDeleteView.as_view(), name='report_delete'),
]