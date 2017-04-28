
# Importar las dependencias de flask
from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for

# importar flask login
from app import login_manager
from flask_login import (current_user, login_required, login_user, logout_user, confirm_login, fresh_login_required)

# Importar clave / ayudantes de encriptacion
from werkzeug import check_password_hash, generate_password_hash

# Importar FireBase
#from pyfirebase import Firebase

# Definir la coneccion a los nodos de FireBase
#firebase = Firebase('https://ecclesiapp-fe5b2.firebaseio.com/')

# Importar el objeto de base de datos desde el modulo principal de la aplicacion
from app import db

# Importar modulo de formulario
from app.mod_usuario.forms import FormularioAcceso

# Importar modulo de modelos
from app.mod_ecclesi.models import Templo
from app.mod_ecclesi.models import Municipio
from app.mod_ecclesi.models import Zona_Parroquial
from app.mod_ecclesi.models import Diocesis
from app.mod_ecclesi.models import Noticia
from app.mod_ecclesi.models import Categoria
from app.mod_ecclesi.models import Galeria
from app.mod_ecclesi.models import Foto
from app.mod_ecclesi.models import Actividad
from app.mod_ecclesi.models import Tipo_Actividad
from app.mod_ecclesi.models import Servicio_Religioso
from app.mod_ecclesi.models import Horario
from app.mod_usuario.models import Usuario
from app.mod_usuario.models import Presbitero

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
    contenido = {}
    session['visible'] = 0
    form = FormularioAcceso(request.form)
    presbitero = {'foto_portada':'ecclesi_marcador.svg'}
    if 'usuario' in session:
        user = user_loader(session['usuario'])
        if user.id_tipo_usuario == 2:
            presbitero = Presbitero.query.filter_by(id_usuario=user.id_usuario).first()

    return render_template("ecclesi/inicio.html", form=form, presbitero=presbitero)

@mod_ecclesi.route('/prueba/', methods=['GET', 'POST'])
def prueba():
    cat = Categoria.query.filter_by(id_categoria=2).first()
    return render_template("ecclesi/prueba.html", cat=cat)

@mod_ecclesi.route('/templo/', methods=['GET', 'POST'])
@login_required
def templo():
    session['visible'] = 1

    presbitero = {'foto_portada':'ecclesi_marcador.svg'}
    if 'usuario' in session:
        user = user_loader(session['usuario'])
        if user.id_tipo_usuario == 2:
            presbitero = Presbitero.query.filter_by(id_usuario=user.id_usuario).first()

    templo = db.session.query(Templo, Municipio, Zona_Parroquial, Categoria, Galeria, Servicio_Religioso).join(Templo.municipio, Templo.zona_parroquial, Templo.categoria, Templo.galeria, Templo.servicio_religioso).filter(Templo.id_templo == presbitero.id_templo).order_by(Templo.id_templo).first()

    actividad           = Actividad.query.filter_by(id_templo=templo.Templo.id_templo);
    tipo_actividad      = Tipo_Actividad.query.all()
    servicio_religioso  = Servicio_Religioso.query.all()
    municipio           = Municipio.query.filter_by(id_departamento=1).all()
    categoria           = Categoria.query.all()

    return render_template("ecclesi/templo/templo.html", presbitero=presbitero, templo=templo, municipio=municipio, categoria=categoria, actividad=actividad, tipo_actividad=tipo_actividad,servicio_religioso=servicio_religioso)

@mod_ecclesi.route('/guardar_templo/', methods=['GET', 'POST'])
@login_required
def guardar_templo():
    pp = pprint.PrettyPrinter(indent=4)
    form  = request.form
    return form['popular']

@mod_ecclesi.route('/usuario/', methods=['GET', 'POST'])
@login_required
def usuario():
    return redirect(url_for("usuario.perfil"))

@mod_ecclesi.route('/zona-pastoral/', methods=['GET', 'POST'])
@login_required
def zpastoral():
    session['visible'] = 1
    return render_template("ecclesi/zona-pastoral.html")

@mod_ecclesi.route('/diocesis/', methods=['GET', 'POST'])
@login_required
def diocesis():
    session['visible'] = 1

    presbitero = {'foto_portada':'ecclesi_marcador.svg'}
    if 'usuario' in session:
        user = user_loader(session['usuario'])
        if user.id_tipo_usuario == 2:
            presbitero = Presbitero.query.filter_by(id_usuario=user.id_usuario).first()

    return render_template("ecclesi/admin/admin_diocesis.html", presbitero=presbitero)

@mod_ecclesi.route('/noticia/', methods=['GET', 'POST'])
@login_required
def noticia():
    session['visible'] = 1

    presbitero = {'foto_portada':'ecclesi_marcador.svg'}
    if 'usuario' in session:
        user = user_loader(session['usuario'])
        if user.id_tipo_usuario == 2:
            presbitero = Presbitero.query.filter_by(id_usuario=user.id_usuario).first()

    return render_template("ecclesi/admin/admin_noticias.html", presbitero=presbitero)

@mod_ecclesi.route('/actividad/', methods=['GET', 'POST'])
@login_required
def actividad():
    session['visible'] = 1
    return render_template("ecclesi/actividades.html")

@mod_ecclesi.route('/noticia_nueva/', methods=['GET', 'POST'])
@login_required
def noticia_nueva():
    form = request.form
    db.session.add(Noticia(form['titulo'], form['noticia'], '', form['id_templo']))
    db.session.commit()
    db.session.flush()
    return redirect(url_for("ecclesi.templo"))

@mod_ecclesi.route('/actividad_nueva/', methods=['GET', 'POST'])
@login_required
def actividad_nueva():
    form = request.form
    db.session.add(Actividad(form['nombre'], form['dia'], form['hora'], form['descripcion'], form['id_templo'], form['id_tipo_actividad']))
    db.session.commit()
    db.session.flush()
    return redirect(url_for("ecclesi.templo"))
