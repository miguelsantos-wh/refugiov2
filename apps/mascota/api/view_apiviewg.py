from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from apps.mascota.api.serializers import MascotaSerializer, PersonaSerializer, VacunaSerializer
from apps.mascota.models import Mascota, Vacuna
from apps.adopcion.models import Persona

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


from django.http import Http404
from rest_framework.views import APIView

from rest_framework import mixins
from rest_framework import generics


class MascotaListAVG(generics.ListCreateAPIView):
    """
    Lista de todas las mascotas o crear una nueva mascota (Generic ApiView)
    """
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer


class MascotaDetailAVG(generics.RetrieveUpdateDestroyAPIView):
    """
    Obtener una mascota, actualizar o eliminar (Generic ApiView)
    """
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer


class MascotaDetailPersonaAVG(generics.ListCreateAPIView):
    """
    Obtener persona de la mascota (Generic ApiView)
    """
    serializer_class = PersonaSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk', 0)
        queryset = Persona.objects.filter(mascota=pk)
        return queryset


class MascotaDetailVacunaAVG(generics.ListCreateAPIView):
    """
    Obtener persona de la mascota (Generic ApiView)
    """
    serializer_class = VacunaSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk', 0)
        queryset = Vacuna.objects.filter(mascota=pk)
        return queryset


class PersonaListAVG(generics.ListCreateAPIView):
    """
    Lista de todas las personas (Generic ApiView)
    """
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer


class VacunaListAVG(generics.ListCreateAPIView):
    """
    Lista de todas las vacunas (Generic ApiView)
    """
    queryset = Vacuna.objects.all()
    serializer_class = VacunaSerializer
