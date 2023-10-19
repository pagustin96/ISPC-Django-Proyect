from datetime import datetime, timedelta
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.utils import timezone
from .serializer import BarriosSerializer, CampusSerializer, CarrerasSerializer, CiudadesSerializer, FacultadesSerializer, GenerosSerializer, LugaresSerializer, LugaresGetSerializer, PaisesSerializer, PersonasSerializer, PersonasGetSerializer, PersonasTitulacionesSerializer, PersonasTitulacionesGetSerializer, ProvinciasSerializer, TiposPersonaSerializer, TitulacionesSerializer, TitulacionesGetSerializer, UniversidadesSerializer
from .models import Barrios, Campus, Carreras, Ciudades, Facultades, Generos, Lugares, Paises, Personas, PersonasTitulaciones, Provincias, TiposPersona, Titulaciones, Universidades


# Create your views here.
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from .serializer import UserSerializer

@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({'token': token.key, 'user': serializer.data})
    return Response(serializer.errors, status=status.HTTP_200_OK)

@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response("missing user", status=status.HTTP_404_NOT_FOUND)
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(user)
    return Response({'token': token.key, 'user': serializer.data})

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response("passed!")



@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
class BarriosView(viewsets.ModelViewSet):
    serializer_class = BarriosSerializer
    queryset = Barrios.objects.all()

@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
class CampusView(viewsets.ModelViewSet):
    serializer_class = CampusSerializer
    queryset = Campus.objects.all()

@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
class CarrerasView(viewsets.ModelViewSet):
    serializer_class = CarrerasSerializer
    queryset = Carreras.objects.all()

@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
class CiudadesView(viewsets.ModelViewSet):
    serializer_class = CiudadesSerializer
    queryset = Ciudades.objects.all()

@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
class FacultadesView(viewsets.ModelViewSet):
    serializer_class = FacultadesSerializer
    queryset = Facultades.objects.all()

@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
class GenerosView(viewsets.ModelViewSet):
    serializer_class = GenerosSerializer
    queryset = Generos.objects.all()

@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
class LugaresView(viewsets.ModelViewSet):
    queryset = Lugares.objects.all()
    def get_serializer_class(self):
        if self.action in ['retrieve', 'list']:
            return LugaresGetSerializer  # Usar el serializador específico para GET
        return LugaresSerializer  # Usar el serializador original para otras operaciones

@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
class PaisesView(viewsets.ModelViewSet):
    serializer_class = PaisesSerializer
    queryset = Paises.objects.all()

@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
class PersonasView(viewsets.ModelViewSet):
    queryset = Personas.objects.all()
    def get_serializer_class(self):
        if self.action in ['retrieve', 'list']:
            return PersonasGetSerializer  # Usar el serializador específico para GET
        return PersonasSerializer  # Usar el serializador original para otras operaciones

@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])   
@api_view(['GET'])
def buscar_persona_por_dni(request, personal_id):
    try:
        persona = Personas.objects.get(personal_id=personal_id)
        serializer = PersonasGetSerializer(persona)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Personas.DoesNotExist:
        return Response({'error': 'La persona no fue encontrada.'}, status=status.HTTP_404_NOT_FOUND)

@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
class PersonasTitulacionesView(viewsets.ModelViewSet):
    queryset = PersonasTitulaciones.objects.all()
    def get_serializer_class(self):
        if self.action in ['retrieve', 'list']:
            return PersonasTitulacionesGetSerializer  # Usar el serializador específico para GET
        return PersonasTitulacionesSerializer  # Usar el serializador original para otras operaciones

@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])    
class ProvinciasView(viewsets.ModelViewSet):
    serializer_class = ProvinciasSerializer
    queryset = Provincias.objects.all()

@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
class TipoPersonaView(viewsets.ModelViewSet):
    serializer_class = TiposPersonaSerializer
    queryset = TiposPersona.objects.all()

@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
class TitulacionesView(viewsets.ModelViewSet):
    queryset = Titulaciones.objects.all()
    def get_serializer_class(self):
        if self.action in ['retrieve', 'list']:
            return TitulacionesGetSerializer  # Usar el serializador específico para GET
        return TitulacionesSerializer  # Usar el serializador original para otras operaciones

@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
class universidadesView(viewsets.ModelViewSet):
    serializer_class = UniversidadesSerializer
    queryset = Universidades.objects.all()