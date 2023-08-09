import mysql.connector
from mysql.connector import errors
import config

def conectar():
    """Conectar con la base de datos y devolver un obj conexion."""
    try:
        conn = mysql.connector.connect(**config.credenciales)
    except errors.DatabaseError as err:
        print("Error al conectar.", err)
    else:
        return conn

def create_if_not_exists():
    """Crea la base de datos y la tabla si no existen.
    
    Esto asegura que la aplicacion funcione aunque no
    exista la base de datos previamente.
    Si es necesario que exista el usuario (con sus respectivos permisos)
    en el servidor.
    """
    create_database = "CREATE DATABASE IF NOT EXISTS %s" %config.credenciales["database"]
    create_table1 = """CREATE TABLE IF NOT EXISTS usuarios (
                            id INT unsigned PRIMARY KEY AUTO_INCREMENT,
                            nombre VARCHAR(50) NOT NULL,
                            apellido VARCHAR(50) NOT NULL,
                            alias varchar(50) not null,
                            fechas_nacimiento date not null,
                            correo VARCHAR(100) NOT NULL,
                            contrasena VARCHAR(100) NOT NULL
                        )engine InnoDB;"""
    create_table2 = """CREATE TABLE IF NOT EXISTS """
    try:
        conn = mysql.connector.connect(user=config.credenciales["user"],
                                       password=config.credenciales["password"],
                                       host="127.0.0.1")
        cur = conn.cursor()
        cur.execute(create_database)
        cur.execute("USE %s" %config.credenciales["database"])
        cur.execute(create_table2)
        cur.execute(create_table1)
        conn.commit()
        conn.close()
    except errors.DatabaseError as err:
        print("Error al conectar o crear la base de datos.", err)
        raise