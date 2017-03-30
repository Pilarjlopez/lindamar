# EcclesiApp - SistemaWeb
### Sitio Web de la Curia Arzobispal y Sistema de geolocalizacion de templos Catolicos en Nicaragua.

Lo siguiente es un pequeño startup para instalar y hacer funciona el citio web y el sistema de maneral local.

## Instala las dependenencias del sistema

Intalaciond de librerias, aplicacciones y frameworks necesarias por el sistema operativo.

Actualice su sistema operativo.

* Mageia
```bashscript
$ su -c "urpmi.update -a && urpmi --auto-select"
$ su -c "urpmi -y git python-pip mariadb gcc gcc-c++ make cmake lib64python-devel"
```

* Fedora
```bashscript
$ su -c "dnf -y update"
$ su -c "dnf -y install git pip mariadb-server build-essential python-dev python2.7-dev"
```

## Clona o copia el repo

```bashscript
$ git clone https://github.com/lindamar/ecclesi.git
```

## Instala las dependenencias de python

Accede al directorio del repo.

```bashscript
$ cd ecclesi
$ cd ecclesi-web
```

Y ejecuta el siguiente comando para instalar las depencias.

```bashscript
$ pip install -r requirements.txt
```

## Ejecute el servidor de desarrollo

```bashscript
$ python run.py
```

Ahora solo basta con accesar a la direccion http://localhost:8080 desde su navegador web.
