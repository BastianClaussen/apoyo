from django.contrib import admin
from django.urls import path, include
from .views import aportes, insumos, feña2, feña3, index,registrarse,aporteIng

urlpatterns = [
    path('',index,name='index'),
    path('feña3',feña3,name='feña3'),
    path('feña2',feña2,name='feña2'),
    path('aportes',aportes,name='aportes'),
    path('insumos',insumos,name='insumos'),
    path('registrarse',registrarse,name='registrarse'), 
    path('aporteIng',aporteIng,name='aporteIng'), 
]
