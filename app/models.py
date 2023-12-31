from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

# Create your models here.

class Barrios(models.Model):
    nombre = models.CharField(unique=True, max_length=100, blank=True, null=True)
    def __str__(self):
        return self.nombre
    class Meta:
        db_table = 'barrios'
        verbose_name = 'Barrio'
        verbose_name_plural = "Barrios"
    


class Campus(models.Model):
    nombre = models.CharField(unique=True, max_length=100, blank=True, null=True)
    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'campus'
        verbose_name = 'Campus'
        verbose_name_plural = "Campus"
    


class Carreras(models.Model):
    nombre = models.CharField(unique=True, max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'carreras'
        verbose_name = 'Carrera'
        verbose_name_plural = "Carreras"
    


class Ciudades(models.Model):
    nombre = models.CharField(unique=True, max_length=100, blank=True, null=True)
    def __str__(self):
        return self.nombre
    class Meta:
        db_table = 'ciudades'
        verbose_name = 'Ciudad'
        verbose_name_plural = "Ciudades"
    


class Facultades(models.Model):
    nombre = models.CharField(unique=True, max_length=100, blank=True, null=True)
    def __str__(self):
        return self.nombre
    class Meta:
        db_table = 'facultades'
        verbose_name = 'Facultad'
        verbose_name_plural = "Facultades"
    


class Generos(models.Model):
    nombre = models.CharField(unique=True, max_length=50, blank=True, null=True)
    def __str__(self):
        return self.nombre
    class Meta:
        db_table = 'generos'
        verbose_name = 'Genero'
        verbose_name_plural = "Generos"
    
class Paises(models.Model):
    nombre = models.CharField(unique=True, max_length=100, blank=True, null=True)
    def __str__(self):
        return self.nombre
    class Meta:
        db_table = 'paises'
        verbose_name = 'Pais'
        verbose_name_plural = "Paises"
    

class Provincias(models.Model):
    nombre = models.CharField(unique=True, max_length=100, blank=True, null=True)
    def __str__(self):
        return self.nombre
    class Meta:
        db_table = 'provincias'
        verbose_name = 'Provincia'
        verbose_name_plural = "Provincias"


class Lugares(models.Model):
    pais = models.ForeignKey(Paises, models.PROTECT, blank=True, null=True)
    ciudad = models.ForeignKey(Ciudades, models.PROTECT, blank=True, null=True)
    barrio = models.ForeignKey(Barrios, models.PROTECT, blank=True, null=True)
    provincia = models.ForeignKey(Provincias, models.PROTECT, blank=True, null=True)
    def __str__(self):
        return f'{self.ciudad},{self.provincia},{self.pais},{self.barrio}'
    class Meta:
        db_table = 'lugares'
        unique_together = (('pais', 'ciudad', 'barrio', 'provincia'),)
        verbose_name = 'Lugar'
        verbose_name_plural = "Lugares"
    

class Personas(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    apellido = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(unique=True, max_length=255, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    personal_id = models.IntegerField(unique=True, blank=True, null=True)
    genero = models.ForeignKey(Generos, models.PROTECT, blank=True, null=True)
    lugar = models.ForeignKey(Lugares, models.PROTECT, blank=True, null=True)
    def __str__(self):
        return f'{self.nombre},{self.apellido},{self.email},{self.birthdate},{self.personal_id},{self.genero},{self.lugar}'
    class Meta:
        db_table = 'personas'
        verbose_name = 'persona'
        verbose_name_plural = "Personas"
    
class TiposPersona(models.Model):
    nombre = models.CharField(unique=True, max_length=50, blank=True, null=True)
    def __str__(self):
        return self.nombre
    class Meta:
        db_table = 'tipos_persona'
        verbose_name = 'Tipo de persona'
        verbose_name_plural = "Tipos de persona"

class Universidades(models.Model):
    nombre = models.CharField(unique=True, max_length=100, blank=True, null=True)
    def __str__(self):
        return self.nombre
    class Meta:
        db_table = 'universidades'
        verbose_name = 'Universidad'
        verbose_name_plural = "Universidades"
    

class Titulaciones(models.Model):
    carrera = models.ForeignKey(Carreras, models.PROTECT, blank=True, null=True)
    facultad = models.ForeignKey(Facultades, models.PROTECT, blank=True, null=True)
    universidad = models.ForeignKey(Universidades, models.PROTECT, blank=True, null=True)
    campus = models.ForeignKey(Campus, models.PROTECT, blank=True, null=True)
    def __str__(self):
        return f'{self.carrera},{self.facultad},{self.universidad}'

    class Meta:
        db_table = 'titulaciones'
        unique_together = (('carrera', 'facultad', 'universidad', 'campus'),)
        verbose_name = 'Titulacion'
        verbose_name_plural = "Titulaciones"
    


class PersonasTitulaciones(models.Model):
    persona = models.ForeignKey(Personas, models.PROTECT, blank=True, null=True)
    titulacion = models.ForeignKey(Titulaciones, models.PROTECT, blank=True, null=True)
    tipo = models.ForeignKey(TiposPersona, models.PROTECT, blank=True, null=True)
    def __str__(self):
        return  f'{self.persona},{self.titulacion},{self.tipo}'
    class Meta:
        db_table = 'personas_titulaciones'
        verbose_name = 'Persona Titulaciones'
        verbose_name_plural = "PersonasTitulaciones"
