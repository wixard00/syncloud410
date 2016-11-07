# -*- encoding: utf-8 -*-
#biblioteca para crear documentos html
import os
import sys

class HTMLgen:
	"""Clase generadora de documentos HTML"""
	tab=0
	tabcode="\t"
######################################################################
	def __init__(self,filename="dochtml.html",title="Olesistemas"):
		"""Inicializa el archivo html"""
		self.tab=0
		self.tabcode="\t"
		self.codehtml=""
		self.archivo=open(filename,"w")
		self.membuffer=("""<html>\n\t<head>\n\t\t<title>%s</title></head>\n\t<body>\n"""%title)
		self.tab=self.tab+2
		self.codehtml=self.codehtml+self.membuffer

################ F U N C I O N E S ###################################
######################################
	def addhtml(self):
		"""Agrega el codigo al archivo html temporal"""
		self.codehtml=self.codehtml+(self.tabcode*self.tab)+self.membuffer

######################################
	def createtable(self,style="border-collapse:collapse",border=1,width="30%"):
		"""crea una tabla html"""
		self.membuffer=("""<table style="%s" border="%s" width="%s">\n"""%(style,border,width))
		self.tab=self.tab+1
		self.addhtml()

######################################
	def closetable(self):
		"""cierra una tabla html"""
		self.membuffer=("</table>\n")
		self.tab=self.tab-1
		self.addhtml()


######################################
	def addfil(self,align='center'):
		self.membuffer=("<tr align='%s'>\n"%align)
		self.tab=self.tab+1
		self.addhtml()

######################################
	def closfil(self):
		self.membuffer=("</tr>\n")
		self.tab=self.tab-1
		self.addhtml()

######################################
	def addcol(self):
		self.membuffer=("<td>\n")
		self.tab=self.tab+1
		self.addhtml()


######################################
	def addcolval(self,valor=" ",font="Comic Sans",forecolor="abcdef"):
		self.membuffer=("<a fontsize=25 font='%s' forecolor='%s'>%s</a>\n"%(font,forecolor,valor))
		self.tab=self.tab+1
		self.addhtml()
		self.tab=self.tab-1


######################################
	def addbr(self):
		self.membuffer=("<br>\n")
		self.tab=self.tab+1
		self.addhtml()
		self.tab=self.tab-1


######################################
	def closcol(self):
		self.membuffer=("</td>\n")
		self.tab=self.tab-1
		self.addhtml()

######################################

	def closehtml(self):
		self.membuffer="\t</body>\n</html>"
		self.addhtml()
		self.tab=self.tab-2
		self.archivo.write(self.codehtml)