# Generated by Django 5.0.7 on 2024-07-19 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0014_servicio'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicio',
            name='ingredientes',
            field=models.ManyToManyField(blank=True, to='persona.ingredientes'),
        ),
    ]
