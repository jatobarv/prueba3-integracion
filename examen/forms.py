from django import forms

from .models import paciente, examenes, agenda

class pacienteForm(forms.ModelForm):
    class Meta:
        model = paciente
        fields = '__all__'

class examenesForm(forms.ModelForm):
    class Meta:
        model = examenes
        fields = '__all__'
        
class agendaForm(forms.ModelForm):
    class Meta:
        model = agenda
        fields = '__all__'
        