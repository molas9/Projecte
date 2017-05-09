from django.shortcuts import render
from ..producte.models import Producte
from ..oferta.models import Oferta

def index(request):
    sandvitxos = Producte.objects.filter(tipus="Sandvitxos")
    entrants = Producte.objects.filter(tipus="Entrants")
    begudes = Producte.objects.filter(tipus="Begudes")
    gnomuts = Producte.objects.filter(tipus="Gnomuts")
    ofertes = Oferta.objects.all()
    ctx = {
        'sandvitxos': sandvitxos,
        'entrants': entrants,
        'begudes': begudes,
        'gnomuts': gnomuts,
        'ofertes': ofertes,
    }
    return render(request, 'portal/index.html', ctx)
