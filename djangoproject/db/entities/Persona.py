from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, case, func
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import date
from db.db import Base


class Persona(Base):
    __tablename__ = "personas"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    apellido = Column(String(100))
    email = Column(String(255), unique=True)
    birthdate = Column(Date)
    personal_id = Column(String(50), unique=True)
    genero_id = Column(Integer, ForeignKey("generos.id"))
    lugar_id = Column(Integer, ForeignKey("lugares.id"))

    genero = relationship("Genero", backref="related_generos")
    lugar = relationship("Lugar", backref="related_lugares")

    @hybrid_property
    def age(self):
        today = date.today()
        edad = today.year - self.birthdate.year
        if (today.month, today.day) > (self.birthdate.month, self.birthdate.day):
            edad -= 1
        return edad

    @age.expression
    def age(cls):
        today = date.today()
        birthdate_year = func.extract('year', cls.birthdate)
        birthdate_month = func.extract('month', cls.birthdate)
        birthdate_day = func.extract('day', cls.birthdate)
        return case(
            (
                (
                    (birthdate_month < today.month) |
                    ((birthdate_month == today.month)
                     & (birthdate_day <= today.day)),
                    today.year - birthdate_year - 1
                )
            ),
            else_=today.year - birthdate_year
        )
