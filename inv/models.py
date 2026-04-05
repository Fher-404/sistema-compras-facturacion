from django.db import models

##importamos la clase base que tenemos
from bases.models import ClaseModelo

# Create your models here.

#*--------------------------------------------------------------CATEGORIAS----------------------------------------------------------------


class Categoria(ClaseModelo):
    ###EL campo ID lo hace automatico django y le hace la primary key
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripcion de la categoria',
        unique=True
    )


###Para que no me muestre el id si no lo que esta en la descripcion en el nombre y guardamos en mayusuclas
    def __str__(self):
        return '{}'.format(self.descripcion)
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Categoria, self).save()
        
        ##Definimos como vamos a llamar cuando este en mayusculas
        class Meta:
            verbose_name_plural = "Categorias"


#*--------------------------------------------------------------SUBCATEGORIAS----------------------------------------------------------------

class SubCategoria(ClaseModelo):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, blank=True)
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripcion de la categoria',
        unique=True
    )
    
##Descripcion de categoria y subcategoria
    def __str__(self):
        return '{}:{}'.format(self.categoria.descripcion, self.descripcion)
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(SubCategoria, self).save()
    
    ##Definimos como vamos a llamar cuando este en mayusculas
    class Meta:
        verbose_name_plural = "Sub Categorias"
        ##Asegura que no hayan dos categorias con el la misma descripcion
        models.UniqueConstraint(fields=['categoria', 'descripcion'], name='categoria_unique_descripcion')
        


#*--------------------------------------------------------------MARCAS----------------------------------------------------------------

class Marca(ClaseModelo):
    ###EL campo ID lo hace automatico django y le hace la primary key
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripcion de la Marca',
        unique=True
    )

###Redefinimos el str para que no me muestre el id si no el nombre que esta en la descripcion 
    def __str__(self):
        return '{}'.format(self.descripcion)
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Marca, self).save()
        
        ##Definimos como vamos a llamar cuando este en mayusculas
        class Meta:
            verbose_name_plural = "Marcas"


#*------------------------------------------------------------Unidades de Medida---------------------------------------------------------------
class UnidadMedida(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text="Unidad de medida",
        unique = True
    )
    
    ###Redefinimos el STR que es el detalle del objeto para muestre la descripcion en UPPER
    def __str__(self):
        return '{}'.format(self.descripcion.upper)
    
    def save (self):
        self.descripcion = self.descripcion.upper()
        super(UnidadMedida, self).save()
    
    class Meta:
        verbose_name_plural = "Unidades de Medida"