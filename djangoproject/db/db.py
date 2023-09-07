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
        else:
            pass
        return engine
    except:
        print(
            f"Error al crear conector {db_connector}, servidor: {db_ip_address}")
        return None


def obtener_session(engine):
    Session = sessionmaker(bind=engine)
    return Session()
