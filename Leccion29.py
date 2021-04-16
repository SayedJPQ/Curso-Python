from io import open
#archivo_texto=open("archivo.txt","w")
#frase="Sirve el programa \npara hoy"
#archivo_texto.write(frase)
#archivo_texto.close()
archivo_texto=open("archivo.txt","r")
#Seek se usa para posicionarse en el caracter del texto deseado
#Este sirve para leer en fragmentos
archivo_texto.seek(len(archivo_texto.read())/2)
texto=archivo_texto.read()
archivo_texto.close()
print(texto)
#archivo_texto=open("archivo.txt","r")
#lineas_texto=archivo_texto.readlines()
#archivo_texto.close()
#print(lineas_texto)
#archivo_texto=open("archivo.txt","a")
#archivo_texto.write("\nBuena ocasion para python")
#archivo_texto.close()