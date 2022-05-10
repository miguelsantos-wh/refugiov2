from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

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


class MascotaListAV(APIView):
    """
    Lista de todas las mascotas o crear una nueva mascota (APIView)
    """
    def get(self, request, format=None):
        mascota = Mascota.objects.all()
        mascota_sr = MascotaSerializer(mascota, many=True)
        return Response(mascota_sr.data)

    def post(self, request, format=None):
        mascota_sr = MascotaSerializer(data=request.data)
        if mascota_sr.is_valid():
            mascota_sr.save()
            return Response(mascota_sr.data, status=status.HTTP_201_CREATED)
        return Response(mascota_sr.errors, status=status.HTTP_400_BAD_REQUEST)


class MascotaDetailAV(APIView):
    """
    Obtener una mascota, actualizar o eliminar (APIView)
    """
    def get_object(self, pk):
        try:
            return Mascota.objects.get(pk=pk)
        except Mascota.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        mascota = self.get_object(pk)
        mascota_sr = MascotaSerializer(mascota)
        return Response(mascota_sr.data)

    def put(self, request, pk, format=None):
        mascota = self.get_object(pk)
        mascota_sr = MascotaSerializer(mascota, data=request.data)
        if mascota_sr.is_valid():
            mascota_sr.save()
            return Response(mascota_sr.data)
        return Response(mascota_sr.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        mascota = self.get_object(pk)
        mascota.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MascotaDetailPersonaAV(APIView):
    """
    Obtener persona de la mascota (APIView)
    """
    def get_object(self, pk):
        try:
            return Persona.objects.filter(mascota=pk).first()
        except Persona.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        persona = self.get_object(pk=pk)
        persona_sr = PersonaSerializer(persona)
        return Response(persona_sr.data)


class MascotaDetailVacunaAV(APIView):
    """
    Obtener vacuna de la mascota (APIView)
    """
    def get_object(self, pk):
        try:
            return Vacuna.objects.filter(mascota=pk)
        except Vacuna.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        vacuna = self.get_object(pk=pk)
        vacuna_sr = VacunaSerializer(vacuna, many=True)
        return Response(vacuna_sr.data)


class PersonaListAV(APIView):
    """
    Lista de todas las personas (APIView)
    """
    def get(self, request, format=None):
        persona = Persona.objects.all()
        persona_sr = PersonaSerializer(persona, many=True)
        return Response(persona_sr.data)


class VacunaListAV(APIView):
    """
    Lista de todas las vacunas (APIView)
    """
    def get(self, request, format=None):
        vacuna = Vacuna.objects.all()
        vacuna_sr = VacunaSerializer(vacuna, many=True)
        return Response(vacuna_sr.data)
