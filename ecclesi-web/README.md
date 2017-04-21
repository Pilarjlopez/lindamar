# EcclesiApp - SistemaWeb
### Sitio Web de la Curia Arzobispal y Sistema de geolocalizacion de templos Catolicos en Nicaragua.

Lo siguiente es un pequeño startup para instalar y hacer funciona el citio web y el sistema de maneral local.

## Instala las dependenencias del sistema

Intalaciond de librerias, aplicacciones y frameworks necesarias por el sistema operativo.

Actualice su sistema operativo.

> Mageia

```bashscript
$ su -c "urpmi.update -a && urpmi --auto-select"
$ su -c "urpmi git python-pip python-mysql mariadb gcc gcc-c++ make cmake lib64python-devel"
```

> Fedora

```bashscript
$ su -c "dnf -y update"
$ su -c "dnf -y install git python-pip python2-mysql mariadb-server @development-tools python-devel python2-devel"
```

> Arch

```bashscript
$ su -c "pacman -Syu"
$ su -c "pacman -S git python-pip python-mysql-connector mariadb base-devel python python2"
```

## Clona o copia el repo

```bashscript
$ git clone https://github.com/lindamar/ecclesi.git
```

## Inicar el servidor de Base de Datos

```bashscript
$ cd ecclesi
```

> Solo para ArchLinux

```bashscript
# mysql_install_db --user=mysql --basedir=/usr --datadir=/var/lib/mysql
```

> En adelante para Mageia / Fedora / Arch

1. Iniciar el servidor

```bashscript
$ systemctl start mariadb
```

2. Configuracion basica

```bashscript
$ mysql_secure_installation
```

3. Crear y restaurar la base de datos

```bashscript
$ mysql -u root -p
> CREATE DATABASE ecclesiapp;
> QUIT
$ mysql -u root -p ecclesiapp < db/ecclesiapp.sql
```

## Instala las dependenencias de python

Accede al directorio del repo.

```bashscript
$ cd ecclesi-web
```

Y ejecuta el siguiente comando para instalar las depencias.

```bashscript
$ su -c "pip install -r requirements.txt"
```

## Generar el Entorno Virtual

```bashscript
$ su -c "virtualenv env"
```

## Ejecute el servidor de desarrollo

```bashscript
$ python run.py
```

Ahora solo basta con accesar a la direccion http://localhost:8080 desde su navegador web.
