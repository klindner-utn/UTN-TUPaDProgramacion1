# TP 5 - Listas

#1
notas = [4, 10, 7, 9, 8, 5, 6, 8, 9, 7]
print("Lista de notas:", notas)

total = 0

for nota in notas:
    total += nota

promedio = total / len(notas)
print("Promedio:", promedio)

nota_max = notas[0]
nota_min = notas[0]

for nota in notas:
    if nota > nota_max:
        nota_max = nota
    if nota < nota_min:
        nota_min = nota

print("Nota mas alta:", nota_max)
print("Nota mas baja:", nota_min)

#2
productos = []

# Ingresamos 5 productos
for i in range(5):
    producto = input(f"Ingrese el nombre del producto {i+1}: ")

    # Verificamos que el nombre ingresado sea valido
    while not producto.isalpha() or producto == "":
      producto = input("Nombre invalido, ingrese un nombre de producto valido: ")

    productos.append(producto)

# Mostramos la lista ordenada alfabeticamente
productos_ordenados = sorted(productos)
print("Lista de productos ordenada: ")
for producto in productos_ordenados:
    print(producto, end=" ")

# Preguntamos que producto eliminar
producto_eliminar = input("\nQue producto desea eliminar? ")

# Verificamos que el producto a eliminar se encuentre en la lista
while producto_eliminar not in productos:
    producto_eliminar = input("\nProducto no encontrado, que producto desea eliminar? ")

# Eliminamos el producto indicado
productos.remove(producto_eliminar)

print("\nLista de productos actualizada: ")
for producto in productos:
    print(producto, end=" ")

#3
import random
numeros = []
for i in range(15):
    numeros.append(random.randint(1, 100))

print("\nLista completa: ")
for num in numeros:
    print(num, end=" ")

# Creamos listas de pares e impares
pares = []
impares = []

for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

# Imprimimos los resultados
print(f"\nLa cantidad de numeros pares es {len(pares)}, los cuales son: ")
for par in pares:
    print(par, end=" ")

print(f"\nLa cantidad de numeros impares es {len(impares)}, los cuales son: ")
for impar in impares:
    print(impar, end=" ")

#4
datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]

# Eliminamos los duplicados creando un set y luego convirtiendo a lista
datos_sin_duplicados = list(set(datos))

# Mostramos el resultado
print(f"\nLa lista sin duplicados es: ")
for dato in datos_sin_duplicados:
    print(dato, end=" ")

#5
estudiantes = ["Juan", "Pedro", "Karen", "Mauro", "Ana", "Laura", "Jorge", "Maximiliano"]

print("\nLista de estudiantes:")
for est in estudiantes:
    print(est, end=" ")

opcion = input("\nDesea agregar (A) o eliminar (E) un estudiante? ").upper()

if opcion == "A":
    nuevo = input("Ingrese el nombre del estudiante a agregar: ")
    estudiantes.append(nuevo)

elif opcion == "E":
    eliminar = input("Ingrese el nombre del estudiante a eliminar: ")
    if eliminar in estudiantes:
        estudiantes.remove(eliminar)
    else:
        print("\nEse estudiante no esta en la lista")

else:
    print("\nOpción no valida")

# Mostramos la lista final
print("\nLista final de estudiantes:")
for est in estudiantes:
    print(est, end=" ")

#6
numeros = [10, 11, 12, 13, 14, 15, 16]
print("\nLista original:")
for num in numeros:
    print(num, end=" ")

ultimo = numeros[-1]   
for i in range(len(numeros)-1, 0, -1): 
    numeros[i] = numeros[i-1]
numeros[0] = ultimo

print("\nLista rotada:")
for num in numeros:
    print(num, end=" ")

#7
temperaturas = [
    [5, 18],
    [3, 20],
    [7, 15],
    [2, 22],
    [6, 19],
    [4, 25],
    [8, 16]
  ]

dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

suma_min = 0
suma_max = 0
mayor_amplitud = 0
dia_amplitud = 0

# Calulamos la amplitud termica y el dia correspondiente
for i in range(7):
    suma_min += temperaturas[i][0]
    suma_max += temperaturas[i][1]
    amplitud = temperaturas[i][1] - temperaturas[i][0]
    if amplitud > mayor_amplitud:
        mayor_amplitud = amplitud
        dia_amplitud = i

print(f"\nPromedio de minimas: {suma_min / 7:.2f}")
print(f"\nPromedio de maximas: {suma_max / 7:.2f}")
print(f"\nMayor amplitud termica: {dias[dia_amplitud]} ({mayor_amplitud:.2f} grados)")

#8
notas_estudiantes = [
    [8, 7, 9],
    [6, 5, 7],
    [10, 9, 8],
    [4, 6, 5],
    [7, 8, 6]
]

# Promedio de cada estudiante
print("\nPromedio por estudiante:")
for i in range(5):
    suma = 0
    for j in range(3):
        suma += notas_estudiantes[i][j]
    print(f"\nEstudiante {i+1}: {suma / 3:.2f}")

# Promedio de cada materia
print("\nPromedio por materia:")
for j in range(3):
    suma = 0
    for i in range(5):
        suma += notas_estudiantes[i][j]
    print(f"\nMateria {j+1}: {suma / 5:.2f}")

#9
print("\nTa-Te-Ti!")
tablero = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
  ]

jugador = "X"

for turno in range(9):
    
    # Muestro el tablero actualizado
    for fila in tablero:
        print(" ".join(fila))

    fila = int(input(f"Jugador {jugador}, ingrese fila (0-2): "))
    col = int(input(f"Jugador {jugador}, ingrese columna (0-2): "))

    while fila < 0 or fila > 2 or col < 0 or col > 2 or tablero[fila][col] != "-":
        print("Posicion invalida u ocupada, intente de nuevo.")
        fila = int(input(f"Jugador {jugador}, ingrese fila (0-2): "))
        col = int(input(f"Jugador {jugador}, ingrese columna (0-2): "))

    tablero[fila][col] = jugador

    # Cambio turno jugador
    jugador = "O" if jugador == "X" else "X"

# Muestro como queda el tablero final
for fila in tablero:
    print(" ".join(fila))
print("\nTablero completo!")

#10
ventas = [
    [10, 20, 30, 40, 50, 60, 70],
    [15, 25, 35, 45, 55, 65, 75],
    [20, 30, 40, 50, 60, 70, 80],
    [5, 10, 15, 20, 25, 30, 35]
]
productos_nombres = ["Producto 1", "Producto 2", "Producto 3", "Producto 4"]

print("\nTotal vendido por producto:")

max_producto_total = 0
max_producto_idx = 0

# Calculamos el total vendido por producto y por dia
for i in range(4):
    total_prod = 0
    for j in range(7):
        total_prod += ventas[i][j]
    print(f"\n  {productos_nombres[i]}: {total_prod}")
    if total_prod > max_producto_total:
        max_producto_total = total_prod
        max_producto_idx = i

max_dia_total = 0
max_dia_idx = 0

for j in range(7):
    total_dia = 0
    for i in range(4):
        total_dia += ventas[i][j]
    if total_dia > max_dia_total:
        max_dia_total = total_dia
        max_dia_idx = j

# Mostramos resultados
print(f"\nDia con mayores ventas: Dia {max_dia_idx + 1} ({max_dia_total} unidades)")
print(f"\nProducto mas vendido: {productos_nombres[max_producto_idx]} ({max_producto_total} unidades)")

#11
estudiantes_lista = ["Ana", "Belen", "Carlos", "Diana", "Elena", "Fabian", "Gabriela", "Hugo", "Irene", "Julia"]

buscar = input("Ingrese el nombre a buscar: ")

encontrado = False

# Buscamos el elemento en la lista
for i in range(len(estudiantes_lista)):
    if estudiantes_lista[i] == buscar:
        print(f"\n{buscar} se encuentra en la posicion {i + 1}")
        encontrado = True
        break

if not encontrado:
    print(f"\n{buscar} no esta en la lista")


#12
numeros_lista = []

# Pedimos 8 numeros y los agregamos a la lista
for i in range(8):
    num = int(input(f"Ingrese el numero {i+1}: "))
    numeros_lista.append(num)

print("\nLista original:")
for num in numeros_lista:
    print(num, end=" ")

# Ordenamos la lista de forma ascendente y descendente
ordenada_asc = sorted(numeros_lista)
print("\nLista ordenada de menor a mayor:")
for num in ordenada_asc:
    print(num, end=" ")

ordenada_desc = sorted(numeros_lista, reverse=True)
print("\nLista ordenada de mayor a menor:")
for num in ordenada_desc:
    print(num, end=" ")

#13
puntajes = [450, 1200, 875, 990, 300, 1500, 640]

mas_alto = puntajes[0]
mas_bajo = puntajes[0]

# Calculamos puntaje mas alto y bajo
for p in puntajes:
    if p > mas_alto:
        mas_alto = p
    if p < mas_bajo:
        mas_bajo = p

print(f"\nPuntaje mas alto: {mas_alto}")
print(f"\nPuntaje mas bajo: {mas_bajo}")

# Creamos ranking y mostramos posicion del puntaje 990
ranking = sorted(puntajes, reverse=True)
print("Ranking:")
for i in range(len(ranking)):
    print(f"  {i+1}. {ranking[i]}")

for i in range(len(ranking)):
    if ranking[i] == 990:
        print(f"El puntaje 990 esta en la posicion {i + 1} del ranking")
        break
