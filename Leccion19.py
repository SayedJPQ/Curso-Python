calc=0
while calc<5:
	def suma(num1, num2):
		return num1+num2
	def resta(num1, num2):
		return num1-num2
	def multiplicar(num1, num2):
		return num1*num2
	def dividir(num1, num2):
#Uso de la excepcion
		try:
			return num1/num2
		except ZeroDivisionError:
			print("")
			print("No se puede dividir entre 0")
			print("")
			return "Operación erronea"
	print("")
	try:
		op1=(float(input("Introduce el primer número: ")))
		op2=(float(input("Introduce el segundo número: ")))
	except ValueError:
		print("")
		print("Solo debes colocar números")
	print("")
	operacion=input("Que deseas realizar (+,-,*,/) o cerrar: ")
	print("")
	try:
		if operacion=="+":
			print(suma(op1,op2))
		elif operacion=="-":
			print(resta(op1,op2))
		elif operacion=="*":
			print(multiplicar(op1,op2))
		elif operacion=="/":
			print(dividir(op1,op2))
		elif operacion=="cerrar":
			operacion.lower
			print("Programa finalizado")
			break;
		else:
			print("Operación no contemplada")
	except NameError:
		print("Error")
print("")
print("Operación realizada")
#La instruccion finally se usa para que a pesar de cualquier evento se ejecute si o si 
