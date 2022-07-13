from django.forms import ModelForm
from appContacto.models import *
from django import forms


class ContactoForm(ModelForm):

    IdContacto = forms.CharField(max_length=50, required=False,label=False,widget = forms.NumberInput(attrs={'hidden':True}))
    Nombre_contacto = forms.CharField(max_length=50, required=True, widget = forms.TextInput(attrs={'class':'form-control my-2','placeholder': 'Nombre de contacto'}))
    Apellidos = forms.CharField(max_length=50, required=True  ,widget = forms.TextInput(attrs={'class':'form-control my-2','placeholder': 'Apelldidos contacto'}))
    Telefono = forms.CharField(min_length=9,max_length=9, required=True  ,widget = forms.TextInput(attrs={'class':'form-control my-2','placeholder': 'XXXXXXX90'}))
    Email = forms.CharField(max_length=50, required=True  ,widget = forms.TextInput(attrs={'class':'form-control my-2','placeholder': 'example@gmail.com'}))
    Direccion = forms.CharField(max_length=50, required=True  ,widget = forms.TextInput(attrs={'class':'form-control my-2','placeholder': 'Dirección contacto'}))
    
    
    
    class Meta:
        model = Contacto
        fields = [
            'IdContacto',
            'Nombre_contacto',
            'Apellidos',
            'Telefono',
            'Email',
            'Direccion',
            'Comuna'
        ]

        labels = {
            'Nombre_contacto':'Nombre',
            'Apellidos':'Apellidos',
            'Telefono':'Teléfono',
            'Email':'Email',
            'Direccion':'Dirección',
            'Comuna':'Comuna',
        }

        widgets = {
            'IdContacto': forms.NumberInput(),
        	'Nombre_contacto':forms.TextInput(attrs={'class':'form-control my-3','placeholder': 'Nombre de contacto'}),
        	'Apellidos':forms.TextInput(attrs={'class':'form-control my-3','placeholder': 'Apelldidos contacto'}),
            'Telefono':forms.TextInput(attrs={'class':'form-control my-3','placeholder': 'XXXXXXX90'}),
            'Email':forms.TextInput(attrs={'class':'form-control my-3','placeholder': 'example@gmail.com'}),
        	'Direccion':forms.TextInput(attrs={'class':'form-control my-3','placeholder': 'Dirección contacto'}),
        	'Comuna':forms.Select(attrs={'class':'form-control my-3','placeholder': 'Comuna contacto'})
         }



