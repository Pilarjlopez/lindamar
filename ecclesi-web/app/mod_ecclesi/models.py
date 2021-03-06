# Importar el objeto de base de datos (DB) desde el modulo principal de la aplicacion
# Definiremos esta /app/__init__.py el interior en las siguientes secciones.
from app import db
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

# Definir un modelo de base para otras tablas de la base de heredar
class Base(db.Model):
    __abstract__  = True
    date_created  = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

# Definir modelo de Categoria
class Categoria(db.Model):
    __tablename__ = 'categoria'
    id_categoria  = db.Column('id_categoria', db.Integer, primary_key=True)
    tipo          = db.Column('tipo', db.Unicode)

# Definir modelo de Oficio Eclesiastico
class Oficio(db.Model):
    __tablename__          = 'oficio_eclesiastico'
    id_oficio_eclesiastico = db.Column(db.Integer, primary_key=True)
    tipo                   = db.Column(db.String(128), nullable=False)

# Definir modelo de Munnicipio
class Departamento(db.Model):
    __tablename__   = 'departamento'
    id_departamento = db.Column(db.Integer, primary_key=True)
    nombre          = db.Column(db.String(128), nullable=False)

# Definir modelo de Munnicipio
class Municipio(db.Model):
    __tablename__   = 'municipio'
    id_municipio    = db.Column(db.Integer, primary_key=True)
    nombre          = db.Column(db.String(128), nullable=False)
    id_departamento = db.Column(db.Integer, db.ForeignKey('departamento.id_departamento'))

    departamento    = db.relationship('Departamento')

# Definir modelo de Zona Parroquial
class Zona_Parroquial(db.Model):
    __tablename__      = 'zona_parroquial'
    id_zona_parroquial = db.Column(db.Integer, primary_key=True)
    nombre             = db.Column(db.String(128), nullable=False)
    id_zona_pastoral   = db.Column(db.Integer, nullable=True)

    #zona_pastoral     = db.relationship('Zona_Pastoral')

    def __init__(self, nombre=None, id_zona_pastoral=None):
        self.nombre            = nombre
        self.id_zona_pastoral  = id_zona_pastoral

#definir modelo de Galeria de fotos
class Galeria(db.Model):
    __tablename__ = 'galeria'
    id_galeria    = db.Column(db.Integer, primary_key=True)
    descripcion   = db.Column(db.String(45), nullable=False)
    portada       = db.Column(db.String(45), nullable=False)

#definir modelo de Galeria de fotos
class Foto(db.Model):
    __tablename__ = 'foto'
    id_foto       = db.Column(db.Integer, primary_key=True)
    foto          = db.Column(db.String(45), nullable=False)
    ubicacion     = db.Column(db.String(45), nullable=False)
    id_galeria    = db.Column(db.Integer, db.ForeignKey('galeria.id_galeria'), nullable=False)

    galeria       = db.relationship('Galeria')

#definir modelo de Servicio Religioso
class Servicio_Religioso(db.Model):
    __tablename__           = 'servicio_religioso'
    id_servicio_religioso   = db.Column(db.Integer, primary_key=True)
    tipo                    = db.Column(db.String(45), nullable=False)
    descripcion             = db.Column(db.String(45), nullable=False)

#definir modelo de horario
class Horario(db.Model):
    __tablename__           = 'horario'
    id_horario              = db.Column(db.Integer, primary_key=True)
    hora                    = db.Column(db.Integer, nullable=False)
    dia                     = db.Column(db.Integer, nullable=False)
    id_servicio_religioso   = db.Column(db.Integer, db.ForeignKey('servicio_religioso.id_servicio_religioso'))

    servicio_religioso      = db.relationship('Servicio_Religioso')

#definir modelo de actividad
class Actividad(db.Model):
    __tabletname__      = 'actividad'
    id_actividad        = db.Column(db.Integer, primary_key=True)
    nombre              = db.Column(db.String(128), nullable=False)
    dia                 = db.Column(db.String(128), nullable=False)
    hora                = db.Column(db.String(128), nullable=False)
    descripcion         = db.Column(db.String(128), nullable=False)
    id_templo           = db.Column(db.Integer, nullable=False)
    id_tipo_actividad   = db.Column(db.Integer, nullable=False)

    #tipo_actividad      = db.relationship('Tipo_Actividad')

    def __init__(self, nombre=None, dia=None, hora=None, descripcion=None, id_templo=None, id_tipo_actividad=None):
        self.nombre            = nombre
        self.dia               = dia
        self.hora              = hora
        self.descripcion       = descripcion
        self.id_templo         = id_templo
        self.id_tipo_actividad = id_tipo_actividad

#Definir modelo de tipo de actividad
class Tipo_Actividad(db.Model):
    __tabletname__     = 'tipo_actividad'
    id_tipo_actividad  = db.Column(db.Integer, primary_key=True)
    tipo               = db.Column(db.String(45), nullable=False)

#Definir diocesis
class Diocesis(db.Model):
    __tablename__       = 'diocesis'
    id_diocesis         = db.Column(db.Integer, primary_key=True)
    nombre              = db.Column(db.String(45),nullable=False)

#Definir noticia
class Noticia(db.Model):
    __tablename__       = 'noticia'
    id_noticia          = db.Column(db.Integer, primary_key=True)
    titulo              = db.Column(db.String(45),nullable=False)
    noticia             = db.Column(db.String(45),nullable=False)
    imagen              = db.Column(db.String(45))
    id_templo           = db.Column(db.Integer, nullable=False)

    def __init__(self, titulo=None, noticia=None, imagen=None, id_templo=None):
        self.titulo     = titulo
        self.noticia    = noticia
        self.imagen     = imagen
        self.id_templo  = id_templo

# Definir modelo de Templo
class Templo(db.Model):
    __tablename__         = 'templo'
    id_templo             = db.Column(db.Integer, primary_key=True)
    nombre                = db.Column(db.String(128), nullable=False)
    nombre_popular        = db.Column(db.String(128), nullable=False)
    direccion             = db.Column(db.String(128), nullable=False)
    telefono              = db.Column(db.String(128), nullable=False)
    historia              = db.Column(db.String(128), nullable=False)
    nombre_institucion    = db.Column(db.String(128), nullable=False)
    portada               = db.Column(db.String(128), nullable=False)
    institucion           = db.Column(db.String(128), nullable=False)
    id_zona_parroquial    = db.Column(db.Integer, db.ForeignKey('zona_parroquial.id_zona_parroquial'), nullable=False)
    id_municipio          = db.Column(db.Integer, db.ForeignKey('municipio.id_municipio'), nullable=False)
    id_categoria          = db.Column(db.Integer, db.ForeignKey('categoria.id_categoria'), nullable=False)
    id_galeria            = db.Column(db.Integer, db.ForeignKey('galeria.id_galeria'), nullable=False)
    id_servicio_religioso = db.Column(db.Integer, db.ForeignKey('servicio_religioso.id_servicio_religioso'), nullable=False)

    zona_parroquial    = db.relationship('Zona_Parroquial')
    municipio          = db.relationship('Municipio')
    categoria          = db.relationship('Categoria')
    galeria            = db.relationship('Galeria')
    servicio_religioso = db.relationship('Servicio_Religioso')

    def __init__(
        self,
        nombre=None,
        nombre_popular=None,
        direccion=None,
        telefono=None,
        historia=None,
        nombre_institucion=None,
        portada=None,
        institucion=None,
        id_zona_parroquial=None,
        id_municipio=None,
        id_categoria=None,
        id_galeria=None,
        id_servicio_religioso=None
    ):
        self.nombre                 = nombre
        self.nombre_popular         = nombre_popular
        self.direccion              = direccion
        self.telefono               = telefono
        self.historia               = historia
        self.nombre_institucion     = nombre_institucion
        self.portada                = portada
        self.institucion            = institucion
        self.id_zona_parroquial     = id_zona_parroquial
        self.id_municipio           = id_municipio
        self.id_categoria           = id_categoria
        self.id_galeria             = id_galeria
        self.id_servicio_religioso  = id_servicio_religioso
