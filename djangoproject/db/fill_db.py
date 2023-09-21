import pandas as pd
import os
from sqlalchemy.orm import declarative_base
from sqlalchemy import and_
from dotenv import load_dotenv
from db.db import crear_conexion, obtener_session, bind_engine
from db.entities.Pais import Pais
from db.entities.Ciudad import Ciudad
from db.entities.Barrio import Barrio
from db.entities.Lugar import Lugar
from db.entities.Provincia import Provincia
from db.entities.TipoPersona import TipoPersona
from db.entities.Persona import Persona
from db.entities.Genero import Genero


def fill_db():
    load_dotenv()

    engine_mysql = crear_conexion(
        os.getenv('DIALECT'), os.getenv('USER'), os.getenv('PASSWORD'), os.getenv('HOST'), os.getenv('DB'))
    session_mysql = obtener_session(engine_mysql)

    profesoresDF = pd.read_csv("raw_data/Profesores.csv")
    # Agregamos esta nueva columna con la constante profesor en el tipo de persona para este DF
    profesoresDF["tipopersona"] = "profesor"

    alumnosDF = pd.read_csv("raw_data/Alumnos.csv")
    # Agregamos esta nueva columna con la constante alumno en el tipo de persona para este DF
    alumnosDF["tipopersona"] = "alumno"

    cursos_profesoresDF = pd.read_csv("raw_data/cursos_profesores.csv")

    ###

    personasDF = pd.concat([profesoresDF, alumnosDF])

    lista_personas = []
    lista_errores = []

    for index, fila in personasDF.iterrows():
        lista_personas.append({**fila})

    ##########

    # Nuevo dataframe desde la unión de los DF de profesores y alumnos

    for fila in lista_personas:
        session_mysql.begin()
        try:
            # Se procesa la dirección de la persona, insertando si corresponde los items faltantes
            pais = session_mysql.query(Pais).filter(
                Pais.nombre == fila['country']).first()
            if pais == None:
                pais = Pais(nombre=fila['country'])
                session_mysql.add(pais)

            ciudad = session_mysql.query(Ciudad).filter(
                Ciudad.nombre == fila['city']).first()
            if ciudad == None:
                ciudad = Ciudad(nombre=fila['city'])
                session_mysql.add(ciudad)

            barrio = session_mysql.query(Barrio).filter(
                Barrio.nombre == fila['town']).first()
            if barrio == None:
                barrio = Barrio(nombre=fila['town'])
                session_mysql.add(barrio)

            provincia = session_mysql.query(Provincia).filter(
                Provincia.nombre == fila['state']).first()
            if provincia == None:
                provincia = Provincia(nombre=fila['state'])
                session_mysql.add(provincia)

            lugar = session_mysql.query(Lugar).filter(and_(
                Lugar.pais == pais, Lugar.barrio == barrio, Lugar.provincia == provincia, Lugar.ciudad == ciudad)).first()
            if lugar == None:
                lugar = Lugar(pais=pais, barrio=barrio,
                              provincia=provincia, ciudad=ciudad)
                session_mysql.add(lugar)
            # ************************************************************************************************

            genero = session_mysql.query(Genero).filter(
                Genero.nombre == fila['gender']).first()
            if genero == None:
                genero = Genero(nombre=fila['gender'])
                session_mysql.add(genero)

            tipopersona = session_mysql.query(TipoPersona).filter(
                TipoPersona.nombre == fila['tipopersona']).first()
            if tipopersona == None:
                tipopersona = TipoPersona(nombre=fila['tipopersona'])
                session_mysql.add(tipopersona)

            # La persona se inserta al final porque se necesitan las entidades de genero, tipopersona y lugar ya cargadas
            persona = session_mysql.query(Persona).filter(
                Persona.personal_id == fila['personal_id']).first()
            if persona == None:
                persona = Persona(nombre=fila['first_name'], apellido=fila['last_name'], email=fila['email'],
                                  birthdate=fila['birthdate'], personal_id=fila['personal_id'], lugar=lugar, genero=genero)
                session_mysql.add(persona)
                # Saque tipo persona de Persona, se debe agregar en personas_titulaciones

            session_mysql.commit()
        except Exception as e:
            session_mysql.rollback()
            lista_errores.append(fila)
    #         errores = []
    #         errores.append(e)
    # print(errores)
    session_mysql.close()
    engine_mysql.dispose()
