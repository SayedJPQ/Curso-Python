import math
#Bucle While
bucle=1

while bucle<=10:
	print("Ejecucion" + str(bucle))
	bucle=bucle+1
print("Termino la ejecucion")
#Bucle while con condicional
edad=int(input("Introduce tu edad: "))
intentos=1
while edad<5 or edad>100:
	print("Pon tu edad correctamente por favor")
	print("")
	edad=int(input("Introduce tu edad: "))
	print("")
	intentos=intentos + 1
	if intentos==5:
		print("We ya pon tu edad")
	elif intentos>=10:
		print("Por favor pon bien tu edad sino me vere en la obligacion de cerrar el programa")
	if intentos==12:
		print("Has usado muchos intentos")
		break;
print("Gracias por tu tiempo")
print("")
print("Tu edad: " + str(edad))
print("")
print("Veces de intentos " + str(intentos))
print("")
if intentos>=5 and intentos<12:
	print("Ves que no fue dificil")
elif intentos==12:
	print("El programa ha finalizado por favor vuelva a abrirlo para poder escribir la edad")
else:
	print("Gracias por tu cooperación")
print("")
print("El programa cerro")
print("")
#Usar raiz cuadrada
print("Programa para calcular la raiz cuadrada")
print("")
numero=int(input("Pon el numero para calcularlo por favor: "))
Intentos=1
while numero<0:
	print("No se puede calcular raiz de numeros negativos")
	Intentos=Intentos + 1
	numero=int(input("Pon el numero para calcularlo por favor: "))
	if Intentos==3:
		print("Has usado muchos intentos")
		print("")
		print("El programa finalizo")
		break;
print("")
if Intentos<3:
	solucion=math.sqrt(numero)
	print("La solucion de: " + str(numero) + " es " + str(solucion) )
print("")
print("El programa cerro")
