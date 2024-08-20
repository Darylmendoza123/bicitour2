from django.shortcuts import render
from .forms import registroUsuarioForm
from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required

def login(request):
    return render(request,"inicio_sesion/login.html")
def registrar(request):
    if request.method == 'POST':
        form = registroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Principal')
    else:
        form = registroUsuarioForm()
    return render(request, 'inicio_sesion/registrar.html', {'form': form})
def nueva_contraseña(request):
    return render(request,"inicio_sesion/nueva_contraseña.html")
