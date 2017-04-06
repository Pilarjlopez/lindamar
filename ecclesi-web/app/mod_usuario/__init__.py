# importar flask y los operadores de plantilla
from flask import Flask, render_template

# flask login
from flask_login import LoginManager

# Importar SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# Importar FireBase
from firebase import firebase

# Definir la aplicacion del objeto WSGI
app = Flask(__name__)

# Configuraciones
app.config.from_object('config')

# Definir el objeto de base de datos que se importa por modulos y controladores
db = SQLAlchemy(app)

# Definir la coneccion a los nodos de FireBase
firebase = firebase.FirebaseApplication('https://ecclesiapp-fe5b2.firebaseio.com', None)

login_manager = LoginManager()
login_manager.init_app(app)

# Ejemplo de manejo de error HTTP
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Importar a modulo / componente usando la variable de manejo blueprint (mod_usuario)
from app.mod_usuario.controllers import mod_usuario as usuario_module

# Registrar blueprint(s)
app.register_blueprint(usuario_module)
