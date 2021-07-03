from core.models import Aportes
from django.shortcuts import redirect, render

# Create your views here.
def index(request):
    return render(request,'core/index.html')

def feña2(request):
    return render(request,'core/feña2.html')

def feña3(request):
    return render(request,'core/feña3.html')

def aportes(request):
    aportes = Aportes.objects.all()
    contexto ={'aportes':aportes}
    return render(request,'core/aportes.html',contexto)

def aporteIng(request):
    Aportes.objects.create(rut = request.POST['rut'],nombre= request.POST['nombre'],aporte= request.POST['aporte'])
    return redirect(aportes)

def insumos(request):
    return render(request,'core/insumos.html')

def registrarse(request):
    return render(request,'core/registrar.html')



    