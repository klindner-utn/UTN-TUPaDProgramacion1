# Ejercicio 8
# Diccionario inicial con productos y su stock
stock = {"Manzana": 10, "Banana": 5, "Leche": 8}

# Mostramos el stock inicial
print("Stock actual:", stock)

# Pedimos al usuario el nombre del producto a consultar/modificar
producto = input("Ingrese el nombre del producto: ")

# Verificamos si el producto existe en el diccionario
if producto in stock:
    # Si existe, mostramos su stock actual
    print(f"{producto} tiene {stock[producto]} unidades en stock.")

    # Permitimos agregar unidades al stock existente
    agregar = int(input("Cuántas unidades desea agregar? "))
    stock[producto] += agregar
    print(f"Nuevo stock de {producto}: {stock[producto]} unidades.")
else:
    # Si no existe, lo agregamos como nuevo producto
    print(f"{producto} no existe en el inventario.")
    cantidad = int(input("Con cuántas unidades desea agregarlo? "))
    stock[producto] = cantidad
    print(f"{producto} agregado con {cantidad} unidades.")

# Mostramos el stock final
print("Stock final:", stock)