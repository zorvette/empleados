# Generated by Django 5.0.7 on 2024-07-19 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0027_alter_pedido_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='name',
            field=models.CharField(choices=[('pedido', 'Pedido'), ('espera', 'Espera'), ('pagado', 'Pagado'), ('deuda', 'Deuda')], default='pedido', max_length=6, verbose_name='Status'),
        ),
    ]
