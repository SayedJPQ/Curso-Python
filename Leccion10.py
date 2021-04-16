#Uso de and y or
print("Programa de becas 2020")
Distancia=float(input("Pon la distancia de tu casa la instituto: "))
print(Distancia)
Hermanos=int(input("Pon tu cantidad de hermanos: "))
print(Hermanos)
Salario=int(input("Pon tu salario bruto: "))
print(Salario)
print("Debes usar 1 Para verdadero o 0 para Falso para contestar a esta pregunta")
Discapacidad=int(input("¿Tienes alguna discapacidad?: "))
print(Discapacidad)
if Distancia>=1 and Hermanos>=1 and Salario<=350000 or Discapacidad==1:
	print("Tienes derecho a beca")
else:
	print("No tienes derecho a beca")
#Uso del in
print("Asignaturas disponibles 2020")
print("Materias disponibles: informatica", "contabilidad" " y " "turismo")
Asignatura=input("Escribe la materia escogida: ")
Opcion=Asignatura.lower()
if Asignatura in ("informatica", "contabilidad", "turismo"):
	print("Asignatura elegidad: " + Asignatura) 
else:
	print("La asignatura escrita no es valida")