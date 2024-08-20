
from django.shortcuts import render
from rutas.models import Ruta  

def principal(request):
    rutas_proximas = Ruta.objects.filter(fecha__year=2024)  
    return render(request, 'inicio/principal.html', {'rutas_proximas': rutas_proximas})




    