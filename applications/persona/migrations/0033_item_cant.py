# Generated by Django 5.0.7 on 2024-07-20 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0032_rename_items_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='cant',
            field=models.IntegerField(default=1, verbose_name='Cantidad'),
            preserve_default=False,
        ),
    ]
