from django.contrib import admin
from django.urls import path, include
from .views import aportes, insumos, registrarficha, ingresosalida, index,registrarse,aporteIng,ingresos, Prestadores,ficha

urlpatterns = [
    path('',index,name='index'),
    path('registrarficha',registrarficha, name='registrarficha'),
    path('ingresosalida',ingresosalida,name='ingresosalida'),
    path('aportes',aportes,name='aportes'),
    path('insumos',insumos,name='insumos'),
    path('registrarse',registrarse,name='registrarse'), 
    path('aporteIng',aporteIng,name='aporteIng'), 
    path('ingresos',ingresos, name='ingresos'),
    path('Prestadores',Prestadores, name='Prestadores'),
    path('ficha',ficha, name='ficha'),
]
