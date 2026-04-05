from django.shortcuts import render, redirect
###Para que la funcionalidad solo se pueda utilizar logeado
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from django.views import generic

from .models import Categoria, SubCategoria, Marca, UnidadMedida

from .forms import CategoriaForm, SubCategoriaForm, MarcaForm, UnidadMedidaForm
###Para que cuando el formulario sea enviado se reverse a una pagina
from django.urls import reverse_lazy

# Create your views here.

#*--------------------------------------------------------------CATEGORIAS----------------------------------------------------------------

class CategoriaView(LoginRequiredMixin, generic.ListView):
    ##El modelo que va a mostar
    model = Categoria
    ##Nombre de la vista
    template_name = "inv/categoria_list.html"
    ##Es la variable que va a pasar la vista con la informacion que va a renderizar a la plantilla
    context_object_name = "obj"
    ###Es la url que va a saltar cuando no este logueado
    login_url = "bases:login"

####Creando una vista para enviar
class CategoriaNew(LoginRequiredMixin, generic.CreateView):
    ##El modelo con el que va a trabajar
    model= Categoria
    ##El template que va a utilizar
    template_name = "inv/categoria_form.html"
    ##el context (por si acaso)
    context_object_name = "obj"
    ###El formulario que va a actuar
    form_class = CategoriaForm
    ##La pagina a donde redireccionara cuando este listo el formulario (para evitar datos duplicados)
    success_url = reverse_lazy("inv:categoria_list")
    ##Que tengas que estar logeado para usar
    login_url= "base:login"

    #####Obtener el usuario que esta logeado en este momento, el que va a procesar el formulario
    def form_valid(self, form):
        form.instance.usuario_creador = self.request.user
        return super().form_valid(form)
    
    
    ####Creando una vista editar, es exactamente lo mismo solo pondremos UpdateView
class CategoriaEdit(LoginRequiredMixin, generic.UpdateView):
    model= Categoria
    template_name = "inv/categoria_form.html"
    context_object_name = "obj"
    form_class = CategoriaForm
    success_url = reverse_lazy("inv:categoria_list")
    login_url= "base:login"

    #####Obtener el usuario que esta logeado en este momento, el que va a modificar el formulario
    def form_valid(self, form):
        form.instance.usuario_modifica = self.request.user.id
        return super().form_valid(form)

###Clase para borrar de la base de datos (aunque es importante no darle tanta libertad al usuario de borrar datos de la base de datos)
class CategoriaDel(LoginRequiredMixin, generic.DeleteView):
    model = Categoria
    template_name='inv/categoria_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy("inv:categoria_list")
    
    

#*--------------------------------------------------------------SUBCATEGORIAS----------------------------------------------------------------

class SubCategoriaView(LoginRequiredMixin, generic.ListView):
    ##El modelo que va a mostar
    model = SubCategoria
    ##Nombre de la vista
    template_name = "inv/subcategoria_list.html"
    ##Es la variable que va a pasar la vista con la informacion que va a renderizar a la plantilla
    context_object_name = "obj"
    ###Es la url que va a saltar cuando no este logueado
    login_url = "bases:login"
    
    
class SubCategoriaNew(LoginRequiredMixin, generic.CreateView):
    ##El modelo con el que va a trabajar
    model= SubCategoria
    ##El template que va a utilizar
    template_name = "inv/subcategoria_form.html"
    ##el context (por si acaso)
    context_object_name = "obj"
    ###El formulario que va a actuar
    form_class = SubCategoriaForm
    ##La pagina a donde redireccionara cuando este listo el formulario (para evitar datos duplicados)
    success_url = reverse_lazy("inv:subcategoria_list")
    ##Que tengas que estar logeado para usar
    login_url= "base:login"

    def form_valid(self, form):
        form.instance.usuario_creador = self.request.user
        return super().form_valid(form)
    
    
class SubCategoriaEdit(LoginRequiredMixin, generic.UpdateView):
    model= SubCategoria
    template_name = "inv/subcategoria_form.html"
    context_object_name = "obj"
    form_class = SubCategoriaForm
    success_url = reverse_lazy("inv:subcategoria_list")
    login_url= "base:login"

    #####Obtener el usuario que esta logeado en este momento, el que va a modificar el formulario
    def form_valid(self, form):
        form.instance.usuario_modifica = self.request.user.id
        return super().form_valid(form)

###Clase para borrar de la base de datos (aunque es importante no darle tanta libertad al usuario de borrar datos de la base de datos)
class SubCategoriaDel(LoginRequiredMixin, generic.DeleteView):
    model = SubCategoria
    template_name='inv/subcategoria_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy("inv:subcategoria_list")

#*--------------------------------------------------------------MARCAS----------------------------------------------------------------

class MarcaView(LoginRequiredMixin, generic.ListView):
    model = Marca
    template_name = "inv/marcas_list.html"
    context_object_name = "obj"
    login_url = "base:login"


class MarcaNew(LoginRequiredMixin, generic.CreateView):
    model = Marca
    template_name = "inv/marcas_form.html"
    context_object_name = "obj"
    form_class = MarcaForm
    success_url = reverse_lazy("inv:marcas_list")
    login_url = "base:login"

    def form_valid(self, form):
        form.instance.usuario_creador = self.request.user
        messages.success(self.request, "Marca creada correctamente")
        return super().form_valid(form)


class MarcaEdit(LoginRequiredMixin, generic.UpdateView):
    model = Marca
    template_name = "inv/marcas_form.html"
    context_object_name = "obj"
    form_class = MarcaForm
    success_url = reverse_lazy("inv:marcas_list")
    login_url = "base:login"
    
    def form_valid(self, form):
        form.instance.usuario_modifica = self.request.user.id
        messages.success(self.request, "Marca editada correctamente")
        return super().form_valid(form)
    

#*----------------------------------------------------------------FUNCION INACTIVAR----------------------------------------------

####Funcion para inhabilitar una marca que son se esta usando (Esto controla que los usuarios no puedan estar elimando cosas de la bbdd ya que no es una buena practica)

def Marca_inactivar(request, id):
    ###Realizamos una consulta de la marca que este en la direccion URL, Esto mediante una select que filtre por marca que sea igual al id de la url y que muestre el primer resultado
    marca = Marca.objects.filter(pk=id).first()
    
    ###El modelo que vamos a utilizar
    contexto = {}
    template_name = "inv/marcas_inactivar.html"
    
    ###Si la marca no existe nos redirecciona a la pagina de las listas de marcas
    
    if not marca:
        return redirect("inv:marcas_list")
        
    #### Mostrar en pantalla la marca a inactivar, dado el resultado del select previamente realizado nos va a dar la descripcion de la marca que en este caso es el nombre y lo va a transformar en el obj lo cual sera pasado a
    #### plantilla y por eso nos muestra el nombre de la marca cuando vamos a inactivar METODO GET = Devuelve un registro y lo muestra en pantalla
    if request.method=='GET':
        contexto={'obj':marca}
    
    ##### El metodo POST Envia el formularo y actualiza base de datos 
    ##### Como el resultado de apretar el boton de inactivar es un post el sistema por lo consiguiente dada las instrucciones modifica el estado a False lo que lo muestra en pantalla inactivo
    ##### Ponemos el Save para guardar la BBDD
    #### Redireccionamos a la listas
    if request.method=="POST":
        marca.estado=False
        marca.save()    
        return redirect("inv:marcas_list")
    
    return render(request, template_name, contexto)


#*----------------------------------------------------------------UNIDADES DE MEDIDA----------------------------------------------
class UnidadMedidaView(LoginRequiredMixin, generic.ListView):
    name = "Unidad de medida"
    model = UnidadMedida
    template_name = "inv/unidad_medida_list.html"
    context_object_name = "unidad_medida"
    login_url = "bases:login"


class UnidadMedidaNew(LoginRequiredMixin, generic.CreateView):
    name = "Unidad de Medida"
    model = UnidadMedida
    template_name = "inv/unidad_medida_form.html"
    context_object_name = "unidad_medida"
    form_class = UnidadMedidaForm
    success_url = reverse_lazy("inv:unidad_medida_list")
    login_url = "base:login"
