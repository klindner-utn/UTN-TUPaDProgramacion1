def cargar_csv(path):
    """Lee el CSV y devuelve una lista de diccionarios con los datos de países.
    Convierte población y superficie a int. Omite filas con formato inválido"""
    paises = []
    try:
        with open(path, "r", encoding="utf-8") as f:
            # Saltamos la linea de encabezado
            f.readline()
            for linea in f:
                linea = linea.strip()
                if not linea:
                    continue
                campos = linea.split(",")
                if len(campos) != 4:
                    print("WARN: Se omitió una fila con formato inválido.")
                    continue
                try:
                    # Parseamos los datos del pais a un diccionario
                    pais = {
                        "nombre": campos[0].strip(),
                        "poblacion": int(campos[1]),
                        "superficie": int(campos[2]),
                        "continente": campos[3].strip()
                    }
                    paises.append(pais)
                except ValueError:
                    print("WARN: Se omitió una fila con formato inválido.")
    except FileNotFoundError:
        print(f"ERROR: No se encontró el archivo '{path}'.")
        return None
    except Exception as e:
        print(f"ERROR: Ocurrió un error al leer el archivo: {e}")
        return None
    return paises


def guardar_csv(path, paises):
    """Escribe la lista de países al archivo CSV, sobreescribiendo el contenido"""
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write("nombre,poblacion,superficie,continente\n")
            for pais in paises:
                f.write(f"{pais['nombre']},{pais['poblacion']},{pais['superficie']},{pais['continente']}\n")
    except Exception as e:
        print(f"ERROR: Ocurrió un error al guardar el archivo: {e}")
