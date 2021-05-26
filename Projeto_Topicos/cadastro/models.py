from django.db import models

# Create your models here. 
# Note that I have used an uppercase letter for class name

class Cadastro(models.Model):
    nome = models.CharField(max_length=122)
    email = models.CharField(max_length=120)
    skype = models.CharField(max_length=120)
    idade = models.IntegerField()
    horario = models.CharField(max_length=120)
    nickPs = models.CharField(max_length=120)    
    def _str_(self):
        return self.name