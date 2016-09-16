# Importar las dependencias de flask
from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for

# Importar clave / ayudantes de encriptacion
from werkzeug import check_password_hash, generate_password_hash

# Importar el objeto de base de datos desde el modulo principal de la aplicacion
from app import db

# Importar modulo de formulario
#from app.mod_curia.forms import LoginForm

# Importar modulo de usuario (i.e. User)
#from app.mod_curia.models import User

# Definir el blueprint: 'Curia', establecer el prefijo de la url: app.url/auth
mod_curia = Blueprint('curia', __name__, url_prefix='/curia')

# Establecer las rutas y metodos aceptados
@mod_curia.route('/inicio/', methods=['GET', 'POST'])
def inicio():
    return render_template("curia/inicio.html") 

@mod_curia.route('/obispos/', methods=['GET', 'POST'])
def obispos():
    return render_template("curia/obispos.html") 

@mod_curia.route('/arquidiocesis/', methods=['GET', 'POST'])
def arquidiocesis():
    return render_template("curia/arquidiocesis.html") 

@mod_curia.route('/parroquias/', methods=['GET', 'POST'])
def parroquias():
    return render_template("curia/parroquias.html") 

@mod_curia.route('/noticias/', methods=['GET', 'POST'])
def noticias():
    return render_template("curia/noticias.html") 

@mod_curia.route('/contacto/', methods=['GET', 'POST'])
def contacto():
    return render_template("curia/contacto.html")





