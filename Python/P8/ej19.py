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

    apariciones:dict[str, int] = {}
    lineas:list[str] = archivo.readlines()
    archivo.close()
    for linea in lineas:
        palabras:list[str] = linea.split() # Uso split() que es de python, pero ya hice una funcion que funciona practicamente igual
        for palabra in palabras:
            if not apariciones.get(palabra):
                apariciones[palabra] = 0
            apariciones[palabra] += 1
    
    if apariciones.get(palabra_buscada): 
        res = apariciones[palabra_buscada]

    return res