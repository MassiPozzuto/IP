from typing import TextIO
"""
Dado un archivo de texto y una frase, implementar una función agregar_frase_al_principio(in nombre_archivo : str, in frase : str), que agregue la frase al comienzo del archivo original (similar al ejercicio anterior, sin hacer una copia del archivo).
    problema agregar_frase_al_principio (in nombre_archivo: seq⟨Char⟩, in frase: seq⟨Char⟩ ) {
        requiere: {nombre_archivo es el path de un archivo existente y accesible}
        requiere: {frase no es vacía}
        asegura: {frase se agrega como primera línea del archivo nombre_archivo, desplazando las anteriores hacia abajo}
    }
Este problema no crea una copia del archivo de entrada, sino que lo modifica
"""
def agregar_frase_al_principio(nombre_archivo:str, frase:str) -> None:
    archivo:TextIO = open(nombre_archivo, "r+", encoding="utf8")
    contenido:str = archivo.readlines()
    contenido.insert(0, frase + "\n")
    archivo.seek(0) # Llevo el cursor a la posicion inicial... Sino deberia cerrar el archivo y volverlo a abrir...
    archivo.writelines(contenido)
    archivo.close()
