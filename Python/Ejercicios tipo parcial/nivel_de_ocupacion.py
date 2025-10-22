"""
Vamos a representar un hospital con una matriz en donde las filas son los pisos, y las columnas son las camas. Los valores de la matriz son Booleanos que indican si la cama está ocupada o no. Si el valor es verdadero (True) indica que la cama está ocupada.
    problema nivel_de_ocupacion (in camas_por_piso:seq⟨seq⟨Bool⟩⟩) : seq⟨R⟩ {
        requiere: {Todos los pisos tienen la misma cantidad de camas.}
        requiere: {Hay por lo menos 1 piso en el hospital.}
        requiere: {Hay por lo menos una cama por piso.}
        asegura: {|res| es igual a la cantidad de pisos del hospital.}
        asegura: {Para todo 0 ≤ i < |res| se cumple que res[i] es igual a la cantidad de camas ocupadas del piso i dividido el total de camas del piso i).}
    }
Ejemplo: dada la entrada camas_por_piso = [[True, False, True], [False, False, True], [True, True, True]], devuelve res = [2/3, 1/3, 1.0].
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