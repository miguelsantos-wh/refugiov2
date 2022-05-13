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