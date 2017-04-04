# Formulario de importacion y RecaptchaField (opcional)
from flask_wtf import Form # , RecaptchaField

# Los elementos de formulario de importacion como de campo de texto y BooleanField (opcional)
from wtforms import StringField, BooleanField, StringField, PasswordField, SelectField

#  Importacion de Validadores del formulario
from wtforms.validators import Required, Email, EqualTo

# Definir el formulario de acceso (WTForms)
class FormularioAcceso(Form):
    email    = StringField('Correo Electronico', validators=[Email(), Required(message='Olvido su direccion de correo electronico?')])
    password = PasswordField('Contrase&ntilde;a', validators=[Required(message='Debe de proveer una clave. ;-)')]) 

class PerfilUsuario(Form):
    nombre   = StringField('Nombre', validators=[Required(message='El Nombre es requerido.')])
    apellido = StringField('Apellido', validators=[Required(message='El Apellido es requerido.')])
    correo   = StringField('Correo Electronico', validators=[Email(), Required(message='El Correo Electronico es requerido.')])
    contra   = StringField('Contrasena', validators=[Required(message='La Contrasena es requerida.')])

class NuevoUsuario(Form):
    nombre   	   	 = StringField('Nombre', validators=[Required(message='El Nombre es requerido.')])
    apellido 	   	 = StringField('Apellido', validators=[Required(message='El Apellido es requerido.')])
    correo   	   	 = StringField('Correo Electronico', validators=[Email(), Required(message='El Correo Electronico es requerido.')])
    contra   	   	 = StringField('Contrase&ntilde;a', validators=[Required(message='La Contrase&ntilde;a es requerida.')])
    nombre_popular 	 = StringField('Nombre Popular')
    carne_confer     = StringField('Carnet CONFER', validators=[Required(message='El Numero de Carnet es requeridoo.')])
    fecha_ordenacion = StringField('Fecha de Ordenacion')
    foto_portada 	 = StringField()

