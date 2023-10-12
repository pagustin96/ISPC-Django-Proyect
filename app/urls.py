from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.urls import re_path
from.create_db import create_db
from app import views


router = routers.DefaultRouter()
router.register(r'barrios', views.BarriosView, 'barrios')
router.register(r'campus', views.CampusView, 'campus')
router.register(r'carreras', views.CarrerasView, 'carreras')
router.register(r'ciudades', views.CiudadesView, 'ciudades')
router.register(r'facultades', views.FacultadesView, 'facultades')
router.register(r'generos', views.GenerosView, 'generos')
router.register(r'lugares', views.LugaresView, 'lugares')
router.register(r'paises', views.PaisesView, 'paises')
router.register(r'personas', views.PersonasView, 'personas')
router.register(r'personasTitulaciones', views.PersonasTitulacionesView, 'personasTitulaciones')
router.register(r'provincias', views.ProvinciasView, 'provincias')
router.register(r'tiposPersona', views.TipoPersonaView, 'tiposPersona')
router.register(r'titulaciones', views.TitulacionesView, 'titulaciones')
router.register(r'universidades', views.universidadesView, 'universidades')


urlpatterns = [
    re_path('signup', views.signup),    
    re_path('login', views.login),
    re_path('test_token', views.test_token),
    path('api/v1/', include(router.urls)),
    path('docs/', include_docs_urls(title='App API')),
    path('api/v1/db', create_db, name='db'),
    path('api/v1/buscar_persona/<str:personal_id>/', views.buscar_persona_por_dni, name='buscar_persona_por_dni'),
]
