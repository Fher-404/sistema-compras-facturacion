
#3Importar el path
from django.urls import path

#Importar la vista
from .views import CategoriaView, CategoriaNew, CategoriaEdit, CategoriaDel, SubCategoriaView, SubCategoriaNew, SubCategoriaEdit, SubCategoriaDel, MarcaView , MarcaNew, MarcaEdit, Marca_inactivar, UnidadMedidaView, UnidadMedidaNew

##Creamos la nueva ruta aqui asegurandonos de pasar la vista y incluirla aqui as a view y poner el nombre de la misma
##Al momento en que la ruta principal llame a esta ruta lo que hara es cargar la vista categoria la cual tiene todos los datos para renderizar la plantilla

urlpatterns = [
    path('categorias/', CategoriaView.as_view(), name="categoria_list"),
    path('categorias/new', CategoriaNew.as_view(), name="categoria_new"),
    ###Al trabajar con edit necesitamos el id del registro que se va a editar entre simbolos de mayor y menor ponemos el tipo de dato y pk por que estamos trabajanod con vista de clase generica
    path('categorias/edit/<int:pk>', CategoriaEdit.as_view(), name="categoria_edit"),
    path('categorias/delete/<int:pk>', CategoriaDel.as_view(), name="categoria_del"),
    ##*Subcategoria---------------------------------------------------------------------------
    path('subcategorias/', SubCategoriaView.as_view(), name="subcategoria_list"),
    path('subcategorias/new', SubCategoriaNew.as_view(), name="subcategoria_new"),
    path('subcategorias/edit/<int:pk>', SubCategoriaEdit.as_view(), name="subcategoria_edit"),
    path('subcategorias/delete/<int:pk>', SubCategoriaDel.as_view(), name="subcategoria_del"),
    ##*MARCAS------------------------------------------------------------------------------------
    path('marcas/', MarcaView.as_view(), name="marcas_list"),
    path('marcas/new', MarcaNew.as_view(), name="marcas_new"),
    path('marca/edit/<int:pk>', MarcaEdit.as_view(), name="marcas_edit"),
    path('marca/inactivar/<int:id>', Marca_inactivar, name="marca_inactivar"),
    ##*Unidades de medida------------------------------------------------------------------------------------
    path('unidad_medida/', UnidadMedidaView.as_view(), name="unidad_medida_list"),
    path('unidad_medida/new', UnidadMedidaNew.as_view(), name="unidad_medida_new"),
]