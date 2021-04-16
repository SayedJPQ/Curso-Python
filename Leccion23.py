#Polimorfismo
class auto():
	def desplazamiento(self):
		print("Me desplazo en 4 ruedas")
class moto():
	def desplazamiento(self):
		print("Me desplazo en 2 ruedas")
class camion():
	def desplazamiento(self):
		print("Me desplazo en 6 ruedas")
def DesplazamientoVehiculo(Vehiculo):
	vehiculo.desplazamiento()
miVehiculo=camion()
DesplazamientoVehiculo(miVehiculo)
