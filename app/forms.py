from django.forms import ModelForm
from app.models import carros

class carrosForm(ModelForm):
    class Meta:
        model = carros
        fields = ['modelo','marca','ano']