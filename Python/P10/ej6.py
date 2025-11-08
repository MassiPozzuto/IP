"""
Sala de Escape - Tiempo más rápido

Dada una lista con los tiempos (en minutos) registrados para cada sala de escape de Capital, escribir una función en Python que devuelva la posición (índice) en la cual se encuentra el tiempo más rápido, excluyendo las salas en las que no haya salido (0 o mayor a 60).

    problema tiempo_mas_rapido (in tiempos_salas: seq⟨Z⟩) : Z {
        requiere: {Hay por lo menos un elemento en tiempos_salas entre 1 y 60 inclusive.}
        requiere: {Todos los tiempos en tiempos_salas están entre 0 y 61 inclusive.}
        asegura: {res es la posición de la sala en tiempos_salas de la que más rápido se salió (en caso que haya más de una, devolver la primera, osea la de menor índice).}
    }
"""

def tiempo_mas_rapido(tiempos_salas: list[int]) -> int:
    res:int = 0
    tiempo_mas_rapido:int = 62

    for i in range(len(tiempos_salas)):
        if (tiempos_salas[i] > 0 and tiempos_salas[i] < 61) and tiempo_mas_rapido > tiempos_salas[i] :
            res = i
            tiempo_mas_rapido = tiempos_salas[i]

    return res


