from django.db import models

# Create your models here.


class Autor(models.Model):
    name = models.CharField(max_length=100)
    secondname = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField()
    bday = models.DateTimeField()

    def __str__(self):
        return f"{self.name} {self.secondname}"
