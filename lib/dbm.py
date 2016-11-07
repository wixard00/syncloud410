#programa de control
from __future__ import print_function
import os
import datetime
import MySQLdb as mysql
import time
import sqlite3


########################################################################
##################### MySQL ############################################

def mysqlcon(hostmysql="127.0.0.1",usermysql="root",
	passmysql="",basemysql="fss1",portmysql=3306):
	"""crea una conexion mysql"""
	db = mysql.connect(hostmysql, usermysql, passmysql, basemysql, portmysql)
	return db



########################################################################
#################### SQLITE ############################################

def sql3base(ruta):
	"""Crea una base sqlite """
	estado = 0
	try:
		con = sqlite3.connect(ruta)
		if con:
			estado = 1
	except:
		estado = 0
	return estado
	

########################################################################
#creacion de tabla tables
def sql3tables(ruta):
	"""Crea una tabla tables sqlite"""
	estado = 0
	try:
		con = sqlite3.connect(ruta)
		cursor = con.cursor()
		#cursor.execute('''create table tables(id int primary key not null)''')
		cursor.execute('''CREATE TABLE 'tables' (
					'id'	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
					'ntable'	varchar(50) NOT NULL UNIQUE)''')
		con.commit()
		estado = 1
	except:
		estado = 0
	return estado

########################################################################
#creacion de tabla fields
def sql3fields(ruta):
	"""Crea una tabla  fields sqlite"""
	estado = 0
	try:
		con = sqlite3.connect(ruta)
		cursor = con.cursor()
		cursor.execute('''CREATE TABLE 'fields' (
							'id'		int		NOT NULL,
							'field'		varchar(50)	NOT NULL,
							'type'		varchar(50)	NOT NULL,
							'null'		varchar(50)	NOT NULL,
							'key'		varchar(50),
							'default'	varchar(50),
							'extra'		varchar(50));''')
		con.commit()
		estado = 1
	except:
		estado = 0
	return estado


########################################################################
#insercion de registro en la tabla tables
def sql3regtables(ruta,_valor):
	"""Agrega un nuevo registro en la tabla tables"""
	estado = 0
	try:
		con = sqlite3.connect(ruta)
		cursor = con.cursor()
		cadenasql=""
		for nval in _valor:
			cursor.execute('''INSERT INTO tables (ntable) values (?)''',(nval))
		con.commit()
		estado = 1
	except:
		estado = 0
	return estado


########################################################################
#busqueda del valor id en la tabla tables del valor ntable
def sql3searchid(ruta,_valor):
	"""busqueda del valor id en la tabla tables del valor ntable"""
	value = 0
	#try:
	con = sqlite3.connect(ruta)
	cursor = con.cursor()
	cursor.execute('''select id from tables where ntable=?''',(_valor))
	value=cursor.fetchone()[0]
	#except:
		#value = 0
	return value
	

########################################################################
#insercion de registro en la tabla fields
def sql3regfields(ruta,_valor):
	"""Agrega un nuevo registro en la tabla fields"""
	estado = 0
	#try:
	con = sqlite3.connect(ruta)
	cursor = con.cursor()
	for n in _valor:
		cursor.execute('''INSERT INTO fields values (?,?,?,?,?,?,?)''',(n))
	con.commit()
	estado = 1
	#except:
		#estado = 0
	return estado


########################################################################
#actualizacion de registro
def searchreg(ruta, _id):
	"""Agrega un nuevo registro en la tabla fields"""
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


########################################################################
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


