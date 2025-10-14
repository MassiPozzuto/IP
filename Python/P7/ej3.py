"""
Implementar una función para conocer el estado de aprobación de una materia a partir de las notas obtenidas por un/a alumno/a cumpliendo con la siguiente especificación:

    problema resultado_materia (in notas: seq⟨Z⟩) : Z {
        requiere: { |notas| > 0 }
        requiere: { Para todo i ∈ Z si 0 ≤ i < |notas| → 0 ≤ notas[i] ≤ 10) }
        asegura: { res = 1 ↔ todos los elementos de notas son mayores o iguales a 4 y el promedio es mayor o igual a 7 }
        asegura: { res = 2 ↔ todos los elementos de notas son mayores o iguales a 4 y el promedio está entre 4 (inclusive) y 7 }
        asegura: { res = 3 ↔ alguno de los elementos de notas es menor a 4 o el promedio es menor a 4 }
    }
"""
def resultado_materia(notas:list[int]) -> int:
    promedio:float = 0
    notas_desaprobadas:int = 0
    for nota in notas:
        promedio += nota
        if nota < 4: notas_desaprobadas += 1

    promedio /= len(notas)
    res:int = 2
    if notas_desaprobadas == 0 and promedio >=7: res = 1
    if notas_desaprobadas != 0 or promedio < 4: res = 3

    return res
