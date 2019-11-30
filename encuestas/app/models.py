from django.db import models

# Create your models here.
class Pregunta(models.Model):
    texto = models.TextField()
    img = models.ImageField()

    def __str__(self):
        return self.texto

class Respuesta(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    texto = models.TextField()
    votos= models.IntegerField()
    def __str__(self):
        return self.texto