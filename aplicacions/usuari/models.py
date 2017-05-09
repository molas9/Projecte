from django.db import models
from django.utils import timezone

class Usuari(models.Model):
    nom = models.CharField(max_length=50)
    adreca = models.CharField(max_length=200)
    poblacio = models.CharField(max_length=50)
    telefon = models.CharField(max_length=9)

    def __unicode__(self):
        return str(self.nom)
