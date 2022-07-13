from django.urls import path
from appContacto.views import *


urlpatterns = [
    path('Eliminar_contacto/<IdContacto>/',EliminarContacto, name='Eliminar_contacto'),
    
]