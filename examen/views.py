from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import paciente, examenes, agenda
from .forms import pacienteForm, agendaForm, examenesForm
from .serializers import pacienteSerializer
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

class listapaciente(viewsets.ModelViewSet):
    queryset = paciente.objects.all()
    serializer_class = pacienteSerializer

    #  def get(self, request):
    #     paciente1 = paciente.objects.all()
    #     serializer = pacienteSerializer(paciente1, many=True)
    #     return Response(serializer.data)

    # def post(self):
    #     pass

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def paciente_view(request):
    form = pacienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = pacienteForm()

    context = {
        'form': form
    }
    return render(request, "pacienteForm/paciente_form.html", context)

def examenes_view(request):
    form = examenesForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = examenesForm()

    context = {
        'form': form
    }
    return render(request, "pacienteForm/examen_form.html", context)


def agenda_view(request):
    form = agendaForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = agendaForm()

    context = {
        'form': form
    }
    return render(request, "pacienteForm/agenda_form.html", context)
