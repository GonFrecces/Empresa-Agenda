from tkinter.tix import Tree
from django.forms import ModelForm
from appEmpresa.models import *
from appContacto.models import *
from django import forms


class EmpresaForm(ModelForm):

    IdEmpresa = forms.CharField(max_length=50, required=False,label=False,widget = forms.NumberInput(attrs={'hidden':True}))
    Nombre_empresa = forms.CharField(max_length=50, required=True, widget = forms.TextInput(attrs={'class':'form-control my-2','placeholder': 'Nombre de empresa'}))
    Rut = forms.CharField(min_length=9,max_length=10, required=True  ,widget = forms.TextInput(attrs={'class':'form-control my-2','placeholder': 'Rut empresa'}))
    Direccion = forms.CharField(max_length=50, required=True  ,widget = forms.TextInput(attrs={'class':'form-control my-2','placeholder': 'Dirección empresa'}))
    
    
    class Meta:
        model = Empresa
        fields = [
            'IdEmpresa',
            'Nombre_empresa',
            'Rut',
            'Direccion',
            'Comuna'
        ]

        labels = {
            'Nombre_empresa': 'Nombre',
            'Rut':'Rut empresa',
            'Direccion':'Dirección',
            'Comuna':'Comuna',
        }

        widgets = {
            'IdEmpresa': forms.NumberInput(),
        	'Nombre_empresa':forms.TextInput(attrs={'class':'form-control my-3','placeholder': 'Nombre empresa'}),
        	'Rut':forms.TextInput(attrs={'class':'form-control my-3','placeholder': 'Rut empresa'}),
        	'Direccion':forms.TextInput(attrs={'class':'form-control my-3','placeholder': 'Dirección empresa'}),
        	'Comuna':forms.Select(attrs={'class':'form-control my-3','placeholder': 'Comuna empresa'})
         }


class AgendaForm(ModelForm):
    class Meta:
        model = Agenda
        fields = [
            'Empresa_agenda',
            'Contacto_agenda'
        ]

        labels = {
            'Empresa_agenda':'Empresas',
            'Contacto_agenda':'Contactos',
        }

        widgets = {
            'Empresa_agenda':forms.Select(attrs={'class':'form-control my-3'}),
        	'Contacto_agenda':forms.Select(attrs={'class':'form-control my-3'})
         }