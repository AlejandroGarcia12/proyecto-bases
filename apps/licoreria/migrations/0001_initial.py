# Generated by Django 3.1.2 on 2020-10-30 22:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('id_admin', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
                ('apellido', models.CharField(max_length=45)),
                ('cedula', models.BigIntegerField()),
                ('telefono', models.BigIntegerField()),
                ('correo', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id_carrito', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('valor_total', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_categoria', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
                ('apellido', models.CharField(max_length=45)),
                ('cedula', models.BigIntegerField()),
                ('fecha_nacimiento', models.DateField()),
                ('telefono', models.BigIntegerField()),
                ('correo', models.CharField(max_length=200)),
                ('clave', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Domiciliario',
            fields=[
                ('id_domiciliario', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
                ('apellido', models.CharField(max_length=45)),
                ('cedula', models.BigIntegerField()),
                ('telefono', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id_factura', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('valor_total', models.BigIntegerField()),
                ('estado', models.CharField(max_length=45)),
                ('id_domiciliario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='licoreria.domiciliario')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
                ('precio', models.BigIntegerField()),
                ('tamano', models.IntegerField()),
                ('unidades_disponibles', models.IntegerField()),
                ('id_admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='licoreria.administrador')),
                ('id_categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='licoreria.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Producto_factura',
            fields=[
                ('id_producto_factura', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('id_factura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='licoreria.factura')),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='licoreria.producto')),
            ],
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id_direccion', models.IntegerField(primary_key=True, serialize=False)),
                ('barrio', models.CharField(max_length=45)),
                ('via_principal', models.CharField(max_length=10)),
                ('num_1', models.SmallIntegerField()),
                ('aux_1', models.CharField(max_length=5)),
                ('num_2', models.SmallIntegerField()),
                ('aux_2', models.CharField(max_length=5)),
                ('num_3', models.SmallIntegerField()),
                ('inmueble', models.CharField(max_length=45)),
                ('interior', models.CharField(max_length=5)),
                ('num_4', models.SmallIntegerField()),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='licoreria.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Carrito_producto',
            fields=[
                ('id_carrito_producto', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('id_carrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='licoreria.carrito')),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='licoreria.producto')),
            ],
        ),
        migrations.AddField(
            model_name='carrito',
            name='ic_cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='licoreria.cliente'),
        ),
    ]
