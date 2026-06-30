# Ejercicio 9
# Diccionario donde las claves son tuplas (dia, hora) y los valores son eventos
agenda = {
    ("Lunes", "09:00"): "Reunion de equipo",
    ("Lunes", "14:00"): "Capacitación Python",
    ("Martes", "10:00"): "Entrega de proyecto",
    ("Miércoles", "16:00"): "Revision de código",
}

# Mostramos la agenda completa
print("Agenda:")
for (dia, hora), evento in agenda.items():
    print(f"  {dia} {hora} - {evento}")

# Pedimos al usuario un dia y hora para consultar
dia = input("\nIngrese el dia: ")
hora = input("Ingrese la hora (ej: 09:00): ")

# Usamos la tupla (dia, hora) como clave para buscar el evento
clave = (dia, hora)

if clave in agenda:
    print(f"Actividad: {agenda[clave]}")
else:
    print("No hay actividad programada en ese dia y hora")
