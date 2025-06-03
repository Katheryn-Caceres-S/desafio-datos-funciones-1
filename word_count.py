
import sys

if len(sys.argv) != 2:
    print("python ejemplo.py 'celsius'")
    sys.exit(1)

archivo = sys.argv[1]

#leer archivo
# "r" es de read leer

with open(archivo, "r", encoding="utf-8") as f:
    print(f.read())