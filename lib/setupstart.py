#sistema de configuracion
import os
#import sys
import _winreg
import autopy

#librerias dentro de carpeta lib (privadas)
import monolib
import dataconnect

listaid = ["enterprise",
			"hostmysql", "usermysql", "passmysql", "portmysql",
			"siteftp",  "userftp",  "passftp", "timebackup",
			"siteftp2", "userftp2", "passftp2"]

rutas = ["configuracion/",
		"temp/",
		"temp/syncloud/",
		"temp/visualweb/",
		"temp/syncloud/zip/",
		"temp/syncloud/sql/",
		"temp/visualweb/sql/",
		"temp/visualweb/zip/"]

#funciones
############################################################################################
def createfolder(carpeta):
	"""Crea carpetas, si es que no existen"""
	errorinstall = 0
	if os.path.exists(carpeta):
		print("Ruta %s encontrada..." % carpeta)
	else:
		try:
			os.mkdir(carpeta)
			print("Ruta %s creada..." % carpeta)
		except:
			print("No se ha podido crear la carpeta %s..." % carpeta)
			errorinstall = 1
	return errorinstall

#######################################################################################
#Ingreso manual de valores de configuracion############################################
def manualinput(regvalid,ids,valorid,_updatevalor,rutabase):
	"Aqui el usuario puede ingresar los valores de configuracion manualmente"
	if regvalid:
		print("""El registro '%s' ya existe con el valor '%s'
		\nDesea actualizarlo s :""" % (ids, valorid)),
		if (raw_input() == "s"):
			print("Ingrese %s: " % ids),
			_updatevalor = raw_input()
			estadosql = dataconnect.updatereg(rutabase, ids, _updatevalor)
			if estadosql:
				print("Ok\n")
		else:
			print("\n")
	else:
		print("Ingrese %s :" % ids),
		_updatevalor = raw_input()
		estadosql = dataconnect.createreg(rutabase, ids, _updatevalor)
		if estadosql:
			print("Ok\n")
		else:
			print("Error al guardar el registro %s \n" % _updatevalor)

#######################################################################################
#Configuracion principal de syncloud###################################################
def iniciaconfiguracion():
	"""Configuracion principal de syncloud y visualweb"""
	os.system("CLS")
	ruta = os.getcwd()
	rutatask = ruta + "\\syncloud.exe"
	timetask = ""
	key = _winreg.CreateKey(_winreg.HKEY_LOCAL_MACHINE, 'SOFTWARE\\Olesistemas\\syncloud')
	try:
		_winreg.SetValueEx(key, 'Location', 0, _winreg.REG_SZ, ruta)
	except:
		print("No se ha podido crear el registro del systema")
	ruta = monolib.validapath(ruta)
	print(ruta)
	if os.path.exists(ruta):
		print ("Carpeta Principal encontrada...")
		for rutafinal in rutas:
			createfolder(ruta+rutafinal)
#Se conecta a la base sqlite del programa
		estado = dataconnect.createbase(ruta + "configuracion/system.db")
		if estado:
			print("Base de sistema creada...\n")
			dataconnect.createtables(ruta + "configuracion/system.db")
			rutabase = ruta + "configuracion/system.db"
#cargando parametros por defecto desde archivo account.txt
			if not os.path.isfile(ruta + "configuracion/account.txt"):
				listabd = ""
			else:
				listabd = monolib.loadparameters(ruta + "configuracion/account.txt")
			for i in listabd:
#preconfiguracion en archivo account
				for parametro in listaid:
					if i[0] == parametro:
						print ("Valor aceptado: %s" % i)
						if not dataconnect.existreg(rutabase, parametro):
							dataconnect.createreg(rutabase, parametro, i[1])
						else:
							dataconnect.updatereg(rutabase, parametro, i[1])
#aqui empieza a pedir datos de configuracion
			print("Preconfiguracion desde archivo terminada\n\n")
			ingresomanual = autopy.alert.alert("Ingresar paramentros manualmente?","Syncloud", "SI", "NO")
			for ids in listaid:
				regvalid = dataconnect.existreg(rutabase, ids)
				valorid = dataconnect.searchreg(rutabase, ids)
				_updatevalor = valorid
				if ingresomanual:
					manualinput(regvalid,ids,valorid,_updatevalor,rutabase)
				if ids == "timebackup":
					timetask = _updatevalor
		else:
			print ("No se ha podido verificar la ruta: %s \n" % ruta)
	taskstate = os.system('schtasks /create /sc DAILY /TN "Syncloud" /TR "%s -s" /ST %s /RU SYSTEM /F' % (rutatask, timetask))
	if(taskstate != 0):
		print("Error al crear la tarea programada, %s" % taskstate)
	taskstate2 = os.system('schtasks /create /SC ONSTART /TN "VisualWeb" /TR "%s -v" /RU SYSTEM /F' % (rutatask))
	if(taskstate2 != 0):
		print("Error al crear la tarea programada, %s" % taskstate2)
	print ("\nConfiguracion finalizada en %s \n" % ruta)
	os.system("PAUSE")
