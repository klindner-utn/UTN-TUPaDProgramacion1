# TP Integrador - Repetitivas, Condicionales y Secuenciales
# Ejercicio 3 - Agenda de Turnos con Nombres (Sin listas)

# Validacion del nombre del operador (solo letras)
nombre_operador = input("Ingrese su nombre: ").strip()
while not nombre_operador.isalpha() or nombre_operador == "":
    nombre_operador = input("Nombre invalido, ingrese un nombre valido: ").strip()

# Inicialización de turnos vacíos ("")
lunes_turno1 = lunes_turno2 = lunes_turno3 = lunes_turno4 = ""
martes_turno1 = martes_turno2 = martes_turno3 = ""

# Bucle principal del sistema
while True:
    print("\nMenu Principal")
    print("1) Reservar turno 2) Cancelar turno 3) Ver agenda 4) Resumen general 5) Salir")
    opcion = input("Opcion: ").strip()

    # Validacion de opcion ingresada
    if not opcion.isdigit():
        print("ERROR: Ingrese un numero valido")
        continue

    opcion = int(opcion)

    if opcion < 1 or opcion > 5:
        print("ERROR: Opcion fuera de rango")
        continue

    # Reserva de turno
    if opcion == 1:
        dia = input("Dia (1 = Lunes, 2 = Martes): ").strip()
        while dia not in ["1", "2"]:
            print("ERROR: El dia ingresado es invalido")
            dia = input("Dia (1 = Lunes, 2 = Martes): ").strip()

        nombre_paciente = input("Ingrese el nombre del paciente: ").strip()
        while not nombre_paciente.isalpha():
            print("ERROR: El nombre ingresado es invalido")
            nombre_paciente = input("Ingrese el nombre del paciente: ").strip()

        # Normalizamos el nombre para que la logica sea case insensitive
        nombre_paciente = nombre_paciente.upper()

        # Reserva para el Lunes
        if dia == "1":
            if nombre_paciente in [lunes_turno1, lunes_turno2, lunes_turno3, lunes_turno4]:
                print(f"El paciente {nombre_paciente.capitalize()} ya está registrado para el Lunes")
            else:
                if lunes_turno1 == "":
                    lunes_turno1 = nombre_paciente
                elif lunes_turno2 == "":
                    lunes_turno2 = nombre_paciente
                elif lunes_turno3 == "":
                    lunes_turno3 = nombre_paciente
                elif lunes_turno4 == "":
                    lunes_turno4 = nombre_paciente
                else:
                    print("No hay mas turnos disponibles para el Lunes")
                    continue

                print(f"Turno reservado para el paciente {nombre_paciente.capitalize()} el dia Lunes")

        # Reserva para el Martes
        else:
            if nombre_paciente in [martes_turno1, martes_turno2, martes_turno3]:
                print(f"El paciente {nombre_paciente.capitalize()} ya está registrado para el Martes")
            else:
                if martes_turno1 == "":
                    martes_turno1 = nombre_paciente
                elif martes_turno2 == "":
                    martes_turno2 = nombre_paciente
                elif martes_turno3 == "":
                    martes_turno3 = nombre_paciente
                else:
                    print("No hay mas turnos disponibles para el Martes")
                    continue

                print(f"Turno reservado para el paciente {nombre_paciente.capitalize()} el dia Martes")

    # Cancelacion de turno
    elif opcion == 2:
        dia = input("Dia (1 = Lunes, 2 = Martes): ").strip()
        if dia not in ["1", "2"]:
            print("ERROR: El dia ingresado es invalido")
            dia = input("Dia (1 = Lunes, 2 = Martes): ").strip()

        nombre_paciente = input("Ingrese el nombre del paciente: ").strip()
        if not nombre_paciente.isalpha():
            print("ERROR: El nombre ingresado es invalido")

        # Normalizamos el nombre para que la logica sea case insensitive
        nombre_paciente = nombre_paciente.upper()

        encontrado = False

        # Cancelacion para el dia Lunes
        if dia == "1":
            if lunes_turno1 == nombre_paciente:
                lunes_turno1 = ""
                encontrado = True
            elif lunes_turno2 == nombre_paciente:
                lunes_turno2 = ""
                encontrado = True
            elif lunes_turno3 == nombre_paciente:
                lunes_turno3 = ""
                encontrado = True
            elif lunes_turno4 == nombre_paciente:
                lunes_turno4 = ""
                encontrado = True

        # Cancelacion para el dia Martes
        else:
            if martes_turno1 == nombre_paciente:
                martes_turno1 = ""
                encontrado = True
            elif martes_turno2 == nombre_paciente:
                martes_turno2 = ""
                encontrado = True
            elif martes_turno3 == nombre_paciente:
                martes_turno3 = ""
                encontrado = True

        if encontrado:
            print(f"El turno para el paciente {nombre_paciente.capitalize()} ha sido cancelado")
        else:
            print(f"El paciente {nombre_paciente.capitalize()} no registra turnos en sistema")

    # Visualizar agenda del dia
    elif opcion == 3:
        dia = input("Dia (1 = Lunes, 2 = Martes): ").strip()
        while dia not in ["1", "2"]:
            print("ERROR: El dia ingresado es invalido")
            dia = input("Dia (1 = Lunes, 2 = Martes): ").strip()

        if dia == "1":
            print("\nAgenda Lunes:")
            print(f"Turno 1: {lunes_turno1 if lunes_turno1 != '' else 'DISPONIBLE'}")
            print(f"Turno 2: {lunes_turno2 if lunes_turno2 != '' else 'DISPONIBLE'}")
            print(f"Turno 3: {lunes_turno3 if lunes_turno3 != '' else 'DISPONIBLE'}")
            print(f"Turno 4: {lunes_turno4 if lunes_turno4 != '' else 'DISPONIBLE'}")

        elif dia == "2":
            print("\nAgenda Martes:")
            print(f"Turno 1: {martes_turno1 if martes_turno1 != '' else 'DISPONIBLE'}")
            print(f"Turno 2: {martes_turno2 if martes_turno2 != '' else 'DISPONIBLE'}")
            print(f"Turno 3: {martes_turno3 if martes_turno3 != '' else 'DISPONIBLE'}")


    # Resumen general de turnos
    elif opcion == 4:

        # Conteo manual de ocupados
        ocupados_lunes = sum([lunes_turno1 != "", lunes_turno2 != "", lunes_turno3 != "", lunes_turno4 != ""])
        ocupados_martes = sum([martes_turno1 != "", martes_turno2 != "", martes_turno3 != ""])

        disponibles_lunes = 4 - ocupados_lunes
        disponibles_martes = 3 - ocupados_martes

        print("\nResumen:")
        print(f"Lunes - Turnos ocupados: {ocupados_lunes}, turnos libres: {disponibles_lunes}")
        print(f"Martes - Turnos ocupados: {ocupados_martes}, turnos libres: {disponibles_martes}")

        # Determina que dia tiene mas turnos
        if ocupados_lunes > ocupados_martes:
            print("Dia con mas turnos tomados: Lunes")
        elif ocupados_martes > ocupados_lunes:
            print("Dia con mas turnos tomados: Martes")
        else:
            print("Ambos dias tienen la misma cantidad de turnos tomados")

    # Salida del sistema
    elif opcion == 5:
        print("Cerrando sistema")
        break
