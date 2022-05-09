from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated

from apps.mascota.api.serializers import MascotaSerializer, PersonaSerializer, VacunaSerializer
from apps.mascota.models import Mascota, Vacuna
from apps.adopcion.models import Persona

from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response


from django.http import Http404
from rest_framework.views import APIView

from rest_framework import mixins
from rest_framework import generics


@api_view(['GET', 'POST'])
def mascota_list_ad(request, format=None):
    """
    Lista de todas las mascotas o crear una nueva mascota (APIView Decorate)
    """
    if request.method == 'GET':
        mascota = Mascota.objects.all()
        mascota_sr = MascotaSerializer(mascota, many=True)
        return Response(mascota_sr.data)

    elif request.method == 'POST':
        mascota_sr = MascotaSerializer(data=request.data)
        if mascota_sr.is_valid():
            mascota_sr.save()
            return Response(mascota_sr.data, status=status.HTTP_201_CREATED)
        return Response(mascota_sr.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def mascota_detail_ad(request, pk, format=None):
    """
    Obtener una mascota, actualizar o eliminar (APIView Decorate)
    """
    try:
        mascota = Mascota.objects.get(pk=pk)
    except Mascota.DoesNotExist:
        raise Http404

    if request.method == 'GET':
        mascota_sr = MascotaSerializer(mascota)
        return Response(mascota_sr.data)

    elif request.method == 'PUT':
        mascota_sr = MascotaSerializer(mascota, data=request.data)
        if mascota_sr.is_valid():
            mascota_sr.save()
            return Response(mascota_sr.data)
        return Response(mascota_sr.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        mascota.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def mascota_detail_persona_ad(request, pk, format=None):
    """
    Obtener persona de la mascota (APIView Decorate)
    """
    try:
        persona = Persona.objects.filter(mascota=pk)
    except Persona.DoesNotExist:
        raise Http404

    if request.method == 'GET':
        persona_sr = PersonaSerializer(persona, many=True)
        return Response(persona_sr.data)


@api_view(['GET'])
def mascota_detail_vacuna_ad(request, pk, format=None):
    """
    Obtener persona de la mascota (APIView Decorate)
    """
    try:
        vacuna = Vacuna.objects.filter(mascota=pk)
    except Vacuna.DoesNotExist:
        raise Http404

    if request.method == 'GET':
        vacuna_sr = VacunaSerializer(vacuna, many=True)
        return Response(vacuna_sr.data)


@api_view(['GET'])
def persona_list_ap(request, format=None):
    """
    Lista de todas las personas (APIView Decorate)
    """
    if request.method == 'GET':
        persona = Persona.objects.all()
        persona_sr = PersonaSerializer(persona, many=True)
        return Response(persona_sr.data)


@api_view(['GET'])
def vacuna_list_ap(request, format=None):
    """
    Lista de todas las vacunas (APIView Decorate)
    """
    if request.method == 'GET':
        vacuna = Vacuna.objects.all()
        vacuna_sr = VacunaSerializer(vacuna, many=True)
        return Response(vacuna_sr.data)
