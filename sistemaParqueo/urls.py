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

from sistemaParqueo.controllers import controllerLogIn, controllerReporteCaja, \
    controllerMenuAdmin, controllerMenuEmpleado, controllerControlAlquileres


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',controllerLogIn.mostrarLogin),
    path('menuPrincipal/',controllerLogIn.controlLogIn),

    path('menuPrincipal/controlPersonal/', controllerMenuAdmin.mostrarControlPersonal, name="ADMcontrolPersonal"),
    path('menuPrincipal/reporteUbicacion/', controllerMenuAdmin.mostrarReporteUbicacion, name="ADMreporteUbicacion"),
    path('menuPrincipal/nuevoUsuario/', controllerMenuAdmin.mostrarNuevoUsuario,name="ADMnuevoUsuario"),
    path('menuPrincipal/gestionTarifas/', controllerMenuAdmin.mostrarGestionTarifas, name="ADMgestionTarifas"),
    path('menuPrincipal/reporteCaja/', controllerMenuAdmin.mostrarReporteCaja, name="ADMreporteCaja"),

    path('menuPrincipal/ingresoVehiculos/', controllerMenuEmpleado.mostrarIngresoVehiculos, name="EMPIngresoVehiculos"),
    path('menuPrincipal/ingresoVehiculos/', controllerMenuEmpleado.mostrarIngresoVehiculos, name="EMPIngresoVehiculos"),

    path('menuPrincipal/aperturaCaja/', controllerMenuEmpleado.mostrarAperturaCaja, name="EMPAperturaCaja"),
    path('menuPrincipal/salidaVehiculos/', controllerMenuEmpleado.mostrarSalidaVehiculos, name="EMPSalidaVehiculos"),
    path('menuPrincipal/clausuraCaja/', controllerMenuEmpleado.mostrarClausuraCaja, name="EMPClausuraCaja"),
    path('menuPrincipal/consultaEspacios/', controllerMenuEmpleado.mostrarConsultaEspacios, name="EMPconsultaEspacios"),
    path('menuPrincipal/reporteAlquileres/', controllerMenuEmpleado.mostrarReporteAlquileres, name="ADMreporteAlquileres"),
    path('menuPrincipal/reporteAlquileres/nuevoAlquiler',controllerControlAlquileres.mostrarRegistroAlquiler, name='EMPnuevoAlquiler'),
]
