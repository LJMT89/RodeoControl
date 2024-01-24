from django.db import models

# Create your models here.
class AuditoriaFecha(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Finca(AuditoriaFecha):
    nombre = models.CharField("Nombre de la Finca", max_length=60, default='', null=True, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'Finca'
        verbose_name_plural = 'Fincas'

    def __str__(self):
        return "{0}".format(str(self.nombre))
    
class Rodeo(AuditoriaFecha):
    finca = models.ForeignKey(Finca, on_delete=models.CASCADE)
    nombre = models.CharField("Nombre del Rodeo", max_length=60, default='', null=True, blank=True)
    fecha  = models.DateField("Fecha de creación", null=True, blank=True)
    descripcion = models.TextField("Descripción", null=True, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'Rodeo'
        verbose_name_plural = 'Rodeos'

    def __str__(self):
        return "{0}".format(str(self.nombre))
    
class Animal(AuditoriaFecha):
    rodeo = models.ForeignKey(Rodeo, on_delete=models.CASCADE)
    numero = models.IntegerField("Número del animal", blank=True, null=True)
    fecha  = models.DateField("Fecha de nacimiento", null=True, blank=True)
    observacion = models.TextField("Observaciones", null=True, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'Animal'
        verbose_name_plural = 'Animales'

    def __str__(self):
        return "{0} - {1}".format(str(self.rodeo.nombre), str(self.numero))
