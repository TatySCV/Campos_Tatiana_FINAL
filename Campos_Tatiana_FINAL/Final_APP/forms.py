from django import forms
from Final_APP.models import Participantes
from Final_APP.models import Institucion

class FormParticipantes(forms.ModelForm):
    class Meta:
        model = Participantes
        fields = '__all__'

class FormInstitucion(forms.ModelForm):
    class Meta:
        model = Institucion
        fields = '__all__'