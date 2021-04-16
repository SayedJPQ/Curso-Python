#Uso de range
for bucle in range(6):
	print(bucle)
	print("")
	print(f"Valor de la variable: {bucle}")
	print("")
#Usar rango de range
for bucle2 in range(2,9):
	print(bucle2)
	print("")
#Usar saltos en range
for bucle3 in range(10,30,2):
	print(bucle3)
	print("")
#Usar longitud
Valido=False
miemail=input("Introduce tu email: ")
for email in range(len(miemail)):
	if miemail[email]=="@":
		Valido=True
if Valido:
	print("El correo es valido")
else:
	print("Correo no valido")


