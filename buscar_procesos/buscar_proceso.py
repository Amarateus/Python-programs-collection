import os
import subprocess
import sys

try:
    nombre_proceso_ingresado = sys.argv[1].lower()
except IndexError:
    print("Indique el nombre de un proceso.")
    sys.exit()

if os.name == "nt":
    p = subprocess.run(["python","processinfo.py"], capture_output = True ,encoding="cp850")
else:
    p = subprocess.run(["python3","processinfo.py"], capture_output = True ,encoding="cp850")

lineas = p.stdout.strip().split("\n")[3:-1]

for linea in lineas:
    columnas = linea[1:-1].split("|")
    proceso = columnas[1].strip()
    
    if proceso.lower() == nombre_proceso_ingresado:
        pid = columnas[0].strip()
        try:
            usuario = columnas[2].strip()
        except IndexError:
            # En algunos procesos no aparece el usuario.
            usuario = ""
        print(f"PID: {pid}. Usuario: {usuario}.")
