from tkinter import *
root=Tk()
root.geometry("750x650")
miFrame=Frame(root, width=500, height=450)
miFrame.pack()
miLabel=Label(miFrame, text="Hola mundo", fg="red", font=("Times New Romans",20))
miLabel.place(x=200, y=100)
root.mainloop()