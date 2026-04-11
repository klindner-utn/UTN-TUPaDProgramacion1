# TP Integrador - Repetitivas, Condicionales y Secuenciales
# Ejercicio 1 - Caja del Kiosco

total_sin_descuento = 0
total_con_descuento = 0

nombre_cliente = input("Ingrese nombre del cliente: ")
# Validamos que el nombre ingresado tenga letras y no este vacio
while not nombre_cliente.isalpha() or nombre_cliente == "":
    nombre_cliente = input("Nombre invalido, ingrese un nombre valido: ")

cant_productos = input("Ingrese cantidad de productos a comprar: ")
# Validamos que la cantidad de productos sea un entero positivo
while not cant_productos.isdigit() or int(cant_productos) <= 0:
    cant_productos = input("Cantidad invalida, ingrese una cantidad valida: ")

# Una vez validada la cantidad de productos, convertimos a int
cant_productos = int(cant_productos)

for i in range(int(cant_productos)):
    precio = input(f"Ingrese el precio del producto {i+1}: ")
    while not precio.isdigit():
        precio = input(f"Precio invalido, ingrese precio del producto {i+1}: ")

    # Una vez validado que precio es numero entero, convertimos a int
    precio = int(precio)

    # Llevamos la cuenta de total sin aplicar descuento
    total_sin_descuento += precio

    # Preguntamos si el producto tiene descuento, normalizamos el valor de respuesta
    descuento = input(f"Producto {i+1} posee descuento? (S/N): ").strip().lower()
    while descuento != "s" and descuento != "n":
        descuento = input(f"Respuesta invalida, el producto {i+1} posee descuento? Indique S/N: ").strip().lower()
    
    if descuento == "s":
        # Si tiene descuento, aplicamos el 10%
        precio_final = precio * 0.9
    else:
        # Si no tiene descuento, precio final no cambia
        precio_final = precio

    # Llevamos la cuenta del total con descuento aplicado
    total_con_descuento += precio_final

# Reportamos los datos
print(f"Cliente: {nombre_cliente}")
print(f"Cantidad de productos: {cant_productos}")
print(f"Total sin descuentos: ${total_sin_descuento}")
print(f"Total con descuentos: ${total_con_descuento}")
print(f"Ahorro: ${total_sin_descuento - total_con_descuento}")
print(f"Promedio por producto: ${total_con_descuento/cant_productos:.2f}")
