#Serializacion
import pickle
lista_nombres=["Sayed", "Sara", "Lisandro", "Wendy"]
fichero_bin=open("Lista nombres", "wb")
pickle.dump(lista_nombres, fichero_bin)
fichero_bin.close()
del (fichero_bin)
fichero=open("Lista nombres", "rb")
lista=pickle.load(fichero)
print(lista)