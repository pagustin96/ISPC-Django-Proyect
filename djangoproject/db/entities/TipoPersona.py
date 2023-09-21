from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer
from db.db import Base


class TipoPersona(Base):
    __tablename__ = "tipos_persona"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), unique=True)
