from validaciones import validar_texto, validar_entero, validar_opcion

# Modulo con lógica de negocio

# Agregar país

def agregar_pais(paises):
    """Solicita datos al usuario y agrega un nuevo país a la lista"""
    nombre = validar_texto("Nombre del país: ")
    # Verificar duplicado (case-insensitive)
    if any(p["nombre"].lower() == nombre.lower() for p in paises):
        print(f"ERROR: '{nombre}' ya existe en el dataset de países")
        return None
    poblacion = validar_entero("Población: ")
    superficie = validar_entero("Superficie (km²): ")
    continente = validar_texto("Continente: ")
    pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }
    paises.append(pais)
    print(f"País '{nombre}' agregado exitosamente")
    return pais


# Actualizar país

def actualizar_pais(paises):
    """Permite actualizar población y/o superficie de un país existente"""
    nombre = validar_texto("Nombre del país a actualizar: ")
    pais = next((p for p in paises if p["nombre"].lower() == nombre.lower()), None)
    if not pais:
        print(f"No se encontró el país '{nombre}'.")
        return False
    print(f"País encontrado: {pais['nombre']} | Población: {pais['poblacion']} | Superficie: {pais['superficie']}")
    pais["poblacion"] = validar_entero("Nueva población: ")
    pais["superficie"] = validar_entero("Nueva superficie (km²): ")
    print("País actualizado exitosamente")
    return True


# Buscar país

def buscar_pais(paises):
    """Busca países por nombre (coincidencia parcial, case-insensitive)"""
    termino = validar_texto("Ingrese nombre a buscar: ").lower()
    resultados = [p for p in paises if termino in p["nombre"].lower()]
    mostrar_lista(resultados, "búsqueda")


# Filtrar país

def filtrar_paises(paises):
    """Submenú de filtrado por continente, rango de población o superficie"""
    print("\n--- Filtrar por ---")
    print("1. Continente")
    print("2. Rango de población")
    print("3. Rango de superficie")
    opcion = validar_opcion("Seleccione filtro: ", ["1", "2", "3"])

    if opcion == "1":
        continente = validar_texto("Continente: ")
        resultados = [p for p in paises if p["continente"].lower() == continente.lower()]
    elif opcion == "2":
        minimo = validar_entero("Población mínima: ", 0)
        maximo = validar_entero("Población máxima: ")
        resultados = [p for p in paises if minimo <= p["poblacion"] <= maximo]
    else:
        minimo = validar_entero("Superficie mínima (km²): ", 0)
        maximo = validar_entero("Superficie máxima (km²): ")
        resultados = [p for p in paises if minimo <= p["superficie"] <= maximo]

    mostrar_lista(resultados, "filtro")


# Ordenar países

def ordenar_paises(paises):
    """Submenú de ordenamiento por nombre, población o superficie"""
    print("\n--- Ordenar por ---")
    print("1. Nombre")
    print("2. Población")
    print("3. Superficie")
    campo_opcion = validar_opcion("Seleccione campo: ", ["1", "2", "3"])
    orden = validar_opcion("Orden (asc/desc): ", ["asc", "desc"])

    campos = {"1": "nombre", "2": "poblacion", "3": "superficie"}
    campo = campos[campo_opcion]
    descendente = orden == "desc"

    ordenados = sorted(paises, key=lambda p: p[campo] if isinstance(p[campo], int) else p[campo].lower(), reverse=descendente)
    mostrar_lista(ordenados, "ordenamiento")


# Estadisticas

def mostrar_estadisticas(paises):
    """Muestra estadísticas: mayor/menor población, promedios, cantidad por continente"""
    if not paises:
        print("No hay países cargados")
        return

    mayor_pob = max(paises, key=lambda p: p["poblacion"])
    menor_pob = min(paises, key=lambda p: p["poblacion"])
    prom_pob = sum(p["poblacion"] for p in paises) // len(paises)
    prom_sup = sum(p["superficie"] for p in paises) // len(paises)

    # Cantidad por continente
    continentes = {}
    for p in paises:
        continentes[p["continente"]] = continentes.get(p["continente"], 0) + 1

    print("\n--- Estadísticas ---")
    print(f"Mayor población: {mayor_pob['nombre']} ({mayor_pob['poblacion']:,})")
    print(f"Menor población: {menor_pob['nombre']} ({menor_pob['poblacion']:,})")
    print(f"Promedio de población: {prom_pob:,}")
    print(f"Promedio de superficie: {prom_sup:,} km²")
    print("Cantidad de países por continente:")
    for cont, cant in continentes.items():
        print(f"  {cont}: {cant}")


# Listar formato tabla

def mostrar_lista(paises, contexto):
    """Muestra una lista de países en formato tabla"""
    if not paises:
        print(f"No se encontraron resultados para {contexto}")
        return
    print(f"\n{'Nombre':<20} {'Población':>15} {'Superficie':>12} {'Continente':<15}")
    print("-" * 65)
    for p in paises:
        print(f"{p['nombre']:<20} {p['poblacion']:>15,} {p['superficie']:>12,} {p['continente']:<15}")
    print(f"\nTotal: {len(paises)} país(es)")
