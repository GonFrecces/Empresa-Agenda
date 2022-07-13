from django.db import models
from appComuna.models import Comuna

# Create your models here.
class Empresa(models.Model):

    IdEmpresa = models.AutoField(primary_key=True,serialize=False,verbose_name='IdContacto')
    Nombre_empresa = models.CharField(max_length=255, null=False)
    Rut = models.CharField(max_length=10, null=False)
    Direccion = models.CharField(max_length=100, null=False)
    Comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, db_column='Nombre')
    

    def __str__(self):
        return '%s' %(self.Nombre_empresa)



 