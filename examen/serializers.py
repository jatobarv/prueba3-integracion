from rest_framework import serializers
from .models import paciente


class pacienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = paciente
        fields = '__all__'
