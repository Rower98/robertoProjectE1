from django.shortcuts import render
from django.http import HttpResponse

def display(request):
    return HttpResponse("<h1>Hola mundo- Roberto Espinoza</h1>")