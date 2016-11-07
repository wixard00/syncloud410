# -*- encoding: utf-8 -*-
#genera un documento html
from __future__ import print_function
import os

os.system("CLS")
filename="vfbackup.html"
print("Generando reporte vfbackup.html...")
archivo=open(filename,"w+")
membuffer="""<html>
	<head>
		<title>Olesistemas</title>
	</head>
	<body>
		<table style="simple" border="1"  class="cuerpotabla" width="30%">\n"""
archivo.write(membuffer)
for i in range(0,10,1):
	archivo.write("\t\t\t<tr align='center'>\n")
	for j in range(0,6,1):
		archivo.write("\t\t\t\t<td>\n\t\t\t\t\t<p>%s:%s</p>\n\t\t\t\t</td>\n"%(i+1,j+1))
	print("hecho %s" % i)
archivo.write("\t\t</table>\n\t</body>\n</html>")
print("archivo generado")