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

# Definir el blueprint: 'Curia', establecer el prefijo de la url: app.url/curia
mod_curia = Blueprint('curia', __name__, url_prefix='/curia')

# Establecer las rutas y metodos aceptados

### Rutas del menu principal

@mod_curia.route('/inicio/', methods=['GET', 'POST'])
def inicio():
    return render_template("curia/inicio.html") 

@mod_curia.route('/obispos/', methods=['GET', 'POST'])
def obispos():
    return render_template("curia/obispos.html") 

@mod_curia.route('/noticias/', methods=['GET', 'POST'])
def noticias():
    return render_template("curia/noticias.html") 

@mod_curia.route('/contacto/', methods=['GET', 'POST'])
def contacto():
    return render_template("curia/contacto.html")

### Rutas del menu de arquidocesis

@mod_curia.route('/arquidiocesis/catedral/', methods=['GET', 'POST'])
def catedral():
    return render_template("/curia/arquidiocesis/catedral.html") 

@mod_curia.route('/arquidiocesis/santuario-diocesano/', methods=['GET', 'POST'])
def santuario_dio():
    return render_template("/curia/arquidiocesis/santuario-diocesano.html") 

@mod_curia.route('/carquidiocesis/seminario-diocesano/', methods=['GET', 'POST'])
def seminario_diocesano():
    return render_template("/curia/arquidiocesis/seminarios-diocesanos.html") 

@mod_curia.route('/arquidiocesis/vicario-pastoral/', methods=['GET', 'POST'])
def vicario_pastoral():
    return render_template("/curia/arquidiocesis/vicario-pastoral.html")

### Rutas del menu de curia arzobispal

@mod_curia.route('/curia-arzobispal/consejo-gobierno/', methods=['GET', 'POST'])
def consejo_gobierno():
    return render_template("/curia/curia-arzobispal/consejo-gob.html") 

@mod_curia.route('/curia-arzobispal/colegio-consultores/', methods=['GET', 'POST'])
def colegio_consultores():
    return render_template("/curia/curia-arzobispal/colegio-consul.html") 

@mod_curia.route('/curia-arzobispal/consejo-pastoral/', methods=['GET', 'POST'])
def consejo_pastoral():
    return render_template("/curia/curia-arzobispal/consejo-pas.html") 

@mod_curia.route('/curia-arzobispal/tribunal-ecle/', methods=['GET', 'POST'])
def tribunal_ecle():
    return render_template("/curia/curia-arzobispal/tribunal-ecle.html") 

@mod_curia.route('/curia-arzobispal/consejo-presbiteral/', methods=['GET', 'POST'])
def consejo_presbiteral():
    return render_template("/curia/curia-arzobispal/consejo-presbiteral.html") 

### Parte de parroquias del menu parroquias 

@mod_curia.route('/parroquias/zona-central/', methods=['GET', 'POST'])
def zona_c():
    return render_template("curia/parroquias/zona-central.html")

@mod_curia.route('/parroquias/zona-oriental/', methods=['GET', 'POST'])
def zona_or():
    return render_template("curia/parroquias/zona-oriental.html") 

@mod_curia.route('/parroquias/zona-occidental/', methods=['GET', 'POST'])
def zona_oc():
    return render_template("curia/parroquias/zona-occidental.html") 

@mod_curia.route('/parroquias/masaya/', methods=['GET', 'POST'])
def masaya():
    return render_template("/curia/parroquias/masaya.html") 

@mod_curia.route('/parroquias/carazo/', methods=['GET', 'POST'])
def carazo():
    return render_template("curia/parroquias/carazo.html") 