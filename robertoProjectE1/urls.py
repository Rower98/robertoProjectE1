"""robertoProjectE1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.dom.minidom import Document
from django.conf import settings
from django.contrib import admin
from django.urls import path
from firstAPPE1.views import index, proyecto1, proyecto2, proyecto3



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('p1/', proyecto1),
    path('p2/', proyecto2),
    path('p3/', proyecto3),
]


