"""
Implementar una solución para el siguiente problema.
    problema calcular_promedio_por_estudiante (in notas: seq⟨seq⟨Char⟩ × R⟩) : Diccionario ⟨ seq⟨Char⟩, R⟩ {
        requiere: {El primer componente de las tuplas de notas no es una cadena vacía}
        requiere: {El segundo componente de las tuplas de notas está en el rango [0, 10]}
        asegura: {Todas las claves de res son nombres que aparecen en notas (primer componente)}
        asegura: {Todos los nombres de notas (primer componente) son clave en res}
        asegura: {El valor de cada clave de res es el promedio de todas las notas que obtuvo el estudiante (segundo componente de notas)}
    }
Cada nota de la lista recibida como parámetro es una tupla que tiene como primer componente el nombre del estudiante y, como segundo, la nota que se sacó en un examen.
Por ejemplo:
    notas: list[tuple[str, float]] = [("Sole", 9.5), ("Maxi", 8.0), ("Sole", 9.0)]
    calcular_promedio_por_estudiante(notas) # debe devolver {"Sole": 9.25, "Maxi": 8.0}
"""

def calcular_promedio_por_estudiante(notas:list[tuple[str, float]]) -> dict[str, float]:
    notas_reordenadas:dict[str, list[float, int]] = dict()

    for nota in notas:
        # nota[0] es el nombre del estudiante
        # nota[1] es la nota que se sacó en un examen
        if notas_reordenadas.get(nota[0]):
            notas_reordenadas[nota[0]][0] += nota[1]
            notas_reordenadas[nota[0]][1] += 1
        else:
            notas_reordenadas[nota[0]] = [nota[1], 1]

    promedio_por_estudiante: dict[str, float] = {}
    for (estudiante, info_notas) in notas_reordenadas.items():
        promedio_por_estudiante[estudiante] = info_notas[0] / info_notas[1]

    return promedio_por_estudiante

notas: list[tuple[str, float]] = [("Sole", 9.5), ("Maxi", 8.0), ("Sole", 9.0)]
print(calcular_promedio_por_estudiante(notas)) # debe devolver {"Sole": 9.25, "Maxi": 8.0}