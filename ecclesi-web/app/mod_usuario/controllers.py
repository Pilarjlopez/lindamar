# Importar las dependencias de flask
from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for

# importar flask login
from app import login_manager
from flask_login import (current_user, login_required, login_user, logout_user, confirm_login, fresh_login_required)
from datetime import datetime, timedelta

# Importar clave / ayudantes de encriptacion
from werkzeug import check_password_hash, generate_password_hash

# Importar el objeto de base de datos desde el modulo principal de la aplicacion
from app import db

# Importar modulo de formulario
from app.mod_usuario.forms import PerfilUsuario
from app.mod_usuario.forms import FormularioAcceso
from app.mod_usuario.forms import NuevoUsuario

# Importar Modelos
from app.mod_usuario.models import Usuario
from app.mod_usuario.models import Tipo_Usuario
from app.mod_usuario.models import Presbitero
from app.mod_ecclesi.models import Templo
from app.mod_ecclesi.models import Oficio

@login_manager.user_loader
def user_loader(user_id):
    """
    Given *user_id*, return the associated User object.
    :param unicode user_id: user_id (email) user to retrieve
    """
    return Usuario.query.filter_by(email=user_id).first()

# Definir el blueprint: 'auth', establecer el prefijo de la url: app.url/auth
mod_usuario = Blueprint('usuario', __name__, url_prefix='/usuario')

# Establecer las rutas y metodos aceptados
@mod_usuario.route('/acceso/', methods=['GET', 'POST'])
def acceso():
    """
    For GET requests, display the login form. For POSTS, login the current user by processing the form.
    """
    form = FormularioAcceso(request.form)
    
    if form.validate_on_submit():
        user = Usuario.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.contrasenha, form.password.data):
            user.authenticated = True
            login_user(user, remember=True)
            session['usuario'] = user.email
            return redirect(url_for('usuario.perfil'))
        
    return redirect(url_for("ecclesi.descarga"))

@mod_usuario.route('/denegar/', methods=['GET', 'POST'])
@login_required
def denegar():
    logout_user()
    return redirect(url_for("ecclesi.descarga"))

@mod_usuario.route('/perfil/', methods=['GET', 'POST'])
@login_required
def perfil():
    session['visible'] = 1
    user = user_loader(session['usuario'])
    if user.id_tipo_usuario == 2:
        presbitero = Presbitero.query.filter_by(id_usuario=user.id_usuario).first()
        presbitero.fecha_ordenacion = datetime.fromtimestamp(presbitero.fecha_ordenacion).strftime('%d/%m/%Y')
        templo     = Templo.query.filter_by(id_templo=presbitero.id_templo).first()
        oficio     = Oficio.query.filter_by(id_oficio_eclesiastico=presbitero.id_oficio_eclesiastico).first()
        return render_template('ecclesi/presbitero/perfil.html', presbitero=presbitero, templo=templo, oficio=oficio)
    else:
        nuevo_usuario = NuevoUsuario()
        presbitero    = {'foto_portada':'person.svg'}
        tipo_usuario  = Tipo_Usuario.query.all()
        oficio        = Oficio.query.all()
        return render_template('ecclesi/usuario/perfil.html', presbitero=presbitero, tipo_usuario=tipo_usuario, oficio=oficio, nuevo_usuario=nuevo_usuario)

@mod_usuario.route('/nuevo/', methods=['GET', 'POST', 'HEAD'])
@login_required
def nuevo():
    form = request.form
    if form['tipo_usuario'] == 2:
        usuario = Usuario(form['email'], generate_password_hash(form['confer']), form['nombre'], form['apellido'], 1, form['tipo_usuario'])
        db.session.add(usuario)
        db.session.commit()
        usuario = Usuario.query(ObjectRes).order_by(ObjectRes.id.desc()).first()
        presbitero = Presbitero(usuario.nombre, usuario.apellido, form['confer'], form['popular'], form['ordenacion'], form['portada'], usuario.id_usuario, 0, form['oficio'])
        db.session.add(presbitero)
        db.session.commit()
    else:
        usuario = Usuario(form['email'], generate_password_hash(form['contrasehna']), form['nombre'], form['apellido'], 1, form['tipo_usuario'])
        db.session.add(usuario)
        db.session.commit()

    return usuario['id_usuario']
