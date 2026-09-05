from django.db import models


class Post(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    resumen = models.CharField(max_length=300, blank=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    publicado = models.BooleanField(default=True)

    class Meta:
        ordering = ['-fecha_publicacion']

    def __str__(self):
        return self.titulo
