from rest_framework import serializers
from Final_APP import models

class AutorSerial(serializers.ModelSerializer):
    class Meta:
        model = models.Autor
        fields = '__all__'

class ParticipanteSerial(serializers.ModelSerializer):
    class Meta:
        model = models.Participantes
        fields = '__all__'

class InstitucionSerial(serializers.ModelSerializer):
    class Meta:
        model = models.Institucion
        fields = '__all__'