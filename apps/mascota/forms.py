from django import forms

from apps.mascota.api.utils import ChoiceFieldNoValidation
from apps.mascota.models import Mascota, Vacuna


class MascotaForm(forms.Form):

    nombre = forms.CharField()
    sexo = forms.CharField()
    edad_aproximada = forms.CharField()
    fecha_rescate = forms.DateField()
    persona = ChoiceFieldNoValidation(widget=forms.Select(
        attrs={'required': 'False', "data-toggle": "select2"}))
    vacuna = ChoiceFieldNoValidation(widget=forms.CheckboxSelectMultiple(
        attrs={"data-toggle": "select2"}), required=False, choices=[])

    # class Meta:
        # model = Mascota

        # fields = [
        #     'nombre',
        #     'sexo',
        #     'edad_aproximada',
        #     'fecha_rescate',
        #     'persona',
        #     'vacuna',
        #     # 'imagen',
        # ]
        # labels = {
        #     'nombre': 'Nombre',
        #     'sexo': 'Sexo',
        #     'edad_aproximada': 'Edad Aproximada',
        #     'fecha_rescate': 'Fecha de rescate',
        #     'persona': 'Adoptante',
        #     'vacuna': 'Vacunas',
        #     # 'imagen': 'Imagen',
        # }
        # widgets = {
        #     'nombre': forms.TextInput(attrs = {'class': 'form-control'}),
        #     'sexo': forms.TextInput(attrs = {'class': 'form-control'}),
        #     'edad_aproximada': forms.TextInput(attrs = {'class': 'form-control'}),
        #     'fecha_rescate': forms.TextInput(attrs = {'class': 'form-control'}),
        #     'persona': forms.Select(attrs = {'class': 'form-control'}),
        #     'vacuna': forms.CheckboxSelectMultiple(),
        # }


class VacunaForm(forms.ModelForm):

    class Meta:
        model = Vacuna

        fields = [
            'nombre',
        ]
        labels = {
            'nombre': 'Nombre de la vacuna',
        }
        widgets = {
            'nombre': forms.TextInput(attrs = {'class': 'form-control'}),
        }