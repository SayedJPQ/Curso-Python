#If simple
def evaluacion(nota):
	valoracion="Aprobado"
	if nota<65:
		valoracion="Aplazado"
	return valoracion
print(evaluacion(66))
		
#Ingresar datos
NotaAlumno=input("Introduce la nota del alumno: ")
def evaluacion2(nota):
	print("Programa de notas de alumnos")
	valoracion2="Aprobado"
	if nota<65:
		valoracion2="Aplazado"
	return valoracion

print(evaluacion(int(NotaAlumno)))