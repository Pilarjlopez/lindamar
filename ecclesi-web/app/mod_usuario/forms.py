# Formulario de importacion y RecaptchaField (opcional)
from flask_wtf import Form # , RecaptchaField

# Los elementos de formulario de importacion como de campo de texto y BooleanField (opcional)
from wtforms import TextField, PasswordField # BooleanField

#  Importacion de Validadores del formulario
from wtforms.validators import Required, Email, EqualTo

# Definir el formulario de acceso (WTForms)
class FormularioAcceso(Form):
    email    = TextField('Email Address', [Email(), Required(message='Olvido su direccion de correo electronico?')])
    password = PasswordField('Password', [Required(message='Debe de proveer una clave. ;-)')]) 

class PerfilUsuario(Form):
    nombre   = TextField('Nombre', [Required(message='El Nombre es requerido.')])
    apellido = TextField('Apellido', [Required(message='El Apellido es requerido.')])
    correo   = TextField('Correo Electronico', [Email(), Required(message='El Correo Electronico es requerido.')])
    contra   = TextField('Contrasena', [Required(message='La Contrasena es requerida.')])