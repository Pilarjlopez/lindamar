# Importar el objeto de base de datos (DB) desde el modulo principal de la aplicacion
# Definiremos esta /app/__init__.py el interior en las siguientes secciones.
from app import db

# Definir un modelo de usuario
class Usuario(db.Model):
    """
    An admin user capable of viewing reports.
    
    :param str email: email address of user
    :param str password: encrypted password for the user
    """
    __tablename__   = 'usuario'
    
    id_usuario      = db.Column(db.Integer, primary_key=True)
    email           = db.Column(db.String(128), nullable=False, unique=True)
    contrasenha     = db.Column(db.String(192), nullable=False)
    nombre          = db.Column(db.String(128), nullable=False)
    apellido        = db.Column(db.String(128), nullable=False)
    is_active       = db.Column(db.SmallInteger, nullable=True)
    id_tipo_usuario = db.Column(db.Integer, nullable=False)
    
    def is_active(self):
        """True, as all users are active."""
        return True
    
    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.email
    
    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.is_active
    
    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False
    
    def get_type(self):
        """Return the type od user authenticated."""
        return self.id_tipo_usuario 
    
# Definir un modelo de usuario
class Tipo_Usuario(db.Model):
    
    __tablename__   = 'tipo_usuario'
    
    id_tipo_usuario = db.Column(db.Integer, primary_key=True)
    tipo            = db.Column(db.String(128), nullable=False, unique=True)
    id_privilegio   = db.Column(db.Integer, nullable=False)
    
    def is_active(self):
        """True, as all users are active."""
        return True

# Definir un modelo de usuario
class Presbitero(db.Model):
    """
    An admin user capable of viewing reports.
    
    :param str email: email address of user
    :param str password: encrypted password for the user
    """
    __tablename__           = 'presbitero'
    
    id_presbitero           = db.Column(db.Integer, primary_key=True)
    nombre                  = db.Column(db.String(128), nullable=False)
    apellido                = db.Column(db.String(128), nullable=False)
    cane_confer             = db.Column(db.String(128), nullable=False, unique=True)
    nombre_popular          = db.Column(db.String(128), nullable=False)
    fecha_ordenacion        = db.Column(db.Integer, nullable=True)
    foto_portada            = db.Column(db.String(128), nullable=False)
    id_usuario              = db.Column(db.Integer, nullable=False)
    id_templo               = db.Column(db.Integer, nullable=False)
    id_oficio_eclesiastico  = db.Column(db.Integer, nullable=False)