from django.urls import path
from apps.licoreria.views import sesion, AgregarCliente, ConsultarCliente, AgregarDireccion
from apps.licoreria.views import AgregarProducto, ConsultarProducto, EditarProducto, EliminarProducto
from apps.licoreria.views import AgregarDomiciliario, ConsultarDomiciliario, EditarDomiciliario, EliminarDomiciliario
from apps.licoreria.views import ConsultarCarrito , CarritoProducto #, AnadirProducto,

urlpatterns = [
    path('', sesion, name='sesion'),
    path('AgregarCliente/', AgregarCliente, name = 'AgregarCliente'),
    path('ConsultarCliente/<orden>', ConsultarCliente, name = 'ConsultarCliente'),
    path('AgregarDireccion/', AgregarDireccion, name = 'AgregarDireccion'),

    path('AgregarProducto/', AgregarProducto, name = 'AgregarProducto'),
    path('ConsultarProducto/<orden>', ConsultarProducto, name = 'ConsultarProducto'),
    path('EditarProducto/<id_prod>', EditarProducto, name = 'EditarProducto'),
    path('EliminarProducto/<id_prod>', EliminarProducto, name = 'EliminarProducto'),

    path('AgregarDomiciliario/', AgregarDomiciliario, name = 'AgregarDomiciliario'),
    path('ConsultarDomiciliario/', ConsultarDomiciliario, name = 'ConsultarDomiciliario'),
    path('EditarDomiciliario/<id_dom>', EditarDomiciliario, name = 'EditarDomiciliario'),
    path('EliminarDomiciliario/<id_dom>', EliminarDomiciliario, name = 'EliminarDomiciliario'),

    #path('AnadirProducto/<id_prod>', AnadirProducto, name = 'AnadirProducto'),
    path('ConsultarCarrito/', ConsultarCarrito, name = 'ConsultarCarrito'),
    path('CarritoProducto/<id_prod>', CarritoProducto, name = 'CarritoProducto'),
]
