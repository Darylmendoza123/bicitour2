from django.db import models

class registroUsuario(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="clave")
    correo = models.TextField()
    nombre = models.TextField()
    contraseña = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "registroUsuario"
        verbose_name_plural = "registroUsuarios"
        ordering = ["-created"]

    def _str_(self):
        return self.nombre 
