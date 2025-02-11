from rest_framework import serializers
from .models import Empleados,clientes,productos

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleados
        fields = '__all__'
class clientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = clientes
        fields = '__all__'        
        
class productosSerializer(serializers.ModelSerializer):
    class Meta:
        model = productos
        fields = '__all__'                