"""
sistemaParqueo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

Para arrancar el proyecto
http://127.0.0.1:8000/
"""
from django.contrib import admin
from django.urls import path

from sistemaParqueo.controllers import controllerLogIn, controllerReporteCaja
from sistemaParqueo.controllers import controllerMenuAdmin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',controllerLogIn.mostrarLogin),
    path('menuAdministrador/',controllerLogIn.controlLogIn),
    path('registroCaja/',controllerReporteCaja.activarReporteCaja),
    path('menuAdministrador/controlPersonal/', controllerMenuAdmin.mostrarControlPersonal, name="ADMcontrolPersonal"),
    path('menuAdministrador/reporteUbicacion/', controllerMenuAdmin.mostrarReporteUbicacion, name="ADMreporteUbicacion"),
    path('menuAdministrador/nuevoUsuario/', controllerMenuAdmin.mostrarNuevoUsuario,name="ADMnuevoUsuario"),
    path('menuAdministrador/gestionTarifas/', controllerMenuAdmin.mostrarGestionTarifas, name="ADMgestionTarifas"),
    path('menuAdministrador/reporteCaja/', controllerMenuAdmin.mostrarReporteCaja, name="ADMreporteCaja"),
    path('menuAdministrador/reporteAlquileres/', controllerMenuAdmin.mostrarReporteAlquileres, name="ADMreporteAlquileres"),

]
