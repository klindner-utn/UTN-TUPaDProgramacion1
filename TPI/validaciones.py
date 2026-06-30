def validar_entero(mensaje, minimo=1):
    """Solicita un entero positivo al usuario. Repite hasta obtener un valor válido"""
    while True:
        entrada = input(mensaje)
        try:
            valor = int(entrada)
            if valor < minimo:
                print(f"ERROR: Debe ser un número mayor o igual a {minimo}")
            else:
                return valor
        except ValueError:
            print("ERROR: Debe ingresar un número entero válido")


def validar_texto(mensaje):
    """Solicita texto no vacío al usuario, sin comas para no corromper el CSV"""
    while True:
        entrada = input(mensaje).strip()
        if not entrada:
            print("ERROR: El campo no puede estar vacío")
        elif "," in entrada:
            print("ERROR: El texto no puede contener comas")
        else:
            return entrada


def validar_opcion(mensaje, opciones):
    """Solicita una opción válida dentro de una lista de opciones permitidas"""
    while True:
        entrada = input(mensaje).strip()
        if entrada in opciones:
            return entrada
        print(f"ERROR: Opción inválida. Opciones válidas: {', '.join(opciones)}")
