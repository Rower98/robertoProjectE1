from django.shortcuts import render


def index(request):
    return render(request,'index.html')

def userAdmin(request):
    data = {
        'isAdmin': True 
    }
    return render(request, 'index.html',data)

def userView(request):
    data = {
        'isAdmin': False 
    }
    return render(request, 'index.html',data)       
