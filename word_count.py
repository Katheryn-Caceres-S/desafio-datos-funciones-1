
import sys

if len(sys.argv) != 2:
    print("python word_count.py 'celsius'")
    sys.exit(1)

archivo = sys.argv[1]

#leer archivo
# "r" es de read leer
#El número de caracteres distintos es: 40
#El número de palabras distintas es: 243

with open(archivo, "r", encoding="utf-8") as f:
    texto = f.read()


total_palabras = texto.split()

letras_distintas = set(texto)
palabras_distintas = set(total_palabras)


print("El número de caracteres distintos es de: ", len(letras_distintas))
print("El número de palabras distintas es de: ", len(palabras_distintas))

