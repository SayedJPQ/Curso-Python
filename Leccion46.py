import re
nombre1="Sandra Lopez"
nombre2="Sayed Paniagua"
nombre3="Sara Paniagua"
nombre4="Sara Quiros"
if re.match(".ara", nombre3, re.IGNORECASE):
	#\d sirve para encontrar numeros
	#El punto sirve para buscar a partir de los caracteres que esten por delante
	#IGNORECASE sirve para ignorar mayuscula y minuscula
	print("Hemos encontrado 1 coincidencia")
else:
	print("No se ha encontrado ninguna coincidencia")
if re.search("P", nombre3, re.IGNORECASE):
	#Search busca en toda la cadena match busca solo el principio
	#\d sirve para encontrar numeros
	#El punto sirve para buscar a partir de los caracteres que esten por delante
	#IGNORECASE sirve para ignorar mayuscula y minuscula
	print("Hemos encontrado 1 coincidencia")
else:
	print("No se ha encontrado ninguna coincidencia")