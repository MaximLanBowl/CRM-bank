from django.urls import path

from clients import views
from clients.views import (
    ClientListView,
    ClientCreateView,
    ClientDeleteView,
    ClientDetailView,
    ClientUpdateView,
)

app_name = "clients"

urlpatterns = [
    path('', ClientListView.as_view(), name='client_list'),
    path('create/', ClientCreateView.as_view(), name='client_create'),
    path('<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('<int:pk>/update/', ClientUpdateView.as_view(), name='client_update'),
    path('<int:pk>/delete/', ClientDeleteView.as_view(), name='client_delete'),
    path('<int:client_id>/files/', views.client_files, name='client_files')

]
