#Tupla
Tupla1=("Juan", "Daniel", 1,2,3)
print(Tupla1)
#Llamar indics
print(Tupla1[4])
#Construir Lista a partir de la tupla
Tupla2=("S", "A", "Y")
Lista1=list(Tupla2)
print(Lista1)
#Pasar de lista a tupla
Lista2=["J", "O", "S"]
Tupla3=tuple(Lista2)
print(Tupla3)
#Buscar elementos en tuplas
print("Juan" in Tupla1)
print("Sayed" in Tupla1)
#Usar contador de elementos
print(Tupla1.count(1))
#Usar medidor de longitud de tupla
print(len(Tupla1))
print(len(Tupla2))
#Tupla unitaria
Tupla4=("Pan",)
print(Tupla4)
print(len(Tupla4))
#Desempaquetado de tupla
Nombre, Nombre2, Numero1, Numero2, Numero3=Tupla1
print(Numero3)
print(Nombre)
print(Nombre2)
print(Numero1)