from django.db import models

class Producte(models.Model):
    id = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=50)
    preu = models.FloatField()
