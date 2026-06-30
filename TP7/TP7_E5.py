# Ejercicio 5
# Solicitamos la frase
frase = input('Ingrese una frase: ')
# Generamos un array con las palabras de la frase
palabras = frase.split()
# Recorremos cada palabra y la vamos agregando al diccionario
# En caso que ya exista la entrada, le incrementamos la cantidad
recuento = {}
for p in palabras:
  if p in recuento:
      recuento[p] += 1
  else:
      recuento[p] = 1
# Imprimimos las palabras unicas y el recuento
print('Palabras unicas:', set(palabras))
print('Recuento:', recuento)
