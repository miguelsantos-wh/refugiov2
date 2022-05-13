import json

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.http import HttpResponse
from django.core import serializers

import requests.exceptions

from apps.mascota.forms import MascotaForm, VacunaForm
from apps.mascota.models import Mascota, Vacuna

from apps.mascota.api.utils import get_protocol
from apps.mascota.api.view_apiviewd import (mascota_list_ad, mascota_detail_ad, mascota_detail_persona_ad,
                                            persona_list_ap, vacuna_list_ap)
from apps.mascota.api.view_apiview import (MascotaListAV, MascotaDetailAV, MascotaDetailPersonaAV, PersonaListAV,
                                           VacunaListAV)
from apps.mascota.api.view_apiviewg import (MascotaListAVG, MascotaDetailAVG, MascotaDetailPersonaAVG,
                                            PersonaListAVG, VacunaListAVG)
from apps.mascota.api.view_viewsets import (MascotaViewSet, PersonaViewSet, VacunaViewSet)

# class MascotaList(ListView):
#     model = Mascota
#     template_name = "mascota/mascota_list.html"
#     paginate_by = 10

protocol = get_protocol()
# apiVersion = "v1"


def index(request):
    return redirect('mascota-list', api_v='v1')


def mascota_create(request, api_v):
    # cookies = request.COOKIES
    # host = request.get_host()
    # csrftoken = request.COOKIES.get('csrftoken')
    form = MascotaForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            data = form.cleaned_data
            data['fecha_rescate'] = form.data['fecha_rescate']
            data['persona'] = int(data['persona'])
            data['vacuna'] = eval(data['vacuna']) if data['vacuna'] else []
            # url_mascota = "{0}{1}/api/{2}/mascotas/".format(protocol, host, api_v)
            # response = requests.post(url=url_mascota, data=data, headers={"X-CSRFToken": csrftoken}, cookies=cookies)
            # if response.ok:
            instance = {
                'v1': mascota_list_ad,
                'v2': MascotaListAV.as_view(),
                'v3': MascotaListAVG.as_view(),
                'v4': MascotaViewSet.as_view({'post': 'create'}),
            }
            data = instance.get(api_v)(request).data
            return redirect('mascota-list', api_v=api_v)
    # form = set_mascota_form(form, cookies, host, api_v)
    form = set_mascota_form(form=form, api_v=api_v, request=request)
    return render(request, 'mascota/mascota_form.html', {'form': form})


def set_mascota_form(form=None, cookies=None, host=None, api_v=None, request=None):
    # url_persona = "{0}{1}/api/{2}/personas/".format(protocol, host, api_v)
    # url_vacuna = "{0}{1}/api/{2}/vacunas/".format(protocol, host, api_v)
    # response_persona = requests.get(url=url_persona, cookies=cookies)
    # response_vacuna = requests.get(url=url_vacuna, cookies=cookies)
    instance_persona = {
        'v1': persona_list_ap(request).data,
        'v2': PersonaListAV.as_view()(request).data,
        'v3': PersonaListAVG.as_view()(request).data,
        'v4': PersonaViewSet.as_view({'get': 'list'})(request).data,
    }
    instance_vacuna = {
        'v1': vacuna_list_ap(request).data,
        'v2': VacunaListAV().as_view()(request).data,
        'v3': VacunaListAVG.as_view()(request).data,
        'v4': VacunaViewSet.as_view({'get': 'list'})(request).data,
    }
    data_persona = instance_persona.get(api_v)
    data_vacuna = instance_vacuna.get(api_v)
    list_persona, list_vacuna = [], []
    tuple_vacuna, tuple_persona = (), ()
    # if response_persona.ok and response_vacuna.ok:
    if data_persona and data_vacuna:
        # response_persona = response_persona.json()
        # response_vacuna = response_vacuna.json()
        for persona in data_persona:
            list_persona.append((persona['id'], persona['nombre']+' '+persona['apellidos']))
        for vacuna in data_vacuna:
            list_vacuna.append((vacuna['id'], vacuna['nombre']))
        tuple_persona = tuple(list_persona)
        tuple_vacuna = tuple(list_vacuna)
    form.fields['persona']._set_choices(tuple_persona)
    form.fields['vacuna']._set_choices(tuple_vacuna)
    return form


def mascota_list(request, api_v):
    # cookies = request.COOKIES
    # host = request.get_host()
    # url = "{0}{1}/api/{2}/mascotas/".format(protocol, host, api_v)
    instance = {
        'v1': mascota_list_ad(request).data,
        'v2': MascotaListAV.as_view()(request).data,
        'v3': MascotaListAVG.as_view()(request).data,
        'v4': MascotaViewSet.as_view({'get': 'list'})(request).data,
    }
    # Verificar respuesta, v2(apiview) funciona sin verificacion de session
    data = instance.get(api_v) if 'id' in json.dumps(instance.get(api_v)) else {}
    # response = requests.request("GET", url, cookies=cookies)
    # if response.status_code == 200:
    #     print(response)
    #     response = response.json()
    contexto = {'mascotas': data, 'api_v': api_v}
    return render(request, 'mascota/mascota_list.html', contexto)


def mascota_delete(request, api_v, pk):
    # cookies = request.COOKIES
    # host = request.get_host()
    # csrftoken = request.COOKIES.get('csrftoken')
    # url = "{0}{1}/api/{2}/mascotas/{3}/".format(protocol, host, api_v, pk)
    if request.method == 'POST':
        request.method = 'DELETE'
        instance = {
            'v1': mascota_detail_ad,
            'v2': MascotaDetailAV.as_view(),
            'v3': MascotaDetailAVG.as_view(),
            'v4': MascotaViewSet.as_view({'delete': 'destroy'}),
        }
        delete = instance.get(api_v)(request=request, pk=pk).data
        # headers = {'Content-Type': 'application/json', "X-CSRFToken": csrftoken}
        # response = requests.delete(url, cookies=cookies, headers=headers)
        #
        return redirect('mascota-list', api_v=api_v)
    instance = {
        'v1': mascota_detail_ad(request=request, pk=pk).data,
        'v2': MascotaDetailAV().get(request=request, pk=pk).data,
        'v3': MascotaDetailAVG.as_view()(request=request, pk=pk).data,
        'v4': MascotaViewSet.as_view({'get': 'retrieve'})(request=request, pk=pk).data,
    }
    data = instance.get(api_v)
    # response = requests.request("GET", url, cookies=cookies)
    # response = response.json()
    return render(request, 'mascota/mascota_delete.html', {'mascota': data})


def mascota_edit(request, api_v, pk):
    # cookies = request.COOKIES
    # host = request.get_host()
    # csrftoken = request.COOKIES.get('csrftoken')
    form = MascotaForm(request.POST or None)
    # url = "{0}{1}/api/{2}/mascotas/{3}/".format(protocol, host, api_v, pk)
    if request.method == 'GET':
        # response_mascota = requests.get(url=url, cookies=cookies)
        # response_mascota = response_mascota.json()
        instance = {
            'v1': mascota_detail_ad,
            'v2': MascotaDetailAV.as_view(),
            'v3': MascotaDetailAVG.as_view(),
            'v4': MascotaViewSet.as_view({'get': 'retrieve'}),
        }
        data = instance.get(api_v)(request=request, pk=pk).data
        # form = set_mascota_edit_form(form, cookies, host, data)
        form = set_mascota_edit_form(form, data)
    else:
        if form.is_valid():
            data = form.cleaned_data
            data['fecha_rescate'] = form.data['fecha_rescate']
            data['persona'] = int(data['persona'])
            data['vacuna'] = eval(data['vacuna']) if data['vacuna'] else []
            # response = requests.put(url=url, data=data, headers={"X-CSRFToken": csrftoken}, cookies=cookies)
            # if response.ok:
            request.method = 'PUT'
            instance = {
                'v1': mascota_detail_ad,
                'v2': MascotaDetailAV.as_view(),
                'v3': MascotaDetailAVG.as_view(),
                'v4': MascotaViewSet.as_view({'put': 'update'}),
            }
            data = instance.get(api_v)(request=request, pk=pk).data
            return redirect('mascota-list', api_v=api_v)
    # form = set_mascota_form(form, cookies, host, api_v)
    form = set_mascota_form(form=form, api_v=api_v, request=request)
    return render(request, 'mascota/mascota_form.html', {'form': form})


def set_mascota_edit_form(form, response_mascota):
    form.fields['nombre'].initial = response_mascota['nombre']
    form.fields['sexo'].initial = response_mascota['sexo']
    form.fields['edad_aproximada'].initial = response_mascota['edad_aproximada']
    form.fields['fecha_rescate'].initial = response_mascota['fecha_rescate']
    form.fields['persona'].initial = response_mascota['persona']['id']
    list_vacunas = []
    for vacuna in response_mascota['vacuna']:
        list_vacunas.append(vacuna['id'])
    form.fields['vacuna'].initial = list_vacunas
    return form


def mascota_persona(request, api_v, pk):
    # cookies = request.COOKIES
    # host = request.get_host()
    # url = "{0}{1}/api/{2}/mascotas/{3}/persona/".format(protocol, host, api_v, pk)
    # response = requests.get(url=url, cookies=cookies)
    # if response.ok:
    #     response = response.json()
    instance = {
        'v1': mascota_detail_persona_ad(request=request, pk=pk).data,
        'v2': MascotaDetailPersonaAV.as_view()(request=request, pk=pk).data,
        'v3': MascotaDetailPersonaAVG.as_view()(request=request, pk=pk).data,
        'v4': MascotaViewSet.as_view({'get': 'retrieve'})(request=request, pk=pk).data['persona'],
    }
    data = instance.get(api_v)
    try:
        data = data[0]
    except:
        pass
    return render(request, 'mascota/mascota_persona.html',  {'object': data})

