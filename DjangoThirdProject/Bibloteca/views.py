from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    
    context={}
    return render(request, 'Bibloteca/home.html',context)
def librosView(request):
    libros = Libro.objects.all()
    context= {'libros':libros}
    
    return render(request, 'Bibloteca/libros.html', context)
def alumnosView(request):
    alumnos = Alumno.objects.all()
    context= {'alumnos':alumnos}
    return render(request, 'Bibloteca/alumnos.html', context)