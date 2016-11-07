#programa de control
from __future__ import print_function
#import os
#import ftplib
#import datetime
import time
#import MySQLdb as mysql

import comlib
#import registro
#import monolib
#import dataconnect

mensaje_config_inicial="""Es necesario configurar SynCloud por primera vez, se
procedera a ejecutar el asistente pero debe proporcionar los
credenciales necesarios, si esta de acuerdo presione ACEPTAR,
caso contrario presione CANCELAR."""

def config_inicial():
	animatedmsg(mensaje_config_inicial)

def formatohora(fecha):
	"""formatea la hora a presentar"""
	cadena = ""
	cadena = str(fecha.year) + "-" + comlib.dobdig(fecha.month)
	cadena = cadena + "-" + comlib.dobdig(fecha.day) + " @ "
	cadena = cadena + comlib.dobdig(fecha.hour) + ":"
	cadena = cadena + comlib.dobdig(fecha.minute) + ":"
	cadena = cadena + comlib.dobdig(fecha.second)
	return cadena

def centrar(cadena):
	"""Centra un texto"""
	print(cadena.center(80,"="), sep="", end="\n")
	return None


def animatedmsg(cadena):
	for x in cadena:
		print(x,sep="",end="")
		time.sleep(0.005)


#esta funcion devuelve el tipo de variable pero en formato
#cadena y no "TYPE", es decir si la variable es una cadena
#tipovar devuelve una cadena con el valor "str"
def tipovar(variable):
	var=("%s" % type(variable))
	var2=var.split("'")
	return(var2[1])
