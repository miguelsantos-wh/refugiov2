# Generated by Django 3.2.13 on 2022-05-20 15:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascota', '0002_alter_mascota_fecha_rescate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='edad_aproximada',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(30), django.core.validators.MinValueValidator(1)]),
        ),
    ]
