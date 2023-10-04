from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv
from .db import crear_conexion, obtener_session, bind_engine, Base
from .fill_db import fill_db
from .entities import Persona, Barrio, Campus, Carrera, Ciudad, Facultad, Genero, Lugar, Pais, Provincia, TipoPersona, Titulacion, Universidad, PersonaTitulacion
from rest_framework import status
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view, renderer_classes

@api_view(['POST'])  # Indicar que esta vista acepta solicitudes GET
@renderer_classes([JSONRenderer])  # Establecer JSONRenderer como renderizador
def create_db(request):
    load_dotenv()

    engine_mysql = crear_conexion(
        os.getenv('DIALECT'), os.getenv('USER'), os.getenv('PASSWORD'), os.getenv('HOST'), os.getenv('DB'))

    bind_engine(engine_mysql)

    Base.metadata.create_all(engine_mysql)
    session_mysql = obtener_session(engine_mysql)
    fill_db()
    session_mysql.close()
    engine_mysql.dispose()
    return Response({"database!!"}, status=status.HTTP_200_OK)
