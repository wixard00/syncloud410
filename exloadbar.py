import os
lista=["sal","queso","pan","leche"]

class uno():
	
	def __init__(self):
		self.__privada=1
	
	def imprime(self):
		print("saludos")
		print(self.__privada)



i=4
lnum=len(lista)
print(lnum)
while True:
	if(i==lnum):
		break
	print("Elemento %s : %s"%(i+1,lista[i]))
	i+=1

ss=uno()
ss.imprime()
