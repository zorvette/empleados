# Generated by Django 5.0.7 on 2024-07-19 23:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0024_pedido_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='hora',
            field=models.DateTimeField(default=datetime.date.today, verbose_name='Date'),
        ),
    ]
