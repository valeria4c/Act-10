from django.db import models

# Create your models here.
class producto(models.Model):
    DETALLES = [
        ('AROMATERAPIA', 'Aromaterapia'),
        ('CUIDADO FACIAL', 'Cuidado facial'),
        ('CUIDADO CORPORAL', 'Cuidado corporal'),
        ('MASAJES', 'Masajes y aceites'),
        ('BAÑO RELAJANTE', 'Baño relajante'),
        ('BELLEZA', 'Belleza y estética'),
        ('SALUD Y BIENESTAR', 'Salud y bienestar'),
        ('ACCESORIOS SPA', 'Accesorios de spa'),
        ('OTROS', 'Otros'),
    ]

    ID_CATEGORIAS = [
        (1001, '1001 - Aromaterapia y Esencias Naturales'),
        (1002, '1002 - Aceites y Lociones para Masaje'),
        (1003, '1003 - Cuidado Facial (Mascarillas, Sérums, Cremas)'),
        (1004, '1004 - Cuidado Corporal (Exfoliantes, Cremas, Sales de Baño)'),
        (1005, '1005 - Belleza y Estética (Maquillaje, Uñas, Cabello)'),
        (1006, '1006 - Productos para Baño y Relajación'),
        (1007, '1007 - Accesorios Spa (Toallas, Velas, Difusores)'),
        (1008, '1008 - Salud y Bienestar (Herbolaria, Suplementos Naturales)'),
        (1099, '1099 - Otros Productos de Spa'),
        (0000, '0000 - N/A'),
    ]
    
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    id_categoria = models.CharField(max_length=100, choices=ID_CATEGORIAS, default='OTROS')
    imagen_url = models.URLField(max_length=200, blank=True)
    id_detalle_de_producto = models.IntegerField(choices=DETALLES, default=0000)
    def __str__(self):
        return f'producto: {self.nombre} - {self.id_categoria} - ${self.precio}'