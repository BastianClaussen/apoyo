from core.models import Aportes, Ficha, Ingresos 
from django.shortcuts import redirect, render

# Create your views here.
def index(request):
    return render(request,'core/index.html')

def ficha(request):
    return render(request,'core/ficharesidente.html')

def registrarficha(request):
    nombre=request.POST['txtNombre_ap']
    medicamento=request.POST['txtMedicamentos']
    situa=request.POST['txtSituación_salud']
    cuidadoEs=request.POST['txtCuidado_espe']
    nombreApeFAM=request.POST['txtNombre_ap_fam']
    date=request.POST['dateNacimiento']
    domicilioFam=request.POST['txtDomicilio_fam']
    sexoFam=request.POST['sexo']
    ocupacionFam=request.POST['txtOcupaFAM']

    Ficha.objects.create(Medicamentos = medicamento, Cuidados_especiales = cuidadoEs,
                               Situación_salud = situa, NombreApe = nombre, NombreCom_fam = nombreApeFAM,
                               fechaNa_fam = date, Domicilio_fam = domicilioFam, Ocupacion_fam = ocupacionFam,
                               sexoFam = sexoFam)

    return redirect (ficha)

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


    