from django.shortcuts import render


def index(request):
    data = {
        "nombre" : "Roberto",
        "apellido" :"Espinoza",
        "profesion" : "GUERREROOOO AU AU AU",
        "edad" : "24",
        "ciudad" : "talca",
        "foto" : "/static/img/perfil.jpg",
        "logo" : "/static/img/favicon.ico"
    }
    return render(request,'index.html',data)    

def proyecto1(request):
    data = {
        "foto":"/static/img/PDC.jpg",
        "nombre":"Pazo de Colón",
        "detalles":"Empresa que se dedica a la prestación de servicio para realización de matrimonios, bautizos y otros tipos de ceremonias",
        "cliente": "Juan Jose Colón",
        "fecha":"25 de abril del 2000",
        "tiempo":"6 meses",
        "ubicacion":"Santiago de la compostela",
        "estado":"En funcionamiento"
    }
    return render (request,'template.html',data)

def proyecto2(request):
    data = {
        "foto":"/static/img/NOS.jpg",
        "nombre":"NOS-TIC",
        "detalles":"",
        "cliente": "",
        "fecha":"",
        "tiempo":"",
        "ubicacion":"",
        "estado":""
    }
    return render (request,'template.html',data)

def proyecto3(request):
    data = {
        "foto":"",
        "nombre":"",
        "detalles":"",
        "cliente": "",
        "fecha":"",
        "tiempo":"",
        "ubicacion":"",
        "estado":""
    }
    return render (request,'template.html',data)    

    