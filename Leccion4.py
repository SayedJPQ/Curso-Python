#Listas
Lista1=["El pepe", "Ete Sech", "El pepeX2"]
Lista2=[1,2,3,4,5]
#Agregar elementos a las listas
Lista1.append("Sandro")
#Agregar los elementos controlando la posicion
Lista1.insert(1, "Chao")
#Agregar 2 o mas elementos
Lista1.extend(["Hallo", "Ja", "Da"])
#Eliminar elementos
Lista1.remove("El pepeX2")
#Eliminar ultimo elemento
Lista1.pop()
print(Lista1)
#Llamar indices
print(Lista1[0])
print(Lista1[2])
#Indices negativos
print(Lista1[-2])
#Exclusiones
print(Lista1[0:2])
#Encontrar si el elemento esta en lista
print("El pepe" in Lista1)
print("SS" in Lista1)
#Fusionar Listas
Lista3=Lista1+Lista2
print(Lista3)
#Repetir lista
Lista4=[12,12,13,13,14,14] * 3
print(Lista4)
