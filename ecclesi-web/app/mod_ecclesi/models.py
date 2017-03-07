# Importar el objeto de base de datos (DB) desde el modulo principal de la aplicacion
# Definiremos esta /app/__init__.py el interior en las siguientes secciones.
from app import db

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
    
# Definir modelo de Templo
class Templo(db.Model):
    __tablename__      = 'templo'
    id_templo          = db.Column(db.Integer, primary_key=True)
    nombre             = db.Column(db.String(128), nullable=False)
    nombre_popular     = db.Column(db.String(128), nullable=False)
    direccion          = db.Column(db.String(128), nullable=False)
    telefono           = db.Column(db.String(128), nullable=False)
    historia           = db.Column(db.String(128), nullable=False)
    nombre_institucion = db.Column(db.String(128), nullable=False)
    portada            = db.Column(db.String(128), nullable=False)
    #georeferencia      = db.Column(db.String(128), nullable=False)
    id_zona_parroquial = db.Column(db.Integer, nullable=False)
    id_municipio       = db.Column(db.Integer, nullable=False)
    id_categoria       = db.Column(db.Integer, nullable=False)

# Definir modelo de Oficio Eclesiastico
class Oficio(db.Model):
    __tablename__          = 'oficio_eclesiastico'
    id_oficio_eclesiastico = db.Column(db.Integer, primary_key=True)
    tipo                   = db.Column(db.String(128), nullable=False)

	