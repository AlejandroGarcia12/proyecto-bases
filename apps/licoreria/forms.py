from django import forms
from apps.licoreria.models import Cliente, Direccion, Producto, Carrito, Domiciliario, Factura

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields =[
        'id_cliente', 
        'nombre',
        'apellido',
        'cedula',
        'fecha_nacimiento',
        'telefono', 
        'correo',
        'clave',
        ]
        fields ={
        'id_cliente':'Id', 
        'nombre':'Nombre',
        'apellido':'Apellido',
        'cedula':'Cedula',
        'fecha_nacimiento':'Fecha de nacimiento',
        'telefono':'Telefono', 
        'correo':'Correo',
        'clave':'Clave',
        }
        widgets={
        'id_cliente':forms.TextInput(), 
        'nombre':forms.TextInput(),
        'apellido':forms.TextInput(),
        'cedula':forms.NumberInput(),
        'fecha_nacimiento':forms.TextInput(),
        'telefono':forms.NumberInput(), 
        'correo':forms.TextInput(),
        'clave':forms.TextInput(),
        }