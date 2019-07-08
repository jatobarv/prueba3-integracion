from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import usuario, producto, servicio
from .forms import pacienteForm, agendaForm, examenesForm
from .serializers import pacienteSerializer, examenesSerializer, agendaSerializer
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class listapaciente(viewsets.ModelViewSet):
    queryset = usuario.objects.all()
    serializer_class = pacienteSerializer


class listaexamenes(viewsets.ModelViewSet):
    queryset = producto.objects.all()
    serializer_class = examenesSerializer


class listaagenda(viewsets.ModelViewSet):
    queryset = servicio.objects.all()
    serializer_class = agendaSerializer


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
    return render(request, "pacienteForm/usuario_form.html", context)


def examenes_view(request):
    form = examenesForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = examenesForm()

    context = {
        'form': form
    }
    return render(request, "pacienteForm/producto_form.html", context)


def agenda_view(request):
    form = agendaForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = agendaForm()

    context = {
        'form': form
    }
    return render(request, "pacienteForm/servicio_form.html", context)


def detalle_paciente(request):
    pac = usuario.objects.all()
    context = {'pac': pac}
    return render(request, 'pacienteForm/usuario.html', context)
