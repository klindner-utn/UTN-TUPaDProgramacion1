# Ejercicio 5
a = 10
b = input("Introduce un número: ")
try:
    result = a / b
    numbers = [1, 2, 3]
    print(numbers[5])
except (TypeError, IndexError) as e:
    print(f"Error: {type(e).__name__} - {e}")
else:
    print(f"Resultado: {result}")
finally:
    print("Ejecucion finalizada")