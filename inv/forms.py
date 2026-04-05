from django import forms
from .models import Categoria, SubCategoria, Marca, UnidadMedida


#*--------------------------------------------------------------CATEGORIAS-------------------------------------------------------------------

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria  # Aquí decimos con qué modelo trabajamos
        fields = ['descripcion', 'estado']  # Campos que usará el formulario



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Correcto llamado a super con args y kwargs
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

#*--------------------------------------------------------------SUBCATEGORIAS----------------------------------------------------------------

class SubCategoriaForm(forms.ModelForm):
    ###Modificar el query para que solo muestren las categorias que estan activas en las subcategoria
    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.filter(estado=True).order_by('descripcion')
    )
    
    class Meta:
        model = SubCategoria  # Aquí decimos con qué modelo trabajamos
        fields = ['categoria', 'descripcion', 'estado']  # Campos que usará el formulario
        



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Correcto llamado a super con args y kwargs
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['categoria'].empty_label = "Seleccione Categoria"


#*--------------------------------------------------------------MARCAS--------------------------------------------------------------------------
class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca  # Aquí decimos con qué modelo trabajamos
        fields = ['descripcion', 'estado']  # Campos que usará el formulario



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Correcto llamado a super con args y kwargs
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


#*--------------------------------------------------------------Unidad medidas--------------------------------------------------------------------------
class UnidadMedidaForm(forms.ModelForm):
    class Meta:
        model = UnidadMedida
        fields = ['descripcion', 'estado']
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Correcto llamado a super con args y kwargs
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })