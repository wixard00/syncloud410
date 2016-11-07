import os

#valida una ruta absoluta y la traduce a python
#ejemplo c:\ruta = c:/ruta/
def validapath(dir):
##############################################################################
	"""valida una ruta absoluta y la traduce a python
		ejemplo c:\\ruta = c:/ruta/"""
##############################################################################
	tec = dir.split("\\")
	bak = ""
	for i in tec:
		bak = bak + i + "/"
		bak = bak.replace("//", "/")
	if len(bak)>1:
		return(bak)
	else:
		return ("")

#valida una ruta python y la traduce a absoluta
#ejemplo c:/ruta = c:\ruta\
def invalidapath(dir):
##############################################################################
	"""valida una ruta python y la traduce a absoluta
	ejemplo c:/ruta = c:\\ruta\\ """
##############################################################################
	tec = dir.split("/")
	bak = ""
	for i in tec:
		bak = bak + i + "\\"
		bak = bak.replace("\\\\", "\\")
	return(bak)

#lee un archivo de texto y extrae y separa los datos
#ejemplo color=rojo se traduce a [("color","rojo"),]
#y si el segundo valor es una ruta le aplica "validapath"
def loadlist(pathfile):
##############################################################################
	"""lee un archivo de texto y extrae y separa los datos
		ejemplo color=rojo se traduce a [('color','rojo'),]
		y si el segundo valor es una ruta le aplica 'validapath'"""
##############################################################################
	listadatos = []
	if os.path.isfile(pathfile):
		listabd = open(pathfile)
		c = listabd.read()
		c1 = c.split("\n")
		for y in c1:
			datasize = len(y)
			tec = y.split("=")
			if (tec[0][0:4] == "path") or (tec[0][0:4] == "PATH"):
				tec[1] = validapath(tec[1])
			if datasize:
				listadatos.append(tec)
		listabd.close()
	return listadatos

#lee un archivo de texto y extrae y separa los datos tipo parametro
#ejemplo color=rojo se traduce a [("color","rojo"),]
#y si el segundo valor es una ruta le aplica 'validapath'
#los demas datos son ignorados, y si la linea empieza por # es exluida
def loadparameters(pathfile):
##############################################################################
	"""lee un archivo de texto y extrae y separa los datos tipo parametro
		ejemplo color=rojo se traduce a [("color","rojo"),]
		y si el segundo valor es una ruta le aplica 'validapath'
		los demas datos son ignorados, y si la linea empieza por # es exluida"""
##############################################################################
	listadatos = []
	if os.path.isfile(pathfile):
		listabd = open(pathfile)
		c = listabd.read()
		c1 = c.split("\n")
		for y in c1:
			datasize = len(y)
			if datasize:
				if (y[0] == "#"):
					datasize = 0
			tec = y.split("=",1)
			if (tec[0][0:4] == "path") or (tec[0][0:4] == "PATH"):
				tec[1] = validapath(tec[1])
			if ("=" in y) and (datasize>1):
				listadatos.append(tec)
		listabd.close()
	return listadatos

#Convierte una lista tipo ["tabla1","tabla2","tabla3"] en una cadena
#tipo cadena = " tabla1 tabla2 tabla3 "
def listtablesbackup(listatablas):
##############################################################################
	"""Convierte una lista tipo ['tabla1','tabla2','tabla3'] en una cadena
		tipo cadena = ' tabla1 tabla2 tabla3 '"""
##############################################################################
	lista = " "
	for x in listatablas:
		lista = lista + x[0] + " "
	return lista

#genera un archivo "nombre_archivo" en la ruta "ruta_archivo" y
#le agrega la linea use "nombre_archivo"
def createfilesql(ruta_archivo, nombre_archivo, nombre_base):
##############################################################################
	"""genera un archivo 'nombre_archivo' en la ruta 'ruta_archivo' y
		le agrega la linea use 'nombre_archivo'"""
##############################################################################
	estado = 1
	linea = ("use %s\n" % nombre_base)
	ruta = ("%s%s" % (ruta_archivo, nombre_archivo))
	try:
		createfile = open(ruta, "w")
		createfile.write(linea)
		createfile.close()
	except:
		estado = 0
	return estado

