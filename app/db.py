from sqlalchemy_utils import database_exists, create_database
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

Session = sessionmaker()
Base = declarative_base()


def bind_engine(engine):
    Base.metadata.bind = engine
    Session.configure(bind=engine)


def crear_conexion(db_connector, db_user, db_password, db_ip_address, db_name):
    url = f"{db_connector}://{db_user}:{db_password}@{db_ip_address}/{db_name}"
    try:
        engine = create_engine(url, echo=False)
        if not database_exists(engine.url):
            create_database(engine.url)
            print('se creo la base de datos')
        else:
            pass
        print('no se creo la base else')
        return engine
    except:
        print(
            f"Error al crear conector {db_connector}, servidor: {db_ip_address}")
        return None


def obtener_session(engine):
    Session = sessionmaker(bind=engine)
    return Session()




'''
    import pandas as pd
    from rest_framework import status
    from rest_framework.response import Response
    from .models import (Barrios, Campus, Carreras, Ciudades, Facultades, Generos,
                        Lugares, Paises, Personas, PersonasTitulaciones, Provincias,
                        TiposPersona, Titulaciones, Universidades)
    from .serializer import (BarriosSerializer, CampusSerializer, CarrerasSerializer,
                            CiudadesSerializer, FacultadesSerializer, GenerosSerializer,
                            LugaresSerializer, PaisesSerializer, PersonasSerializer,
                            PersonasTitulacionesSerializer, ProvinciasSerializer,
                            TiposPersonaSerializer, TitulacionesSerializer, UniversidadesSerializer)

    def fill_db():
        try:
            # Leer el archivo CSV y crear un DataFrame

            profesoresDF = pd.read_csv("raw_data/Profesores.csv")
            # Agregamos esta nueva columna con la constante profesor en el tipo de persona para este DF
            profesoresDF["tipopersona"] = "profesor"

            alumnosDF = pd.read_csv("raw_data/Alumnos.csv")
            # Agregamos esta nueva columna con la constante alumno en el tipo de persona para este DF
            alumnosDF["tipopersona"] = "alumno"

            cursos_profesoresDF = pd.read_csv("raw_data/cursos_profesores.csv")
            personasDF = pd.concat([profesoresDF, alumnosDF], ignore_index=True)
            /// lo de aca abajo de debe comentar
            lista_personas = []
            lista_errores = []

            for index, fila in personasDF.iterrows():
                lista_personas.append({**fila})
            ///            
            # Iterar a través de las filas del DataFrame y crear objetos de modelo
            for _, row in personasDF.iterrows():
                print(row)
                # Aquí debes mapear las columnas del DataFrame a los campos de tu modelo
                # Agregar el mapeo y creación de objetos para el modelo Pais
                pais_data = {
                    'nombre': row['country'],  # Ajusta la columna del DataFrame
                }
                pais_serializer = PaisesSerializer(data=pais_data)
                if pais_serializer.is_valid():
                    pais_serializer.save()
                else:
                    # Maneja errores de validación
                    return Response(pais_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

                # Agregar el mapeo y creación de objetos para el modelo Ciudad
                ciudad_data = {
                    'nombre': row['city'],  # Ajusta la columna del DataFrame
                }

                ciudad_serializer = CiudadesSerializer(data=ciudad_data)

                if ciudad_serializer.is_valid():
                    ciudad_serializer.save()
                else:
                    # Maneja errores de validación
                    return Response(ciudad_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

                # Agregar el mapeo y creación de objetos para el modelo Barrio
                barrio_data = {
                    'nombre': row['town'],  # Ajusta la columna del DataFrame
                }

                barrio_serializer = BarriosSerializer(data=barrio_data)

                if barrio_serializer.is_valid():
                    barrio_serializer.save()
                else:
                    # Maneja errores de validación
                    return Response(barrio_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

                # Agregar el mapeo y creación de objetos para el modelo Provincia
                provincia_data = {
                    'nombre': row['state'],  # Ajusta la columna del DataFrame
                }

                provincia_serializer = ProvinciasSerializer(data=provincia_data)

                if provincia_serializer.is_valid():
                    provincia_serializer.save()
                else:
                    # Maneja errores de validación
                    return Response(provincia_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

                # Agregar el mapeo y creación de objetos para el modelo Lugar
                lugar_data = {
                    'pais': pais_serializer.data['id'],  # Usar el ID del objeto creado para Pais
                    'barrio': barrio_serializer.data['id'],  # Usar el ID del objeto creado para Barrio
                    'provincia': provincia_serializer.data['id'],  # Usar el ID del objeto creado para Provincia
                    'ciudad': ciudad_serializer.data['id'],  # Usar el ID del objeto creado para Ciudad
                }

                lugar_serializer = LugaresSerializer(data=lugar_data)

                if lugar_serializer.is_valid():
                    lugar_serializer.save()
                else:
                    # Maneja errores de validación
                    return Response(lugar_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

                # Agregar el mapeo y creación de objetos para el modelo Genero
                genero_data = {
                    'nombre': row['gender'],  # Ajusta la columna del DataFrame
                }

                genero_serializer = GenerosSerializer(data=genero_data)

                if genero_serializer.is_valid():
                    genero_serializer.save()
                else:
                    # Maneja errores de validación
                    return Response(genero_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

                # Agregar el mapeo y creación de objetos para el modelo TipoPersona
                tipopersona_data = {
                    'nombre': row['tipopersona'],  # Ajusta la columna del DataFrame
                }

                tipopersona_serializer = TiposPersonaSerializer(data=tipopersona_data)

                if tipopersona_serializer.is_valid():
                    tipopersona_serializer.save()
                else:
                    # Maneja errores de validación
                    return Response(tipopersona_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


                # Agregar el mapeo y creación de objetos para el modelo Persona
                persona_data = {
                    'nombre': row['first_name'],
                    'apellido': row['last_name'],
                    'email': row['email'],
                    'genero': genero_serializer.data['id'],  # Usar el ID del objeto creado para Genero
                    'birthdate': row['birthdate'],
                    'personal_id': row['personal_id'],
                    'lugar': lugar_serializer.data['id'],  # Usar el ID del objeto creado para Lugar
                    'tipopersona': tipopersona_serializer.data['id'],  # Usar el ID del objeto creado para TipoPersona
                }

                persona_serializer = PersonasSerializer(data=persona_data)

                if persona_serializer.is_valid():
                    persona_serializer.save()
                else:
                    # Maneja errores de validación
                    return Response(persona_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


            # Puedes seguir el mismo patrón para otros modelos

            return Response({'message': 'Datos cargados con éxito'}, status=status.HTTP_201_CREATED)

        except Exception as e:
            # Maneja errores generales
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
'''