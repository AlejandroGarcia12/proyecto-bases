from django.shortcuts import render
from django.http import HttpResponse
from apps.licoreria.models import Cliente, Producto, Domiciliario
from apps.licoreria.forms import ClienteForm, ProductoForm, DomiciliarioForm

# Create your views here.

def index(request):
    #return HttpResponse("Hola mundo")
    return render(request, 'licoreria/inicio.html')

def AgregarCliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        form.save()
    else:
        form = ClienteForm()
    return render(request, 'licoreria/AgregarCliente.html', {'form' : form})

def ConsultarCliente(request):
    clientes = Cliente.objects.all()
    contexto = {'clientes':clientes}
    return render(request, 'licoreria/ConsultarCliente.html', contexto)

def AgregarProducto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        form.save()
    else:
        form = ProductoForm()
    return render(request, 'licoreria/AgregarProducto.html', {'form' : form})

def ConsultarProducto(request):
    productos = Producto.objects.all()
    contexto = {'productos':productos}
    return render(request, 'licoreria/ConsultarProducto.html', contexto)

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

def EliminarProducto(request, id_prod):
    producto = Producto.objects.get(id_producto = id_prod)
    if request.method == 'POST':
        producto.delete()
        return ConsultarProducto(request)
    else:
        return render(request, 'licoreria/EliminarProducto.html', {'producto': producto})

def AgregarDomiciliario(request):
    if request.method == 'POST':
        form = DomiciliarioForm(request.POST)
        form.save()
    else:
        form = DomiciliarioForm()
    return render(request, 'licoreria/AgregarDomiciliario.html', {'form' : form})

def ConsultarDomiciliario(request):
    domiciliarios = Domiciliario.objects.all()
    contexto = {'domiciliarios':domiciliarios}
    return render(request, 'licoreria/ConsultarDomiciliario.html', contexto)

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

def EliminarDomiciliario(request, id_dom):
    domiciliario = Domiciliario.objects.get(id_domiciliario = id_dom)
    if request.method == 'POST':
        domiciliario.delete()
        return ConsultarDomiciliario(request)
    else:
        return render(request, 'licoreria/EliminarDomiciliario.html', {'domiciliario': domiciliario})
