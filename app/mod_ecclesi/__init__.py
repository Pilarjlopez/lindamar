# importar flask y los operadores de plantilla
from flask import Flask, render_template

# flask login
from flask_login import LoginManager

# Importar SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# Definir la aplicacion del objeto WSGI
app = Flask(__name__)

# Configuraciones
app.config.from_object('config')

login_manager = LoginManager()
login_manager.init_app(app)

# Definir el objeto de base de datos que se importa por modulos y controladores
db = SQLAlchemy(app)

# Ejemplo de manejo de error HTTP
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Importar a modulo / componente usando la variable de manejo blueprint (mod_auth)
from app.mod_ecclesi.controllers import mod_ecclesi as ecclesi_module

# Registrar blueprint(s)
app.register_blueprint(ecclesi_module)

# Construir la base de datos
# Esto debera crear un archivo usando SQLAlchemy
#db.create_all() 
