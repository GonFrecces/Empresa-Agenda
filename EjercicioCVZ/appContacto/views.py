from django.shortcuts import render, redirect
from django.contrib import messages
from appContacto.models import Contacto
from appContacto.forms import ContactoForm
# Create your views here.

def AppContacto(request):
    contacto = Contacto.objects.all()
    data = {'form':ContactoForm(),
    'contacto':contacto
    }
    if request.method == 'POST':
        
        IdContacto = request.POST.get('IdContacto')
        Telefono_contacto = request.POST.get('Telefono')
        
        
        formulario = ContactoForm(request.POST)

        if formulario.is_valid():
            existe = Contacto.objects.filter(Telefono = Telefono_contacto)
            if existe:
                messages.warning(request, 'Este contacto ya ha sido ingresado.')
                return redirect('Contacto')
            else:

                if (IdContacto == ''):
                    
                    formulario.save()
                    messages.success(request, 'Contacto ingresado con exíto.')
                    return redirect('Contacto')
                    
                else:
                    print(IdContacto)
                    contacto = Contacto.objects.get(IdContacto=IdContacto)
                    formulario = ContactoForm(data = request.POST, instance=contacto)
                    if formulario.is_valid():
                        formulario.save()
                        data['form'] = formulario
                        messages.success(request, 'Contacto Editado con exíto.')
                        return redirect('Contacto')

    return render(request,"AppContacto/Contacto.html",data)



def EliminarContacto(request, IdContacto):
    contacto = Contacto.objects.get(IdContacto = IdContacto)
    if contacto is not None:
        contacto.delete()
        messages.success(request, "Contacto eliminado con exíto!")
        return redirect("Contacto")

