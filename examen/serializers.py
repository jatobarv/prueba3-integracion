from rest_framework import serializers
from .models import paciente, agenda, examenes


class pacienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = paciente
        fields = '__all__'

class examenesSerializer(serializers.ModelSerializer):

    class Meta:
        model = examenes
        fields = '__all__'

class agendaSerializer(serializers.ModelSerializer):

    class Meta:
        model = agenda
        fields = '__all__'

