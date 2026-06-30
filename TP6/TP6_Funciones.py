import math

# TP 6 - Funciones

def saludo(nombre):
    return f"Hola, {nombre}!"

print(saludo("Ana"))

# Ejercicio 1
def imprimir_hola_mundo():
    print("Hola Mundo!")

# Ejercicio 2
def saludar_utuario(nombre):
    return f"Hola {nombre}!"

# Ejercicio 3
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# Ejercicio 4
def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

# Ejercicio 5
def segundos_a_horas(segundos):
    return segundos / 3600

# Ejercicio 6
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# Ejercicio 7
def operaciones_basicas(a, b):
    return (a + b, a - b, a * b, a / b)

# Ejercicio 8
def calcular_imc(peso, altura):
    return peso / altura ** 2

# Ejercicio 9
def celsius_a_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

# Ejercicio 10
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

# Programa Principal con llamados a funciones

# Ej1
imprimir_hola_mundo()

# Ej2
nombre = input("Ingresa tu nombre: ")
print(saludar_utuario(nombre))

# Ej3
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = input("Ingresa tu edad: ")
residencia = input("Ingresa tu residencia: ")
informacion_personal(nombre, apellido, edad, residencia)

# Ej4
radio = float(input("Ingresa el radio del círculo: "))
print(f"Área: {calcular_area_circulo(radio):.2f}")
print(f"Perímetro: {calcular_perimetro_circulo(radio):.2f}")

# Ej5
segundos = float(input("Ingresa la cantidad de segundos: "))
print(f"Horas: {segundos_a_horas(segundos):.2f}")

# Ej6
numero = int(input("Ingresa un numero para ver su tabla de multiplicar: "))
tabla_multiplicar(numero)

# Ej7
a = float(input("Ingresa el primer numero: "))
b = float(input("Ingresa el segundo numero: "))
suma, resta, producto, division = operaciones_basicas(a, b)
print(f"Suma: {suma}, Resta: {resta}, Multiplicacion: {producto}, Division: {division}")

# Ej8
peso = float(input("Ingresa tu peso en KG (Kilogramos): "))
altura = float(input("Ingresa tu altura en M (Metros): "))
print(f"Tu IMC es: {calcular_imc(peso, altura):.2f}")

# Ej9
celsius = float(input("Ingrese la temperatura en Celsius: "))
print(f"Temperatura en Fahrenheit: {celsius_a_fahrenheit(celsius):.2f}")

# Ej10
a = float(input("Ingrese el primer numero: "))
b = float(input("Ingrese el segundo numero: "))
c = float(input("Ingrese el tercer numero: "))
print(f"Promedio: {calcular_promedio(a, b, c):.2f}")

def saludo(nombre):
    return f"Hola, {nombre}!"

print(saludo("Ana"))