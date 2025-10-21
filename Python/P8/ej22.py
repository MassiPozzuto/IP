from typing import TextIO
"""
Implementar una solución para el siguiente problema.
    problema clonar_sin_comentarios (in nombre_archivo_entrada: seq⟨Char⟩, in nombre_archivo_salida: seq⟨Char⟩) {
        requiere: {nombre_archivo_entrada es el path con el nombre de un archivo existente y accesible}
        requiere: {nombre_archivo_salida es el path con el nombre de un archivo que, si existe, se puede modificar, y si no existe, se puede crear}
        asegura: {El archivo indicado por nombre_archivo_salida contiene las mismas líneas y en el mismo orden que el archivo nombre_archivo_entrada, excepto aquellas que comienzan con el carácter #}
    }
Para este ejercicio vamos a considerar que una línea es un comentario si tiene un '#' como primer carácter de la línea, o si no es el primer carácter, se cumple que todos los anteriores son espacios.
Por ejemplo, si se llama a clonar sin comentarios con un archivo con este contenido:
    # esto es un comentario
    # esto tambien
    esto no es un comentario # esto tampoco
nombre_archivo_salida solo contendrá la última línea:
    esto no es un comentario # esto tampoco
"""

def clonar_sin_comentarios(nombre_archivo_entrada:str, nombre_archivo_salida:str) -> None:
    archivo_entrada:TextIO = open(nombre_archivo_entrada, "r", encoding="utf8")
    lineas:list[str] = archivo_entrada.readlines()
    archivo_entrada.close()

    archivo_salida:TextIO = open(nombre_archivo_salida, "w", encoding="utf8")
    archivo_salida.truncate()
    for linea in lineas:
        if primer_caracter(linea) != '#': archivo_salida.write(linea)
    
    archivo_salida.close()

def primer_caracter(string: str) -> str:
    for letra in string:
        if letra != " " and letra != "\t":
            return letra
    return ""