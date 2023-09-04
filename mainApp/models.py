from django.db import models
from django.contrib.auth.models import User

class EstacionesTransformadoras(models.Model):
    nombre = models.CharField(max_length=50)
    codificacion = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=50)
    nivelTension = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.codificacion}'
    
    class Meta:
        verbose_name = "Estación Transformadora"
        verbose_name_plural = "Estaciones Transformadoras"

class EquipoRed(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    nivel_tension = models.CharField(max_length=50)
    edificio = models.CharField(max_length=50)
    gabinete = models.CharField(max_length=50)
    ip = models.CharField(max_length=50)
    mask = models.CharField(max_length=50)
    defGw = models.CharField(max_length=50)
    estacionTransformadora = models.ForeignKey(EstacionesTransformadoras, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.estacionTransformadora.codificacion} - {self.nombre}'
    
    class Meta:
        verbose_name = "Equipo de Red"
        verbose_name_plural = "Equipos de Red"

class EquipoTelecontrol(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    nivel_tension = models.CharField(max_length=50)
    edificio = models.CharField(max_length=50)
    gabinete = models.CharField(max_length=50)
    ip = models.CharField(max_length=50)
    mask = models.CharField(max_length=50)
    defGw = models.CharField(max_length=50)
    estacionTransformadora = models.ForeignKey(EstacionesTransformadoras, null=False, blank=False, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.estacionTransformadora.codificacion} - {self.nombre}'
    
    class Meta:
        verbose_name = "Equipo de Telecontrol"
        verbose_name_plural = "Equipos de Telecontrol"

class EquipoProteccion(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    nivel_tension = models.CharField(max_length=50)
    edificio = models.CharField(max_length=50)
    gabinete = models.CharField(max_length=50)
    ip = models.CharField(max_length=50)
    mask = models.CharField(max_length=50)
    defGw = models.CharField(max_length=50)
    estacionTransformadora = models.ForeignKey(EstacionesTransformadoras, null=False, blank=False, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.estacionTransformadora.codificacion} - {self.nombre}'
    
    class Meta:
        verbose_name = "Equipo de Protección"
        verbose_name_plural = "Equipos de Proteccion"

class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} {self.imagen}'