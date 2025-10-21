from typing import TextIO
"""
Implementar una solución para el siguiente problema.
    problema agrupar_por_longitud (in nombre_archivo: seq⟨Char⟩) : Diccionario⟨Z, Z⟩ {
        requiere: {nombre_archivo es el path con el nombre de un archivo existente y accesible}
        asegura: {Para cada longitud n tal que existe al menos una palabra de longitud n en el archivo indicado por nombre archivo, res[n] es igual a la cantidad de palabras de esa longitud}
        asegura: {No hay otras claves en res que no correspondan a longitudes de palabras presentes en el archivo}
    }

Por ejemplo, el diccionario
    {
        1: 2 ,
        2: 10 ,
        5: 4
    }
indica que se encontraron 2 palabras de longitud 1, 10 palabras de longitud 2 y 4 palabras de longitud 5. Para este ejercicio se consideran como palabras todas aquellas secuencias de caracteres delimitadas por espacios en blanco.
"""
def agrupar_por_longitud(nombre_archivo:str) -> dict[int, int]:
    res:dict[int, int] = {}
    archivo:TextIO = open(nombre_archivo, "r", encoding="utf8")

    lineas:list[str] = archivo.readlines()
    archivo.close()
    for linea in lineas:
        palabras:list[str] = separar_palabras(linea) # Podria usar .split() que es de python
        for palabra in palabras:
            if not res.get(len(palabra)):
                res[len(palabra)] = 0
            res[len(palabra)] += 1

    return res

def separar_palabras(string:str) -> list[str]:
    res:list[str] = []

    palabra_actual:str = ""
    for letra in string:
        if letra not in  [" ", "\n", ".", ",", ";", ":", '"', "'", "¡", "!", "¿", "?", "(", ")", "[", "]", "{", "}", ">", "<"]:
            palabra_actual += letra
        elif palabra_actual != "":
            res.append(palabra_actual)
            palabra_actual = ""
    
    if palabra_actual != "": 
        res.append(palabra_actual)
    return res