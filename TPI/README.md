# Gestión de Datos de Países en Python - TPI Programacion 1

Aplicación de consola desarrollada en Python que permite gestionar información sobre países, aplicando listas, diccionarios, funciones, estructuras condicionales y repetitivas, ordenamientos y estadísticas a partir de un dataset en formato CSV.

## Integrantes

- Kenneth Lindner

## Instrucciones de uso

### Requisitos

- Python 3.x

### Ejecución

```bash
python3 main.py
```

El programa cargará automáticamente el archivo `paises.csv` y mostrará un menú interactivo con las siguientes opciones:

1. Agregar país
2. Actualizar país (población y superficie)
3. Buscar país por nombre (coincidencia parcial)
4. Filtrar países (por continente, rango de población o superficie)
5. Ordenar países (por nombre, población o superficie, ascendente o descendente)
6. Mostrar estadísticas
7. Mostrar todos los países
8. Salir

## Ejemplos de entradas/salidas

### Buscar un país

```
Seleccione una opción: 3
Ingrese nombre a buscar: arg

Nombre                     Población   Superficie Continente     
-----------------------------------------------------------------
Argentina                 45,376,763    2,780,400 América        

Total: 1 país(es).
```

### Mostrar estadísticas

```
Seleccione una opción: 6

--- Estadísticas ---
Mayor población: India (1,428,627,663)
Menor población: Australia (26,473,055)
Promedio de población: 244,777,417
Promedio de superficie: 2,754,384 km²
Cantidad de países por continente:
  América: 3
  Asia: 2
  Europa: 2
  África: 2
  Oceanía: 1
```

### Agregar un país

```
Seleccione una opción: 1
Nombre del país: Chile
Población: 19493184
Superficie (km²): 756102
Continente: América
País 'Chile' agregado exitosamente.
```

## Estructura del proyecto

```
TPI/
├── main.py          # Menú principal y flujo del programa
├── archivo.py       # Lectura y escritura del archivo CSV
├── paises.py        # Lógica de negocio (CRUD, filtros, ordenamiento, estadísticas)
├── validaciones.py  # Validación de entradas del usuario
├── paises.csv       # Dataset base
└── README.md
```

## Documentación

- [Informe PDF](./TPI_Programacion1_Lindner.pdf)

## Video demostrativo

- [Link al video]([https://drive.google.com/file/d/1VtE-lNsRe3y1yr9VRBX4oSDmoK7LK5Rv/view?usp=sharing])
