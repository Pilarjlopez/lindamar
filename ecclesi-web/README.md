# EcclesiApp - SistemaWeb
### Sitio Web de la Curia Arzobispal y Sistema de geolocalizacion de templos Catolicos en Nicaragua.

Lo siguiente es un pequeño startup para instalar y hacer funciona el citio web y el sistema de maneral local.

## Instala las dependencias del sistema

Intalaciond de librerias, aplicacciones y frameworks requeridas por el sistema operativo.

1. Actualice su sistema operativo.

> Mageia

```bashscript
$ sudo urpmi.update -a && urpmi --auto-select
```

> Fedora

```bashscript
$ su -c "dnf -y update"
```

> Arch

```bashscript
$ su -c "pacman -Syu"
```

2. Instalar dependencias del sistema operativo

> Mageia

```bashscript
$ sudo urpmi git python-pip python-mysql mariadb gcc gcc-c++ make cmake lib64python-devel
```

> Fedora

```bashscript
$ su -c "dnf -y install git python-pip python2-mysql mariadb-server @development-tools python-devel python2-devel"
```

> Arch

```bashscript
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

1. Iniciar el servidor

> Mageia

```bashscript
$ systemctl start mysqld
```

> Fedora

```bashscript
$ systemctl start mysqld
```

> Arch

```bashscript
$ systemctl start mysqld
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

## Instala las dependencias de python

1. Accede al directorio del sistema web.

```bashscript
$ cd ecclesi-web
```

2. Instalar las dependencias de flask.

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
