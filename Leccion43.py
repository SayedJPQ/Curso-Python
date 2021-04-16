#: es igual a return
area_triangulo= lambda base, altura:(base*altura)/2
print(area_triangulo(1,6))
print(area_triangulo(2,5))
print(area_triangulo(2,9))
elevar_cubo= lambda numero:numero**3#Se puede usar pow(numero, exponente)
print(elevar_cubo(3))
salario=lambda comision:"¡{}$!".format(comision)
salario_ana=15000
print(salario(salario_ana))