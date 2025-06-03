#conversion de moneda  =sys.argv()

import sys

if len(sys.argv) != 5:
    print("python conversiones.py <sol> <peso_chileno> <dolar> <peso_chileno>")
    sys.exit(1)


sol = float(sys.argv[1])
peso_argentino = float(sys.argv[2])
dolar = float(sys.argv[3])
peso_chileno = int(sys.argv[4])


#diccionario

conversiones = {
    "Soles" : (peso_chileno * sol),
    "Pesos Argentinos" : (peso_chileno * peso_argentino),
    "Dolares Americanos" : (peso_chileno * dolar)
}

print(f"Los {peso_chileno} pesos equivalen a: ")

for k,v in conversiones.items():
    print(v,k)