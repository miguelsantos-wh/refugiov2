from __future__ import unicode_literals

import datetime

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from apps.adopcion.models import Persona


# Create your models here.
class Vacuna(models.Model):
    nombre = models.CharField(max_length=50)

    def __unicode__(self):
        return '{}'.format(self.nombre)


def upload_location(instance, filename):
    filebase, extension = filename.split('.')
    return '%s-%s-%s.%s' %(instance.persona, instance.nombre, instance.fecha_rescate, extension)


# class Raza(models.Model):
#     nombre = models.CharField(max_length=50)
#
#     def __unicode__(self):
#         return '{}'.format(self.nombre)


class Mascota(models.Model):
    # folio = models.CharField(max_length=10,primary_key=True)
    nombre = models.CharField(max_length=20)
    sexo = models.CharField(max_length=10)
    edad_aproximada = models.IntegerField(validators=[
            MaxValueValidator(30),
            MinValueValidator(1)
        ])
    fecha_rescate = models.DateField(validators=[MaxValueValidator(limit_value=datetime.date.today())])
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    vacuna = models.ManyToManyField(Vacuna, null=True, blank=True)
    # raza = models.ForeignKey(Raza, null=True, blank=True, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to=upload_location, null=True, blank=True)

    class Meta:
        ordering = ('-id',)
