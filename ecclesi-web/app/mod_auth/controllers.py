# Importar las dependencias de flask
from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for

# Importar clave/ayudantes de encriptacion
from werkzeug import check_password_hash, generate_password_hash

# Importar el objeto de base de datos desde el modulo principal de la aplicacion
from app import db

# Importar modulo de formulario
from app.mod_auth.forms import LoginForm

# Importar modulo de usuario (i.e. User)
from app.mod_auth.models import User

# Definir el blueprint: 'auth', establecer el prefijo de la url: app.url/auth
mod_auth = Blueprint('auth', __name__, url_prefix='/auth')

# Establecer las rutas y metodos aceptados
@mod_auth.route('/signin/', methods=['GET', 'POST'])
def signin():
    # Si el formulario de acceso es mandado
    form = LoginForm(request.form)

    # Verificar el formulario de acceso
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        
        if user and check_password_hash(user.password, form.password.data):
            session['user_id'] = user.id
            flash('Welcome %s' % user.name)
            return redirect(url_for('auth.home'))
        
        flash('Wrong email or password', 'error-message')
        
    return render_template("auth/signin.html", form=form) 

@mod_auth.route('/nada/', methods=['GET', 'POST'])
def nada():
    passwd = "1234"
    pw_hash = generate_password_hash(passwd)
    return pw_hash