# Ejercicio 1
# Inicializamos el diccionario y añadimos mas frutas
precios_frutas = {'Banana': 1200, 'Anana': 2500, 'Melon': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

# Ejercicio 2
# Actualizamos precios
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

# Ejercicio 3
# Lista solo con nombres de frutas
lista_frutas = list(precios_frutas.keys())

# Imprimimos los resultados
print("Diccionario de frutas con precios:", precios_frutas)
print("Lista de frutas:", lista_frutas)