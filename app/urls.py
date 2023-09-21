from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse


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
    path('api/v1/', include(router.urls)),
    path('docs/', include_docs_urls(title='App API'))
]


'''


from .db import fill_db



def fill_db_view(request):
    result = fill_db()  # Llama a la función fill_db
    if result:
            return JsonResponse({'message': 'Datos cargados con éxito'}, status=201)
    else:
        return JsonResponse({'error': 'Hubo un problema al cargar los datos'}, status=500)
urlpatterns = [
    path('api/v1/', include([
        path('barrios/', views.BarriosView.as_view({'get': 'list', 'post': 'create'}), name='barrios-list'),
        path('campus/', views.CampusView.as_view({'get': 'list', 'post': 'create'}), name='campus-list'),
        path('carreras/', views.CarrerasView.as_view({'get': 'list', 'post': 'create'}), name='carreras-list'),
        # ... otras rutas para tus viewsets ...

        # Agrega la ruta para llamar a la función fill_db_view
        
        path('filldb/', fill_db_view, name='filldb'),
        
    ])),
    path('docs/', include_docs_urls(title='App API')),
]


'''