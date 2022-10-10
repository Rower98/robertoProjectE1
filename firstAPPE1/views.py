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
        "detalles":"Propuesta para nueva farmacia moderna",
        "cliente": "Dario Buena Salud",
        "fecha":"30 de octubre de 2019",
        "tiempo":"7 meses y 18 días",
        "ubicacion":"Cerca de donde murio Colón",
        "estado":"Activo"
    }
    return render (request,'template.html',data)

def proyecto3(request):
    data = {
        "foto":"/static/img/LIMON.jpg",
        "nombre":"Limon Brunch",
        "detalles":"Nuevo restaurante, en el cual puedes hacer reservas por la pagina web que ellos mantienen",
        "cliente": "Patricia Cid",
        "fecha":"18 de septiembre 2021",
        "tiempo":"4 meses",
        "ubicacion":"Galicia, España",
        "estado":"Activo"
    }
    return render (request,'template.html',data)    

    