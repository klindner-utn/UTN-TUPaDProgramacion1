# Ejercicio 7
# Lista con el registro diario de asistencia (puede tener nombres repetidos)
asistencias = ["Ana", "Pedro", "Luis", "Ana", "María", "Pedro", "Ana", "Luis", "Pedro", "María"]
# Mostramos la lista original
print("Lista original:", asistencias)
# Generamos un set para obtener los nombres sin repetir
unicos = set(asistencias)
print("Empleados que asistieron al menos una vez:", unicos)
# Contamos cuántas veces asistio cada empleado usando un diccionario
conteo = {}
for nombre in asistencias:
    if nombre in conteo:
        conteo[nombre] += 1
    else:
        conteo[nombre] = 1
# Imprimimos las asistencias por empleado
print("Asistencias por empleado:", conteo)
