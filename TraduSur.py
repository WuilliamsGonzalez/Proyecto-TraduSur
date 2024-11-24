import re

# Título del programa, primera interacción con el usuario.
print("****************************")
print("    TraduSur")
print("****************************")
print("¡Bienvenido al traductor interactivo de Tradusur!")
print()

# Diccionario de traducción inglés -> español
diccionario_ingles_a_espanol = {
    "hello": "hola",
    "good": "buenos",
    "morning": "días",
    "how": "cómo",
    "are": "estás",
    "you": "tú",
    "thank": "gracias",
    "bye": "adiós",
    "my": "mi",
    "name": "nombre",
    "is": "es",
    "what": "qué",
    "your": "tu",
    "my": "mi",
    "i": "yo",
    "like": "agradas",
    "friend": "amigo",
    "goodbye": "adiós",
    "how are you?": "¿cómo estás?",
    "what's your name?": "¿cómo te llamas?",
    "i like you": "Me agradas",
    "how's it going?": "¿cómo va todo?"
}

# Diccionario de traducción español -> inglés
diccionario_espanol_a_ingles = {v: k for k, v in diccionario_ingles_a_espanol.items()}

# Función para traducir una palabra
def traducir_palabra(palabra, direccion):
    """
    Función para traducir palabras el metodo está hecho para retornar la palabra, por lo que si no encuentra la palabra en el diccionario
    la deja tal cual, y la repite.
    """
    # Convertir la palabra a minúsculas para evitar problemas con mayúsculas
    palabra = palabra.lower()
    
    if direccion == "ingles_a_espanol":
        # Traducir de inglés a español
        return diccionario_ingles_a_espanol.get(palabra, palabra)
    elif direccion == "espanol_a_ingles":
        # Traducir de español a inglés
        return diccionario_espanol_a_ingles.get(palabra, palabra)
    else:
        return palabra

# Función para manejar mayúsculas y minúsculas en las traducciones
def manejar_mayusculas(palabra_original, palabra_traducida):
    if palabra_original[0].isupper():
        return palabra_traducida.capitalize()
    return palabra_traducida


def separar_palabras_y_puntuacion(oracion):
    """
    Función para separar las palabras de la puntuación usando expresiones regulares
    Se utiliza la libreria "re" para que separe los signos de las palabras
    """
    return re.findall(r'\b\w+\b|[^\w\s]', oracion) 

# Función para traducir una oración completa
def traducir_oracion(oracion, direccion):
    # Separar la oración en palabras y signos de puntuación
    elementos = separar_palabras_y_puntuacion(oracion)
    
    oracion_traducida = []
    
    for palabra in elementos:
        # Traducir las palabras, pero dejar los signos de puntuación y asi no tirar error
        if palabra.isalpha():
            traduccion = traducir_palabra(palabra, direccion)
            traduccion_mayuscula = manejar_mayusculas(palabra, traduccion)
            oracion_traducida.append(traduccion_mayuscula)
        else:
            oracion_traducida.append(palabra)
    
    return " ".join(oracion_traducida)

# Función para mostrar las opciones de traducción
def mostrar_menu():
    print("\nOpciones de traducción:") #\n para hacer el salto de línea
    print("1. Traducir de Inglés a Español")
    print("2. Traducir de Español a Inglés")
    print("3. Salir")

# Función principal que interactúa con el usuario
def traductor():
    while True:
        mostrar_menu()
        
        # Elegir el sentido de la traducción
        direccion = input("\nElige la dirección de la traducción (1, 2 o 3): ")
        
        if direccion == "1":
            direccion = "ingles_a_espanol"
            print("\nTraducción de Inglés a Español")
        elif direccion == "2":
            direccion = "espanol_a_ingles"
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

    """
    una vez traducido se convierte a audio, descargar google trans $ pip install googletrans
    """

# Ejecutar el programa TraduSur
traductor()
