# TP Integrador - Repetitivas, Condicionales y Secuenciales
# Ejercicio 5 - Escape Room: La Arena Del Gladiador

print("\n--- BIENVENIDO A LA ARENA ---")

# Configuracion del personaje
nombre_gladiador = input("\nIngrese el nombre del gladiador: ").strip()
while not nombre_gladiador.isalpha():
  print("ERROR: Solo se permiten letras")
  nombre_gladiador = input("\nIngrese el nombre del gladiador: ").strip()

# Inicializacion de estadisticas
vida_gladiador = 100
vida_enemigo = 100
pociones_vida = 3
danio_base_ataque_pesado = 15
danio_base_enemigo = 12
turno_gladiador = True

# Ciclo de combate
print("\n=== INICIO DEL COMBATE ===")
while vida_gladiador > 0 and vida_enemigo > 0:
  if turno_gladiador:
    # Muestra vida y pociones
    print(f"Gladiador {nombre_gladiador} (HP: {vida_gladiador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones_vida}")

    # Muestra menu opciones
    print("""
          Elige accion:
          1. Ataque Pesado
          2. Ráfaga Veloz
          3. Curar
          """)
    
    opcion = input("Opcion: ")
    while not opcion.isdigit() or opcion not in ["1", "2", "3"]:
      print("ERROR: Ingrese un numero valido")
      opcion = input("- Opcion: ")

    # Ataque pesado
    if opcion == "1":
      # Hacemos una copia para no modificar el valor original del daño base
      danio = danio_base_ataque_pesado
      if vida_enemigo < 20:
        # Golpe critico
        danio *= 1.5
      vida_enemigo -= danio
      print(f"\n>>> Atacaste al enemigo por {danio} puntos de daño!")
    
    # Rafaga veloz
    elif opcion == "2":
      for i in range(3):
        vida_enemigo -= 5
        print("\n>>> Golpe conectado por 5 de daño")
    
    # Curar
    elif opcion == "3":
      if pociones_vida > 0:
        vida_gladiador += 30
        pociones_vida -= 1
        print("\n>>> Te has curado! +30 HP")
        # Evitamos que vida supere 100 HP
        if vida_gladiador > 100:
          vida_gladiador = 100
      else:
        print("\n- No quedan pociones!")
    
    # Finalizamos turno jugador
    turno_gladiador = False

  # Turno enemigo
  else:
    vida_gladiador -= danio_base_enemigo
    print("\n>>> El enemigo te ataco por 12 puntos de daño!")

    # Finalizamos turno enemigo
    turno_gladiador = True
    print("\n=== NUEVO TURNO ===")

# Termino el ciclo de combate
if vida_gladiador > 0:
  # El jugador gano
  print(f"\nVICTORIA! El gladiador {nombre_gladiador} ha ganado la batalla")

else:
  # El judagor perdio
  print("\nDERROTA. Has caido en combate...")