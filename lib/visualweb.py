#programa de control
from __future__ import print_function
import os
import ftplib
import datetime
import comlib
import MySQLdb as mysql
import time

import registro
import monolib
import dataconnect
import formato
#import datamysql

def cargarbases():
	rutacen = monolib.validapath(registro._locatesyncloud())
	rutabase = rutacen + "configuracion/system.db"
	while True:
	#ruta de sistema centinela
			nbd = 0
			narc = 0
			statefilesql = 0
	##########################################################################################
	#variables de envio FTP
	##########################################################################################
	#datos servidor ftp
			enterprise = dataconnect.searchreg(rutabase, "enterprise")
			hostftp = dataconnect.searchreg(rutabase, "siteftp2")
			portftp = 21
			userftp = dataconnect.searchreg(rutabase, "userftp2")
			passftp = dataconnect.searchreg(rutabase, "passftp2")
			hostmysql = dataconnect.searchreg(rutabase, "hostmysql")
			usermysql = dataconnect.searchreg(rutabase, "usermysql")
			passmysql = dataconnect.searchreg(rutabase, "passmysql")
	###############################################################################
	###########################################################################################
	#variables de respaldo BD
	###########################################################################################
	###############################################################################
	#lista de tablas a respaldar
			listabd = monolib.listtablesbackup(monolib.loadlist(rutacen + "configuracion/tablelist.txt"))
	###############################################################################
			fecha = datetime.datetime.now()
	###############################################################################
	#validacion de usuario mysql
			mysqlvalid = ("-h %s -u %s " % (hostmysql, usermysql))
			if passmysql:
					mysqlvalid = ("%s -p%s" % (mysqlvalid, passmysql))
	###############################################################################
	#comando dump
			comandodump = ("mysqldump.exe %s --skip-lock-tables --skip-comments " % mysqlvalid)
	#comando check
			comandocheck = ("mysqlcheck.exe %s --auto-repair --silent --databases " % mysqlvalid)
	###############################################################################
	#ruta de compresor 7Z
			ruta7z = rutacen + "bin/" + "7z.exe"
	#ruta de archivos .7Z
			archivado = rutacen + "temp/visualweb/zip/"
	###############################################################################
	#ruta de archivos .SQL
			respaldo = rutacen + "temp/visualweb/sql/"
	#bases de datos a respaldar
			rutabd = registro._mysqldata()
	###############################################################################
	#comando para respaldar base de datos
			myd = rutacen + "bin/" + comandodump
	#comando para reparar BD
			repararbd = rutacen + "bin/" + comandocheck
	###############################################################################
	#nombre de archivo para respaldar
			arczip = comlib.nomarc(enterprise + "-", fecha, "")
	#ruta de archivo para respaldar
			resbdzip = archivado + arczip
	##########################################################################################
	#						 I N I C I O  D E L   P R O G R AM A																				#
	##########################################################################################
			os.system("cls")
			print("================================ L o a d B D =================================")
			print("Proceso de respaldo de BD iniciado en ", sep="", end="")
			print(formato.formatohora(fecha))
	###############################################################################
	#Listando archivos y carpetas en /data/
			if passmysql:
					passmysql = ("-p%s" % passmysql)
			db = mysql.connect(hostmysql, usermysql, passmysql,)
			cursor = db.cursor()
			bases = monolib.loadlist(rutacen + "configuracion/bdlist.txt")
	#lista = os.listdir(rutabd)
	#reparando y respaldando las BD en archivos
	#en la ruta "respaldo", omitiendo archivos
			for ix in bases:
					i = ix[0]
					nombre_sql = ix[1]
					if i:
							try:
									db = mysql.connect(hostmysql, usermysql, passmysql, i)
									spacio = ""
									for x in range(len(i), 30):
											spacio = spacio + " "
									print ("BD  " + i + spacio, sep="", end="")
									print ("Reparando >> ", sep="", end="")
									os.system(repararbd + i)
									estatefilesql = monolib.createfilesql(respaldo, nombre_sql + "-" + arczip, nombre_sql)
									print("Respaldando >> ", sep="", end="")
									if estatefilesql:
											os.system(myd + i + " --tables " + listabd + " >> " + respaldo + nombre_sql + "-" + arczip)
									else:
											print("No se pudo crear el archivo %s" % i)
									nbd = nbd + 1
									db.close()
									print (" Ok")
							except:
									print(i + " no es una BD MySQL valida")
									try:
											os.remove(respaldo + i)
									except:
											print ("El archivo " + i + "no ha podido ser removido")
							narc = narc + 1
	###############################################################################
			print ("Bases de datos Mysql respaldadas        : " + str(nbd))
			print ("Numero de archivos no BD no respaldados : " + str(narc))
	###############################################################################
	#############################################################################
	#Comprimiendo los respaldo .SQL en un archivo .7Z en la ruta "archivado"
	#############################################################################
			lista = os.listdir(respaldo)
			print ("")
			print (">> Comprimiendo a archivo >> " + arczip)
			comandzip = ruta7z + " a -mx9 -m0=PPmd -mo=32 -mmem=256m " + archivado + arczip
			comandzip = comandzip + " " + respaldo + "*"
	#print (comandzip)
			os.system(comandzip)
	# for i in lista:
	# comandzip=ruta7z+" a "+archivado+arczip+" "+respaldo+i
	# os.system(comandzip)
			print("")
			print("")
			state_del = os.system("")
			for xxx in lista:
					os.chdir(respaldo)
					print ("Eliminando archivo ", sep="", end="")
					try:
							print("%s " % xxx, sep="", end="")
							state_del = os.remove("%s" % xxx)
							if not state_del:
									print ("Ok ")
							else:
									print ("\nError al Eliminar el archivo %s >> %s" % (xxx, state_del))
					except:
							print ("\nError al Eliminar el archivo %s >> %s" % (xxx, state_del))
			print("")
	###############################################################################
	#								 E n v i a n d o   v i a   F T P
	###############################################################################
	###############################################################################
	##ABRIR CONEXION CON EL SERVIDOR
			arc_trans = ""
			try_transfer = 0
			transfer_sucess = 1
			while transfer_sucess:
					print ("Creando conexion con servidor FTP...")
					ftpconnect = ftplib.FTP()
					print ("Abriendo conexion...")
					ftpconnect.connect(hostftp, portftp, -999)
					print ("Verificando usuario con servidor FTP...")
					ftpconnect.login(userftp, passftp, "")
					print (ftpconnect.getwelcome())
					filetrans = archivado + arczip + ".7z"
					print ("Iniciando transferencia...")
					complete_cero = ""
					try:
							arc_env = open(filetrans, "rb")
							print ("Archivo listo para transferir")
							ftpconnect.cwd("/")
							try:
									print ("Transfiriendo archivo %s.7z" % arczip)
									arc_trans = arczip
#aqui se completa con ceros el numero de intento de envio
									if try_transfer < 10:
										complete_cero = "0000"
									else:
										if try_transfer < 100:
											complete_cero = "000"
										else:
											if try_transfer < 1000:
												complete_cero = "00"
											else:
												if try_transfer < 10000:
													complete_cero = "0"
												else:
													complete_cero = ""
##############################################################
									arc_trans = ("%s_%s%s" % (arczip, complete_cero, try_transfer))
									print (arc_trans)
									ftpconnect.storbinary('STOR ' + arc_trans, arc_env)
									ftpconnect.rename(arc_trans, ("%s.7z" % arc_trans))
									arc_env.close()
									ftpconnect.quit()
									print("Archivo transferido exitosamente...")
									transfer_sucess = 0
							except:
									print("No se ha podido enviar el archivo al servidor FTP\n\n")
									print("Reiniciando transferencia FTP")
					except:
							print("No se ha podido leer archivo a transferir")
					try_transfer = try_transfer + 1
	###############################################################################
			#ftpconnect = ftplib.FTP()
			#ftpconnect.connect(hostftp, portftp, -999)
			#ftpconnect.login(userftp, passftp, "")
			#ftpconnect.rename(arc_trans, ("%s.7z" % arc_trans))
			#arc_env.close()
			#ftpconnect.quit()
			print ("Servicio finalizado")
			print("")
			print("")
			#
			#
	#Mostrando hora de inicio y hora final
			print("Proceso de respaldo de BD SQL iniciado  : ", sep="", end="")
			print(formato.formatohora(fecha))
			print("Proceso de respaldo de BD SQL finalizado: ", sep="", end="")
			print(formato.formatohora(datetime.datetime.now()))
			time.sleep(3600 * 5)
	################
	