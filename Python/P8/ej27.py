from typing import TextIO
from ej6 import separar_string
"""
Implementar una solución para el siguiente problema.
    problema calcular_promedio_por_estudiante (in nombre_archivo_notas: seq⟨Char⟩, in nombre_archivo_promedios: seq⟨Char⟩) {
        requiere: {nombre_archivo_notas es el path de un archivo existente y accesible, con formato CSV: cada línea tendrá número de LU, materia, fecha y nota, todo separado por comas}
        requiere: {nombre_archivo_promedios es el path de un archivo distinto, accesible para escritura}
        asegura: {El archivo nombre_archivo_promedios contiene una línea por estudiante del archivo nombre_archivo_notas, con su LU y su promedio separados por una coma}
    }
El contenido del archivo nombre_archivo_notas tiene el siguiente formato: 
    nro de LU ( str ) , materia ( str ) , fecha ( str ) , nota ( float )

Analizar el problema y modularizar el código apropiadamente. Una opción es implementar una función auxiliar que cumpla la siguiente especificación.
    problema promedio_estudiante (in notas_de_estudiantes: seq⟨seq⟨Char⟩⟩, in lu: seq⟨Char⟩ ) : R {
        requiere: {notas_de_estudiantes tiene el contenido del archivo de notas. Cada elemento de la lista es una línea de ese archivo, con formato CSV: tendrá número de LU, materia, fecha y nota, todo separado por comas}
        requiere: {lu corresponde a una LU presente en notas_de_estudiantes}
        asegura: {res es el promedio de las notas asociadas a lu en notas_de_estudiantes}
    }
"""
def calcular_promedio_por_estudiante(nombre_archivo_notas:str, nombre_archivo_promedios:str) -> None:
    archivo_notas:TextIO = open(nombre_archivo_notas, "r", encoding="utf8")
    notas:list[str] = archivo_notas.readlines()
    archivo_notas.close()
    
    promedios:dict[str, float] = {}
    for nota in notas:
        info_nota:list[str] = separar_string(nota, ',')
        if info_nota[0] not in promedios.keys():
            promedios[info_nota[0]] = promedio_estudiante(notas, info_nota[0])

    archivo_promedios:TextIO = open(nombre_archivo_promedios, "w", encoding="utf8")
    for lu, promedio in promedios.items():
        archivo_promedios.write(f"{lu},{promedio}\n")
    archivo_promedios.close()

def promedio_estudiante (notas_de_estudiantes: list[str], lu: str ) -> float:
    suma_notas:float = 0
    cantidad_notas:int = 0
    for nota in notas_de_estudiantes:
        info_nota:list[str] = separar_string(nota, ',')
        if info_nota[0] == lu:
            suma_notas += float(info_nota.pop()) # No hay problema si el string contiene un salto de linea, float lo ignora
            cantidad_notas += 1

    promedio:float = round(suma_notas / cantidad_notas, 2)
    return promedio



calcular_promedio_por_estudiante("archivos/notas.csv", "archivos/promedios.csv")