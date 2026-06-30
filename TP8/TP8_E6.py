# Ejercicio 6
try:
    numero = float(input("Ingrese un número: "))
    print(numero)
except ValueError:
    print("Debe ingresar un numero valido")
except Exception as e:
    print(f"Se produjo un error inesperado: {e}")
