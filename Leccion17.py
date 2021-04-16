#Cuando se usa * es que se le dara un numero indeterminado de elementos en forma de tuplas 
def devuelve_ciudades(*ciudades):
	for elemento in ciudades:
#Uso de for anidado
		#for subElemento in elemento:
#Uso del yield from
			yield from elemento
ciudades_devueltas=devuelve_ciudades("San Jose","Cartago","Heredia","Alajuela","Puntarenas","Limon","Guanacaste")
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))