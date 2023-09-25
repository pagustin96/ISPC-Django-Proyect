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
from .serializer import BarriosSerializer, CampusSerializer, CarrerasSerializer, CiudadesSerializer, FacultadesSerializer, GenerosSerializer, LugaresSerializer, PaisesSerializer, PersonasSerializer, PersonasTitulacionesSerializer, ProvinciasSerializer, TiposPersonaSerializer, TitulacionesSerializer, UniversidadesSerializer, CustomUserSerializer
from .models import Barrios, Campus, Carreras, Ciudades, Facultades, Generos, Lugares, Paises, Personas, PersonasTitulaciones, Provincias, TiposPersona, Titulaciones, Universidades, CustomUser


# Create your views here.
class CreateUserView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response({'detail': 'Usuario creado con éxito'}, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        print(username)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
             # Calcula la fecha de expiración (30 minutos desde ahora)
            expiration_time = timezone.now() + timedelta(minutes=30)
            token, created = Token.objects.get_or_create(user=user)
            token.expires = expiration_time
            token.save()
            # Crear una respuesta JSON HTTP con la cookie del token
            response = JsonResponse({'message': 'Inicio de sesión exitoso'}, status=status.HTTP_200_OK)
            response.set_cookie(key='auth_token', value=token.key, httponly=True, secure=True)
            return (response)
        else:
            return JsonResponse({'error': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)




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