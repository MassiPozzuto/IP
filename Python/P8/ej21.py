from typing import TextIO
"""
Implementar una solución para el siguiente problema.
    problema la_palabra_mas_frecuente (in nombre_archivo: seq⟨Char⟩) : seq⟨Char⟩ {
        requiere: {nombre_archivo es un archivo existente y accesible que tiene, por lo menos, una palabra}
        asegura: {res es una palabra que aparece en el archivo nombre archivo}
        asegura: {No hay ninguna palabra contenida en el archivo nombre archivo que aparezca más veces que la palabra res }
    }
Para resolver el problema se aconseja utilizar un diccionario de palabras.
"""
from ej19 import cantidad_de_apariciones_lista

def la_palabra_mas_frecuente(nombre_archivo:str) -> str:
    archivo:TextIO = open(nombre_archivo, "r", encoding="utf8")

    lineas:list[str] = archivo.readlines()
    archivo.close()
    apariciones:dict[str, int] = cantidad_de_apariciones_lista(lineas)

    palabra_mas_frecuente:str = list(apariciones.items())[1]
    for palabra, cant_apariciones in apariciones.items():
        if cant_apariciones > palabra_mas_frecuente[1]:
            palabra_mas_frecuente = (palabra, cant_apariciones)

    return palabra_mas_frecuente[0]
