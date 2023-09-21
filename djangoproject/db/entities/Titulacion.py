from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, String, Integer, UniqueConstraint, ForeignKey
from db.db import Base


class Titulacion(Base):
    __tablename__ = "titulaciones"
    __table_args__ = (UniqueConstraint('carrera_id', 'facultad_id', 'universidad_id',
                      'campus_id', name='uix_table_carrera_facultad_universidad_campus'),)
    id = Column(Integer, primary_key=True)
    carrera_id = Column(Integer, ForeignKey("carreras.id"))
    facultad_id = Column(Integer, ForeignKey("facultades.id"))
    universidad_id = Column(Integer, ForeignKey("universidades.id"))
    campus_id = Column(Integer, ForeignKey("campus.id"))

    carrera = relationship("Carrera", backref="related_carreras")
    facultad = relationship("Facultad", backref="related_facultades")
    universidad = relationship("Universidad", backref="related_universidades")
    campus = relationship("Campus", backref="related_campus")
