from django.db import models
from appComuna.models import Comuna
from appEmpresa.models import Empresa


# Create your models here.
class Contacto(models.Model):
    IdContacto = models.AutoField(primary_key=True,serialize=False,verbose_name='IdContacto')
    Nombre_contacto = models.TextField(max_length=255, null=False)
    Apellidos = models.TextField(max_length=255, null=False)
    Telefono = models.TextField(max_length=8, null=False)
    Email = models.EmailField(max_length=50, null=False)
    Direccion = models.TextField(max_length=150, null=False)
    Comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, db_column='Nombre')

  

    def __str__(self):
        return '%s' %(self.Nombre_contacto)

class Agenda(models.Model):
    IdAgenda = models.AutoField(primary_key=True,serialize=False)
    Empresa_agenda = models.ForeignKey(Empresa, on_delete=models.CASCADE,db_column='Empresa')
    Contacto_agenda = models.ForeignKey(Contacto, on_delete=models.CASCADE,db_column='Contacto')

    def __str__(self):
        return '%s,%s,%s' %(self.IdAgenda,self.Empresa_agenda,self.Contacto_agenda)