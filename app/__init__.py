# Importar flask y plantillas de operadores
from flask import Flask, render_template

# flask login
from flask_login import LoginManager

# Importar SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# Define el objeto de aplicacion WSGI
app = Flask(__name__)

# Configuraciones
app.config.from_object('config')

login_manager = LoginManager()
login_manager.init_app(app)

# Define el objeto de base de datos que se desea importar
# por los modulos y controloadores
db = SQLAlchemy(app)

# Ejemplo de como hacerse cargo de un error HTTP
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(401)
def not_found(error):
    return render_template('401.html'), 401

# Importar modulo/componente usando la su variable (mod_auth)  del blueprint
from app.mod_inicio.controllers import mod_inicio as inicio_module
from app.mod_auth.controllers import mod_auth as auth_module
from app.mod_curia.controllers import mod_curia as curia_module
from app.mod_ecclesi.controllers import mod_ecclesi as ecclesi_module
from app.mod_usuario.controllers import mod_usuario as usuario_module

# Registrar blueprint(s)
app.register_blueprint(inicio_module)
app.register_blueprint(auth_module)
app.register_blueprint(curia_module)
app.register_blueprint(ecclesi_module)
app.register_blueprint(usuario_module)

# Construlledo la base de datos
# Esto creara una base de datos usando SQLAlchemy
#db.create_all() 
