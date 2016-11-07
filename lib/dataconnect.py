#proyecto sqlite
#import os
import sqlite3


#creation de base de datos
def createbase(ruta):
    estado = 0
    try:
        con = sqlite3.connect(ruta)
        estado = 1
    except:
        estado = 0
    return estado


#creation de tabla
def createtables(ruta):
    estado = 0
    try:
        con = sqlite3.connect(ruta)
        cursor = con.cursor()
        cursor.execute('''create table setup(
                        id           varchar(50)     primary key    not null,
                        valor        varchar(500)    not null)''')
        con.commit()
        estado = 1
    except:
        estado = 0
    return estado


#insercion de registro
def createreg(ruta, _id, _valor):
    estado = 0
    try:
        con = sqlite3.connect(ruta)
        cursor = con.cursor()
        cursor.execute('''INSERT INTO setup (id,valor) values(?,?)''', (_id, _valor))
        con.commit()
        estado = 1
    except:
        estado = 0
    return estado


#actualizacion de registro
def searchreg(ruta, _id):
    estado = ""
    try:
        con = sqlite3.connect(ruta)
        cursor = con.cursor()
        cursor.execute('''SELECT * FROM setup WHERE id=(?)''', (_id,))
        row = cursor.fetchone()
        estado = row[1]
    except:
        estado = ""
    return estado

#actualizacion de registro
def existreg(ruta, _id):
    estado = 0
    try:
        con = sqlite3.connect(ruta)
        cursor = con.cursor()
        cursor.execute('''SELECT * FROM setup WHERE id=(?)''', (_id,))
        if cursor.fetchone():
            estado = 1
    except:
        estado = 0
    return estado

#actualizacion de registro
def updatereg(ruta, _id, _valor):
    estado = 0
    try:
        con = sqlite3.connect(ruta)
        cursor = con.cursor()
        cursor.execute('''UPDATE setup set valor=(?) where id=(?)''', (_valor, _id))
        con.commit()
        estado = 1
    except:
        estado = 0
    return estado
