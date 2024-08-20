from django.db import models
from django.contrib.auth.models import User 


class Ruta(models.Model):
    id = models.AutoField(primary_key=True) 
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    distancia = models.FloatField()
    Status=models.BooleanField()
    precio=models.FloatField()
    estado=models.CharField(max_length=15)
    ciudad=models.CharField(max_length=15)
    duracion=models.FloatField()
    fecha = models.DateField(null=True, blank=True)
    imagen = models.ImageField(upload_to='rutas/', blank=True, null=True)
    

    class Meta:
        verbose_name = "Ruta"
        verbose_name_plural = "Rutas"
        
    
    def _str_(self):
        return self.nombre

class RutaRealizada(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) 
    ruta = models.ForeignKey(Ruta, on_delete=models.CASCADE, related_name='rutarealizada') 

    class Meta:
        verbose_name = "RutaRealizada"
        verbose_name_plural = "RutasRealizadas"
        

    def _str_(self):
        return f"{self.usuario.username} - {self.ruta.nombre}"
