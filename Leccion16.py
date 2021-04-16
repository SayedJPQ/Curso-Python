#Uso tradicional de funciones
def generarpares(limite):
	num=1
	Lista=[]
	while num<limite:
		Lista.append(num*2)
		num=num+1
	return Lista
print(generarpares(20))
#Uso de generador
def Generarimpares(limite):
	num=0
	while num<limite:
		yield(num+1)
		num=num+2
Devuelveimpares=Generarimpares(30)
for i in Devuelveimpares:
	print(i)
#Usar next
def Generarnumeros(limite):
	num=0
	while num<limite:
		yield(num+1)
		num=num+1
Devuelvenumeros=Generarnumeros(30)
print(next(Devuelvenumeros))
print(next(Devuelvenumeros))
print(next(Devuelvenumeros))
print(next(Devuelvenumeros))