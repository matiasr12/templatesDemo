from django.shortcuts import render
from templatesApp.forms import FormTrabajadores
from templatesApp.models import Trabajadores
from django.shortcuts import redirect


# Create your views here.
def index(request):
    return render(request,'index.html')

def Listado(request):
    trabJadores=Trabajadores.objects.all()
    data ={'trabJadores':trabJadores}
    return render(request,'proyectos.html',data)

def agregarProyecto(request):
    form = FormTrabajadores()
    if request.method =='POST':
        form =FormTrabajadores(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data={'form':form}
    return render(request,'agregarProyecto.html',data)

def elinarProyecto(request,nombre):
    trabajadores=Trabajadores.objects.get(nombre=nombre)
    trabajadores.delete()
    return redirect('/proyectos')

def actualizarProyecto(request,nombre):
     trabajadores=Trabajadores.objects.get(nombre=nombre)
     form=FormTrabajadores(instance=trabajadores)
     if request.method =='POST':
         form = FormTrabajadores(request.POST,instance=trabajadores)
         if form.is_valid():
             form.save()
         return index(request)
     data={'form':form}
     return render(request,'agregarProyecto.html',data)
     
      
        
