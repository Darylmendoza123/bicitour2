"""
URL configuration for BiciTour project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inicio import views 
from contacto import views as views_contacto
from inicio_sesion import views as views_inicio_sesion
from inscripcion import views as views_inscripcion
from rutas import views as views_rutas
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.principal, name='Principal'),
    path('login/', views_inicio_sesion.login,name="Login"),
    path('registrar/', views_inicio_sesion.registrar,name="Registrar"),
    path('nueva_contraseña/', views_inicio_sesion.nueva_contraseña,name="Nueva Contraseña"),
    path('ruta/<int:ruta_id>/Pre_inscripcion/', views_inscripcion.pre_inscripcion, name='Pre_inscripcion'),
    path('ruta/<int:ruta_id>/lista/', views_inscripcion.lista, name='Lista'),
    path('confirmacion/<int:ruta_id>/', views_inscripcion.confirmacion_inscripcion, name='confirmacion_inscripcion'),
    path('proximos/', views_rutas.proximos,name="Proximos"),
    path('realizados/', views_rutas.realizados,name="Realizados"),
    path('personalizada/', views_rutas.personalizada,name="Personalizados"),
    path('contactanos/', views_contacto.contactanos,name="Contactanos"),
    path('quien_somos/', views_contacto.quien_somos,name="Quienes somos"),
    path('busqueda/', views_rutas.busqueda,name="Busqueda"),
    path('ruta/<int:ruta_id>/', views_rutas.detalles, name='Detalles'),
    path('marca_ruta_realizada/<int:ruta_id>/', views_rutas.marca_ruta_realizada, name='marcar_ruta_realizada'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
