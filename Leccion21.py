#Una clase tiene 3 tipos de variables: Propiedad, Comportamiento, Estado
class Auto():
	#Propiedades
	#Uso de constructor
	def __init__(self):

		self.Largochasis=300
		self.Puertas=4
		#Encapsular
		self.__Llantas=4
		self.Anchochasis=140
		self.Arrancado=False
		self.Marchas=["N","R",1,2,3,4,5,6]
		self.Marcha="N"
	#Comportamientos
	def marcha(self,arranque):
		self.Arrancado=arranque
		if(self.Arrancado):
			chequeo=self.__revision()
		if(self.Arrancado and chequeo):
			self.Marcha=1
			return "Auto en marcha primera"
		elif(self.Arrancado and chequeo==False):
			return "Algo anda mal, no se puede arrancar"
		else:
			self.Marcha="N"
			return "Marcha",self.Marcha
			return "El auto no esta en marcha"
	def estado(self):
		print("El largo de este auto es:",self.__Llantas,"Llantas","Este auto tiene",self.Largochasis,"cm de largo",
			"El ancho de este auto es de:", self.Anchochasis,"cm de ancho","Puertas=",self.Puertas,
			"El auto tiene estas marchas:",self.Marchas)
	def __revision(self):
		print("Realizando revision")
		print("")
		self.gasolina="Ok"
		self.aceite="Ok"
		self.puertas="Cerradas"
		if (self.gasolina=="Ok" and self.aceite=="Ok" and self.puertas=="Cerradas"):
			return True
		else:
			return False
miauto=Auto()
print(miauto.marcha(False))
print("")
miauto.estado()
print("")
print("-----Ahora creamos el siguiente objeto-----")
miauto2=Auto()
print("")
print(miauto2.marcha(True))
print("")
miauto2.estado()
print("")

