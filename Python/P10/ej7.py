"""
Sala de Escape - Racha más larga

Dada una lista con los tiempos (en minutos) registrados para cada sala de escape a la que fue una persona, escribir una función en Python que devuelva una tupla con el índice de inicio y el índice de fin de la subsecuencia más larga de salidas exitosas de salas de escape consecutivas.

    problema racha_mas_larga (in tiempos: seq⟨Z⟩) : <Z×Z> {
        requiere: {Hay por lo menos un elemento en tiempos entre 1 y 60 inclusive.}
        requiere: {Todos los tiempos en tiempos están entre 0 y 61 inclusive.}
        asegura: {En la primera posición de res está la posición (índice de la lista) de la sala que inicia la racha más larga.}
        asegura: {En la segunda posición de res está la posición (índice de la lista) de la sala que finaliza la racha más larga.}
        asegura: {El elemento de la primer posición de res en tiempos es mayor estricto 0 y menor estricto que 61.}
        asegura: {El elemento de la segunda posición de res en tiempos es mayor estricto 0 y menor estricto que 61.}
        asegura: {La primera posición de res es menor o igual a la segunda posición de res.}
        asegura: {No hay valores iguales a 0 o a 61 en tiempos entre la primer posición de res y la segunda posición de res.}
        asegura: {No hay otra subsecuencia de salidas exitosas, en tiempos, de mayor longitud que la que está entre la primer posición de res y la segunda posición de res.}
        asegura: {Si hay dos o más subsecuencias de salidas exitosas de mayor longitud en tiempos, res debe contener la primera de ellas.}
    }
"""

def racha_mas_larga(tiempos: list[int]) -> tuple[int, int]:
    racha_mas_larga:tuple = (0, 0)

    racha_actual:list[str] = []
    for i in range(len(tiempos)):
        if tiempos[i] > 0 and tiempos[i] < 61:
            racha_actual.append(i)
        else:
            if len(racha_actual) > racha_mas_larga[1]:
                racha_mas_larga = (i - len(racha_actual), len(racha_actual))
            racha_actual.clear()
    
    if len(racha_actual) > racha_mas_larga[1]:
        indice_subsecuencia:int = len(tiempos) - len(racha_actual)
        racha_mas_larga = (indice_subsecuencia, len(racha_actual))

    return (racha_mas_larga[0], (racha_mas_larga[0] + racha_mas_larga[1] - 1))

print(racha_mas_larga([45,32,0,15,56,34,54,0,61,15,56,0]))