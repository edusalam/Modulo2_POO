#SON CASOS DE USOS Y SON REUTILIZABLES
Productos = [
    {'nombre': 'laptop', 'Precio':1500},
    {'nombre': 'celular', 'Precio':1000},
    {'nombre': 'tablet', 'Precio':1600}            
]
productos_ordenados = sorted(Productos, key=lambda x: x['Precio']<1000)
print(productos_ordenados)