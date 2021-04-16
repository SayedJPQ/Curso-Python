import math
def raiz_cuadrada(lista_numeros):
	"""La funcion devuelve una lista con raiz cuadrada a los numeros con otra lista
	>>> lista=[]
	>>> for i in [4,9,16]:
	... 	lista.append(i)
	>>> raiz_cuadrada(lista)
	[2.0, 3.0, 4.0]

	>>> lista=[]
	>>> for i in [4,-9,16]:
	... 	lista.append(i)
	>>> raiz_cuadrada(lista)
	Traceback (most recent call last):
	...
	ValueError: math domain error
	"""
# ... sirve para identar y/o anidar, tambien como con
	return [math.sqrt(n) for n in lista_numeros]
print(raiz_cuadrada([9,12,25,65,14,79,2,3]))

import doctest
doctest.testmod()