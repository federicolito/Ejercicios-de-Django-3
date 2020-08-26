from django.contrib import admin
from .models import *
# Register your models here.

class PrestamoInLine(admin.TabularInline):
    model = Prestamo

class AlumnoAdmin(admin.ModelAdmin):
    inlines = [PrestamoInLine, ]
    list_display = ('matricula', 'apellido',)
    search_fields = ['nombre', 'apellido', 'correo', 'telefono','matricula']
    fieldsets = (
        ("Persona", {
            'fields': ('nombre', 'apellido',)
        }),
        ('Contacto', {
            'fields': ('correo', 'telefono',)
        }),
        ('Alumno', {
            'fields': ('matricula',)
        }),
        ('Bibloteca', {
            'fields': ('num_libros','adeudo',)
        }),
    )

class ProfesorAdmin(admin.ModelAdmin):
    inlines = [PrestamoInLine, ]
    search_fields = ['nombre', 'apellido', 'correo', 'telefono', 'num_empleado']
    fieldsets = (
        ("Persona", {
            'fields': ('nombre', 'apellido',)
        }),
        ('Contacto', {
            'fields': ('correo', 'telefono',)
        }),
        ('Empleado', {
            'fields': ('num_empleado',)
        }),
        ('Bibloteca', {
            'fields': ('num_libros','adeudo',)
        }),
    )

class LibroAdmin(admin.ModelAdmin):
    inlines = [PrestamoInLine, ]
    list_display = ('titulo', 'autor',)
    search_fields = ['titulo',]
    list_filter = ('autor','anio',)
    fieldsets = (
        ("Material", {
            'fields': ('codigo', 'autor','titulo','anio','foto_portada')
        }),
        ('Estado', {
            'fields': ('status',)
        }),
        ('Editorial', {
            'fields': ('editorial',)
        }),
    )

class RevistaAdmin(admin.ModelAdmin):
    inlines = [PrestamoInLine, ]
    list_display = ('titulo', 'autor',)
    search_fields = ['titulo', ]
    list_filter = ('autor', 'anio',)
    fieldsets = (
        ("Material", {
            'fields': ('codigo', 'autor', 'titulo', 'anio')
        }),
        ('Estado', {
            'fields': ('status',)
        }),
    )

class PrestamoAdmin(admin.ModelAdmin):
    list_display = ('fecha_salida','fecha_regreso','persona', 'material',)
    list_filter = ('persona','material','fecha_salida','fecha_regreso',)


admin.site.register(Editorial)
admin.site.register(Libro,LibroAdmin)
admin.site.register(Revista,RevistaAdmin)
admin.site.register(Alumno,AlumnoAdmin)
admin.site.register(Profesor,ProfesorAdmin)
admin.site.register(Prestamo,PrestamoAdmin)