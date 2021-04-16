#Diccionario
Diccionario={"Alemania":"Berlin", "Costa Rica":"San Jose", "Francia":"Paris"}
#Agregar nuevo elemento a diccionario
Diccionario["Portugal"]="Lisboa"
print(Diccionario)
print(["Alemania"])
#Imprimir Llaves
print(Diccionario.keys())
#Imprimir Valores
print(Diccionario.values())
#Ver cantidad de valores
print(len(Diccionario))
del Diccionario["Costa Rica"]
print(Diccionario)
#Usar Diccionario con tuplas
Tupla1=("España", "Nicaragua", "EEUU")
Diccionario2={Tupla1[0]:"Madrid", Tupla1[1]:"Managua", Tupla1[2]:"Washington"}
print(Diccionario2)