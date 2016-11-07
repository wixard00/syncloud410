#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
import os
import time
import datetime
import hashlib

####################################################################################
def checkfile(exe,filezip):
	estado=0


####################################################################################
def getmd5(filepath):
	md5value=""
	#blocksize es el tamaño de buffer de lectura del archivo(10 Mb por defecto)
	blocksize=10485760
	md5=hashlib.md5()
	if(os.path.isfile(filepath)):
		archivo=open(filepath,"rb")
		while True:
			data=archivo.read(blocksize)
			#data=archivo.read()
			if not data:
				break
			md5.update(data)
		md5value=md5.hexdigest()
	#archivo.close()
	return md5value


####################################################################################
def filetimedate(filepath):
	fecha=""
	hora=""
	if (os.path.isfile(filepath)):
		cdate1=datetime.datetime.fromtimestamp(os.path.getmtime(filepath))
		cdate=("%s" % cdate1)
		fecha=cdate[0:10]
		hora=cdate[11:19]
	return fecha,hora


####################################################################################
def listfiles(path):
	lista2=[]
	lista_files=[]
	x,y="",""
	filesize=0
	#bs="\\"
	if os.path.isdir(path):
		#print(path)
		lista=os.listdir(path)
		for ls in lista:
			if (os.path.isfile(path+ls)):
				#lista2.append(ls)
				#for ls2 in lista2:
					#x,y=filetimedate(path+ls)
				x,y=filetimedate(path+ls)
				lista_files.append([ls,x,y,filesize])
				#print(ls,x,y,filesize)
	return lista_files



####################################################################################
class search_reg():

##### v a r i a b l e  s ###########################################################
	mainpath=""
	listadir=[]


####################################################################################
	def __init__(self,mainpath="",arch_reg=""):
		self.lista_files=[]
		if not arch_reg:
			self.datefile=("%s" % datetime.datetime.now())
			self.namefile=("logbackup_"+self.datefile[0:10]+"_")
			self.namefile=(self.namefile+self.datefile[11:13]+"-"+self.datefile[14:16])
			self.namefile=(self.namefile+"-"+self.datefile[17:19]+".csv")
			self.namefile=os.getcwd()+"\\"+self.namefile
		else:
			self.namefile=arch_reg
		if not mainpath:
			self.mainpath=os.getcwd()
		else:
			self.mainpath=mainpath
		self.lista=os.listdir(self.mainpath)
		for x in self.lista:
			if os.path.isdir(mainpath+x):
				self.listadir.append(x)


####################################################################################
	def filesize(self,archivo):
		fsize=(archivo)
		return fsize

####################################################################################
	def genreg(self):
		#print("Ruta principal: " + os.getcwd())
		for ls in self.lista:
			if os.path.isdir(self.mainpath+"\\"+ls):
				lista2=os.listdir(self.mainpath+"\\"+ls)
				x=None
				#namefile=None
				for ls2 in lista2:
					#print(ls2)
					if os.path.isfile(os.getcwd()+"\\"+ls+"\\"+ls2):
						cdate1=datetime.datetime.fromtimestamp(os.path.getmtime(self.mainpath+"\\"+ls+"\\"+ls2))
						cdate=("%s" % cdate1)
						if cdate>x:
							x=cdate[0:10]
							y=cdate[11:19]
							#namefile=ls2
							filesize=(os.path.getsize(self.mainpath+"\\"+ls+"\\"+ls2))
				self.lista_files.append([ls,x,y,filesize])
	
		#print(self.namefile)
		


############################################################################
	def writofil(self,pathlog=mainpath):
		archivo_r=open(pathlog+self.namefile,"a")
		archivo_r.write("EMPRESA;Fecha;Hora;Peso\n")
		for ls3 in self.lista_files:
			registro=("%s;%s;%s;%s\n" % (ls3[0],ls3[1],ls3[2],ls3[3]))
			#print(registro)
			archivo_r.write(registro)
			print(ls3[0])
		#print("Proceso finalizado")