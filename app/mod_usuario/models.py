# Importar el objeto de base de datos (DB) desde el modulo principal de la aplicacion
# Definiremos esta /app/__init__.py el interior en las siguientes secciones.
from app import db

# Definir un modelo de usuario
class Usuario(db.Model):
    __tablename__   = 'usuario'
    id_usuario      = db.Column(db.Integer, primary_key=True)
    email           = db.Column(db.String(128),  nullable=False, unique=True)
    contrasenha     = db.Column(db.String(192),  nullable=False)
    nombre          = db.Column(db.String(128),  nullable=False)
    apellido        = db.Column(db.String(128),  nullable=False)
    is_active       = db.Column(db.SmallInteger,  nullable=True)
    id_tipo_usuario = db.Column(db.Integer, nullable=False)