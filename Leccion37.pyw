from tkinter import *
root=Tk()
Opcion=IntVar()
def gender():
	#print(Opcion.get())
	if Opcion.get()==1:
		Etiqueta.config(text="Has elegido genero Masculino")
	else:
		Etiqueta.config(text="Has elegido genero Femenino")
Label(root, text="Selecciona tu genero").pack()
Radiobutton(root, text="Masculino", variable=Opcion, value=1, command=gender).pack()
Radiobutton(root, text="Femenino", variable=Opcion, value=2, command=gender).pack()
Etiqueta=Label(root)
Etiqueta.pack()
root.mainloop()