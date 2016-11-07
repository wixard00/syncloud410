#cifrado de datos
from __future__ import print_function
import os


def crypt(data):
	valor = 0
	valor = ord(data[-1:])
	datacrypt = ""
	for i in data:
		valor = valor + ord(i)
		if (valor > 255):
			valor = valor - 256
		datacrypt = datacrypt + chr(valor)
	return datacrypt


def decrypt(data):
	data=data[::-1]
	valor = 0
	if size == 1:
		valor = ord(data[0])/2
	else:
		valor = ord(data[size - 2])
	datacrypt = ""
	for i in range(0, size - 1, -1):
		if i>0:
			datacrypt = chr(valor) + datacrypt
	return datacrypt


#def decrypt(data):
	#datacrypt=crypt(data[::-1])
	#return datacrypt
#