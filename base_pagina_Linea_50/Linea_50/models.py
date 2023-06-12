from django.db import models

# Ejemplo de modelo
"""
class YourModel(models.Model):
    # Definir los campos del modelo
    field1 = models.CharField(max_length=50)
    field2 = models.IntegerField()
    field3 = models.DateTimeField()
    
    # Definicion de las relaciones con otros modelos
    related_model = models.ForeignKey(RelatedModel, on_delete=models.CASCADE)
    
    # Posibles metodos (acciones para realizar con el modelo) extras o meta (ordenar, agrupar, constraints, etc) opciones
    # Ninguna de estas opciones es obligatoria
    def custom_method(self):
        # Metodos personalizados
        pass
    
    class Meta:
        # Opciones extras para el modelo
        ordering = ['-field1']
"""

# TODO: Crear los modelos de la base de datos