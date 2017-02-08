# Importar las dependencias de flask
from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for

# importar flask login
from app import login_manager
from flask_login import (current_user, login_required, login_user, logout_user, confirm_login, fresh_login_required)

# Importar clave / ayudantes de encriptacion
from werkzeug import check_password_hash, generate_password_hash

# Importar el objeto de base de datos desde el modulo principal de la aplicacion
from app import db

# Importar modulo de formulario
from app.mod_usuario.forms import FormularioAcceso

# Importar modulo de modelos
from app.mod_ecclesi.models import Categoria

# Importar Modelos
from app.mod_usuario.models import Usuario

@login_manager.user_loader
def user_loader(user_id):
    """
    Given *user_id*, return the associated User object.
    :param unicode user_id: user_id (email) user to retrieve
    """
    return Usuario.query.filter_by(email=user_id).first()

# Definir el blueprint: 'auth', establecer el prefijo de la url: app.url/auth
mod_ecclesi = Blueprint('ecclesi', __name__, url_prefix='/ecclesi')

# Establecer las rutas y metodos aceptados
@mod_ecclesi.route('/descarga/', methods=['GET', 'POST'])
def descarga():
    session['visible'] = 0;
    form = FormularioAcceso(request.form)
    return render_template("ecclesi/inicio.html", form=form)

@mod_ecclesi.route('/prueba/', methods=['GET', 'POST'])
def prueba():
    cat = Categoria.query.filter_by(id_categoria=2).first()
    return render_template("ecclesi/prueba.html", cat=cat)

@mod_ecclesi.route('/templo/', methods=['GET', 'POST'])
@login_required
def templo():
    session['visible'] = 1;
    return render_template("ecclesi/registro.html")

@mod_ecclesi.route('/nueva/', methods=['GET', 'POST'])
def nueva():
    return render_template("ecclesi/nueva.html")