#Guardado permanente
import pickle
class Persona:
	def __init__(self,nombre,edad,genero):
		self.nombre=nombre
		self.edad=edad
		self.genero=genero
		print("La persona es:", self.nombre)
	def __str__(self):
		return "{} {} {}".format(self.nombre, self.edad, self.genero)
class ListaPersonas:
	personas=[]
	def __init__(self):
		listadepersonas=open("Fichero_externo", "ab+")
		listadepersonas.seek(0)
		try:
			self.personas=pickle.load(listadepersonas)
			print("Se cargaron {} del fichero".format(len(self.personas)))
		except:
			print("El fichero esta vacio")
		finally:
			listadepersonas.close()
			del(listadepersonas)
	def agregaPersonas(self,p):
		self.personas.append(p)
		self.guardarpersonas()
	def mostrarPersonas(self):
		for p in self.personas:
			print(p)
	def guardarpersonas(self):
		listadepersonas=open("Fichero_externo","wb")
		pickle.dump(self.personas, listadepersonas)
		listadepersonas.close()
		del (listadepersonas)
	def mostrarinfo(self):
		print("La informacion del fichero es: ")
		for p in self.personas:
			print (p)
Milista=ListaPersonas()
persona=Persona("Sara", 12, "Femenino")
Milista.agregaPersonas(persona)
Milista.mostrarinfo()