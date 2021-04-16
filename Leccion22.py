#Herencia
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
class furgoneta(Vehiculos):
	def carga(self, cargar):
		self.cargado=cargar
		if (self.cargado):
			print("Esta cargado")
		else:
			print("No esta cargado")
class Moto(Vehiculos):
	def caballito(self):
		self.ccaballito="Voy haciendo el caballito"
	def estado(self):
		print("Marca:",self.marca,"\nModelo:",self.modelo,"\nMarcha:",self.marcha,
			"\nAcelerando:",self.arranque,"\nFreno:",self.freno,"\n",self.ccaballito)
class V_electricos(Vehiculos):
	def __init__(self,marca,modelo):
		super().__init__(marca,modelo)
		self.autonomia=100
	def cargarenergia(self):
		self.cargando=True
Mimoto=Moto("Honda", "CBR")
Mimoto.caballito()
Mimoto.estado()
Mifurgoneta=furgoneta("Renault","Kangoo")
Mifurgoneta.estado()
Mifurgoneta.carga(False)
#Herencia multiple
class bicielectrica(V_electricos,Vehiculos):
	def estado(self):
		print("Marca:",self.marca,"\nModelo:",self.modelo,"\nMarcha:",self.marcha,
			"\nAcelerando:",self.arranque,"\nFreno:",self.freno)
miBici=bicielectrica("Orbea","Condor")
miBici.estado()
#Uso de isinstance
print(isinstance("Orbea",Vehiculos))

