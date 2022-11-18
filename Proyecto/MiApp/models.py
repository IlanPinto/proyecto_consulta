from django.db import models

# Create your models here.
class Jugadores(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    nacionalidad = models.CharField(max_length=40)

    def __str__(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}"

class Torneos(models.Model):
    nombre = models.CharField(max_length=40)
    pais = models.CharField(max_length=40)
    puntos_otorgados = models.IntegerField()
    def __str__(self):
        return f"Nombre: {self.nombre}, Pais: {self.pais}"

class Entrenadores(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    entrenado = models.CharField(max_length=40)
    email = models.EmailField()
    def __str__(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}"


