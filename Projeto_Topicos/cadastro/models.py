from django.db import models



class Cadastro(models.Model):
    nome = models.CharField(max_length=122)
    email = models.CharField(max_length=120)
    skype = models.CharField(max_length=120)
    idade = models.IntegerField()
    horario = models.CharField(max_length=120)
    nickPs = models.CharField(max_length=120)    
    def _str_(self):
        return self.name