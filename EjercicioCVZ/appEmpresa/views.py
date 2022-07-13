from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from appEmpresa.models import Empresa
from appContacto.models import Contacto, Agenda
from appEmpresa.forms import EmpresaForm, AgendaForm
# Create your views here.

def login_users(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print(user)
        if user :
            login(request, user)
            return redirect('Empresa:Dashboard')
        else:
            messages.warning(request, "Correo o contrasena invalidas")
            return render(request, "Authenticate/Login.html")

    else:
        return render(request,"Authenticate/Login.html")

def logout(request):
    logout(request)
    return redirect('/')


def Dashboard(request):
    empresas = Empresa.objects.count()
    contactos = Contacto.objects.count()
    data = {'empresas': empresas, 'contactos': contactos}
    print(empresas)
    print(contactos)
    return render(request, "Home/Dashboard.html",data)

def ListarEmpresa(request):
    empresa = Empresa.objects.all()
    data = {'form':EmpresaForm(),
    'empresa':empresa
    }
    if request.method == 'POST':
        
        IdEmpresa = request.POST.get('IdEmpresa')
        RutEmpresa = request.POST.get('Rut')

        existe = Empresa.objects.filter(Rut = RutEmpresa)

        formulario = EmpresaForm(request.POST)
        if formulario.is_valid():
            if existe :
                messages.warning(request, 'Esta empresa ya ha sido ingresada.')
                return redirect('Empresa')
            else:
                if (IdEmpresa == ''):
                    
                    formulario.save()
                    messages.success(request, 'Empresa ingresada con exito.')
                    return redirect('Empresa')
                    
                else:
                    print(IdEmpresa)
                    empresa = Empresa.objects.get(IdEmpresa=IdEmpresa)
                    formulario = EmpresaForm(data = request.POST, instance=empresa)
                    if formulario.is_valid():
                        formulario.save()
                        data['form'] = formulario
                        messages.success(request, 'Empresa Editada con exito.')
                        return redirect('Empresa')

    return render(request,"AppEmpresa/Empresa.html",data)


def EliminarEmpresa(request, IdEmpresa):
    empresa = Empresa.objects.get(IdEmpresa = IdEmpresa)
    if empresa is not None:
        empresa.delete()
        messages.success(request, "Empresa eliminada con exito!")
        return redirect("Empresa")


def Agenda_empresa(request):
    data = {'form':AgendaForm()}
    if request.method == 'POST':
        
        formulario = AgendaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            print(formulario.fields.values)
            messages.success(request, 'Contacto asociado con exito.')
            return redirect('Agenda')


    return render(request,"Agenda/Agenda.html",data)


def Informacion(request):
    contactos = Contacto.objects.all()
    empresas = Empresa.objects.all()
    agenda = Agenda.objects.all().values('Empresa_agenda','Contacto_agenda')
    data = {'agenda':agenda, 'empresas': empresas, 'contacto': contactos}
    
    return render(request,"AppEmpresa/InformacionEmpresas.html",data)







