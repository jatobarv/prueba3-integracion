from django.contrib import admin
from . models import paciente, examenes, agenda

admin.site.register(paciente)
admin.site.register(examenes)
admin.site.register(agenda)

