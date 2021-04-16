def decorador(parametro):
#*args sirve para poner un indeterminado de parametros, **kwargs sirve para palabras clave valor
	def interior(*args):
		print("A continuacion se realizara un calculo")
		parametro(*args)
		print("Se ha realizado el calculo")
	return interior
@decorador
def suma(num1,num2,num3):
	print(num1+num2+num3)
@decorador
def resta(num1,num2):
	print(num1-num2)
@decorador
def potencia(base,exponente):
	print(base**exponente)
suma(12,12,5)
resta(12,4)
potencia(5,3)
#potencia(base=5,exponente=3) con kwargs

