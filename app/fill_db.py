import pandas as pd
import os
from sqlalchemy.orm import declarative_base
from sqlalchemy import and_
from dotenv import load_dotenv
from .db import crear_conexion, obtener_session, bind_engine
from .entities.Pais import Pais
from .entities.Ciudad import Ciudad
from .entities.Barrio import Barrio
from .entities.Lugar import Lugar
from .entities.Provincia import Provincia
from .entities.TipoPersona import TipoPersona
from .entities.Persona import Persona
from .entities.Genero import Genero

from .entities.Campus import Campus
from .entities.Carrera import Carrera
from .entities.Universidad import Universidad
from .entities.Facultad import Facultad
from .entities.Titulacion import Titulacion
from .entities.PersonaTitulacion import PersonaTitulacion


def fill_db():
    load_dotenv()
    print('entro a fill db')

    engine_mysql = crear_conexion(
        os.getenv('DIALECT'), os.getenv('USER'), os.getenv('PASSWORD'), os.getenv('HOST'), os.getenv('DB'))
    session_mysql = obtener_session(engine_mysql)

    profesoresDF = pd.read_csv("app/raw_data/Profesores.csv")
    # Agregamos esta nueva columna con la constante profesor en el tipo de persona para este DF
    profesoresDF["tipopersona"] = "profesor"

    alumnosDF = pd.read_csv("app/raw_data/Alumnos.csv")
    # Agregamos esta nueva columna con la constante alumno en el tipo de persona para este DF
    alumnosDF["tipopersona"] = "alumno"
    cursos_profesoresDF = pd.read_csv("app/raw_data/cursos_profesores.csv")

    ### ACA TIENEN QUE ITERAR EL ARCHIVO cursos_profesoresDF y hacer la misma logica de personasDF cambiando el nombre de los campos
    ### tambien hay que importar las entities que faltan de la carpeta entities (ej: campus, universidades, etc) 

    ### for fila in cursos_profesoresDF:
    ###

    personasDF = pd.concat([profesoresDF, alumnosDF])

    lista_personas = []
    lista_errores = []

    for index, fila in personasDF.iterrows():
        lista_personas.append({**fila})
    
    
    # Nuevo dataframe desde la unión de los DF de profesores y alumnos
    ### ESTA ES LA LOGICA QUE TIENEN QUE COPIAR
    for fila in lista_personas:
        session_mysql.begin()
        try:
            # Se procesa la dirección de la persona, insertando si corresponde los items faltantes
            pais = session_mysql.query(Pais).filter(
                Pais.nombre == fila['country']).first()
            if pais == None:
                pais = Pais(nombre=fila['country'])
                session_mysql.add(pais)
            # Se procesa la dirección de la persona, insertando si corresponde los items faltantes

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

            # La persona se inserta al final porque se necesitan las entidades de genero, tipopersona y lugar ya cargadas testttt
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

    # ---------------------------------------------------------------------------------------------------------

    lista_profesores = []


    for index, fila in cursos_profesoresDF.iterrows():
        lista_profesores.append({**fila})
 
    for fila in lista_profesores:
        session_mysql.begin()
        try:
            campus = session_mysql.query(Campus).filter(
                Campus.nombre == fila['campus']).first()
            if campus == None:
                campus = Campus(nombre=fila['campus'])
                session_mysql.add(campus)

            # Se procesa la dirección de la persona, insertando si corresponde los items faltantes
            facultad = session_mysql.query(Facultad).filter(
                Facultad.nombre == fila['program']).first()
            if facultad == None:
                facultad = Facultad(nombre=fila['program'])
                session_mysql.add(facultad)

            carrera = session_mysql.query(Carrera).filter(
                Carrera.nombre == fila['branch']).first()
            if carrera == None:
                carrera = Carrera(nombre=fila['branch'])
                session_mysql.add(carrera)
            
            universidad = session_mysql.query(Universidad).filter(
                Universidad.nombre == fila['institute']).first()
            if universidad == None:
                universidad = Universidad(nombre=fila['institute'])
                session_mysql.add(universidad)

            titulaciones = session_mysql.query(Titulacion).filter(and_(
                Titulacion.campus == campus, Titulacion.carrera == carrera, Titulacion.facultad == facultad, Titulacion.universidad == universidad)).first()
            if titulaciones == None:
                titulaciones = Titulacion(campus=campus, carrera=carrera,
                              facultad=facultad, universidad=universidad)
                session_mysql.add(titulaciones)

            session_mysql.commit()
        except Exception as e:
            session_mysql.rollback()
            lista_errores.append(fila)
#---------------------------------------------------------------------------------
    session_mysql.close()
    engine_mysql.dispose()
