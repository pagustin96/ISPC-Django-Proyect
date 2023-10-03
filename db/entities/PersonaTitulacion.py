from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from datetime import date
from db.db import Base


class PersonaTitulacion(Base):
    __tablename__ = "personas_titulaciones"
    id = Column(Integer, primary_key=True)
    persona_id = Column(Integer, ForeignKey("personas.id"))
    titulacion_id = Column(Integer, ForeignKey("titulaciones.id"))
    tipo_id = Column(Integer, ForeignKey("tipos_persona.id"))

    persona = relationship("Persona", backref="related_personas")
    titulacion = relationship("Titulacion", backref="related_titulaciones")
    tipopersona = relationship("TipoPersona", backref="related_tipos_persona")
