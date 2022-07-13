from django.urls import path
from appEmpresa.views import *


urlpatterns = [
    
    path('',login_users,name='Login'),
    path('Dashboard/',Dashboard, name='Dashboard'),
    path('Eliminar_empresa/<IdEmpresa>/',EliminarEmpresa, name='Eliminar_empresa'),
    
]