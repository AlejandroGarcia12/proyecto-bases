from django import forms
from apps.licoreria.models import Cliente, Producto, Domiciliario, Carrito, Carrito_producto, Direccion

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

class DireccionForm(forms.ModelForm):
    class Meta:
        model = Direccion
        fields = [
            'id_direccion',
            'barrio',
            'via_principal',
            'num_1',
            'aux_1',
            'num_2',
            'aux_2',
            'num_3',
            'inmueble',
            'interior',
            'num_4',
            'id_cliente',
        ]
        fields = {
            'id_direccion' : 'Id',
            'barrio' : 'Barrio',
            'via_principal' : 'Via Principal',
            'num_1' : 'Numero',
            'aux_1' : 'Aux',
            'num_2' : 'Numero',
            'aux_2' : 'Aux',
            'num_3' : 'Numero',
            'inmueble' : 'Tipo de inmueble',
            'interior' : 'Interior',
            'num_4' : 'Numero',
            'id_cliente' : 'Id_Cliente',
        }
        widgets = {
            'id_direccion' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'barrio' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'via_principal' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'num_1' : forms.NumberInput(attrs = {'class' : 'form-control'}),
            'aux_1' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'num_2' : forms.NumberInput(attrs = {'class' : 'form-control'}),
            'aux_2' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'num_3' : forms.NumberInput(attrs = {'class' : 'form-control'}),
            'inmueble' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'interior' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'num_4' : forms.NumberInput(attrs = {'class' : 'form-control'}),
            'id_cliente' : forms.NumberInput(attrs = {'class' : 'form-control'}),
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

class CarritoForm(forms.ModelForm):
    class Meta:
        model = Carrito
        fields = [
            'id_carrito',
        ]
        fields = {
            'id_carrito' : 'Id',
        }
        widgets = {
            'id_carrito' : forms.TextInput(attrs = {'class' : 'form-control'}),
        }

class Carrito_productoForm(forms.ModelForm):
    class Meta:
        model = Carrito_producto
        fields = [
            # 'id_carrito_producto',
            'cantidad',
            # 'id_producto',
            # 'id_carrito',
        ]
        fields = {
            # 'id_carrito_producto' : 'Id',
            'cantidad' : 'Cantidad',
            # 'id_producto' : 'Id producto',
            # 'id_carrito' : 'Id carrito',
        }
        widgets = {
            # 'id_carrito_producto' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'cantidad' :  forms.NumberInput(attrs = {'class' : 'form-control'}),
            # 'id_producto' :  forms.TextInput(attrs = {'class' : 'form-control'}),
            # 'id_carrito' : forms.TextInput(attrs = {'class' : 'form-control'}),
        }