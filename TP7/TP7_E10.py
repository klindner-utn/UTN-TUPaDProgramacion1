# Ejercicio 10
# Diccionario original: pais - capital
paises = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "Uruguay": "Montevideo",
}

print("Original: ", paises)

# Construimos un nuevo diccionario invirtiendo claves y valores
capitales = {}
for pais, capital in paises.items():
    capitales[capital] = pais

print("Invertido: ", capitales)