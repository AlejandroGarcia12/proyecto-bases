from django.shortcuts import render
from django.http import HttpResponse
from apps.licoreria.models import Cliente
from apps.licoreria.forms import ClienteForm

def index(request):
 return render(request, 'licoreria/inicio.html')

def AgregarCliente(request):
    if request.method== 'POST':
        form=ClienteForm(request.POST)
        form.save()
    else:
        form= ClienteForm()
    return render(request, 'licoreria/AgregarCliente.html',{'form':form}) 