
#crear lista de productos 
#id, nombre, detalle, precio

productos = [
    ["001", "telefono", "nuevo", 100],
    ["002", "telefono", "nuevo", 100,[1,2,3]],
    ["003", "telefono", "nuevo", 100],
    ["003", "telefono", "nuevo", 100]
]

#con append se agregan datos a la lista

productos.append(["005","telefono","nuevo",100])

productos[0][1]="telefono"

productos[2][1]= "telefono"

productos[1][4][2] = 12

#-1 quiere decir el ultimo de la lista
productos.remove([1][-1])
productos.pop()

print(productos)