# Generated by Django 5.0.14 on 2025-05-24 07:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PrendasPerdidas', '0002_alter_prendasperdidas_options_and_more'),
        ('empeños', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prendasperdidas',
            name='Fk_empeño',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='empeños.empeños'),
        ),
    ]
