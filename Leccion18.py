calc=0
while calc<5:
	def suma(num1, num2):
		return num1+num2
	def resta(num1, num2):
		return num1-num2
	def multiplicar(num1, num2):
		return num1*num2
	def dividir(num1, num2):
		try:
			return num1/num2
		except ZeroDivisionError:
			print("")
			print("No se puede dividir entre 0")
			print("")
			return "Operación erronea"
	print("")
	op1=(float(input("Introduce el primer número: ")))
	op2=(float(input("Introduce el segundo número: ")))
	operacion=input("Introduce la operación a realizar (+,-,*,/): ")
	calc=calc + 1
	print("")
	if operacion=="+":
		print(suma(op1,op2))
	elif operacion=="-":
		print(resta(op1,op2))
	elif operacion=="*":
		print(multiplicar(op1,op2))
	elif operacion=="/":
		print(dividir(op1,op2))
	else:
		print("Operación no contemplada")
	if calc==5:
		print("")
		print("Usastes muchos intentos")
		break;
print("")
print("Operación realizada")
