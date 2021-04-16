import sqlite3
miConexion=sqlite3.connect("Primera base de datos")
miCursor=miConexion.cursor()
#miCursor.execute("CREATE TABLE Productos (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))") esta linea solo sirve para crear la tabla
#miCursor.execute("INSERT INTO Productos VALUES('Arroz',700,'Comida')") AGregar registro
#Meter varios registros a la vez
#Variosproductos=[
	#("Camisa", 4000, "Deportes"),
	#"Pantalon", 7000, "Deportes"),
	#("Computadora", 250000, "Tecnologia"),
	#("Frijoles", 800, "Comidas")
#]
#miCursor.executemany("INSERT INTO Productos VALUES (?,?,?)", Variosproductos)
miCursor.execute("SELECT * FROM Productos")
Variosproductos=miCursor.fetchall()
for i in Variosproductos:
	print("Nombre Producto: ",i[0]," Precio: ",i[1], " Seccion: ",i[2])
miConexion.commit()
miConexion.close()