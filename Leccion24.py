#Metodos de cadenas
nombreusuario=input("Introduce tu nombre de usuario: ")
print("")
print("Tu nombre es:",nombreusuario.capitalize())
print("")
intentos=0
edad=input("Introduce tu edad: ")
print("")
while(edad.isdigit()==False):
	print("Introduce un numero valido")
	print("")
	print("Tu edad es:",edad)
	print("")
	edad=input("Introduce tu edad: ")
	print("")
	intentos=intentos+1
	if intentos==4:
		print("Advertencia estas usando muchos intentos")
		print("")
	if intentos==7:
		print("Has usado muchos intentos")
		print("")
		print("Has usado",intentos,"intentos")
		break;
try:
	if (int(edad)<18):
		print("")
		print("No puede pasar")
		intentos=intentos+1
	else:
		print("")
		print("Puede pasar")
		intentos=intentos+1
except ValueError:
	print("")
	print("Cierra y abre el programa")
print("")
print("Programa finalizado")

