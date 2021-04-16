from tkinter import *
from tkinter import messagebox
import sqlite3
#Funciones
def conexiondatabases():
	miconexion=sqlite3.connect("Control de Usuarios")
	micursor=miconexion.cursor()
	try:
		micursor.execute('''
			CREATE TABLE DatosUsuarios (
			ID INTEGER PRIMARY KEY AUTOINCREMENT,
			Nombre_Usuario VARCHAR(50),
			Password VARCHAR(50),
			Apellido VARCHAR(20),
			Direccion VARCHAR(50),
			Comentarios VARCHAR(150))
			''')
		messagebox.showinfo("Bases de datos","Base de datos creada con exito")
	except:
		messagebox.showwarning("Atencion", "La base de datos ya existe")
def salir():
	valor=messagebox.askquestion("Salir", "¿Deseas salir de la aplicacion?")
	if valor=="yes":
		root.destroy()
def limpiar():
	miNombre.set("")
	miID.set("")
	miApellido.set("")
	mipass.set("")
	midireccion.set("")
	comentario.delete(1.0, END)
def crear():
	miconexion=sqlite3.connect("Control de Usuarios")
	micursor=miconexion.cursor()
	datos=miNombre.get(),mipass.get(),miApellido.get(),midireccion.get(),comentario.get("1.0", END)
	"""micursor.execute("INSERT INTO DatosUsuarios VALUES(NULL,'"+ miNombre.get()+
		"','"+ mipass.get()+"','"+ miApellido.get()+"','"+midireccion.get()+"','"+comentario.get("1.0", END)+"')")"""
	micursor.execute("INSERT INTO DatosUsuarios VALUES(NULL,?,?,?,?,?)",(datos))
	miconexion.commit()
	messagebox.showinfo("Operacion exitosa", "Registro insertado con exito")
def leer():
	miconexion=sqlite3.connect("Control de Usuarios")
	micursor=miconexion.cursor()
	micursor.execute("SELECT * FROM DatosUsuarios WHERE ID="+miID.get())
	elUsuario=micursor.fetchall()
	for usuario in elUsuario:
		miID.set(usuario[0])
		miNombre.set(usuario[1])
		mipass.set(usuario[2])
		miApellido.set(usuario[3])
		midireccion.set(usuario[4])
		comentario.insert(1.0, usuario[5])
		miconexion.commit()
def actualizar():
	miconexion=sqlite3.connect("Control de Usuarios")
	micursor=miconexion.cursor()
	datos=miNombre.get(),mipass.get(),miApellido.get(),midireccion.get(),comentario.get("1.0", END)
	"""micursor.execute("UPDATE DatosUsuarios SET Nombre_Usuario='"+miNombre.get() + 
		"',Password='" + mipass.get() +
		"',Apellido='" + miApellido.get() + 
		"',Direccion='" + midireccion.get() +
		"',Comentarios='" + comentario.get("1.0", END) +
		"'WHERE ID=" + miID.get())"""
	micursor.execute("UPDATE DatosUsuarios SET Nombre_Usuario=?, Password=?, Apellido=?, Direccion=?, Comentarios=?" +
		"WHERE ID=" + miID.get(), (datos))
	miconexion.commit()
	messagebox.showinfo("Operacion exitosa", "Registros actualizados con exito")
def eliminar():
	miconexion=sqlite3.connect("Control de Usuarios")
	micursor=miconexion.cursor()
	micursor.execute("DELETE FROM DatosUsuarios WHERE ID=" + miID.get())
	miconexion.commit()
	messagebox.showinfo("Bases de datos", "Registros borrado con exito")
root=Tk()
root.geometry("300x300")
Barramenu=Menu(root)
root.config(menu=Barramenu, width=300, height=300)
databasesmenu=Menu(tearoff=0)
databasesmenu.add_command(label="Conectar", command=conexiondatabases)
databasesmenu.add_command(label="Salir", command=salir)
borrarmenu=Menu(tearoff=0)
borrarmenu.add_command(label="Borrar campos", command=limpiar)
CRUDmenu=Menu(tearoff=0)
CRUDmenu.add_command(label="Crear",command=crear)
CRUDmenu.add_command(label="Leer", command=leer)
CRUDmenu.add_command(label="Actualizar", command=actualizar)
CRUDmenu.add_command(label="Eliminar", command=eliminar)
ayudamenu=Menu(tearoff=0)
ayudamenu.add_command(label="Licencia")
ayudamenu.add_command(label="Acerca de....")
Barramenu.add_cascade(label="Bases de datos", menu=databasesmenu)
Barramenu.add_cascade(label="Borrar", menu=borrarmenu)
Barramenu.add_cascade(label="CRUD", menu=CRUDmenu)
Barramenu.add_cascade(label="Ayuda", menu=ayudamenu)
miFrame=Frame(root)
miFrame.pack()
miID=StringVar()
miNombre=StringVar()
miApellido=StringVar()
mipass=StringVar()
midireccion=StringVar()
CuadroID=Entry(miFrame, textvariable=miID)
CuadroID.grid(row=0, column=1, padx=5, pady=5)
Cuadronombre=Entry(miFrame,textvariable=miNombre)
Cuadronombre.grid(row=1, column=1, padx=5, pady=5)
Cuadronombre.config(fg="red")
Cuadropass=Entry(miFrame,textvariable=mipass)
Cuadropass.grid(row=2, column=1, padx=5, pady=5)
Cuadropass.config(show="*")
CuadroApellido=Entry(miFrame, textvariable=miApellido)
CuadroApellido.grid(row=3, column=1, padx=5, pady=5)
CuadroDireccion=Entry(miFrame,textvariable=midireccion)
CuadroDireccion.grid(row=4, column=1, padx=5, pady=5)
comentario=Text(miFrame, width=15, height=5)
comentario.grid(row=5, column=1, padx=5, pady=5)
Vertical=Scrollbar(miFrame,command=comentario.yview)
Vertical.grid(row=5, column=2, sticky="nsew")
comentario.config(yscrollcommand=Vertical.set)
#Labels
idlabel=Label(miFrame, text="ID")
idlabel.grid(row=0, column=0, sticky="e", padx=5, pady=5)
nombrelabel=Label(miFrame, text="Nombre")
nombrelabel.grid(row=1, column=0, sticky="e", padx=5, pady=5)
passlabel=Label(miFrame, text="Contraseña")
passlabel.grid(row=2, column=0, sticky="e", padx=5, pady=5)
apellidolabel=Label(miFrame, text="Apellido")
apellidolabel.grid(row=3, column=0, sticky="e", padx=5, pady=5)
direccionlabel=Label(miFrame, text="Direccion")
direccionlabel.grid(row=4, column=0, sticky="e", padx=5, pady=5)
comentariolabel=Label(miFrame, text="Comentario")
comentariolabel.grid(row=5, column=0, sticky="e", padx=5, pady=5)
#Botones
miFrame2=Frame(root)
miFrame2.pack()
botoncrear=Button(miFrame2, text="Crear",command=crear)
botoncrear.grid(row=0,column=0,sticky="e", padx=5, pady=10)
botonleer=Button(miFrame2, text="Leer",command=leer)
botonleer.grid(row=0,column=1,sticky="e", padx=5, pady=10)
botonactualizar=Button(miFrame2, text="Actualizar",command=actualizar)
botonactualizar.grid(row=0,column=2,sticky="e", padx=5, pady=10)
botonborrar=Button(miFrame2, text="Borrar",command=eliminar)
botonborrar.grid(row=0,column=3,sticky="e", padx=5, pady=10)
root.mainloop()