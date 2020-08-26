from django.db import models

# Create your models here.
OPCIONES_ESTADO = [
        ('li', 'Libre'),
        ('pt', 'Prestado'),
    ]
class Material(models.Model):
    codigo = models.CharField(max_length = 30)
    autor = models.CharField(max_length = 30)
    titulo = models.CharField(max_length = 30)
    anio = models.IntegerField()
    
    status = models.CharField(max_length=2,choices=OPCIONES_ESTADO,default='li',)
    def __str__(self):
        return self.titulo

class Editorial(models.Model):
    nombre = models.CharField(max_length = 30)

    def __str__(self):
        return self.nombre

class Libro(Material):
    
    foto_portada = models.ImageField(max_length=100, upload_to='imagenes/', blank=True)
    editorial = models.ForeignKey(Editorial,on_delete=models.CASCADE,null=False)

class Revista(Material):
    pass

class Persona(models.Model):
    nombre = models.CharField(max_length = 30)
    apellido = models.CharField(max_length = 30)
    correo = models.EmailField((""), max_length=254)
    telefono = models.CharField(max_length = 30)
    num_libros = models.IntegerField()
    adeudo = models.FloatField()

    def __str__(self):
        return "{} {}".format(self.nombre,self.apellido)

class Alumno(Persona):
    
    matricula = models.IntegerField()

class Profesor(Persona):
    num_empleado = models.IntegerField()

class Prestamo(models.Model):
    codigo = models.CharField(max_length = 30)
    fecha_salida = models.DateField(auto_now=False)
    fecha_regreso = models.DateField(auto_now=False)
    persona = models.ForeignKey(Persona,on_delete=models.CASCADE,null=False)
    material = models.ForeignKey(Material,on_delete=models.CASCADE,null=False)
    def __str__(self):
        return self.codigo


