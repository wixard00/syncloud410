#stdata

import os

def ruta(rutaori):
	rutaori = rutaori.split("\\")
	rutaori = "/".join(rutaori)
	rutaori = rutaori+"/"
	return rutaori;
	
