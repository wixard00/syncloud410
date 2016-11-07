import lib.handlemysql

mysqlhost="127.0.0.1"
mysqluser="root"
con=lib.handlemysql.conexion()

ignorelist=["mysql","test","information_schema"]
onlydb=("header","jimenez","fss1")
listadb=[]
lista=con.uniconsulta("show databases")

for l in lista:
	if not(l in ignorelist):
		if (l in onlydb): listadb.append(l)
for l in listadb:
	print(l)

valor=False

if valor: print("casita")
