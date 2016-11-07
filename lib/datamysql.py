#proyecto mysql
#import os
import MySQLdb as mysql

# lista de conexiones conocidas
listconnect = [("127.0.0.1", "root", "", 3306),
("127.0.0.1", "root", "tovacompu", 3306),
("127.0.0.1", "visual", "tovacompu", 3306),
("127.0.0.1", "binsoft", "binsoft", 3306)]

# lista las bases de datos y devuelve una lista de estas
def listdatabases(conexion):
    cursor = conexion.cursor()
    cursor.execute("show databases")
    bases = cursor.fetchall()
    lista = []
    for l in bases:
        lista.append(l[0])
    return lista

# verificar si existe una base de datos, si existe
# devuelve 1, sino 0
def ifdatabase(conexion,database):
    estado = False
    cursor = conexion.cursor()
    cursor.execute("use information_schema")
    cursor.execute("select * from schemata where schema_name = %s" % database)
    bases = cursor.fetchall()
    if bases:
        estado = True
    return estado

# lista las tablas de una base de datos "database"
# y devuelve una lista de estas
def listtables(conexion, database):
    cursor = conexion.cursor()
    cursor.execute("use %s" % database)
    cursor.execute("show tables")
    tables = cursor.fetchall()
    lista = []
    for l in tables:
        lista.append(l[0])
    return lista

# verificar si existe una tabla en la base de
# datos "database", si existe devuelve 1, sino 0
def iftable(conexion, database, table):
    estado = False
    xd = database
    xt = table
    cursor = conexion.cursor()
    cursor.execute("use INFORMATION_SCHEMA")
    cursor.execute("""select * from TABLES where
                    TABLE_SCHEMA='%s' and
                    TABLE_NAME='%s' and
                    TABLE_TYPE='BASE TABLE'""" % (xd, xt))
    tables = cursor.fetchone()
    if tables:
        estado = True
    return estado