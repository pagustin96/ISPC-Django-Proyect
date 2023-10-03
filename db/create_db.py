from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv
from db.db import crear_conexion, obtener_session, bind_engine, Base
from db.entities import Persona, Barrio, Campus, Carrera, Ciudad, Facultad, Genero, Lugar, Pais, Provincia, TipoPersona, Titulacion, Universidad, PersonaTitulacion


def create_db():
    load_dotenv()

    engine_mysql = crear_conexion(
        os.getenv('DIALECT'), os.getenv('USER'), os.getenv('PASSWORD'), os.getenv('HOST'), os.getenv('DB'))

    bind_engine(engine_mysql)

    Base.metadata.create_all(engine_mysql)
    session_mysql = obtener_session(engine_mysql)

    session_mysql.close()
    engine_mysql.dispose()
