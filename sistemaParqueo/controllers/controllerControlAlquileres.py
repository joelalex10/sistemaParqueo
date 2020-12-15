from django.shortcuts import render


def mostrarRegistroAlquiler(request):
    ctx={}
    return render(request, "viewNuevoAlquiler.html", ctx)