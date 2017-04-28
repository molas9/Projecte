from django.db import models
from django.utils import timezone

class Usuari(models.Model):
    id = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=50)
    adreca = models.CharField(max_length=200)
    poblacio = models.CharField(max_length=50)
    telefon = models.CharField(max_length=9)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title