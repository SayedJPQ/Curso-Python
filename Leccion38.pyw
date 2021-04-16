from tkinter import *
root=Tk()
root.title("Ejemplo")
playa=IntVar()
montagna=IntVar()
rio=IntVar()
def opciones():
	opcionescogida=""
	if (playa.get()==1):
		opcionescogida+=" Playa"
	if (montagna.get()==1):
		opcionescogida+=" Montaña"
	if (rio.get()==1):
		opcionescogida+=" Rio"
	textofinal.config(text=opcionescogida)
frame=Frame(root)
frame.pack()
Label(frame, text="Elige destinos", width=30).pack()
Checkbutton(root, text="Playa", variable=playa, onvalue=1, offvalue=0, command=opciones).pack()
Checkbutton(root, text="Montaña",variable=montagna, onvalue=1, offvalue=0, command=opciones).pack()
Checkbutton(root, text="Rio",variable=rio, onvalue=1, offvalue=0, command=opciones).pack()
textofinal=Label(frame)
textofinal.pack()
root.mainloop()