# Ejercicio 4
# Generamos la agenda con input del usuario
contactos = {}
for i in range(5):
  nombre = input(f"Ingrese el nombre del contacto {i+1}: ")
  numero = input(f"Ingrese el numero telefonico de {nombre}: ")
  contactos[nombre] = numero
buscar = input("Ingrese nombre del contacto: ")
if buscar in contactos:
  print(f"El numero de {buscar} es: {contactos[buscar]}")
else:
  print(f"No se encontraron resultados para {buscar}")