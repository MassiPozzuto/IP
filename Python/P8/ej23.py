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

    archivo_salida:TextIO = open(nombre_archivo_salida, "w", encoding="utf8") # "w" abre el archivo para escritura, truncando primero el fichero
    i:int = 0
    while len(lineas):
        linea:str = lineas.pop()
        if i == 0 and linea[len(linea) - 1] != '\n':  
            linea += '\n'
        if len(lineas) == 0 and linea[len(linea) - 1] == '\n':
            linea = sacar_new_line(linea)

        archivo_salida.write(linea)
        i += 1

    archivo_salida.close()

def sacar_new_line(string:str) -> str:
    res:str = string
    if string[len(string) - 1] == '\n':
        res = ''
        for i in range(len(string) - 1):
            res += string[i]
    
    return res


invertir_lineas("archivos/archivo2.txt", "archivos/archivo3.txt")