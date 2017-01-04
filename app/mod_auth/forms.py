# Formulario de importacion y RecaptchaField (opcional)
from flask_wtf import FlaskForm # , RecaptchaField

# Los elementos de formulario de importacion como de campo de texto y BooleanField (opcional)
from wtforms import TextField, PasswordField # BooleanField

# Validadores del formulario de importacion
from wtforms.validators import Required, Email, EqualTo


# Definir el formulario de acceso (WTForms)
class LoginForm(FlaskForm):
    email    = TextField('Email Address', [Email(), Required(message='Olvido su direccion de correo electronico?')])
    password = PasswordField('Password', [Required(message='Debe de proveer una clave. ;-)')]) 
