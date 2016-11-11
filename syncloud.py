#programa de control
from __future__ import print_function
import os
import autopy
import sys

import lib.registro as registro
import lib.monolib as monolib
import lib.respaldo as respaldo
import lib.formato as formato
import lib.setupstart as setupstart
import getpass

clave = "vuros"

####################################################################################
####################################################################################
def _menu():
	"""Menu de opciones manuales de SynCloud"""
	bucle = 1
	while (bucle):
		os.system("CLS")
		formato.centrar("M E N U   S Y N C L O U D")
		print("\n\n\n")
		print("		1 : Ejecutar SynCloud")
		print("		2 : Ejecutar VisualWeb")
		print("		3 : Configuracion inicial\n\n")
		opcion=raw_input("Escoja una opcion : ")
		if opcion=="1":
			respaldo.syncloud()
			bucle = 0
		if opcion=="2":
			respaldo.visualweb()
			bucle = 0
		if opcion=="3":
			validaclave = getpass.getpass("Ingrese clave para configuracion : ")
			bucle = 0
			if validaclave == clave:
				setupstart.iniciaconfiguracion()
			else:
				print("Error de autenticacion...")
				os.system("PAUSE")
####################################################################################
####################################################################################

os.system("CLS")
rutacen = monolib.validapath(registro._locatesyncloud())
if not rutacen:
	formato.centrar("C O N F I G U R A C I O N   I N I C I A L")
	capturekey = autopy.alert.alert(formato.mensaje_config_inicial,"Syncloud", "SI", "NO")
	if capturekey:
		validaclave = raw_input("Ingrese clave para configuracion : ")
		if validaclave == clave:
			setupstart.iniciaconfiguracion()
	else:
		print("Fallo de autentificacion")
		os.system("PAUSE")
else:
	modo = ""
	narg = len(sys.argv)
	if narg > 1:
		modo = sys.argv[1]
		if modo == "-s":
			respaldo.syncloud()
		if modo == "-v":
			respaldo.visualweb()
	else:
		_menu()
