from setuptools import setup

setup(
    name='ecclesiapp',
    packages=['app'],
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