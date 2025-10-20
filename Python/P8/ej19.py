#Implementar una solución para cada uno de los siguientes problemas.
"""
1. 
    problema contar_lineas (in nombre_archivo: seq⟨Char⟩) : Z {
        requiere: {nombre_archivo es el path con el nombre de un archivo existente y accesible}
        asegura: {res es igual a la cantidad de líneas que contiene el archivo indicado por nombre_archivo}
    }
"""
def contar_linea(nombre_archivo:str) -> int:
    archivo = open(nombre_archivo, "r", encoding="utf8")
    lineas:list[str] = archivo.readlines()
    archivo.close()

    return len(lineas)

"""
2. 
    problema existe_palabra (in nombre_archivo: seq⟨Char⟩, in palabra: seq⟨Char⟩) : Bool {
        requiere: {nombre_archivo es el path con el nombre de un archivo existente y accesible}
        requiere: {palabra no es vacía}
        asegura: {res es verdadero si y solo si palabra aparece al menos una vez en el archivo indicado por nombre_archivo}
    }
"""
def existe_palabra(nombre_archivo:str, palabra:str) -> bool:
    archivo = open(nombre_archivo, "r", encoding="utf8")
    res:bool = palabra in archivo.read()
    archivo.close()

    return res

"""
3. 
    problema cantidad_de_apariciones (in nombre_archivo: seq⟨Char⟩, in palabra: seq⟨Char⟩) : Z {
        requiere: {nombre_archivo es el path con el nombre de un archivo existente y accesible}
        requiere: {palabra no es vacía}
        asegura: {res es la cantidad de veces que palabra aparece en el archivo indicado por nombre_archivo}
    }
"""
def cantidad_de_apariciones(nombre_archivo:str, palabra_buscada:str) -> int:
    res:bool = 0
    archivo = open(nombre_archivo, "r", encoding="utf8")

    lineas:list[str] = archivo.readlines()
    archivo.close()

    apariciones:dict[str, int] = cantidad_de_apariciones_lista(lineas)
    
    if palabra_buscada in apariciones.keys(): 
        res = apariciones[palabra_buscada]

    return res

def cantidad_de_apariciones_lista(string: list[str]) -> dict[str, int]:
    apariciones:dict[str, int] = {}
    for linea in string:
        palabras:list[str] = linea.split() # Uso split() que es de python, pero ya hice una funcion que funciona practicamente igual
        for palabra in palabras:
            if palabra not in apariciones.keys():
                apariciones[palabra] = 0
            apariciones[palabra] += 1

    return apariciones