#Concatenacion de condiciones
Edad=-1
if 0<Edad<100:
	print("La edad es correcta")
else:
	print("La edad es incorrecta")
#Concatenar string con numeros
Salario=int(input("Introduce Salario: "))
Salario2=int(input("Introduce Salario2: "))
Salario3=int(input("Introduce Salario3: "))
print("Salario: " + str(Salario))
print("Salario2: " + str(Salario2))
print("Salario3: " + str(Salario3))
if Salario>Salario2>Salario3:
	print("Funciona Bien")
else:
	print("Algo anda mal")


