from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
import re
def validacion_numeros(value):
    if not value.isdigit():
        raise ValidationError("El valor debe contener solo números")
    
def validar_solo_letras(value):
    if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$', value):
        raise ValidationError("El valor solo puede contener letras y espacios.")    



