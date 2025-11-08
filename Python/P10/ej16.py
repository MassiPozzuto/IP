"""
Hospital - Nivel de ocupación

Queremos saber qué porcentaje de ocupación de camas hay en el hospital. El hospital se representa por una matriz en donde las filas son los pisos, y las columnas son las camas. Los valores de la matriz son Booleanos que indican si la cama está ocupada o no. Si el valor es verdadero (True) indica que la cama está ocupada.

Se nos pide programar en Python una función que devuelve una secuencia de reales, indicando la proporción de camas ocupadas en cada piso.

    problema nivel_de_ocupacion (in camas_por_piso:seq⟨seq⟨Bool⟩⟩) : seq⟨R⟩ {
        requiere: {Todos los pisos tienen la misma cantidad de camas.}
        requiere: {Hay por lo menos 1 piso en el hospital.}
        requiere: {Hay por lo menos una cama por piso.}
        asegura: {|res| = |camas por piso|.}
        asegura: {Para todo 0 ≤ i < |res| se cumple que res[i] es igual a la cantidad de camas ocupadas del piso i dividido el total de camas del piso i).}
    }
"""

def nivel_de_ocupacion(camas_por_piso:list[list[bool]]) -> list[float]:
    res:list[float] = []

    camas_ocupadas_piso_actual:int = 0
    for piso in camas_por_piso:
        for cama in piso:
            if cama: camas_ocupadas_piso_actual += 1
        
        res.append(camas_ocupadas_piso_actual / len(piso)) # No hay problema en la division ya que por lo menos hay una cama por piso (3er requiere)
        camas_ocupadas_piso_actual = 0

    return res