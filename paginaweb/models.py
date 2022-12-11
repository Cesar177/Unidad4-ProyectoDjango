from django.db import models

# Create your models here.

class Proyecto(models.Model):
    foto = models.URLField(max_length=200)
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=800)
    tags = models.CharField(max_length=50, null=True)
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.titulo + self.tags

    class Meta:
        db_table = "proyectos"

    