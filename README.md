# TraduSur - Traductor Interactivo

**TraduSur** es un traductor interactivo que permite realizar traducciones bidireccionales entre inglés y español. El programa está diseñado para ser fácil de usar y proporciona una experiencia interactiva para traducir palabras y oraciones simples. El proyecto está implementado en Python, utilizando diccionarios, expresiones regulares y una interfaz de menú para la interacción con el usuario.

## Características

- Traducción de palabras individuales y frases comunes.
- Traducción bidireccional: de inglés a español y de español a inglés.
- Mantenimiento de formato de mayúsculas en las traducciones.
- Manejo de puntuación en las oraciones sin alterarlas.
- Interfaz de usuario sencilla con menú de opciones.

## Requisitos

- Python 3.x
- Pip instalación de libería Google Translate
- Visual Studio CODE o Pycharm

## Instalación

1. Asegúrate de tener Python 3.x instalado en tu sistema.
2. Clona o descarga este repositorio.
3. Abre una terminal o línea de comandos.
4. Navega hasta la carpeta donde descargaste el repositorio.
5. Ejecuta el archivo `TraduSur.py`:

   ```bash
   python TraduSur.py
Uso
Al ejecutar el programa, se presentará un menú con tres opciones:

    ```(1)Traducir de Inglés a Español
       (2)Traducir de Español a Inglés
       (3)Salir
El usuario podrá ingresar una oración o palabra para traducir, y el programa devolverá la traducción correspondiente.

Ejecuta en la terminal de Powershell, para instalar la librería:

```bash
   pip install gtts
  ```
Ejemplo de uso:

Entrada:
    ```
    Traducción de Inglés a Español: Hello, how are you?
    ```
Salida:
    ```
    Traducción: Hola, ¿cómo estás?
    ```

Estructura del Código
Diccionario de Traducción:
-Se utilizan dos diccionarios para realizar las traducciones entre inglés y español:

- diccionario_ingles_a_espanol = { ... }
- diccionario_espanol_a_ingles = { ... }

Carpeta PDF
- Este repositorio incluye la documentación que se usó para crear el programa, puedes descargarlo libremente.

Contribuciones
- Este proyecto es de código abierto. Si deseas mejorar el traductor o agregar nuevas características, siéntete libre de hacer un fork del repositorio y enviar un pull request. Cualquier contribución es bienvenida.

Licencia
- Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

**¡Gracias por usar TraduSur!** Esperamos que este traductor interactivo te sea útil para tus proyectos y aprendizaje.

Proyecto creado por **Wuilliams González**
