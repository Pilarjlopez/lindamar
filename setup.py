from setuptools import setup

setup(
    name='ecclesiapp',
    packages=['app'],
    version=0.1,
    url='www.curiamagua.org',
    author='Linda Martinez y Rut Herrera',
    author_email='linda.castro@gmail.com',
    maintainer='Samuel Gutierrez',
    maintainer_email='search.sama@gmail.com',
    include_package_data=True,
    install_requires=[
        'virtualenv',
        'flask',
        'flask-sqlalchemy',
        'flask-login',
        'flask-wtf',
        'pymysql',
    ],
)