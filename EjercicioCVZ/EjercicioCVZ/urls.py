"""EjercicioCVZ URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls.static import static
from appComuna.views import *
from appContacto.views import *
from appEmpresa.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(('appEmpresa.urls', 'Empresa'))),
    path('',include(('appContacto.urls', 'Contacto'))),
    path('accounts/', include('django.contrib.auth.urls')),
    path('Empresa/',ListarEmpresa, name='Empresa'),
    path('Contacto/',AppContacto, name='Contacto'),
    path('Agenda/',Agenda_empresa, name='Agenda'),
    path('InformacionEmpresas/',Informacion, name='Informacion'),
    

]