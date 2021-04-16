import math
def evaluaedad(Edad):
#Uso de raise
	if Edad<0:
		raise TypeError("No se permiten numeros negativos")
	if Edad<20:
		return "Eres muy joven"
	elif Edad<40:
		return "Eres joven"
	elif Edad>=40:
		return "Eres viejo"
print(evaluaedad(6))
#Cuando se usa raise solo se pueden poner errores definidas en las bibliotecas a menos que se cree una clase
def calcularaiz(num):
	if num<0:
		raise ValueError("El número no puede ser negativo")
	else:
		return math.sqrt(num)
op=(int(input("Introduce el número a calcular: ")))
try:
	print(calcularaiz(op))
except ValueError as ErrorNegativo:
	print(ErrorNegativo)
print("")
print("Programa finalizado")
