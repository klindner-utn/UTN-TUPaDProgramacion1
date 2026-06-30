# Ejercicio 7
while True:
  try:
      numero = float(input("Ingrese un numero: "))
      print(numero)
      break
  except ValueError:
      print("Debe ingresar un numero valido")
  except Exception as e:
      print(f"Se produjo un error inesperado: {e}")
