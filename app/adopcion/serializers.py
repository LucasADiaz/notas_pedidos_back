from rest_framework import serializers
from .models import Persona

class PersonaSerializer(serializers.Serializer) : 
    id = serializers.ReadOnlyField()
    nombre = serializers.CharField()
    apellido = serializers.CharField()
    edad = serializers.IntegerField()
    telefono = serializers.CharField()
    email = serializers.EmailField()
    domicilio = serializers.CharField()

    def create(self, validate_data) : 
        instance = Persona()
        instance.nombre = validate_data.get('nombre')
        instance.apellido = validate_data.get('apellido')
        instance.edad = validate_data.get('edad')
        instance.telefono = validate_data.get('telefono')
        instance.email = validate_data.get('email')
        instance.domicilio = validate_data.get('domicilio')
        instance.save()
        return instance

    