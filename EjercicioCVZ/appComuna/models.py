from django.db import models

# Create your models here.
class Comuna(models.Model):
    
    IdComuna = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=60, blank=True, null=True)
    
    
    def __str__(self):
        return '%s'%(self.Nombre)