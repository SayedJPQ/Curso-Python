import re
listaNombres=["Sayed Paniagua1", "Sara Paniagua2", "Wendy Quiros3", "Lisandro Paniagua4","Sara Quiros5","Camión","Camion"]
for elemento in listaNombres:
	if re.findall("[0-1x-z]", elemento):
		print(elemento)
		#Los parametros distinguen mayusculas y minusculas
		#Sirve para otros caracteres

	"""if re.findall("^Sara", elemento):
		print(elemento)
	if re.findall("Paniagua$",elemento):
		print(elemento)
	if re.findall("[LPQ]",elemento):
		print(elemento)
	if re.findall("Cami[oó]",elemento):
		print(elemento)"""

"""cadena="Prueba uno de expresiones regulares en python, hecho por Sayed, gracias a python"
texto="python"
encontrar=re.search(texto,cadena)
print(len(re.findall(texto,cadena)))"""

#len sirve para medir la longitud de lo buscado en numeros
"""print(encontrar.start())
print(encontrar.end())
print(encontrar.span())"""

"""if re.search(texto,cadena) is not None:
	print("Se ha encontrado texto")
else:
	print("No se ha encontrado texto")"""
#print(re.search("uno", cadena))

#^ Sirve para el inicio de una cadena de caracteres, tambien para negacion de rango agregandolo dentro del rango[^1-4]
#$ Para el final de una cadena de carateres