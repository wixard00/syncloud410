import MySQLdb as mysql
#import os
#import lsdir

class conexion():
	"""Clase para manipulacion de datos de mysql"""
##########################################################################################
	def __init__(self,hostmysql="127.0.0.1",usermysql="root",passmysql="",basemysql="",portmysql=3306):
		"""Metodo inicial"""
		self.conexion=mysql.connect(hostmysql,usermysql,passmysql,basemysql,portmysql)
		#self.rutapath=(self.uniconsulta("""select valor from setup where id='rutapath'"""))[0]
		#print(self.rutapath)
##########################################################################################

##########################################################################################
	def multiconsulta(self,parameters):
		"""Permite obtener multiples valores en una consulta"""
		act=self.conexion
		cursor=act.cursor()
		cursor.execute(parameters)
		return cursor.fetchall()

##########################################################################################
	def uniconsulta(self,parameters):
		"""Realiza una consulta y devuelve una lista con los datos de la primera columna"""
		act=self.conexion
		cursor=act.cursor()
		cursor.execute(parameters)
		lista=cursor.fetchall()
		lista2=[]
		for i in lista:
			#print(i)
			lista2.append(i[0])
		return lista2


