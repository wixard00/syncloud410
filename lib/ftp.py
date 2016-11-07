# -*- encoding: utf-8 -*-
from __future__ import print_function
import os
import sys
import ftplib
import colorconsole.terminal


class NEWFTP(ftplib.FTP):
	"""docstring for ftp"""
	#def __init__(self):
		#"""Aqui inicia la clase"""
#####################################################################################

	def storbinary(self, cmd, fp, blocksize=8192, callback=None, rest=None,bar="#"):
		"""Store a file in binary mode.  A new port is created for you."""
		lenbar=70.0
		self.voidcmd('TYPE I')
		estado=0
		tamano=len(fp.read())
		valor=((tamano/blocksize)/lenbar)
		limite=int(round(valor,0))
		fp.seek(0)
		combar=0
		print("0% ---------------------------------50%--------------------------------- 100%")
		print("   ",end="",sep="")
		conn = self.transfercmd(cmd, rest)
		while 1:
			buf = fp.read(blocksize)
			if not buf: break
			if estado==limite:
				if combar<lenbar:
					print(bar,sep="",end="")
					combar=combar+1
				estado=0
			conn.sendall(buf)
			estado+=1
		if combar<lenbar:
			for i in range(combar+1,int(lenbar),1):
				print(bar,end="",sep="")
			if callback: callback(buf)
		conn.close()
		print(" ")
		return self.voidresp()
		