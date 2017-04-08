# Sentencia para hablitar el modo de desarrollo
DEBUG = True

# Declaracion para el entorno de desarrollo
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Declaracion de mandato de datos
import signal

# Definir la base de datos - estamos trabajando con
USR  = "root"
PWD  = "root"
DBN  = "ecclesiapp"

# MySQL coneccion con base de datos
SQLALCHEMY_DATABASE_URI = 'mysql://{}:{}@localhost/{}'.format(USR, PWD, DBN)

SQLALCHEMY_TRACK_MODIFICATIONS = True
DATABASE_CONNECT_OPTIONS = {}

# String de connecion para FireBase
#FIREBASE_URL = ('https://ecclesiapp-fe5b2.firebaseio.com/', None)
FIREBASE_URL = ('https://ecclesiapp-fe5b2.firebaseio.com', None)

# Hilos de la aplicacion. Una suposicion general comun es 
# usar 2 por nucleos de procesamiento disponibles - para manejar 
# las peticiones entrantes utilizando uno y la realizacion de 
# operaciones en segundo plano utilizando la otra.
THREADS_PER_PAGE = 2

# Habilitar la proteccion contra *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = True

# Utilizar una clave segura, unica y absolutamente privada para firmar los datos.
CSRF_SESSION_KEY = "secret"

# clave secreta para las cookies
SECRET_KEY = "secret" 