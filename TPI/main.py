from archivo import cargar_csv, guardar_csv
from paises import (agregar_pais, actualizar_pais, buscar_pais, filtrar_paises, ordenar_paises, mostrar_estadisticas, mostrar_lista)
from validaciones import validar_opcion

PATH_CSV = "paises.csv"


def mostrar_menu():
    """Muestra el menú principal de opciones"""
    print("\n========= GESTIÓN DE PAISES =========")
    print("1. Agregar país")
    print("2. Actualizar país")
    print("3. Buscar país por nombre")
    print("4. Filtrar países")
    print("5. Ordenar países")
    print("6. Mostrar estadísticas")
    print("7. Mostrar todos los países")
    print("8. Salir")
    print("=====================================")


def main():
    """Función principal: carga datos, ejecuta menú en loop"""
    print("Iniciando sesión. Bienvenido!\n")
    paises = cargar_csv(PATH_CSV)
    if paises is None:
        print("INFO: Se iniciará con una lista vacía. Los cambios se guardarán en un nuevo archivo.")
        paises = []
    else:
        print(f"INFO: Se cargaron {len(paises)} países desde '{PATH_CSV}'")

    while True:
        mostrar_menu()
        opcion = validar_opcion("Seleccione una opción: ", [str(i) for i in range(1, 9)])

        if opcion == "1":
            if agregar_pais(paises):
                guardar_csv(PATH_CSV, paises)
        elif opcion == "2":
            if actualizar_pais(paises):
                guardar_csv(PATH_CSV, paises)
        elif opcion == "3":
            buscar_pais(paises)
        elif opcion == "4":
            filtrar_paises(paises)
        elif opcion == "5":
            ordenar_paises(paises)
        elif opcion == "6":
            mostrar_estadisticas(paises)
        elif opcion == "7":
            mostrar_lista(paises, "listado completo")
        elif opcion == "8":
            print("Cerrando sesión. Hasta la próxima!\n")
            break


if __name__ == "__main__":
    main()
