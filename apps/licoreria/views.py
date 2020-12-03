from django.shortcuts import render
from django.http import HttpResponse
from apps.licoreria.models import Cliente, Producto, Domiciliario, Carrito, Carrito_producto
from apps.licoreria.forms import ClienteForm, ProductoForm, DomiciliarioForm, CarritoForm #, Carrito_productoForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def inicio(request):
    #return HttpResponse("Hola mundo")
    return render(request, 'licoreria/sesionAdministrador.html')

@login_required
def sesion(request):
    if request.user.groups.filter(name='cliente').exists():
        return render(request, 'licoreria/sesionCliente.html')
    else:
        return render(request, 'licoreria/sesionAdministrador.html')

@login_required
def AgregarCliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        form.save()
    else:
        form = ClienteForm()
    return render(request, 'licoreria/AgregarCliente.html', {'form' : form})

@login_required
def ConsultarCliente(request, orden):
    clientes = Cliente.objects.order_by(orden)
    contexto = {'clientes':clientes, 'orden':orden}
    return render(request, 'licoreria/ConsultarCliente.html', contexto)

@login_required
def AgregarProducto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        form.save()
    else:
        form = ProductoForm()
    return render(request, 'licoreria/AgregarProducto.html', {'form' : form})

def ConsultarProducto(request, orden):
    productos = Producto.objects.order_by(orden)
    contexto = {'productos': productos, 'orden':orden}
    return render(request, 'licoreria/ConsultarProducto.html', contexto)

@login_required
def EditarProducto(request, id_prod):
    producto = Producto.objects.get(id_producto = id_prod)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance = producto)
        if form.is_valid():
            form.save()
        return ConsultarProducto(request)
    else:
        form = ProductoForm(instance = producto)
        return render(request, 'licoreria/EditarProducto.html', {'form' : form})

@login_required
def EliminarProducto(request, id_prod):
    producto = Producto.objects.get(id_producto = id_prod)
    if request.method == 'POST':
        producto.delete()
        return ConsultarProducto(request)
    else:
        return render(request, 'licoreria/EliminarProducto.html', {'producto': producto})

@login_required
def AgregarDomiciliario(request):
    if request.method == 'POST':
        form = DomiciliarioForm(request.POST)
        form.save()
    else:
        form = DomiciliarioForm()
    return render(request, 'licoreria/AgregarDomiciliario.html', {'form' : form})

@login_required
def ConsultarDomiciliario(request):
    domiciliarios = Domiciliario.objects.all()
    contexto = {'domiciliarios':domiciliarios}
    return render(request, 'licoreria/ConsultarDomiciliario.html', contexto)

@login_required
def EditarDomiciliario(request, id_dom):
    domiciliario = Domiciliario.objects.get(id_domiciliario = id_dom)
    if request.method == 'POST':
        form = DomiciliarioForm(request.POST, instance = domiciliario)
        if form.is_valid():
            form.save()
        return ConsultarDomiciliario(request)
    else:
        form = DomiciliarioForm(instance = domiciliario)
        return render(request, 'licoreria/EditarDomiciliario.html', {'form' : form})

@login_required
def EliminarDomiciliario(request, id_dom):
    domiciliario = Domiciliario.objects.get(id_domiciliario = id_dom)
    if request.method == 'POST':
        domiciliario.delete()
        return ConsultarDomiciliario(request)
    else:
        return render(request, 'licoreria/EliminarDomiciliario.html', {'domiciliario': domiciliario})

def AnadirProducto(request, id_prod):
    carrito = Carrito.objects.get(id_cliente = i_cli)
    producto = Producto.objects.get(id_producto = id_prod)
    if carrito == None:
        carrito.save()
    carrito_producto = Carrito_producto.objects.create(producto = producto)
    carrito_producto = Carrito_producto.objects.filter( )
    return render(request, 'licoreria/AnadirProducto.html', {'form' : form})

# def AnadirProducto(request, id_prod):
#     producto = Producto.objects.get(id_producto = id_prod)
#     if request.method == 'POST':
#         form = Carrito_productoForm(request.POST, instance = producto)
#         form.save()
#     else:
#         form = Carrito_productoForm()
#     return render(request, 'licoreria/AnadirProducto.html', {'form' : form})

####### ESTO NO SIRVE :(
def ConsultarCarrito(request):
    clientes = Cliente.objects.all()
    contexto = {'clientes':clientes}
    return render(request, 'licoreria/ConsultarCarrito.html', contexto)

def CarritoProducto(request, id_prod):
    #carrito = Carrito.objects.get(id_cliente = i_cli)
    producto = Producto.objects.get(id_producto = id_prod)
    #if carrito == None:
        #carrito.save()
    #carrito_producto = Carrito_producto.objects.get(id_carrito = carrito.id_carrito, id_producto = id_prod)
    #carrito_producto.id_carrito = carrito.id_carrito
    return render(request, 'licoreria/CarritoProducto.html', {'form' : form})
