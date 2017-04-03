# Formulario de importacion y RecaptchaField (opcional)
from flask_wtf import Form # , RecaptchaField

# Los elementos de formulario de importacion como de campo de texto y BooleanField (opcional)
from wtforms import StringField, BooleanField, StringField, PasswordField, SelectField

#  Importacion de Validadores del formulario
from wtforms.validators import Required, Email, EqualTo

# Definir el formulario de acceso (WTForms)
class FormularioAcceso(Form):
    email    = StringField(u'Correo Electronico', validators=[Email(), Required(message='Olvido su direccion de correo electronico?')])
    password = PasswordField(u'Contrase&ntilde;a', validators=[Required(message='Debe de proveer una clave. ;-)')]) 

class PerfilUsuario(Form):
    nombre   = StringField(u'Nombre', validators=[Required(message='El Nombre es requerido.')])
    apellido = StringField(u'Apellido', validators=[Required(message='El Apellido es requerido.')])
    correo   = StringField(u'Correo Electronico', validators=[Email(), Required(message='El Correo Electronico es requerido.')])
    contra   = StringField(u'Contrasena', validators=[Required(message='La Contrasena es requerida.')])

class NuevoUsuario(Form):
    nombre   	   	 = StringField(u'Nombre', validators=[Required(message='El Nombre es requerido.')])
    apellido 	   	 = StringField(u'Apellido', validators=[Required(message='El Apellido es requerido.')])
    correo   	   	 = StringField(u'Correo Electronico', validators=[Email(), Required(message='El Correo Electronico es requerido.')])
    contra   	   	 = StringField(u'Contrase&ntilde;a', validators=[Required(message='La Contrase&ntilde;a es requerida.')])
    nombre_popular 	 = StringField(u'Nombre Popular')
    carne_confer     = StringField(u'Carnet CONFER', validators=[Required(message='El Numero de Carnet es requeridoo.')])
    fecha_ordenacion = StringField(u'Fecha de Ordenacion')
    foto_portada 	 = StringField()

