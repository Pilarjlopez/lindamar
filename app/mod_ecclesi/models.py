# Importar el objeto de base de datos (DB) desde el modulo principal de la aplicacion
# Definiremos esta /app/__init__.py el interior en las siguientes secciones.
from app import db

# Definir un modelo de base para otras tablas de la base de heredar
class Base(db.Model):
    __abstract__  = True
    date_created  = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

# Definir modelo de templo
class Templo(db.Model):
    __tablename__      = 'templo'
    id_templo          = db.Column('id_templo', db.Integer, primary_key=True)
    nombre             = db.Column('nombre', db.Unicode)
    nombre_popular     = db.Column('nombre_popular', db.Unicode)
    direccion          = db.Column('direccion', db.Unicode)
    telefono           = db.Column('telefono', db.Unicode)
    historia           = db.Column('historia', db.Unicode)
    portada            = db.Column('portada', db.Unicode)
    institucion        = db.Column('institucion', db.Unicode)

# Definir modelo de Categoria
class Categoria(db.Model):
    __tablename__ = 'categoria'
    id_categoria  = db.Column('id_categoria', db.Integer, primary_key=True)
    tipo          = db.Column('tipo', db.Unicode)
	