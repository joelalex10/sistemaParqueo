from django.shortcuts import render
from db.models import TipoVehiculo

def mostrarIngresoVehiculos(request):
    list_tipo_vehiculo = TipoVehiculo.objects.all();
    ctx = {"tipo_vehiculos":list_tipo_vehiculo}
    return render(request, "viewIngresoVehiculo.html", ctx)

def mostrarAperturaCaja(request):
    ctx={}
    return render(request, "viewAperturaCaja.html", ctx)

def mostrarClausuraCaja(request):
    ctx={}
    return render(request, "viewClausuraCaja.html",ctx)

def mostrarSalidaVehiculos(request):
    ctx = {}
    return render(request, "viewSalidaVehiculos.html",ctx)

def mostrarConsultaEspacios(request):
    ctx = {}
    return render(request, "viewConsultaEspacios.html",ctx)

def mostrarReporteAlquileres(request):
    ctx = {}
    return render(request, "viewEMPReporteAlquileres.html", ctx)
