from django.shortcuts import render

def tela1(request):
    return render(request, "maeLuiza/tela1.html")

def tela2(request):
    return render(request, "maeLuiza/tela2.html")

def tela3(request):
    return render(request, "maeLuiza/tela3.html")