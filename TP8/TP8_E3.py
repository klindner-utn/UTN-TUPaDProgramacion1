# Ejercicio 3
a = 10
b = input("Introduce un número: ")
try:
    result = a / b
    print(f"Resultado: {result}")
except TypeError:
    print("Error: No se puede dividir un entero por un string")

numbers = [1, 2, 3]
try:
    print(numbers[5])
except IndexError:
    print("Error: El índice no existe en la lista")