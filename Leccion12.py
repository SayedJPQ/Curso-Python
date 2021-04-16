print("Hola"); print(""), print("Adios")
#Usar argumento end
for bucle in [1,2,3,4]:
	print("Hola", end=" ")
email=False
contador=0
miemail=input("Introduce tu email: ")
for bucle2 in miemail:
	if (bucle2=="@") or (bucle2=="."):
		contador=contador + 1
if contador>=2:
	print("El email es correcto")
else:
	print("El email es incorrecto")
#usar range
for bucle3 in range(5):
	print("Hola")
