import sys

try:
    import psutil
    from tabulate import tabulate
except ModuleNotFoundError:
    print("""
    Faltan instalaciones, Instala con pip :
    pip install psutil
    pip install tabulate    

    ¡Son modulos necesarios para esta experiencia!
    """)
    sys.exit()

encabezado = ["PID", "Process", "User"]

tabla = []

for proc in psutil.process_iter(attrs=["pid", "name", "username"]):
    tabla.append([
        proc.info["pid"],
        proc.info["name"],
        proc.info["username"] or "-"
    ])

print(tabulate(tabla, headers = encabezado, tablefmt="pretty"))

