from django.db import models
from aplicacions.oferta.models import Oferta

class Producte(models.Model):
    nom = models.CharField(max_length=50)
    descripcio = models.CharField(max_length=100, null=True)
    preu = models.FloatField()
    tipusChoices = (
        ('Sandvitxos', 'Sandvitxos'),
        ('Entrants', 'Entrants'),
        ('Begudes', 'Begudes'),
        ('Gnomuts', 'Gnomuts'),
    )
    tipus = models.CharField(
        max_length=50,
        choices=tipusChoices,
        default=0
    )
    imatge = models.ImageField(upload_to='Producte', blank=True, null=True)

    def __unicode__(self):
        return str(self.nom)
