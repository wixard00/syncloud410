# -*- encoding: utf-8 -*-
#programa de control
from __future__ import print_function
import os
#import ftplib
import datetime
import MySQLdb as mysql
import time

import comlib
import registro
import monolib
import dataconnect
import formato
import ftp
import handlemysql



##################################################################################
##################################################################################
##################################################################################
class gensqlfile():
	"""Esta es la clase que permite obtener respaldos de las bases de datos mysql en archivos .SQL"""

##################################################################################
	def __init__(self,rutafolder=os.getcwd(),
		configdic={'hostmysql':'127.0.0.1','usermysql':'root','passmysql':'','portmysql':3306,'basemysql':''},
		exefolder="bin/",tempsql="temp/syncloud/sql/",tempzip="temp/syncloud/zip/",debugmode=False):
		"""Metodo inicial de syncloud 4"""
######Aqui se define donde se encuentra la ruta del sistema
		self.__rutacen = monolib.validapath(rutafolder)
		#Aqui se definen los parametros de conexion MySQL
		self.__hostmysql=configdic['hostmysql']
		self.__usermysql=configdic['usermysql']
		self.__passmysql=configdic['passmysql']
		self.__portmysql=configdic['portmysql']
		self.__basemysql=configdic['basemysql']
		#variables de respaldo BD
		self.__fecha = datetime.datetime.now()
		self.__initmysqlcon()
		self.__mysqlvalid = ("-h '%s' -u '%s' " % (self.__hostmysql, self.__usermysql))
		if self.__passmysql:
			self.__mysqlvalid = ("%s -p%s" % (self.__mysqlvalid, self.__passmysql))
		#comando dump
		#comandodump = ("mysqldump.exe %s --skip-lock-tables --skip-comments --databases " % mysqlvalid)
		self.__c_dump_inodb = ("mysqldump.exe %s --skip-comments --databases " % self.__mysqlvalid)
		self.__c_dump_mysam = ("mysqldump.exe %s --skip-lock-tables --skip-comments --databases " % self.__mysqlvalid)
		#comando check
		self.__comandocheck = ("mysqlcheck.exe %s --auto-repair --silent --databases " % self.__mysqlvalid)
		#ruta de archivos .SQL
		self.__respaldo = self.__rutacen + tempsql
		#comando para RESPALDAR base de datos
		self.__c_dump_inodb = self.__rutacen + exefolder + self.__c_dump_inodb
		self.__c_dump_mysam = self.__rutacen + exefolder + self.__c_dump_mysam
		#comando para REPARAR BD
		self.__repararbd = self.__rutacen + exefolder + self.__comandocheck
		#Aqui se activa la funcion de ver modo debug, si presenta mensajes durante los procesos
		self.__debugmode=debugmode
		#Aqui se crea la lista de bases a ser respaldadas(por defecto en blanco)
		self.__listadb=[]
		#Aqui va el indice de la BD actual (por defecto en cero)
		self.__elemento=0
		#Aqui se abre la conexion con el servidor MySQL
		self.__conexion=handlemysql.conexion(
		hostmysql=self.__hostmysql,
		usermysql=self.__usermysql,
		passmysql=self.__passmysql,
		basemysql=self.__basemysql,
		portmysql=self.__portmysql)



######################################################################################
######### Aqui se lista las bases de datos ###########################################
	def listmysqldb(self,ignorefolder=None,onlydb=None):
		"""Aqui se listan las bases de datos a ser respaldadas"""
		#ignorefolder es la lista de bases a excluir del respaldo
		#onlydb es la lista de bases exclusivas, solo estas bases seran respaldadas
		#si onlydb e ignorefolder contienen elementos, ignore folder tiene precedencia sobre onlydb
		#aqui se genera la lista de bases a respaldar siempre y cuando no se haya generado la lista antes
		if (not self.__listadb):
			listadbaux=self.__conexion.uniconsulta("show databases")
			for ele in listadbaux:
				#si la base no esta en la lista de ignoradas se agrega
				if ignorefolder:
					if not (ele in ignorefolder):
						#si la base esta en la lista exclusiva de bases a respaldar se agrega
						if onlydb:
							if ele in onlydb:
								self.__listadb.append(ele)
						#si la lista exclusiva esta vacia se la agrega
						else:
							self.__listadb.append(ele)
				#si la lista de ignoradas esta vacia se agrega la base a la lista
				else:
					if onlydb:
						#si esta dentro de la lista exclusiva se agrega
						if ele in onlydb:
							self.__listadb.append(ele)
					else:
						#si no esta en la lista exclusiva y no esta en la lista de ignoradas, se agrega
						self.__listadb.append(ele)
		return self.__listadb


######################################################################################
######### Aqui se generan los archivos SQL ###########################################
	def dumpdb(self):
		"""Aqui se generan los archivos SQL de respaldo"""
		if (self.__elemento < len(self.__listadb)):
			print(self.elemento)
			







##################################################################################
##################################################################################
##################################################################################
class genzipfile():
	"""Clase para comprimir los archivos en un archivo .7z"""

##################################################################################
	def __init__(self,rutafolder=None,exefolder="bin/",debugmode=False):
		"""Metodo inicial de genzipfile"""
######Aqui se define donde se encuentra la ruta del sistema
		self.__rutacen = monolib.validapath(rutafolder)
		self.__fecha = datetime.datetime.now()
		#ruta de compresor 7Z
		self._ruta7z = self.__rutacen + exefolder+"7z.exe"
		#Aqui se activa la funcion de ver modo debug, si presenta mensajes durante los procesos
		self.__debugmode=debugmode


##################################################################################
	def zipfiles(self,orifile=None,zipfile=None,metodo="7z"):
		"""Aqui se comprimen los archivos de una carpeta en un archivo .7z"""
		if not(zipfile): zipfile=self.userftp
		#nombre de archivo para respaldar
		self.arczip = self.comlib.nomarc(zipfile + "-", self.fecha, ".7z")
		#ruta de archivo para respaldar
		self.resbdzip = self.archivado + self.arczip



##################################################################################
##################################################################################
##################################################################################
class sendftpfile():
	"""Clase para enviar los archivos via ftp"""

##################################################################################
	def __init__(self,rutafolder=None,
		configdic={'hostftp':'127.0.0.1','userftp':'user','passftp':'pass','portftp':21,'timeout':-999},
		debugmode=False):
		"""Metodo inicial de sendftpfile"""
		self.__rutacen = monolib.validapath(rutafolder)
######Aqui se define donde se encuentra la ruta del sistema
		#if rutafolder:
			#self.rutacen = monolib.validapath(rutafolder)
		#else:
			#self.rutacen = monolib.validapath(registro._locatesyncloud())
		##datos servidor ftp
		self.__hostftp=configdic['hostftp']
		self.__userftp=configdic['userftp']
		self.__passftp=configdic['passftp']
		self.__portftp=configdic['portftp']
		self.__timeout=configdic['timeout']
		self.__debugmode=debugmode




##reparando, optimizando y respaldando las BD en archivos .SQL
##en la ruta "respaldo", omitiendo archivos
	#for i2 in bases:
		#i = i2[0]
		#if (i != "mysql" and i != "test" and i != "information_schema"):
			#try:
				#db = mysql.connect(hostmysql, usermysql, passmysql, i)
				#spacio = ""
				#for x in range(len(i), 30):
					#spacio = spacio + " "
				#print ("BD  " + i + spacio, sep="", end="")
				#print ("Reparando >> ", sep="", end="")
				#os.system(repararbd + i)
				#print("Respaldando >> ", sep="", end="")
				#os.system(myd + i + " >> " + respaldo + i + ".sql")
				#nbd = nbd + 1
				#db.close()
				#print (" Ok")
			#except:
				#print(i + " no es una BD MySQL valida")
				#try:
					#os.remove(respaldo + i + ".sql")
				#except:
					#print ("El archivo " + i + ".sql" + "no ha podido ser removido")
				#narc = narc + 1
	#
	#print ("Bases de datos Mysql respaldadas		: " + str(nbd))
	#print ("Numero de archivos no BD no respaldados : " + str(narc))
##Comprimiendo los respaldo .SQL en un archivo .7Z en la ruta "archivado"
	#lista = os.listdir(respaldo)
	#print ("")
	#print (">> Comprimiendo a archivo >> " + arczip)
	##comandzip = ruta7z + " a -t7z -mx9 -m0=PPmd -mo=32 -mmem=24m -mmt " + archivado + arczip
	#comandzip = ruta7z + " a -t7z -mx9 -m0=PPmd -mmem=64m -mmt " + archivado + arczip
	#comandzip = comandzip + ".7z" + " " + respaldo + "*.sql"
	#os.system(comandzip)
	#print("")
	#print("")
	#state_del = os.system("")
	#for xxx in lista:
		#os.chdir(respaldo)
		#print ("Eliminando archivo ", sep="", end="")
		#try:
			#print("%s " % xxx, sep="", end="")
			#state_del = os.remove("%s" % xxx)
			#if not state_del:
				#print ("Ok ")
			#else:
				#print ("\nError al Eliminar el archivo %s >> %s" % (xxx, state_del))
		#except:
			#print ("\nError al Eliminar el archivo %s >> %s" % (xxx, state_del))
	#print("")
##############################################################################
######################E n v i a n d o   v i a   F T P#########################
##############################################################################
###ABRIR CONEXION CON EL SERVIDOR
	#arc_trans = ""
	#try_transfer = 0
	#transfer_sucess = 1
	#while transfer_sucess:
		#try:
			#print ("Creando conexion con servidor FTP...")
			#ftpconnect = ftp.FTP()
			#print ("Abriendo conexion...")
			#ftpconnect.connect(hostftp, portftp, -999)
			#print ("Verificando usuario con servidor FTP...")
			#ftpconnect.login(userftp, passftp, "")
			#print (ftpconnect.getwelcome())
			#filetrans = archivado + arczip + ".7z"
			#print ("Iniciando transferencia...")
			#complete_cero = ""
			#arc_env = open(filetrans, "rb")
			#print ("Archivo listo para transferir")
			#ftpconnect.cwd("/")
			#try:
				#print ("Transfiriendo archivo %s.7z" % arczip)
				#arc_trans = arczip
##aqui se completa con ceros el numero de intento de envio
				#if try_transfer < 10:
					#complete_cero = "0000"
				#else:
					#if try_transfer < 100:
						#complete_cero = "000"
					#else:
						#if try_transfer < 1000:
							#complete_cero = "00"
						#else:
							#if try_transfer < 10000:
								#complete_cero = "0"
							#else:
								#complete_cero = ""
###############################################################
				#arc_trans = ("%s_%s%s.7z" % (arczip, complete_cero, try_transfer))
				#print (arc_trans)
				#ftpconnect.storbinary('STOR ' + arc_trans, arc_env, bar=u"█")
				#arc_env.close()
				#ftpconnect.quit()
				#print("Archivo transferido exitosamente...")
				#transfer_sucess = 0
			#except:
				#print("No se ha podido enviar el archivo al servidor FTP\n\n")
				#print("Reiniciando transferencia FTP")
		#except:
			#print("No se ha podido leer archivo a transferir")
		#try_transfer = try_transfer + 1
	#print ("Servicio finalizado")
	#print("")
	#print("")
##Mostrando hora de inicio y hora final
	#print("Proceso de respaldo de BD SQL iniciado  : ", sep="", end="")
	#print(formato.formatohora(fecha))
	#print("Proceso de respaldo de BD SQL finalizado: ", sep="", end="")
	#print(formato.formatohora(datetime.datetime.now()))

############################################################################################
####Carga de informacion para visualweb
#def visualweb():
	#"""Carga de informacion para visualweb"""
	#rutacen = monolib.validapath(registro._locatesyncloud())
	#rutabase = rutacen + "configuracion/system.db"
	#while True:
	##ruta de sistema centinela
			#nbd = 0
			#narc = 0
			#statefilesql = 0
	###########################################################################################
	##variables de envio FTP
	###########################################################################################
	##datos servidor ftp
			#enterprise = dataconnect.searchreg(rutabase, "enterprise")
			#hostftp = dataconnect.searchreg(rutabase, "siteftp2")
			#portftp = 21
			#userftp = dataconnect.searchreg(rutabase, "userftp2")
			#passftp = dataconnect.searchreg(rutabase, "passftp2")
			#hostmysql = dataconnect.searchreg(rutabase, "hostmysql")
			#usermysql = dataconnect.searchreg(rutabase, "usermysql")
			#passmysql = dataconnect.searchreg(rutabase, "passmysql")
	################################################################################
	############################################################################################
	##variables de respaldo BD
	############################################################################################
	################################################################################
	##lista de tablas a respaldar
			#listabd = monolib.listtablesbackup(monolib.loadlist(rutacen + "configuracion/tablelist.txt"))
	################################################################################
			#fecha = datetime.datetime.now()
	################################################################################
	##validacion de usuario mysql
			#mysqlvalid = ("-h %s -u %s " % (hostmysql, usermysql))
			#if passmysql:
					#mysqlvalid = ("%s -p%s" % (mysqlvalid, passmysql))
	################################################################################
	##comando dump
			#comandodump = ("mysqldump.exe %s --skip-lock-tables --skip-comments " % mysqlvalid)
	##comando check
			#comandocheck = ("mysqlcheck.exe %s --auto-repair --silent --databases " % mysqlvalid)
	################################################################################
	##ruta de compresor 7Z
			#ruta7z = rutacen + "bin/" + "7z.exe"
	##ruta de archivos .7Z
			#archivado = rutacen + "temp/visualweb/zip/"
	################################################################################
	##ruta de archivos .SQL
			#respaldo = rutacen + "temp/visualweb/sql/"
	##bases de datos a respaldar
			#rutabd = registro._mysqldata()
	################################################################################
	##comando para respaldar base de datos
			#myd = rutacen + "bin/" + comandodump
	##comando para reparar BD
			#repararbd = rutacen + "bin/" + comandocheck
	################################################################################
	##nombre de archivo para respaldar
			#arczip = comlib.nomarc(enterprise + "-", fecha, "")
	##ruta de archivo para respaldar
			#resbdzip = archivado + arczip
	###########################################################################################
	##						 I N I C I O  D E L   P R O G R AM A																				#
	###########################################################################################
			#os.system("cls")
			#print("================================ L o a d B D =================================")
			#print("Proceso de respaldo de BD iniciado en ", sep="", end="")
			#print(formato.formatohora(fecha))
	################################################################################
	##Listando archivos y carpetas en /data/
			#if passmysql:
					#passmysql = ("-p%s" % passmysql)
			#db = mysql.connect(hostmysql, usermysql, passmysql,)
			#cursor = db.cursor()
			#bases = monolib.loadlist(rutacen + "configuracion/bdlist.txt")
	##lista = os.listdir(rutabd)
	##reparando y respaldando las BD en archivos
	##en la ruta "respaldo", omitiendo archivos
			#for ix in bases:
					#i = ix[0]
					#nombre_sql = ix[1]
					#if i:
							#try:
									#db = mysql.connect(hostmysql, usermysql, passmysql, i)
									#spacio = ""
									#for x in range(len(i), 30):
											#spacio = spacio + " "
									#print ("BD  " + i + spacio, sep="", end="")
									#print ("Reparando >> ", sep="", end="")
									#os.system(repararbd + i)
									#estatefilesql = monolib.createfilesql(respaldo, nombre_sql + "-" + arczip, nombre_sql)
									#print("Respaldando >> ", sep="", end="")
									#if estatefilesql:
											#os.system(myd + i + " --tables " + listabd + " >> " + respaldo + nombre_sql + "-" + arczip)
									#else:
											#print("No se pudo crear el archivo %s" % i)
									#nbd = nbd + 1
									#db.close()
									#print (" Ok")
							#except:
									#print(i + " no es una BD MySQL valida")
									#try:
											#os.remove(respaldo + i)
									#except:
											#print ("El archivo " + i + "no ha podido ser removido")
							#narc = narc + 1
	################################################################################
			#print ("Bases de datos Mysql respaldadas        : " + str(nbd))
			#print ("Numero de archivos no BD no respaldados : " + str(narc))
	################################################################################
	##############################################################################
	##Comprimiendo los respaldo .SQL en un archivo .7Z en la ruta "archivado"
	##############################################################################
			#lista = os.listdir(respaldo)
			#print ("")
			#print (">> Comprimiendo a archivo >> " + arczip)
			#comandzip = ruta7z + " a -mx9 -m0=PPmd -mo=32 -mmem=256m " + archivado + arczip
			#comandzip = comandzip + " " + respaldo + "*"
	##print (comandzip)
			#os.system(comandzip)
	## for i in lista:
	## comandzip=ruta7z+" a "+archivado+arczip+" "+respaldo+i
	## os.system(comandzip)
			#print("")
			#print("")
			#state_del = os.system("")
			#for xxx in lista:
					#os.chdir(respaldo)
					#print ("Eliminando archivo ", sep="", end="")
					#try:
							#print("%s " % xxx, sep="", end="")
							#state_del = os.remove("%s" % xxx)
							#if not state_del:
									#print ("Ok ")
							#else:
									#print ("\nError al Eliminar el archivo %s >> %s" % (xxx, state_del))
					#except:
							#print ("\nError al Eliminar el archivo %s >> %s" % (xxx, state_del))
			#print("")
	################################################################################
	##								 E n v i a n d o   v i a   F T P
	################################################################################
	################################################################################
	###ABRIR CONEXION CON EL SERVIDOR
			#arc_trans = ""
			#try_transfer = 0
			#transfer_sucess = 1
			#while transfer_sucess:
					#print ("Creando conexion con servidor FTP...")
					#ftpconnect = ftplib.FTP()
					#print ("Abriendo conexion...")
					#ftpconnect.connect(hostftp, portftp, -999)
					#print ("Verificando usuario con servidor FTP...")
					#ftpconnect.login(userftp, passftp, "")
					#print (ftpconnect.getwelcome())
					#filetrans = archivado + arczip + ".7z"
					#print ("Iniciando transferencia...")
					#complete_cero = ""
					#try:
							#arc_env = open(filetrans, "rb")
							#print ("Archivo listo para transferir")
							#ftpconnect.cwd("/")
							#try:
									#print ("Transfiriendo archivo %s.7z" % arczip)
									#arc_trans = arczip
##aqui se completa con ceros el numero de intento de envio
									#if try_transfer < 10:
										#complete_cero = "0000"
									#else:
										#if try_transfer < 100:
											#complete_cero = "000"
										#else:
											#if try_transfer < 1000:
												#complete_cero = "00"
											#else:
												#if try_transfer < 10000:
													#complete_cero = "0"
												#else:
													#complete_cero = ""
###############################################################
									#arc_trans = ("%s_%s%s" % (arczip, complete_cero, try_transfer))
									#print (arc_trans)
									#ftpconnect.storbinary('STOR ' + arc_trans, arc_env)
									#ftpconnect.rename(arc_trans, ("%s.7z" % arc_trans))
									#arc_env.close()
									#ftpconnect.quit()
									#print("Archivo transferido exitosamente...")
									#transfer_sucess = 0
							#except:
									#print("No se ha podido enviar el archivo al servidor FTP\n\n")
									#print("Reiniciando transferencia FTP")
					#except:
							#print("No se ha podido leer archivo a transferir")
					#try_transfer = try_transfer + 1
			#print ("Servicio finalizado")
			#print("")
			#print("")
			##
			##
	##Mostrando hora de inicio y hora final
			#print("Proceso de respaldo de BD SQL iniciado  : ", sep="", end="")
			#print(formato.formatohora(fecha))
			#print("Proceso de respaldo de BD SQL finalizado: ", sep="", end="")
			#print(formato.formatohora(datetime.datetime.now()))
			#time.sleep(3600 * 5)
#################
#