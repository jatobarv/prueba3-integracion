"""webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from examen import views
from rest_framework import routers
from django.views.generic.base import TemplateView
from examen.views import paciente_view, examenes_view, agenda_view, listapaciente, detalle_paciente


router = routers.DefaultRouter()
router.register('usuario', views.listapaciente)
router.register('producto', views.listaexamenes)
router.register('servicio', views.listaagenda)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('examen.urls')),
    path('crearusuario/', paciente_view, name='crearusuario'),
    path('crearproducto/', examenes_view, name='crearproducto'),
    path('servicio/', agenda_view, name='servicio'),
    path('usuario/', detalle_paciente, name='usuario'),

    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    # path('paciente/', views.listapaciente.as_view()),

]
