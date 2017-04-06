# importar flask y los operadores de plantilla
from flask import Flask, render_template

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

# Ejemplo de manejo de error HTTP
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Importar a modulo / componente usando la variable de manejo blueprint (mod_auth)
from app.mod_auth.controllers import mod_auth as auth_module

# Registrar blueprint(s)
app.register_blueprint(auth_module)
# app.register_blueprint(xyz_module)
# ..

# Construir la base de datos
# Esto debera crear un archivo usando SQLAlchemy
#db.create_all() 
