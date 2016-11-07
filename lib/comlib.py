## funciones adicionales para proyecto centinela

import datetime

## esta funcion convierte un numero de un digito a uno de dos digitos en texto por
## por ejemplo 7 se convierte en "07" y el 23 se convertiria en "23"

def dobdig(numero=0,limite=2):
	"""convierte numeros como 5 a 005 segun el numero de ceros que se establesca en 'limite'"""
	
	cadenadob=str(numero).rjust(limite,"0")
	return cadenadob

#Crea un nombre de archivo con el formato nombre+fecha+hora por ejemplo archivo_20141101_185530.extension

def nomarc(nombre="archivo",fecha=datetime.datetime.now(),ext="txt"):
	"""combina nombre + fecha + hora + extension y lo devuelve como cadena"""
	
	salida = None
	#salida = nombre + fecha
	salida = ("%s%s%s%s-"%(nombre,dobdig(fecha.year),dobdig(fecha.month),dobdig(fecha.day)))
	#salida = salida + hora + extension
	salida = ("%s%s%s%s.%s"%(salida,dobdig(fecha.hour),dobdig(fecha.minute),dobdig(fecha.second),ext))
	return salida


#ejemplo del uso de nomarc
#d=datetime.datetime.now()
#print(nomarc("archivozip",d,"7z"))
#print(nomarc())
