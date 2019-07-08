from django import forms

from .models import usuario, servicio, producto

class pacienteForm(forms.ModelForm):
    class Meta:
        model = usuario
        fields = '__all__'

class examenesForm(forms.ModelForm):
    class Meta:
        model = producto
        fields = '__all__'
        
class agendaForm(forms.ModelForm):
    class Meta:
        model = servicio
        fields = '__all__'
        