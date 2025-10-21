from typing import TextIO
"""
Implementar una solución para el siguiente problema.
    problema agregar_frase_al_final (in nombre_archivo: seq⟨Char⟩, in frase: seq⟨Char⟩ ) {
        requiere: {nombre_archivo es el path de un archivo existente y accesible}
        requiere: {frase no es vacía}
        asegura: {frase se agrega como una nueva línea al final del archivo nombre_archivo}
    }
Este problema no crea una copia del archivo de entrada, sino que lo modifica
"""
def agregar_frase_al_final(nombre_archivo:str, frase:str) -> None:
    archivo:TextIO = open(nombre_archivo, "r+", encoding="utf8")
    contenido:str = archivo.read()
    if contenido != "" and contenido[len(contenido) - 1] != "\n": 
        archivo.write("\n")
    archivo.write(frase)
    archivo.close()
