from django.db import models
from django.contrib.auth.models import User

# Create your models here.
##Crear clase que heredaran todo

class ClaseModelo(models.Model):
    estado = models.BooleanField(default=True)
    
    ####Se obtendra la fecha cuando el objeto se cree
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    ###Cuando se modifique
    fecha_modificacion = models.DateTimeField(auto_now=True)
    
    ##Ver el usuario que crea
    usuario_creador = models.ForeignKey(User, on_delete=models.CASCADE)
    
    ##Tipo entero por que no se pueden referenciar dos veces la misma colunma (el integer va a almacenar el ID del user modificador)
    usuario_modifica = models.IntegerField(blank=True, null=True)
    
    

##No toma en cuenta para realizar las migraciones (solo para heredar)
    class Meta:
        abstract=True