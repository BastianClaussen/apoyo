from core.models import Aportes, Ingresos 
from django.shortcuts import redirect, render

# Create your views here.
def index(request):
    return render(request,'core/index.html')

def ficharesidente(request):
    return render(request,'core/ficharesidente.html')

def ingresosalida(request):
    return render(request,'core/ingresosalida.html')

def aportes(request):
    aportes = Aportes.objects.all()
    contexto ={'aportes':aportes}
    return render(request,'core/aportes.html',contexto)

def aporteIng(request):
    a= Aportes.objects.create(rut = request.POST['rut'],nombre= request.POST['nombre'],aporte= request.POST['aporte'])
    fecha = a.fecha.strftime("%Y-%m-%d")
    b,c= Ingresos.objects.get_or_create(fechaIngreso=fecha)
    b.ingresos +=  int(request.POST['aporte'])
    b.save()
    return redirect(aportes)

def insumos(request):
    return render(request,'core/insumos.html')

def registrarse(request):
    return render(request,'core/registrar.html')


def ingresos(request):
    contexto= {'ingresos':Ingresos.objects.all()}
    return render(request,'core/ingresos.html', contexto)


def Prestadores(request):
    contexto={'Prestadores':Aportes.objects.values('nombre','rut').distinct()}
    return render(request,'core/Prestadores.html',contexto)


    