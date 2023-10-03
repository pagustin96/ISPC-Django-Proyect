from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, String, Integer, UniqueConstraint, ForeignKey
from db.db import Base


class Lugar(Base):
    __tablename__ = "lugares"
    __table_args__ = (UniqueConstraint('pais_id', 'ciudad_id',
                      'barrio_id', 'provincia_id', name='uidx_sitio_unico'), )
    id = Column(Integer, primary_key=True)
    pais_id = Column(Integer, ForeignKey("paises.id"))
    ciudad_id = Column(Integer, ForeignKey("ciudades.id"))
    barrio_id = Column(Integer, ForeignKey("barrios.id"))
    provincia_id = Column(Integer, ForeignKey("provincias.id"))

    pais = relationship("Pais", backref="related_paises")
    ciudad = relationship("Ciudad", backref="related_ciudades")
    barrio = relationship("Barrio", backref="related_barrios")
    provincia = relationship("Provincia", backref="related_provincia")
