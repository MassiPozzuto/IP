from typing import TextIO
"""
Implementar una solución para el siguiente problema.
    problema invertir_lineas (in nombre_archivo_entrada: seq⟨Char⟩, in nombre_archivo_salida: seq⟨Char⟩ ) {
        requiere: {nombre_archivo_entrada es el path de un archivo de texto existente y accesible}
        requiere: {nombre_archivo_salida es el path con el nombre de un archivo que, si existe, se puede modificar, y si no existe, se puede crear}
        asegura: {El archivo indicado por nombre_archivo_salida contiene las mismas líneas que el archivo nombre_archivo_entrada, pero en orden inverso}
    }
Por ejemplo, si el archivo contiene lo siguiente:
        Esta es la primera linea .
        Y esta es la segunda .
debe generar:
        Y esta es la segunda .
        Esta es la primera linea .
"""
def invertir_lineas(nombre_archivo_entrada:str, nombre_archivo_salida:str) -> None: 
    archivo_entrada:TextIO = open(nombre_archivo_entrada, "r", encoding="utf8")
    lineas:list[str] = archivo_entrada.readlines()
    archivo_entrada.close()

    truncate(nombre_archivo_salida) # Vacio el archivo
    archivo_salida:TextIO = open(nombre_archivo_salida, "w", encoding="utf8")
    for i in range(len(lineas) -1, -1, -1):
        linea:str = lineas[i] + ('\n' if len(lineas) - 1 == i else '')
        archivo_salida.write(linea)

    archivo_salida.close()

def truncate(nombre_archivo:str) -> None:
    archivo_entrada:TextIO = open(nombre_archivo, "w+", encoding="utf8") # 'w+' para leer y escribir
    lineas:list[str] = archivo_entrada.readlines()
    for _ in lineas:
        archivo_entrada.writelines([""])
    archivo_entrada.close()

invertir_lineas("archivos/archivo2.txt", "archivos/archivo3.txt")