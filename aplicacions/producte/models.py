from django.db import models
from aplicacions.oferta.models import Oferta

class Producte(models.Model):
    nom = models.CharField(max_length=50)
    descripcio = models.CharField(max_length=100, null=True)
    oferta = models.ForeignKey(Oferta, null=True, blank=True, default=0)
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

    def __unicode__(self):
        return str(self.nom)
