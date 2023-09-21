from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer
from db.db import Base


class Genero(Base):
    __tablename__ = "generos"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), unique=True)
