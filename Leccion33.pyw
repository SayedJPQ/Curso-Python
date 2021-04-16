#Uso de TKinter
from tkinter import *
raiz=Tk()
raiz.title("Ventana de prueba")
#(Ancho,Alto) Se puede usar 1 y 0 o true o false
raiz.resizable(0,0)
raiz.iconbitmap("Iconopython.ico")
raiz.geometry("300x200")
raiz.config(bg="red")
raiz.config(relief=("sunken"))
raiz.config(bd=20)
#Uso de frames
#Todo esto sirve tambien para la raiz
miFrame = Frame()
#miFrame.pack(fill="both", expand=True)
miFrame.pack(side="left", anchor="s")
miFrame.config(bg="blue")
miFrame.config(width="150",height="100")
miFrame.config(bd=25)
miFrame.config(relief=("groove"))
miFrame.config(cursor="pirate")
raiz.mainloop()