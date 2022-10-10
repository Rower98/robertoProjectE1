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
