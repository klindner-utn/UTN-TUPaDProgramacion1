# Ejercicio 6
# Solicitamos ingresar los datos de los alumnos
alumnos = {}
for i in range(3):
  nombre = input("Nombre del alumno: ")
  n1 = float(input("Nota 1: "))
  n2 = float(input("Nota 2: "))
  n3 = float(input("Nota 3: "))
  # Utilizamos una tupla para guardar las notas
  alumnos[nombre] = (n1, n2, n3)
# Calculamos e imprimimos el promedio
for nombre, notas in alumnos.items():
   print(f"{nombre}: promedio {sum(notas) / len(notas):.2f}")
