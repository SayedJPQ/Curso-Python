from tkinter import *
#Uso de grid
raiz=Tk()
#Se puede usar sticky para mover los elementos a algun punto cardinal de la interfaz admite todas las iniciales de cada punto cardinal
#En ingles
miFrame=Frame(raiz, width=600, height=400)
miFrame.pack() 
minombre=StringVar()
Texto1=Entry(miFrame, textvariable=minombre)
Texto1.grid(row=0,column=1)
Texto1.config(fg="red",justify="center")
Texto1.config(show="*")
Texto2=Entry(miFrame)
Texto2.grid(row=1,column=1)
Texto2.config(fg="red",justify="center")
#Uso de text
Texto3=Text(miFrame,width=20,height=5)
Texto3.grid(row=2,column=1)
scroll=Scrollbar(miFrame, command=Texto3.yview)
scroll.grid(row=2,column=2,sticky="nsew")
Texto3.config(yscrollcommand=scroll.set)
Label1=Label(miFrame, text="Nombre",padx=10,pady=5)
Label1.grid(row=0,column=0)
Label2=Label(miFrame, text="Apellido",padx=10,pady=5)
Label2.grid(row=1,column=0)
Label3=Label(miFrame, text="Direccion",padx=10,pady=5)
Label3.grid(row=2,column=0)
def codigoboton():
	minombre.set("Sayed")
Boton1=Button(raiz, text="Enviar", command=codigoboton)
Boton1.pack()
raiz.mainloop()
