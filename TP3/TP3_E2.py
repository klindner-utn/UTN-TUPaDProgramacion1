# TP Integrador - Repetitivas, Condicionales y Secuenciales
# Ejercicio 2 - Acceso al Campus y Menu Seguro

# Credenciales correctas
usuario_correcto = "alumno"
clave_correcta = "python123"

# Contador de intentos fallidos y flag de acceso
intentos = 0
acceso_concedido = False

# Bucle de autenticacion que permite hasta 3 intentos
while intentos < 3:
    usuario_ingresado = input("Usuario: ").strip()
    clave_ingresada = input("Clave: ").strip()

    # Validacion de credenciales ingresadas
    if usuario_ingresado == usuario_correcto and clave_ingresada == clave_correcta:
        print("Acceso concedido")
        acceso_concedido = True # Habilita el acceso al menú principal
        break # Sale del bucle de login
    else:
        # Incrementamos contador de intentos fallidos
        intentos += 1
        print(f"Credenciales invalidas. Intento {intentos}/3")

        # Bloqueamos acceso si se realizan los 3 intentos
        if intentos == 3:
            print("Cuenta bloqueada")

# Bucle principal del sistema (solo se ejecuta si el login fue exitoso)
while acceso_concedido:
    print("\nMenu Principal:")
    print("1) Estado 2) Cambiar clave 3) Mensaje 4) Salir")
    opcion = input("\nOpcion: ").strip()

    # Validacion de opcion ingresada
    if not opcion.isdigit():
        print("ERROR: Ingrese un numero valido")
        continue
    else:
        opcion = int(opcion)
        # Opciones validas entre 1 y 4
        if opcion < 1 or opcion > 4:
            print("ERROR: Opcion fuera de rango")
            continue
        elif opcion == 1:
            print("Inscripto")
        elif opcion == 2:
            nueva_clave = input("Nueva clave: ").strip()
            # La clave debe tener 6 o mas caracteres
            if len(nueva_clave) < 6:
                print("ERROR: Minimo 6 caracteres")
            else:
                confirmacion_clave = input("Confirme la nueva clave: ").strip()
                # Las claves deben coincidir para que se pueda cambiar
                if confirmacion_clave == nueva_clave:
                    clave_correcta = nueva_clave
                    print("La clave ha sido cambiada correctamente")
                else:
                    print("ERROR: Las claves ingresadas no coinciden")
        elif opcion == 3:
            print("Dale que hoy terminamos el TP3!")
        elif opcion == 4:
            print("Saliendo del sistema")
            break # Sale del bucle del menu principal
