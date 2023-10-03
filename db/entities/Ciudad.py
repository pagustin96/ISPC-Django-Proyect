from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer
from db.db import Base


class Ciudad(Base):
    __tablename__ = "ciudades"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), unique=True)
