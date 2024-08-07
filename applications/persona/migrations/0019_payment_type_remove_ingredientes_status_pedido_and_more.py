# Generated by Django 5.0.7 on 2024-07-19 22:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0018_alter_ingredientes_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='payment_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('proceso', 'Proceso'), ('lista', 'Lista'), ('paga', 'Paga'), ('otro', 'Otro')], default='proceso', max_length=7, verbose_name='Estado')),
            ],
        ),
        migrations.RemoveField(
            model_name='ingredientes',
            name='status',
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='States')),
                ('pago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persona.payment_type')),
            ],
        ),
        migrations.CreateModel(
            name='TipoPago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=50, verbose_name='monto')),
                ('pago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persona.payment_type')),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persona.pedido')),
            ],
        ),
    ]
