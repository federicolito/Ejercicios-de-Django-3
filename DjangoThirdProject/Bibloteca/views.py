from django.shortcuts import render

# Create your views here.
def home(request):
    
    context={}
    return render(request, 'Bibloteca/home.html',context)
def librosView(request):
    context= {}
    return render(request, 'Bibloteca/libros.html', context)
def alumnosView(request):
    context= {}
    return render(request, 'Bibloteca/alumnos.html', context)