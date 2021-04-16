class Empleados():
	def __init__(self,nombre,cargo,salario):
		self.nombre=nombre
		self.cargo=cargo
		self.salario=salario
	def __str__(self):
		return "{} que trabaja como {} tiene un salario de {} $".format(self.nombre,self.cargo,self.salario)
listaempleados=[
Empleados("Juan","Director",150000),
Empleados("Sara","Secreatria",15000),
Empleados("Josue","Conserje",8000),
Empleados("Issac","Programador",80000)
]
def comision(empleado):
	if (empleado.salario<=20000):
		empleado.salario=empleado.salario*1.03
	return empleado
listaEmpleadosComision=map(comision,listaempleados)
for empleado in listaEmpleadosComision:
	print(empleado)
"""class Empleados():
	def __init__(self,nombre,cargo,salario):
		self.nombre=nombre
		self.cargo=cargo
		self.salario=salario
	def __str__(self):
		return "{} que trabaja como {} tiene un salario de {} $".format(self.nombre,self.cargo,self.salario)
listaempleados=[
Empleados("Juan","Director",150000),
Empleados("Sara","Secreatria",15000),
Empleados("Josue","Conserje",8000),
Empleados("Issac","Programador",80000)
]
salarios_altos=filter(lambda empleados:empleados.salario>50000, listaempleados)
for salario_empleado in salarios_altos:
	print(salario_empleado)"""
"""def par(num):
	if num % 2==0:
		return True"""
#numeros=[12,13,14,15,16,2,3,4,5]
#print(list(filter(lambda par: par%2==0,numeros)))