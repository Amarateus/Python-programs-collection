import pymysql
from tabulate import tabulate
import os

# conn = sqlite3.connect("productos.sqlite")
# cursor = conn.cursor()

def ingresar_int(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except TypeError:
            print("Error: Ingrese un numero")

def agregar_productos(producto_id, nombre, precio):
    conn = pymysql.connect(
        host = "127.0.0.1",
        port = 3306,
        user = "root",
        passwd = "",
        db = "comercio" 
    )
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO productos VALUES (%s, %s, %s)", (producto_id, nombre, precio))
    except pymysql.ProgrammingError:
        cursor.execute("CREATE TABLE productos (id INT, nombre TEXT, precio INT)")
        cursor.execute("INSERT INTO productos VALUES (%s, %s, %s)", (producto_id, nombre, precio))
    conn.commit()
    conn.close()
    print("¡Producto guardado con exito!")

def ver_productos():
    conn = pymysql.connect(
        host = "127.0.0.1",
        port = 3306,
        user = "root",
        passwd = "",
        db = "comercio" 
    )
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM productos")
        datos = cursor.fetchall()
    except pymysql.ProgrammingError:
        datos = None
        print("La tabla esta vacia")
    conn.close()
    return datos
    
    
################ PROGRAMA #################
if os.name == "nt":
    borrar = "cls"
else:
    borrar = "clear"

salir = True

while salir:
    print("""
    Menu:
    1 - Agregar productos
    2 - Ver productos
    3 - Salir
    """)
    opcion = ingresar_int("Elija una opcion:")
    if opcion == 1:
        print("Ingrese los datos del producto:")
        id_producto = ingresar_int("id producto: ")
        nombre_producto = input("Nombre producto: ")
        precio_producto = ingresar_int("precio producto: $")
        agregar_productos(id_producto, nombre_producto, precio_producto)
    elif opcion == 2:
        productos = ver_productos()
        if productos:
            print(tabulate(productos, headers=["ID", "NOMBRE", "PRECIO $"]))
        else:
            print("No hay productos")
    elif opcion == 3:
        print("Gracias por usar nuestro programa!")
        salir = False          
    else:
        print("Error de opcion. Vuelva a intentar")
    input("Toque ENTER para continuar...")
    os.system(borrar)
