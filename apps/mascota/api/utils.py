from django.conf import settings
from django.forms.fields import ChoiceField, MultipleChoiceField


def get_protocol():
    return "http://" if settings.DEBUG else "https://"


class ChoiceFieldNoValidation(ChoiceField):
    def validate(self, value):
        pass
