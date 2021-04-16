print("Accesso")

Edad=int(input("Introduce tu edad: "))
#If
if 0<Edad<18:
	print("No puedes pasar")
#Elif
elif 0<Edad>120:
	print("Error")
#Else
else:
	print("Puedes pasar")
#Usar varias condicionales
print("Nota")
Nota=int(input("Introduce su nota: "))
if Nota<0:
	print("No valido")
elif Nota<=1:
	print("No estudio")
elif Nota<=2:
	print("Le cuesta bastante")
elif Nota<=3:
	print("No sabe del tema")
elif Nota<=4:
	print("Falta de estudio")
elif Nota<=5:
	print("Deficiente")
elif Nota<=6:
	print("Suficiente")
elif Nota<=7:
	print("Aceptable")
elif Nota<=8:
	print("Bien")
elif Nota<=9:
	print("Excelente")
elif Nota<=10:
	print("Sobresaliente")
else:
	print("No valido")
print("El programa cerro")
