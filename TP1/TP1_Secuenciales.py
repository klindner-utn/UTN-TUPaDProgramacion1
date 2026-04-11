# TP 1 - Secuenciales

#1
print("Hola Mundo!")

#2
nombre = input("Ingresa tu nombre: ")
print(f"Hola {nombre}!")

#3
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = int(input("Ingresa tu edad: "))
lugar_de_residencia = input("Ingresa tu lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_de_residencia}")

#4
radio = float(input("Ingrese el radio del circulo: "))
area_circulo = 3.14 * (radio**2)
perimetro_circulo = 2 * 3.14 * radio
print(f"El area del circulo es {area_circulo} y su perimetro es {perimetro_circulo}")

#5
cant_segundos = int(input("Ingrese una cantidad de segundos: "))
cant_horas = cant_segundos / 3600
print(f"{cant_segundos} segundos equivalen a {cant_horas} horas")

#6
numero = int(input("Ingrese un numero: "))
numero_por_0 = numero * 0
numero_por_1 = numero * 1
numero_por_2 = numero * 2
numero_por_3 = numero * 3
numero_por_4 = numero * 4
numero_por_5 = numero * 5
numero_por_6 = numero * 6
numero_por_7 = numero * 7
numero_por_8 = numero * 8
numero_por_9 = numero * 9
print(f"""
      La tabla de multiplicar del numero {numero} es: 
      {numero} x 0 = {numero_por_0} 
      {numero} x 1 = {numero_por_1} 
      {numero} x 2 = {numero_por_2} 
      {numero} x 3 = {numero_por_3}
      {numero} x 4 = {numero_por_4}
      {numero} x 5 = {numero_por_5} 
      {numero} x 6 = {numero_por_6}
      {numero} x 7 = {numero_por_7}
      {numero} x 8 = {numero_por_8}
      {numero} x 9 = {numero_por_9}
""")

#7
numero_1 = int(input("Ingrese un numero distinto de 0: "))
numero_2 = int(input("Ingrese otro numero distinto de 0: "))
suma = numero_1 + numero_2
resta = numero_1 - numero_2
multiplicacion = numero_1 * numero_2
division = numero_1 / numero_2
print(f"""
      La suma entre {numero_1} y {numero_2} es {suma}, 
      la resta es {resta}, la multiplicacion es {multiplicacion} 
      y la division es {division}
""")

#8
altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en kilogramos: "))
masa_corporal = peso / (altura ** 2)
print(f"Su masa corporal es de {masa_corporal}")

#9
celsius = float(input("Ingrese una temperatura en grados Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C equivalen a {fahrenheit}°F")

#10
numero_1 = int(input("Ingrese el primer numero: "))
numero_2 = int(input("Ingrese el segundo numero: "))
numero_3 = int(input("Ingrese el tercer numero: "))
promedio = (numero_1 + numero_2 + numero_3) / 3
print(f"El promedio entre {numero_1}, {numero_2} y {numero_3} es {promedio}")
