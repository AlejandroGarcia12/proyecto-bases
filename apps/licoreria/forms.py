from django import forms
from apps.licoreria.models import Cliente, Producto, Domiciliario

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'id_cliente',
            'nombre',
            'apellido',
            'cedula',
            'fecha_nacimiento',
            'telefono',
            'correo',
            'clave',
        ]
        fields = {
            'id_cliente' : 'Id',
            'nombre' : 'Nombre',
            'apellido' : 'Apellido',
            'cedula' : 'Cédula',
            'fecha_nacimiento' : 'Fecha',
            'telefono' : 'Teléfono',
            'correo' : 'Correo',
            'clave' : 'Clave',
        }
        widgets = {
            'id_cliente' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'nombre' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'apellido' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'cedula' : forms.NumberInput(attrs = {'class' : 'form-control'}),
            'fecha_nacimiento' : forms.DateInput(attrs = {'class' : 'form-control'}),
            'telefono' : forms.NumberInput(attrs = {'class' : 'form-control'}),
            'correo' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'clave' : forms.TextInput(attrs = {'class' : 'form-control'}),
        }

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            'id_producto',
            'nombre',
            'precio',
            'tamano',
            'unidades_disponibles',
            'id_admin',
            'id_categoria',
        ]
        fields = {
            'id_producto' : 'Id',
            'nombre' : 'Nombre',
            'precio' : 'Precio',
            'tamano' : 'Tamaño ml',
            'unidades_disponibles' : 'Unidades',
            'id_admin' : 'Id administrador',
            'id_categoria' : 'Id categoria',
        }
        widgets = {
            'id_producto' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'nombre' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'precio' : forms.NumberInput(attrs = {'class' : 'form-control'}),
            'tamano' : forms.NumberInput(attrs = {'class' : 'form-control'}),
            'unidades_disponibles' : forms.NumberInput(attrs = {'class' : 'form-control'}),
            'id_admin' : forms.NumberInput(attrs = {'class' : 'form-control'}),
            'id_categoria' : forms.NumberInput(attrs = {'class' : 'form-control'}),
        }

class DomiciliarioForm(forms.ModelForm):
    class Meta:
        model = Domiciliario
        fields = [
            'id_domiciliario',
            'nombre',
            'apellido',
            'cedula',
            'telefono',
        ]
        fields = {
            'id_domiciliario' : 'Id',
            'nombre' : 'Nombre',
            'apellido' : 'Apellido',
            'cedula' : 'Cédula',
            'telefono' : 'Teléfono',
        }
        widgets = {
            'id_domiciliario' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'nombre' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'apellido' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'cedula' : forms.NumberInput(attrs = {'class' : 'form-control'}),
            'telefono' : forms.NumberInput(attrs = {'class' : 'form-control'}),
        }
