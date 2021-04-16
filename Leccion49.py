#def area_triangulo(base,altura):
#Prueba y documentacion
	#"""Calculo de un triangulo
	#>>> area_triangulo(3,6)
	#'El area del triangulo es: 9.0'
	#>>> area_triangulo(4,5)
	#'El area del triangulo es: 10.0'
	#"""
	#return "El area del triangulo es: " + str ((base*altura)/2)
#print(area_triangulo(2,4))
def comprobarmail(mail_usuario):
	"""Funcion que comprueba un mail con la @. Si tiene una @ es correcto, sino es incorrecto o si tambien esta el final es incorrecto
	>>> comprobarmail('sayedjquiros@gmail.com')
	'Es correcto'
	>>> comprobarmail('sayedjquirosgmail.com@')
	'Es incorrecto'
	>>> comprobarmail('sayedjquiros@@gmail.com')
	'Es incorrecto'
	>>> comprobarmail('sayedjquirosgmail.com')
	'Es incorrecto'
	"""
	arroba=mail_usuario.count('@')
	if (arroba!=1 or mail_usuario.rfind('@')==(len(mail_usuario)-1)):
		return "Es incorrecto"
	else:
		return "Es correcto"
import doctest
doctest.testmod()