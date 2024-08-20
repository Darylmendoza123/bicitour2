from django.shortcuts import render
from .forms import  registroContactanosForm
from django.shortcuts import  render, redirect

def contactanos(request):
    if request.method == 'POST':
        form = registroContactanosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Principal') 
    else:
        form = registroContactanosForm()
    return render(request, 'contacto/contactanos.html', {'form': form})
    
def quien_somos(request):
    return render(request,"contacto/quien_somos.html")