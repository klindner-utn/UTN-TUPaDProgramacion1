# TP Integrador - Repetitivas, Condicionales y Secuenciales
# Ejercicio 4 - Escape Room: La Boveda

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
intentos_forzar = 0

# Solicitamos y validamos el nombre del agente
nombre_agente = input("\nIngrese el nombre del agente: ").strip()
while not nombre_agente.isalpha():
  print("ERROR: El nombre ingresado es invalido")
  nombre_agente = input("\nIngrese el nombre del agente: ").strip()

print(f"\nBienvenido agente {nombre_agente}...")

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:
  # Condicion de corte por alarma
  if alarma and tiempo <= 3:
    print("\nSistema bloqueado por alarma! DERROTA")
    break

  print(f"""\nEstado: 
        Energia={energia},
        Tiempo={tiempo},
        Cerraduras={cerraduras_abiertas}/3,
        Alarma={'SI' if alarma else 'NO'}""")
  
  print("\nMenu Principal")

  print("""
        1) Forzar cerradura
        2) Hackear panel 
        3) Descansar """)

  opcion = input("\nSeleccione una opcion: ").strip()

  while not opcion.isdigit() or int(opcion) not in [1, 2, 3]:
    print("ERROR: La opcion seleccionada es invalida")
    opcion = input("\nSeleccione una opcion: ").strip()
  
  if opcion == "1":
    # Registramos el intento de forzar la cerradura
    intentos_forzar += 1
    # Cobramos el costo
    energia -= 20
    tiempo -= 2

    # Si forzamos 3 veces seguidas, se activa la alarma
    if intentos_forzar >= 3:
      alarma = True
      print("La cerradura se trabo! Alarma activada!")

    # Riesgo de alarma si energia es menor a 40
    elif energia < 40:
      print("Riesgo de alarma!")
      numero_alarma = input("Elija un numero entre 1 y 3: ").strip()
      while not numero_alarma.isdigit() or int(numero_alarma) not in [1, 2, 3]:
        print("ERROR: El numero ingresado es invalido")
        numero_alarma = input("Elija un numero entre 1 y 3: ").strip()

      # Si el numero ingresado es 3, se activa la alarma
      if numero_alarma == "3":
        alarma = True
        print("Alarma activada!")
      else:
        cerraduras_abiertas += 1
        print("Cerradura abierta!")
    
    # Si no hay alarma, abrimos la cerradura
    elif not alarma:
      cerraduras_abiertas += 1
      print("Cerradura abierta!")

  elif opcion == "2":
    # Reseteamos el contador de forzar cerradura
    intentos_forzar = 0
    # Cobramos el costo
    energia -= 10
    tiempo -= 3
    # Condicion de corte si ya se consiguio hackear el panel
    if len(codigo_parcial) >= 8:
      print("Ya se ha obtenido el codigo completo")
      continue
    else:
      print("Hackeando panel...")
      for i in range(4):
        codigo_parcial += "X"
        print(f"Paso {i+1}: {codigo_parcial}")
      print("Codigo parcial:", codigo_parcial)

    if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
      cerraduras_abiertas += 1
      print("Codigo descifrado, cerradura abierta!")

  # Opcion 3
  else:
    # Reseteamos el contador de forzar cerradura
    intentos_forzar = 0

    if alarma:
      energia -= 10
      print("ALARMA ACTIVADA! -10 de energia extra")

    energia += 15
    if energia > 100:
      energia = 100

    tiempo -= 1
    print(f"Descansando... Energia={energia} | Tiempo={tiempo}")

# Resultado final
if cerraduras_abiertas == 3:
  print(f"\nFelicitaciones agente {nombre_agente}! Boveda abierta! VICTORIA!")
elif energia <= 0:
  print(f"\nAgente {nombre_agente}, te quedaste sin energia... DERROTA!")
elif tiempo <= 0:
  print(f"\nAgente {nombre_agente}, se acabo el tiempo... DERROTA!")
