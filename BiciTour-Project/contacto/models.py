from django.db import models

class registroContactanos(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="clave")
    nombre = models.TextField()
    apellido = models.TextField()
    correo = models.TextField()
    comentario = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)



    class Meta:
        verbose_name = "registroContactanos"
        verbose_name_plural = "registroContactanos"
        ordering = ["-created"]

    def _str_(self):
        return self.nombre