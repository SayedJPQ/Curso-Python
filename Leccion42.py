import sqlite3
miConexion=sqlite3.connect("Inventario")
miCursor=miConexion.cursor()
miCursor.execute("UPDATE Productos SET Precio=5 WHERE NOMBRE_ARTICULO='pelota'")
#Delete es para borrar registros
#miCursor.execute("DELETE FROM Productos WHERE CODIGO_ARTICULO=5)
miConexion.commit()
miConexion.close()
