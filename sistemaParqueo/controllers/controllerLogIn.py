from django.http import HttpResponse
from django.shortcuts import render
from db.models import Usuario, TipoUsuario

def mostrarLogin(request):
    tipo_usuario = TipoUsuario.objects.all()
    ctx = {"tipo_Usuarios":tipo_usuario}
    return render(request,"viewLogIn.html",ctx)

def controlLogIn(request):

    if(request.GET['username'] and request.GET['password']):
        usuario = request.GET['username']
        password = request.GET['password']
        tipo = request.GET['tipo_usuario']
        mensaje = "%s %s" % (request.GET['username'],  tipo)
    else:
        mensaje = "DEBES LLENAR SUS DATOS"
    ctx = {"mensaje":mensaje}
    return render(request,"viewMenuPrincipal.html",ctx)