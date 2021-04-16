from tkinter import *
from tkinter import filedialog
root=Tk()
def abrefichero():
	fichero=filedialog.askopenfilename(title="Abrir", initialdir="C:/", filetypes=(("Imagenes","*.jpg"),
		("Dibujos de alta calidad", "*.png"),("Todos los ficheros","*.*")))
	print(fichero)
Button(root, text="Abrir fichero", command=abrefichero).pack()
root.mainloop()