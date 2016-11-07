#programa de control
from __future__ import print_function
import os
import ftplib
import datetime
import MySQLdb as mysql
import time
import lib.formato as formato


hostmysql="127.0.0.1"
usermysql="root"
passmysql=""
basemysql="fss1"
portmysql=3306
db = mysql.connect(hostmysql, usermysql, passmysql, basemysql, portmysql)
cursor=db.cursor()
cursor.execute("select version()")
data=cursor.fetchall()
print(data)
comando=""
lista=[(),()]
while comando<>"x":
	print("\n",end="")
	comando=raw_input("Comando: ")
	yx=cursor
########################################################
########################################################
	try:
		yx.execute(comando)
		lista=yx.fetchall()
		if lista:
			#print(type(lista))
			for registro in lista:
				#print(type(registro))
				print(registro,end="\n")
				#print("\n",end="")
				if (formato.tipovar(registro)=="tuple") or(formato.tipovar(registro)=="list"):
					for ss in registro:
						print(" %s " % ss,end="")
						#print(formato.tipovar(ss),ss)
					print("\n",end="")
				else:
					print(registro)
	except:
		print("Comando no reconocido")
