from tkinter import *
from tkinter import messagebox
root=Tk()
def funcionadicional():
	messagebox.showinfo("Titulo", "Texto")
def funcionlicencia():
	messagebox.showwarning("Licencia", "Licencia bajo copyright")
def funcionsalir():
	#valor=messagebox.askquestion("Salir", "Deseas salir?") Se usa yes y en askokcancel se usa booleano
	#El asktrycancel es para reintentar se debe poner el texto para el boton izquierdo
	valor=messagebox.askokcancel("Salir", "Deseas salir?")
	if valor==True:
		root.destroy()
MENU=Menu(root)
root.config(menu=MENU, width=300, height=300)
Menuarchivo=Menu(MENU, tearoff=0)
Menuarchivo.add_command(label="Nuevo")
Menuarchivo.add_command(label="Guardar")
Menuarchivo.add_command(label="Guardar Como")
Menuarchivo.add_separator()
Menuarchivo.add_command(label="Salir", command=funcionsalir)
Edicionarchivo=Menu(MENU)
Edicionarchivo=Menu(MENU, tearoff=0)
Edicionarchivo.add_command(label="Copiar")
Edicionarchivo.add_command(label="Pegar")
Edicionarchivo.add_command(label="Cortar")
Herramientasarchivo=Menu(MENU)
ayudaarchivo=Menu(MENU)
ayudaarchivo=Menu(MENU, tearoff=0)
ayudaarchivo.add_command(label="Licencia", command=funcionlicencia)
ayudaarchivo.add_command(label="Acerca de", command=funcionadicional)
MENU.add_cascade(label="Archivo", menu=Menuarchivo)
MENU.add_cascade(label="Edicion", menu=Edicionarchivo)
MENU.add_cascade(label="Herramientas", menu=Herramientasarchivo)
MENU.add_cascade(label="Ayuda", menu=ayudaarchivo)
root.mainloop()