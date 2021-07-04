from django.contrib import admin
from django.urls import path, include
from .views import aportes, insumos, ficharesidente, ingresosalida, index,registrarse,aporteIng,ingresos, Prestadores

urlpatterns = [
    path('',index,name='index'),
    path('ficharesidente',ficharesidente,name='ficharesidente'),
    path('ingresosalida',ingresosalida,name='ingresosalida'),
    path('aportes',aportes,name='aportes'),
    path('insumos',insumos,name='insumos'),
    path('registrarse',registrarse,name='registrarse'), 
    path('aporteIng',aporteIng,name='aporteIng'), 
    path('ingresos',ingresos, name='ingresos'),
    path('Prestadores',Prestadores, name='Prestadores')

]
