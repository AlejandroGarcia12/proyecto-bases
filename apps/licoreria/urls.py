from django.urls import path
from apps.licoreria.views import index, AgregarCliente

urlpatterns = [
 path('', index),
 path('AgregarCliente/', AgregarCliente),
]