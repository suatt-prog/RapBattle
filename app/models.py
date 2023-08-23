from django.db import models

# Create your models here.

class Battle(models.Model):
    content = models.CharField(max_length=1000,verbose_name="content")
    firstPerson = models.CharField(max_length=50,verbose_name="First Person")
    secondPerson = models.CharField(max_length=50,verbose_name="Second Person")
    def __str__(self) -> str:
        return self.content