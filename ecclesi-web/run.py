# Ejecutar un servidor de prueba.
from app import app
app.run(host='192.168.123.4', port=8080, debug=True)