# Generated by Django 5.0.14 on 2025-05-24 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='correo',
            field=models.EmailField(help_text='ingrese su correo', max_length=100),
        ),
    ]
