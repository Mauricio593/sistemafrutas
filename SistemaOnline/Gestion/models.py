from django.db import models
from .choices import CARGO,GENERO
from django.core.validators import MinLengthValidator,MinValueValidator,MaxLengthValidator,MaxValueValidator
from .validadores import validacion_numeros,validar_solo_letras

# Create your models here.
class Empleados(models.Model):
    cedula = models.CharField(max_length=10, primary_key=True, validators=[MinLengthValidator(10), validacion_numeros])
    nombre = models.CharField(max_length=50, validators=[MinLengthValidator(3), MaxLengthValidator(50)])
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefono = models.CharField(max_length=15,validators= [validacion_numeros] )
    cargo = models.CharField(max_length=50, choices=CARGO)
    
    class Meta:
        verbose_name = '--EMPLEADO--'
        verbose_name_plural = '-----EMPLEADOS----'
        db_table = 'Empleados'
        
    def str(self):
        return self.nombre + ' ' + self.apellido
    
class clientes(models.Model):
    cedula = models.CharField(max_length=10, primary_key=True, validators=[MinLengthValidator(10), validacion_numeros])
    nombre = models.CharField(max_length=50, validators=[MinLengthValidator(3), MaxLengthValidator(50)])
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100,validators=[validar_solo_letras,])
    email = models.EmailField(max_length=50)
    telefono = models.CharField(max_length=20,validators= [validacion_numeros] )
    genero = models.CharField(max_length=50, choices=GENERO)
   
    class Meta:
        verbose_name = 'CLIENTE'
        verbose_name_plural = 'CLIENTES'
        db_table = 'clientes'
        
    def str(self):
        return self.nombre + ' ' + self.apellido
    
    
    
class productos(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True, validators=[MinLengthValidator(10), validacion_numeros])
    nombre = models.CharField(max_length=50, validators=[MinLengthValidator(3), MaxLengthValidator(50)])
    precio = models.CharField(max_length=50)
    marca = models.CharField(max_length=100,validators=[validar_solo_letras,])
    color = models.EmailField(max_length=50)
    
    class Meta:
        verbose_name = 'PRODUCTO'
        verbose_name_plural = 'PRODUCTOS'
        db_table = 'productos'
        
    def str(self):
        return self.nombre + ' ' + self.precio