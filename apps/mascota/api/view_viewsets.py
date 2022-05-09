from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import action
# from .serializers import UserSerializer, GroupSerializer

from apps.mascota.api.serializers import MascotaSerializer, PersonaSerializer, VacunaSerializer
from apps.mascota.models import Mascota, Vacuna
from apps.adopcion.models import Persona


class MascotaViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite ver o editar mascotas (Viewsets)
    """
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer


class MascotaPersonaViewSet(viewsets.ModelViewSet):
    """
    API endpoint para obtener persona de la mascota (Viewsets)
    """
    serializer_class = PersonaSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk', 0)
        queryset = Persona.objects.filter(mascota=pk)
        return queryset


class MascotaVacunaViewSet(viewsets.ModelViewSet):
    """
    API endpoint para obtener persona de la mascota (Viewsets)
    """
    serializer_class = VacunaSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk', 0)
        queryset = Vacuna.objects.filter(mascota=pk)
        return queryset


class PersonaViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite ver todas las personas (Viewsets)
    """
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer


class VacunaViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite ver todas las vacunas (Viewsets)
    """
    queryset = Vacuna.objects.all()
    serializer_class = VacunaSerializer

