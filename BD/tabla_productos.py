import sqlite3

# Coneccion
conn = sqlite3.connect("productos.sqlite")

# Cursor
cursor = conn.cursor()

# Instruccion
cursor.execute("CREATE TABLE productos (id INT, nombre TEXT, precio INT)")
conn.commit()

productos = (
    (1, "Teclado", 25),
    (2, "Mouse", 18),
    (3, "Monitor", 300),
    (4, "Parlantes", 100)
)

for producto in productos:
    cursor.execute("INSERT INTO productos VALUES (?, ?, ?)", producto)
conn.commit()

conn.close()



