# Ejercicio 4
a = 10
b = input("Introduce un número: ")
try:
    result = a / b
    print(f"Resultado: {result}")
    numbers = [1, 2, 3]
    print(numbers[5])
except (TypeError, IndexError) as e:
    print(f"Error: {type(e).__name__} - {e}")