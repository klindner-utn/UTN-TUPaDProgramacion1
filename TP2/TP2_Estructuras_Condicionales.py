# TP 2 - Estructuras Condicionales

#1
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Es mayor de edad")

#2
nota = float(input("Ingrese la nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#3
numero = int(input("Ingrese un numero: "))
# Hacemos uso del operador modulo para ver si un numero es par o no
if numero % 2 == 0:
    print("El numero es par")
else:
    print("Por favor ingrese un numero par")

#4
edad = int(input("Ingrese su edad: "))
if edad >= 0 and edad < 12:
    print("Es un niño")
elif edad >= 12 and edad < 18:
    print("Es un adolescente")
elif edad >= 18 and edad < 30:
    print("Es un adulto joven")
elif edad >= 30:
    print("Es un adulto")
else:
    # Edad es < 0, lo cual no es valido
    print("Ingrese una edad valida")

#5
contraseña = input("Ingrese una contraseña de entre 8 y 14 caracteres: ")
# Hacemos uso de len() para saber la cantidad de elementos de una cadena
if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#6
consumo = float(input("Ingrese el consumo mensual en KWh: "))
if consumo < 150:
    print("Consumo bajo")
elif 150 <= consumo <= 300:
    print("Consumo medio")
else:
    print("Consumo alto")
if consumo > 500:
    print("Considere medidas de ahorro energetico")

#7
frase = input("Ingrese una frase o palabra: ")
# Podemos acceder a la ultima posicion de una cadena con [-1]
if frase[-1].lower() in "aeiou":
    frase = frase + "!"
print(frase)

#8
nombre = input("Ingrese su nombre: ")
opcion = input("Ingrese una opcion (1, 2 o 3): ")
if opcion == "1":
    # upper() convierte una cadena a mayusculas
    print(nombre.upper())
elif opcion == "2":
    # lower() convierte una cadena a minusculas
    print(nombre.lower())
elif opcion == "3":
    # title() convierte la primera letra de cada palabra a mayuscula
    print(nombre.title())
else:
    # Si el usuario ingresa un valor distinto a 1, 2 o 3
    print("Opción inválida")

#9
magnitud = float(input("Ingrese la magnitud del terremoto: "))
if magnitud < 3:
    print("Muy leve (imperceptible)")
elif 3 <= magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif 4 <= magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif 5 <= magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif 6 <= magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")

#10
# Usamos strip() para eliminar espacios en blanco y upper() para convertir a mayuscula
hemisferio = input("¿En que hemisferio se encuentra? (N/S): ").strip().upper()
mes = int(input("Ingrese el mes (1-12): "))
dia = int(input("Ingrese el dia: "))

# Establecemos las estaciones segun el hemisferio
if hemisferio == "N":
    if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20):
        estacion = "Verano"
    else:
        estacion = "Otoño"
elif hemisferio == "S":
    if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
        estacion = "Verano"
    elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20):
        estacion = "Invierno"
    else:
        estacion = "Primavera"

print(estacion)