from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import paciente
from .serializers import pacienteSerializer


class listapaciente(viewsets.ModelViewSet):
    queryset = paciente.objects.all()
    serializer_class = pacienteSerializer

    #  def get(self, request):
    #     paciente1 = paciente.objects.all()
    #     serializer = pacienteSerializer(paciente1, many=True)
    #     return Response(serializer.data)

    # def post(self):
    #     pass
