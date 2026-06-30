# Ejercicio 1
a = 10
b = input("Introduce un número: ")
result = a / b  # Error: TypeError. 'b' es un string (input() devuelve str) y no se puede dividir un int entre un str
print(f"Resultado: {result}")
numbers = [1, 2, 3]
print(numbers[5])  # Error: IndexError. La lista tiene 3 elementos (indices 0, 1, 2), el indice 5 no existe