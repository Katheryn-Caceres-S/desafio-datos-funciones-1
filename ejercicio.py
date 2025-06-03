
#crear lista de productos 
#id, nombre, detalle, precio

productos = [
    ["001", "telefono", "nuevo", 100],
    ["002", "telefono", "nuevo", 100,[1,2,3,[1,2,3]]],
    ["003", "telefono", "nuevo", 100],
    ["003", "telefono", "nuevo", 100]
]

#con append se agregan datos a la lista

productos.append(["005","telefono","nuevo",100])

productos[0][1]="telefono"

productos[2][1]= "telefono"

productos[1][4][2] = 12

#-1 quiere decir el ultimo de la lista

eliminado = productos[1].pop(4)
productos[-1].remove("telefono")

print(eliminado)

print(productos)

#indicar donde se debe guardar algo
#append guarda al final de lista
#insert inserta un objeto antes del indice

navidad = ["8","navidad","nuevo",100]
navidad2 = ["9","cena-navidad","nuevo",100]

productos.insert(3,navidad)
productos.insert(5,navidad2)



print(productos)
