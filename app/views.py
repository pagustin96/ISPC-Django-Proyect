from django.shortcuts import render
from rest_framework import viewsets
from .serializer import BarriosSerializer, CampusSerializer, CarrerasSerializer, CiudadesSerializer, FacultadesSerializer, GenerosSerializer, LugaresSerializer, PaisesSerializer, PersonasSerializer, PersonasTitulacionesSerializer, ProvinciasSerializer, TiposPersonaSerializer, TitulacionesSerializer, UniversidadesSerializer
from .models import Barrios, Campus, Carreras, Ciudades, Facultades, Generos, Lugares, Paises, Personas, PersonasTitulaciones, Provincias, TiposPersona, Titulaciones, Universidades


# Create your views here.
class BarriosView(viewsets.ModelViewSet):
    serializer_class = BarriosSerializer
    queryset = Barrios.objects.all()

class CampusView(viewsets.ModelViewSet):
    serializer_class = CampusSerializer
    queryset = Campus.objects.all()

class CarrerasView(viewsets.ModelViewSet):
    serializer_class = CarrerasSerializer
    queryset = Carreras.objects.all()

class CiudadesView(viewsets.ModelViewSet):
    serializer_class = CiudadesSerializer
    queryset = Ciudades.objects.all()

class FacultadesView(viewsets.ModelViewSet):
    serializer_class = FacultadesSerializer
    queryset = Facultades.objects.all()

class GenerosView(viewsets.ModelViewSet):
    serializer_class = GenerosSerializer
    queryset = Generos.objects.all()

class LugaresView(viewsets.ModelViewSet):
    serializer_class = LugaresSerializer
    queryset = Lugares.objects.all()

class PaisesView(viewsets.ModelViewSet):
    serializer_class = PaisesSerializer
    queryset = Paises.objects.all()

class PersonasView(viewsets.ModelViewSet):
    serializer_class = PersonasSerializer
    queryset = Personas.objects.all()

class PersonasTitulacionesView(viewsets.ModelViewSet):
    serializer_class = PersonasTitulacionesSerializer
    queryset = PersonasTitulaciones.objects.all()

class ProvinciasView(viewsets.ModelViewSet):
    serializer_class = ProvinciasSerializer
    queryset = Provincias.objects.all()

class TipoPersonaView(viewsets.ModelViewSet):
    serializer_class = TiposPersonaSerializer
    queryset = TiposPersona.objects.all()

class TitulacionesView(viewsets.ModelViewSet):
    serializer_class = TitulacionesSerializer
    queryset = Titulaciones.objects.all()

class universidadesView(viewsets.ModelViewSet):
    serializer_class = UniversidadesSerializer
    queryset = Universidades.objects.all()