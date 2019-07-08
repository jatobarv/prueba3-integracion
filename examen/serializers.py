from rest_framework import serializers
from .models import usuario, servicio, producto


class pacienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = usuario
        fields = '__all__'

class examenesSerializer(serializers.ModelSerializer):

    class Meta:
        model = producto
        fields = '__all__'

class agendaSerializer(serializers.ModelSerializer):

    class Meta:
        model = servicio
        fields = '__all__'

