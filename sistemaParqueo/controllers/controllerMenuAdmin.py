from django.shortcuts import render


def mostrarControlPersonal(request):
    ctx = {}
    return render(request,"viewControlPersonal.html",ctx)

def mostrarReporteUbicacion(request):
    ctx={}
    return render(request,"viewReporteUbicacion.html",ctx)

def mostrarNuevoUsuario(request):
    ctx={}
    return render(request,"viewNuevoUsuario.html",ctx)

def mostrarGestionTarifas(request):
    ctx={}
    return render(request,"viewGestionDeTarifas.html",ctx)

def mostrarReporteCaja(request):
    ctx={}
    return render(request,"viewReporteCaja.html",ctx)

def mostrarReporteAlquileres(request):
    ctx = {}
    return render(request, "viewReporteAlquileres.html", ctx)
