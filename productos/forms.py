from django import forms
from .models import producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = producto
        fields = ['nombre','descripcion','precio','stock','id_categoria','imagen_url','id_detalle_de_producto']
        labels = {
            'nombre': 'Nombre del Producto',
            'descripcion': 'Descripción',
            'precio': 'Precio',
            'stock': 'Cantidad en Stock',
            'id_categoria': 'Categoría',
            'imagen_url': 'URL de la Imagen',
            'id_detalle_de_producto': 'Detalle del Producto',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'id_categoria': forms.Select(attrs={'class': 'form-control'}),
            'imagen_url': forms.URLInput(attrs={'class': 'form-control'}),
            'id_detalle_de_producto': forms.Select(attrs={'class': 'form-control'}),
        }