# Generated by Django 3.2.13 on 2022-05-20 14:39

import apps.mascota.models
import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('adopcion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacuna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('sexo', models.CharField(max_length=10)),
                ('edad_aproximada', models.IntegerField(verbose_name=range(1, 30))),
                ('fecha_rescate', models.DateField(validators=[django.core.validators.MaxValueValidator(limit_value=datetime.datetime(2022, 5, 20, 14, 39, 26, 54492))])),
                ('imagen', models.ImageField(blank=True, null=True, upload_to=apps.mascota.models.upload_location)),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adopcion.persona')),
                ('vacuna', models.ManyToManyField(blank=True, null=True, to='mascota.Vacuna')),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
    ]
