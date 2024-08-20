
from django.shortcuts import get_object_or_404, render, redirect
from .models import registroInscripcion
from .forms import RegistroInscripcionForm
from rutas.models import Ruta

def pre_inscripcion(request, ruta_id):
    ruta = get_object_or_404(Ruta, id=ruta_id)

    if request.method == 'POST':
        form = RegistroInscripcionForm(request.POST)
        if form.is_valid():
            inscripcion = form.save(commit=False)
            inscripcion.ruta = ruta
            inscripcion.save()
            return redirect('confirmacion_inscripcion', ruta_id=ruta.id)
    else:
        form = RegistroInscripcionForm()

    return render(request, "inscripcion/pre_inscripcion.html", {'form': form, 'ruta': ruta})

def confirmacion_inscripcion(request, ruta_id):
    ruta = get_object_or_404(Ruta, id=ruta_id)
    return render(request, 'inscripcion/confirmacion.html', {'ruta': ruta})

def lista(request, ruta_id):
    participantes = registroInscripcion.objects.filter(ruta_id=ruta_id)
    return render(request, "inscripcion/lista.html", {'participantes': participantes})