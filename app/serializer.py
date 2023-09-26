from rest_framework import serializers
from .models import Barrios, Campus, Carreras, Ciudades, Facultades, Generos, Lugares, Paises, Personas, PersonasTitulaciones, Provincias, TiposPersona, Titulaciones, Universidades, CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'password')  # Campos a incluir en la creación de usuario
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        if CustomUser.objects.filter(username=username).exists():
            raise serializers.ValidationError('Ya existe un usuario con este nombre de usuario.')
        user = CustomUser(username=username)
        user.set_password(password)
        user.save()
        return user


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

class LugaresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lugares
        fields = '__all__'

class PaisesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paises
        fields = '__all__'

class PersonasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personas
        fields = '__all__'

class PersonasTitulacionesSerializer(serializers.ModelSerializer):
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
    class Meta:
        model = Titulaciones
        fields = '__all__'

class UniversidadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Universidades
        fields = '__all__'