# Generated by Django 5.0.7 on 2024-07-19 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0008_rename_hamburguesa_servicio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Nombre')),
                ('Marca', models.CharField(max_length=50, verbose_name='Nombre')),
            ],
        ),
    ]
