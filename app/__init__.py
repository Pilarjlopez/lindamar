# Importar flask y plantillas de operadores
from flask import Flask, render_template

# Importar SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# Define el objeto de aplicacion WSGI
app = Flask(__name__)

# Configuraciones
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Import a module / component using its blueprint handler variable (mod_auth)
from app.mod_inicio.controllers import mod_inicio as inicio_module
from app.mod_auth.controllers import mod_auth as auth_module
from app.mod_curia.controllers import mod_curia as curia_module
from app.mod_ecclesi.controllers import mod_ecclesi as ecclesi_module

# Register blueprint(s)
app.register_blueprint(inicio_module)
app.register_blueprint(auth_module)
app.register_blueprint(curia_module)
app.register_blueprint(ecclesi_module)

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all() 
