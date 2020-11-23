from django.urls import path
from apps.licoreria.views import index, AgregarCliente, ConsultarCliente
from apps.licoreria.views import AgregarProducto, ConsultarProducto, EditarProducto, EliminarProducto
from apps.licoreria.views import AgregarDomiciliario, ConsultarDomiciliario, EditarDomiciliario, EliminarDomiciliario

urlpatterns = [
    path('', index),
    path('AgregarCliente/', AgregarCliente, name = 'AgregarCliente'),
    path('ConsultarCliente/', ConsultarCliente, name = 'ConsultarCliente'),

    path('AgregarProducto/', AgregarProducto, name = 'AgregarProducto'),
    path('ConsultarProducto/', ConsultarProducto, name = 'ConsultarProducto'),
    path('EditarProducto/<id_prod>', EditarProducto, name = 'EditarProducto'),
    path('EliminarProducto/<id_prod>', EliminarProducto, name = 'EliminarProducto'),

    path('AgregarDomiciliario/', AgregarDomiciliario, name = 'AgregarDomiciliario'),
    path('ConsultarDomiciliario/', ConsultarDomiciliario, name = 'ConsultarDomiciliario'),
    path('EditarDomiciliario/<id_dom>', EditarDomiciliario, name = 'EditarDomiciliario'),
    path('EliminarDomiciliario/<id_dom>', EliminarDomiciliario, name = 'EliminarDomiciliario'),
]
