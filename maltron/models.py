from django.db import models


class Producto(models.Model):
    marca = models.CharField(max_length=64)
    informacion = models.CharField(max_length=10000)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to='productos/', default='default.jpg')


    def __str__(self):
        return f'{self.marca} -> {self.precio}'
    


class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre