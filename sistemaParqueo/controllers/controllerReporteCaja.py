from django.shortcuts import render

def activarReporteCaja(request):
    ctx = {}
    return render(request,"viewReporteCaja.html",ctx)
