from django.db import models

# Create your models here.
class Clientlogo(models.Model):
    img = models.ImageField(upload_to ='service/')

    
class Vehicle(models.Model):
    img = models.ImageField(upload_to = 'vehicle/')
    title = models.TextField(max_length=20)
    des = models.TextField(max_length=100)

    def __str__(self):
        return self.title
    