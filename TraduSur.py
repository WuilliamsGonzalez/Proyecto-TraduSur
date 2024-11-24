import re
from gtts import gTTS
import os

# Diccionario de traducción inglés -> español
diccionario_ingles_a_espanol = {
    """Este permite hacer el diccionario, aquí se colocan las palabras que usará el programa
    para traducir, siempre se usa llaves"""
    "hello": "hola",
    "world": "mundo",
    "good": "bueno",
    "morning": "mañana",
    "night": "noche",
    "cat": "gato",
    "dog": "perro",
    "apple": "manzana",
    "tree": "árbol"
}

# Diccionario de traducción español -> inglés
diccionario_espanol_a_ingles = {v: k for k, v in diccionario_ingles_a_espanol.items()}
"""Esto hace que la función sea 
    bidireccional
"""
# Función para traducir una palabra
def traducir_palabra(palabra, direccion):
    """
    Esto permite convertir a minúsculas, para el tratamiento de lo que
    el usuario ingresó, permitiendo que independiente de cómo lo ingrese el usuario
    el código lo trate como minúsculas. Además de hacer la bidirección, con el if y elif.
    """
    palabra = palabra.lower()  # Convertir a minúsculas
    if direccion == "ingles_a_espanol":
        return diccionario_ingles_a_espanol.get(palabra, palabra)
    elif direccion == "espanol_a_ingles":
        return diccionario_espanol_a_ingles.get(palabra, palabra)
    return palabra

# Función para manejar mayúsculas
def manejar_mayusculas(palabra_original, palabra_traducida):
    if palabra_original[0].isupper():
        return palabra_traducida.capitalize()
    return palabra_traducida

# Función para separar palabras y puntuación
def separar_palabras_y_puntuacion(oracion):
    """ Esta función permite que aunque se coloquen signos que son desconocidos para el código
    este permita devolver los mismos e ignorarlos para hacer la traducción."""
    return re.findall(r'\b\w+\b|[^\w\s]', oracion)

# Función para traducir una oración completa
def traducir_oracion(oracion, direccion):
    """Al igual que la anterior, esta función traduce la oración completa. separando las palabras de la puntuación."""
    elementos = separar_palabras_y_puntuacion(oracion)
    oracion_traducida = []

    for palabra in elementos:
        if palabra.isalpha():
            """el isalpha, permite hacer que el código revise que es todo alfabético usando las demás funciones 
            declaradas anteriormente, permite que no haya errores"""
            traduccion = traducir_palabra(palabra, direccion)
            traduccion_mayuscula = manejar_mayusculas(palabra, traduccion)
            oracion_traducida.append(traduccion_mayuscula)
        else:
            oracion_traducida.append(palabra)

    return " ".join(oracion_traducida)

# Función para convertir texto a voz
def convertir_a_voz(texto, idioma):
    """Esta función es la que permite realizar la conversión a archivo de audio
    Importante, hacer la importación de la biblioteca de google translate al principio del 
    código, para instalarlo en su dispositivo."""
    tts = gTTS(text=texto, lang=idioma)
    archivo_audio = "traduccion_audio.mp3"
    tts.save(archivo_audio)
    os.system(f"start {archivo_audio}")

# Función para mostrar el menú
def mostrar_menu():
    """Este muestra el menú para el usuario, dejando claro las opciones que tiene"""
    print("\nOpciones de traducción:")
    print("1. Traducir de Inglés a Español")
    print("2. Traducir de Español a Inglés")
    print("3. Salir")

# Función principal
def traductor():
    """Esta función es la principal que interactúa con el usuario, 
    haciendo que según lo que eliga, se haga una cosa o la otra."""
    while True:
        mostrar_menu()
        direccion = input("\nElige la dirección de la traducción (1, 2 o 3): ")

        if direccion == "1":
            direccion = "ingles_a_espanol"
            idioma_audio = "es"
            print("\nTraducción de Inglés a Español")
        elif direccion == "2":
            direccion = "espanol_a_ingles"
            idioma_audio = "en"
            print("\nTraducción de Español a Inglés")
        elif direccion == "3":
            print("\n¡Gracias por usar TraduSur! ¡Hasta luego!")
            break
        else:
            print("\nOpción no válida. Elige una opción válida.")
            continue

        oracion = input("\nIntroduce la oración que deseas traducir: ")
        oracion_traducida = traducir_oracion(oracion, direccion)
        print(f"La traducción es: {oracion_traducida}\n")

        # Convertir la traducción a voz
        print("Reproduciendo la traducción en voz...")
        convertir_a_voz(oracion_traducida, idioma_audio)

# Ejecutar el programa
"""Esta es la llamada a la función como tal para ejecutar el programa"""
traductor()
