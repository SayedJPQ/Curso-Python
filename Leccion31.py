import pickle

class Vehiculos():
	def __init__(self, marca, modelo):
		self.marca=marca
		self.modelo=modelo
		self.marcha=False
		self.freno=False
		self.arranque=False
	def arrancar(self):
		self.arranque=True
	def marcha(self):
		self.marcha=True
	def freno(self):
		self.arranque=True
	def estado(self):
		print("Marca:",self.marca,"\nModelo:",self.modelo,"\nMarcha:",self.marcha,
			"\nAcelerando:",self.arranque,"\nFreno:",self.freno)
coche1=Vehiculos("Mazda","MX5")
coche2=Vehiculos("Hyunday","Excel")
coche3=Vehiculos("Hyunday","Acent")
coches=[coche1, coche2, coche3]
fichero=open("Loscoches","wb")
pickle.dump(coches, fichero)
fichero.close()
del (fichero)
ficheroA=open("Loscoches","rb")
misCoches=pickle.load(ficheroA)
ficheroA.close()
for i in misCoches:
	print(i.estado())