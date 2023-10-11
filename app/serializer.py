from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Barrios, Campus, Carreras, Ciudades, Facultades, Generos, Lugares, Paises, Personas, PersonasTitulaciones, Provincias, TiposPersona, Titulaciones, Universidades


    
class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User 
        fields = ['id', 'username', 'password', 'email']


class BarriosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barrios
        fields = '__all__'

class CampusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campus
        fields = '__all__'

class CarrerasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carreras
        fields = '__all__'

class CiudadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciudades
        fields = '__all__'

class FacultadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facultades
        fields = '__all__'

class GenerosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Generos
        fields = '__all__'



class PaisesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paises
        fields = '__all__'

class PersonasTitulacionesSerializer(serializers.ModelSerializer):
    persona = serializers.PrimaryKeyRelatedField(queryset=Personas.objects.all())
    tipo = serializers.PrimaryKeyRelatedField(queryset=TiposPersona.objects.all())
    titulacion = serializers.PrimaryKeyRelatedField(queryset=Titulaciones.objects.all())
    class Meta:
        model = PersonasTitulaciones
        fields = '__all__'

class ProvinciasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provincias
        fields = '__all__'

class TiposPersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TiposPersona
        fields = '__all__'

class TitulacionesSerializer(serializers.ModelSerializer):
    carrera = serializers.PrimaryKeyRelatedField(queryset=Carreras.objects.all())
    facultad = serializers.PrimaryKeyRelatedField(queryset=Facultades.objects.all())
    universidad = serializers.PrimaryKeyRelatedField(queryset=Universidades.objects.all())
    campus = serializers.PrimaryKeyRelatedField(queryset=Campus.objects.all())
    class Meta:
        model = Titulaciones
        fields = '__all__'

class TitulacionesGetSerializer(serializers.ModelSerializer):
    carrera = serializers.StringRelatedField()
    facultad = serializers.StringRelatedField()
    universidad = serializers.StringRelatedField()
    campus = serializers.StringRelatedField()
    class Meta:
        model = Titulaciones
        fields = '__all__'

class UniversidadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Universidades
        fields = '__all__'

class LugaresSerializer(serializers.ModelSerializer):
    pais = serializers.PrimaryKeyRelatedField(queryset=Paises.objects.all())
    ciudad = serializers.PrimaryKeyRelatedField(queryset=Ciudades.objects.all())
    barrio = serializers.PrimaryKeyRelatedField(queryset=Barrios.objects.all())
    provincia = serializers.PrimaryKeyRelatedField(queryset=Provincias.objects.all())
    class Meta:
        model = Lugares
        fields = '__all__'

class LugaresGetSerializer(serializers.ModelSerializer):
    pais = serializers.StringRelatedField()
    ciudad = serializers.StringRelatedField()
    barrio = serializers.StringRelatedField()
    provincia = serializers.StringRelatedField()
    class Meta:
        model = Lugares
        fields = '__all__'
    
class PersonasSerializer(serializers.ModelSerializer):
    genero = serializers.PrimaryKeyRelatedField(queryset=Generos.objects.all())
    lugar = serializers.PrimaryKeyRelatedField(queryset=Lugares.objects.all())
    
    class Meta:
        model = Personas
        fields = '__all__'
  
class PersonasGetSerializer(serializers.ModelSerializer):
    genero = serializers.StringRelatedField()
    lugar = LugaresGetSerializer()
    
    class Meta:
        model = Personas
        fields = '__all__'

class PersonasTitulacionesGetSerializer(serializers.ModelSerializer):
    persona = PersonasGetSerializer()
    tipo = serializers.StringRelatedField()
    titulacion = TitulacionesGetSerializer()
    class Meta:
        model = PersonasTitulaciones
        fields = '__all__'