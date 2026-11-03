import csv
import matplotlib.pyplot as plt

def menu_principal():

    while True:

        print("\n========== MENU PRINCIPAL ==========")
        print("1. Explorar directorio")
        print("2. Procesar textos")
        print("3. Analizar dataset CSV")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            explorar_directorio()

        elif opcion == "2":
            submenu_textos()

        elif opcion == "3":
            submenu_csv()

        elif opcion == "4":
            print("Programa finalizado.")
            break

        else:
            print("Opción inválida.")



def explorar_directorio():

    print("\nArchivos disponibles:")
    print("1. Datos/RomeoyJulieta.txt")
    print("2. Datos/satena.csv")


def submenu_textos():

    lineas = leer_texto("Datos/RomeoyJulieta.txt")

    if len(lineas) == 0:
        return

    while True:

        print("\n===== ROMEO Y JULIETA =====")
        print("1. Resumen estadístico")
        print("2. Gráfico de palabras")
        print("3. Histograma de líneas")
        print("4. Volver")

        opcion = input("Seleccione: ")

        if opcion == "1":

            resumen_texto(lineas)

        elif opcion == "2":

            grafico_palabras(lineas)

        elif opcion == "3":

            grafico_longitudes(lineas)

        elif opcion == "4":

            break

        else:

            print("Opción inválida.")


def leer_texto(nombre_archivo):

    try:

        with open(
            nombre_archivo,
            "r",
            encoding="utf-8"
        ) as archivo:

            lineas = archivo.readlines()

        return lineas

    except:

        print("Error al abrir el archivo.")
        return []


def frecuencias(lineas, n):

    conectores = [
    "el", "la", "los", "las",
    "de", "del", "y", "e",
    "a", "en", "un", "una",
    "unos", "unas",
    "que", "por", "para",
    "con", "sin",
    "se", "su", "sus",
    "es", "son", "era",
    "eran", "ser",
    "al", "lo", "le",
    "les", "como", "ya",
    "más", "menos",
    "o", "u", "mi",
    "tu", "su", "no", 
    "si", "te" ,"me"
]

    contador = {}

    for linea in lineas:

        palabras = linea.lower().split()

        for palabra in palabras:

            palabra = palabra.strip(
                ".,;:!?()[]{}\"'"
            )

            if palabra != "" and palabra not in conectores:

                if palabra in contador:

                    contador[palabra] += 1

                else:

                    contador[palabra] = 1

    resultado = []

    cantidad = min(n, len(contador)) #Minimo valor de palabras 

    for i in range(cantidad):

        mayor_palabra = ""
        mayor_cantidad = 0

        for palabra in contador:

            if contador[palabra] > mayor_cantidad:

                mayor_palabra = palabra
                mayor_cantidad = contador[palabra]

        resultado.append(
            (mayor_palabra, mayor_cantidad)
        )

        del contador[mayor_palabra]

    return resultado


def resumen_texto(lineas):

    if len(lineas) == 0:

        print("Texto vacío.")
        return

    total_lineas = len(lineas)

    total_palabras = 0
    total_caracteres = 0
    total_sin_espacios = 0

    for linea in lineas:

        total_palabras += len(linea.split())
        total_caracteres += len(linea)
        total_sin_espacios += len(
            linea.replace(" ", "")
        )

    print("\n===== RESUMEN =====")

    print("Líneas:", total_lineas)
    print("Palabras:", total_palabras)
    print("Caracteres:", total_caracteres)
    print("Caracteres sin espacios:", total_sin_espacios)

    print("\nTOP 5 PALABRAS")

    top = frecuencias(lineas, 5)

    for palabra, cantidad in top:

        print(palabra, "-", cantidad)


def grafico_palabras(lineas):

    datos = frecuencias(lineas, 10)

    if len(datos) == 0:

        print("No hay palabras.")
        return

    palabras = []
    cantidades = []

    for palabra, cantidad in datos:

        palabras.append(palabra)
        cantidades.append(cantidad)

    palabras.reverse()
    cantidades.reverse()

    plt.figure(figsize=(10, 6))

    plt.barh(
        palabras,
        cantidades
    )

    plt.title("10 Palabras Más Frecuentes")
    plt.xlabel("Frecuencia")
    plt.ylabel("Palabras")

    plt.tight_layout()

    plt.savefig(
        "Graficos/grafico_palabras.png"
    )
    plt.show()
    plt.close()

    print("Gráfico guardado.")


def grafico_longitudes(lineas):

    if len(lineas) == 0:

        print("No hay líneas.")
        return

    longitudes = []

    for linea in lineas:

        longitudes.append(len(linea))

    plt.figure(figsize=(12, 6))

    plt.hist(
        longitudes,
        bins=30,
        edgecolor="black"
    )

    plt.grid(axis="y", linestyle="--")

    plt.title(
        "Distribución de Longitud de Líneas"
    )

    plt.xlabel(
        "Cantidad de Caracteres"
    )

    plt.ylabel(
        "Frecuencia"
    )

    plt.tight_layout()

    plt.savefig(
        "Graficos/grafico_longitudes.png"
    )

    plt.show()

    plt.close()

    print("Gráfico guardado.")

def submenu_csv():

    cabeceras, filas = leer_csv(
        "Datos/satena.csv"
    )

    if len(filas) == 0:
        return

    while True:

        print("\n===== AEROPUERTOS SATENA =====")
        print("1. Vista previa")
        print("2. Estadísticas")
        print("3. Gráfico de líneas")
        print("4. Gráfico de pastel")
        print("5. Gráfico de dispersión")
        print("6. Volver")

        opcion = input("Seleccione: ")

        if opcion == "1":

            vista_previa(
                cabeceras,
                filas
            )

        elif opcion == "2":

            estadisticas(
                cabeceras,
                filas
            )

        elif opcion == "3":

            grafico_lineas(
                cabeceras,
                filas
            )

        elif opcion == "4":

            grafico_pastel(
                cabeceras,
                filas
            )

        elif opcion == "5":

            grafico_dispersion(
                cabeceras,
                filas
            )

        elif opcion == "6":

            break

        else:

            print("Opción inválida.")


def leer_csv(nombre_archivo):

    try:

        with open(
            nombre_archivo,
            "r",
            encoding="utf-8"
        ) as archivo:

            lector = csv.reader(archivo)

            filas = list(lector)

        cabeceras = filas[0]
        datos = filas[1:]

        return cabeceras, datos

    except:

        print("Error al abrir CSV.")
        return [], []


def convertir_numero(valor):

    try:

        valor = valor.replace(",", "")
        return float(valor)

    except:

        return None


def vista_previa(cabeceras, filas):

    print("\nCABECERAS:\n")

    print(cabeceras)

    print("\nPRIMERAS 10 FILAS\n")

    for fila in filas[:10]:

        print(fila)

    print("\nULTIMAS 5 FILAS\n")

    for fila in filas[-5:]:

        print(fila)


def estadisticas(cabeceras, filas):

    print("\nCOLUMNAS DISPONIBLES:\n")

    for columna in cabeceras:
        print("-", columna)

    nombre_columna = input(
        "\nIngrese una columna numérica: "
    )

    if nombre_columna not in cabeceras:

        print("La columna no existe.")
        return

    indice = cabeceras.index(
        nombre_columna
    )

    numeros = []

    for fila in filas:

        numero = convertir_numero(
            fila[indice]
        )

        if numero is not None:

            numeros.append(numero)

    if len(numeros) == 0:

        print(
            "La columna no contiene números."
        )
        return

    numeros.sort() #ordenar de mayor a menor

    promedio = sum(numeros) / len(numeros)

    medio = len(numeros) // 2

    if len(numeros) % 2 == 0:

        mediana = (
            numeros[medio - 1]
            + numeros[medio]
        ) / 2

    else:

        mediana = numeros[medio]

    print("\n===== ESTADÍSTICAS =====")

    print("Registros válidos:", len(numeros))
    print("Promedio:", promedio)
    print("Mediana:", mediana)
    print("Mínimo:", min(numeros))
    print("Máximo:", max(numeros))


def grafico_lineas(cabeceras, filas):

    print("\nCOLUMNAS DISPONIBLES:\n")

    for columna in cabeceras:
        print("-", columna)

    columna_x = input(
        "\nIngrese columna X: "
    )

    columna_y = input(
        "Ingrese columna Y: "
    )

    if columna_x not in cabeceras:

        print("La columna X no existe.")
        return

    if columna_y not in cabeceras:

        print("La columna Y no existe.")
        return

    indice_x = cabeceras.index(columna_x)
    indice_y = cabeceras.index(columna_y)

    x = []
    y = []

    for fila in filas:

        numero = convertir_numero(
            fila[indice_y]
        )

        if numero is not None:

            x.append(
                fila[indice_x]
            )

            y.append(
                numero
            )

    if len(y) < 2:

        print("Datos insuficientes.")
        return

    plt.figure(figsize=(12, 6))

    plt.plot(x, y)

    plt.title("Gráfico de Líneas")

    plt.xlabel(columna_x)
    plt.ylabel(columna_y)

    plt.xticks(rotation=90)

    plt.tight_layout()

    plt.savefig(
        "Graficos/grafico_lineas.png"
    )

    plt.show()
    plt.close()

    print("Gráfico guardado.")


def grafico_pastel(cabeceras, filas):

    print("\nCOLUMNAS DISPONIBLES:\n")

    for columna in cabeceras:
        print("-", columna)

    columna = input(
        "\nIngrese una columna categórica: "
    )

    if columna not in cabeceras:

        print("La columna no existe.")
        return

    indice = cabeceras.index(
        columna
    )

    contador = {}

    for fila in filas:

        valor = fila[indice]

        if valor != "":

            if valor in contador:

                contador[valor] += 1

            else:

                contador[valor] = 1

    if len(contador) == 0:

        print("No hay categorías.")
        return

    etiquetas = list(
        contador.keys()
    )

    cantidades = list(
        contador.values()
    )

    plt.figure(figsize=(7, 7))

    plt.pie(
        cantidades,
        labels=etiquetas,
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title(columna)

    plt.axis("equal")

    plt.savefig(
        "Graficos/grafico_pastel.png"
    )

    plt.show()
    plt.close()

    print("Gráfico guardado.")


def grafico_dispersion(cabeceras, filas):

    print("\nCOLUMNAS DISPONIBLES:\n")

    for columna in cabeceras:
        print("-", columna)

    columna_x = input(
        "\nIngrese columna numérica X: "
    )

    columna_y = input(
        "Ingrese columna numérica Y: "
    )

    if columna_x not in cabeceras:

        print("Columna X inválida.")
        return

    if columna_y not in cabeceras:

        print("Columna Y inválida.")
        return

    indice_x = cabeceras.index(columna_x)
    indice_y = cabeceras.index(columna_y)

    x = []
    y = []

    for fila in filas:

        numero_x = convertir_numero(
            fila[indice_x]
        )

        numero_y = convertir_numero(
            fila[indice_y]
        )

        if (
            numero_x is not None
            and numero_y is not None
        ):

            x.append(numero_x)
            y.append(numero_y)

    if len(x) < 2:

        print("Datos insuficientes.")
        return

    plt.figure(figsize=(8, 5))

    plt.scatter(x, y)

    plt.title("Gráfico de Dispersión")

    plt.xlabel(columna_x)
    plt.ylabel(columna_y)

    plt.tight_layout()

    plt.savefig(
        "Graficos/grafico_dispersion.png"
    )

    plt.show()
    plt.close()

    print("Gráfico guardado.")


menu_principal()