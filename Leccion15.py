#Usar continue
for letra in "python":
	if letra=="h":
		continue
	print("Viendo la letra: " + letra)
print("")
Apellido="paniagua"
print(len(Apellido))
print("")
Nombrecompleto="Sayed Paniagua"
contador=0
for iteracion in Nombrecompleto:
	if iteracion==" ":
		continue
	contador+=1
print(contador)

#Pass se usa para ignorar la intruccion y modificarlo mas tarde

#Uso del else en el bucle y no en la condicional
print("")
email=input("Introduce tu email por favor: ")
for iteracion in email:
	if iteracion=="@":
		arroba=True
		print(arroba)
		break;
else:
	arroba=False
	print(arroba)