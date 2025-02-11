from django.contrib import admin
from .models import Empleados,clientes,productos
# Register your models here.

@admin.register (Empleados)
class EmpleadosAdmin(admin.ModelAdmin):
    list_display = ('cedula', 'nombre', 'apellido', 'direccion', 'email', 'telefono', 'cargo')
    search_fields = ('cedula', 'nombre', 'apellido')
    list_filter = ('nombre', 'email')


@admin.register (clientes)
class clientesAdmin(admin.ModelAdmin):
     list_display = ('cedula', 'nombre', 'apellido', 'direccion', 'email', 'telefono')
     search_fields = ('cedula', 'nombre', 'apellido')
     list_filter = ('nombre', 'email')    
    
    
@admin.register (productos)
class productosAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'precio', 'marca', 'color')
    search_fields = ('cedula', 'nombre', 'precio')
    list_filter = ('nombre', 'precio')