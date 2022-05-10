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


# class MascotaList(ListView):
#     model = Mascota
#     template_name = "mascota/mascota_list.html"
#     paginate_by = 10

protocol = get_protocol()
# apiVersion = "v1"


def index(request):
    return redirect('mascota-list', api_v='v1')


def mascota_create(request, api_v):
    cookies = request.COOKIES
    host = request.get_host()
    csrftoken = request.COOKIES.get('csrftoken')
    form = MascotaForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            data = form.cleaned_data
            data['fecha_rescate'] = form.data['fecha_rescate']
            data['persona'] = int(data['persona'])
            data['vacuna'] = eval(data['vacuna']) if data['vacuna'] else []
            url_mascota = "{0}{1}/api/{2}/mascotas/".format(protocol, host, api_v)
            response = requests.post(url=url_mascota, data=data, headers={"X-CSRFToken": csrftoken}, cookies=cookies)
            if response.ok:
                return redirect('mascota-list', api_v=api_v)
    form = set_mascota_form(form, cookies, host, api_v)
    return render(request, 'mascota/mascota_form.html', {'form': form})


def set_mascota_form(form, cookies, host, api_v):
    url_persona = "{0}{1}/api/{2}/personas/".format(protocol, host, api_v)
    url_vacuna = "{0}{1}/api/{2}/vacunas/".format(protocol, host, api_v)
    response_persona = requests.get(url=url_persona, cookies=cookies)
    response_vacuna = requests.get(url=url_vacuna, cookies=cookies)
    list_persona, list_vacuna = [], []
    tuple_vacuna, tuple_persona = (), ()
    if response_persona.ok and response_vacuna.ok:
        response_persona = response_persona.json()
        response_vacuna = response_vacuna.json()
        for persona in response_persona:
            list_persona.append((persona['id'], persona['nombre']+' '+persona['apellidos']))
        for vacuna in response_vacuna:
            list_vacuna.append((vacuna['id'], vacuna['nombre']))
        tuple_persona = tuple(list_persona)
        tuple_vacuna = tuple(list_vacuna)
    form.fields['persona']._set_choices(tuple_persona)
    form.fields['vacuna']._set_choices(tuple_vacuna)
    return form


def mascota_list(request, api_v):
    cookies = request.COOKIES
    host = request.get_host()
    url = "{0}{1}/api/{2}/mascotas/".format(protocol, host, api_v)
    response = requests.request("GET", url, cookies=cookies)
    if response.status_code == 200:
        response = response.json()
    contexto = {'mascotas': response, 'api_v': api_v}
    return render(request, 'mascota/mascota_list.html', contexto)


def mascota_delete(request, api_v, pk):
    cookies = request.COOKIES
    host = request.get_host()
    csrftoken = request.COOKIES.get('csrftoken')
    url = "{0}{1}/api/{2}/mascotas/{3}/".format(protocol, host, api_v, pk)
    if request.method == 'POST':
        headers = {'Content-Type': 'application/json', "X-CSRFToken": csrftoken}
        response = requests.delete(url, cookies=cookies, headers=headers)
        return redirect('mascota-list', api_v=api_v)
    response = requests.request("GET", url, cookies=cookies)
    response = response.json()
    return render(request, 'mascota/mascota_delete.html', {'mascota': response})


def mascota_edit(request, api_v, pk):
    cookies = request.COOKIES
    host = request.get_host()
    csrftoken = request.COOKIES.get('csrftoken')
    form = MascotaForm(request.POST or None)
    url = "{0}{1}/api/{2}/mascotas/{3}/".format(protocol, host, api_v, pk)
    if request.method == 'GET':
        response_mascota = requests.get(url=url, cookies=cookies)
        response_mascota = response_mascota.json()
        form = set_mascota_edit_form(form, cookies, host, response_mascota)
    else:
        if form.is_valid():
            data = form.cleaned_data
            data['fecha_rescate'] = form.data['fecha_rescate']
            data['persona'] = int(data['persona'])
            data['vacuna'] = eval(data['vacuna']) if data['vacuna'] else []
            response = requests.put(url=url, data=data, headers={"X-CSRFToken": csrftoken}, cookies=cookies)
            if response.ok:
                return redirect('mascota-list', api_v=api_v)
    form = set_mascota_form(form, cookies, host, api_v)
    return render(request, 'mascota/mascota_form.html', {'form': form})


def set_mascota_edit_form(form, cookies, host, response_mascota):
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
    cookies = request.COOKIES
    host = request.get_host()
    url = "{0}{1}/api/{2}/mascotas/{3}/persona/".format(protocol, host, api_v, pk)
    response = requests.get(url=url, cookies=cookies)
    if response.ok:
        response = response.json()
        try:
            response = response[0]
        except:
            pass
    return render(request, 'mascota/mascota_persona.html',  {'object': response})

