from __future__ import unicode_literals
from django.db import models

class Oferta(models.Model):
    nom = models.CharField(max_length=50)
    descripcio = models.CharField(max_length=150)
    descompte = models.IntegerField()
    icona = models.CharField(max_length=150)

    def __unicode__(self):
        return str(self.nom)