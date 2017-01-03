# Importar las dependencias de flask
from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for

# Importar clave / ayudantes de encriptacion
from werkzeug import check_password_hash, generate_password_hash

# Importar el objeto de base de datos desde el modulo principal de la aplicacion
from app import db

# Importar modulo de formulario
#from app.mod_curia.forms import LoginForm

# Importar modulo de modelos
from app.mod_ecclesi.models import Categoria

# Definir el blueprint: 'auth', establecer el prefijo de la url: app.url/auth
mod_ecclesi = Blueprint('ecclesi', __name__, url_prefix='/ecclesi')

# Establecer las rutas y metodos aceptados
@mod_ecclesi.route('/descarga/', methods=['GET', 'POST'])
def descarga():
    return render_template("ecclesi/inicio.html")

@mod_ecclesi.route('/prueba/', methods=['GET', 'POST'])
def prueba():
    cat = Categoria.query.filter_by(id_categoria=2).first()
    return render_template("ecclesi/prueba.html", cat=cat)

@mod_ecclesi.route('/registro/', methods=['GET', 'POST'])
def registro():
    return render_template("ecclesi/registro.html")

@mod_ecclesi.route('/nueva/', methods=['GET', 'POST'])
def nueva():
    return render_template("ecclesi/nueva.html")

