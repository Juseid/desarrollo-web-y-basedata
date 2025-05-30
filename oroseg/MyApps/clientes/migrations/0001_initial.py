# Generated by Django 5.0.14 on 2025-05-24 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Ingrese el nombre del cliente', max_length=100, verbose_name='Nombre del cliente')),
                ('documento', models.CharField(help_text='Ingrese el doumento del cliente', max_length=20)),
                ('telefono', models.CharField(help_text='Ingrese su numero de telefono', max_length=10)),
                ('direccion', models.CharField(help_text='ingrese su direccion', max_length=10)),
                ('correo', models.EmailField(help_text='ingrese su correo', max_length=20)),
            ],
            options={
                'verbose_name': 'cliente',
                'verbose_name_plural': 'clientes',
            },
        ),
    ]
