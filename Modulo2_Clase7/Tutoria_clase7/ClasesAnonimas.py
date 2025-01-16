#CLASES MAS PEQUEMAS Y FACILES DE TRABJAR Y LIMITADA, como para un prototipo
#SE PUEDEN CONVINAR CON CLASES INTERNAS Y EXTERNAS
Producto = type('productos',(),{'nombre': None, 'precio': None})

producto1 = Producto()
producto1.nombre = 'laptop'
producto1.precio = 1500

print(f'producto: {producto1.nombre}, precio: {producto1.precio}')
