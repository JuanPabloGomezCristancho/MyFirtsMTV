from django.db import models

# Create your models here.
class Relative(models.Model): # Clase Familiar
    name = models.CharField(max_length=40)
    age = models.IntegerField()
    birthdate = models.DateField()

    def __str__(self):
        return f'| {self.name} | Age: {self.age} | birthdate: {self.birthdate}'