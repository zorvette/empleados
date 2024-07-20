# Generated by Django 5.0.7 on 2024-07-19 16:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departamento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hamburguesa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('ing1', models.BooleanField(verbose_name='lechuga')),
                ('ing2', models.BooleanField(verbose_name='tomate')),
                ('ing3', models.BooleanField(verbose_name='carne')),
                ('ing4', models.BooleanField(verbose_name='pollo')),
                ('ing5', models.BooleanField(verbose_name='queso')),
                ('ing6', models.BooleanField(verbose_name='jamon')),
                ('user', models.CharField(max_length=50, verbose_name='Usuario')),
                ('price', models.IntegerField(verbose_name='Precio')),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=60, verbose_name='Nombres')),
                ('last_name', models.CharField(max_length=60, verbose_name='Apellidos')),
                ('job', models.CharField(choices=[('0', 'CONTADOR'), ('1', 'ADMINISTRADOR'), ('2', 'ECONOMISTA'), ('3', 'OTRO')], max_length=1, verbose_name='Trabajo')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departamento.departamento')),
            ],
        ),
    ]
