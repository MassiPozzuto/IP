"""
Sala de Escape - Escape en solitario

Dada una matriz donde las columnas representan a cada amigo y las filas representan las salas de escape, y los valores son los tiempos (en minutos) registrados para cada sala (0 si no fueron, 61 si no salieron, y un número entre 1 y 60 si salieron), escribir una función en Python que devuelva los índices de todas las filas (que representan las salas) en las cuales el primer, segundo y cuarto amigo no fueron (0), pero el tercero sí fue independientemente de si salió o no).

    problema escape_en_solitario (in amigos_por_salas: seq⟨seq⟨Z⟩⟩) : seq⟨Z⟩ {
        requiere: {Hay por lo menos una sala en amigos por salas.}
        requiere: {Hay 4 amigos en amigos_por_salas.}
        requiere: {Todos los tiempos en cada sala de amigos_por_salas están entre 0 y 61 inclusive.}
        asegura: {La longitud de res es menor igual que la longitud de amigos_por_salas.}
        asegura: {Por cada sala en amigos_por_salas cuyo primer, segundo y cuarto valor sea 0, y el tercer valor sea distinto de 0, la posición de dicha sala en amigos_por_salas debe aparecer res.}
        asegura: {Para todo i pertenciente a res se cumple que el primer, segundo y cuarto valor de amigos_por_salas[i] es 0, y el tercer valor es distinto de 0.}
    }
"""

def escape_en_solitario(amigos_por_salas: list[list[int]]) -> list[int]:
    res:list[int] = []

    sala_actual_valida:bool = True
    for indice_fila in range(len(amigos_por_salas)):
        for indice_col in range(len(amigos_por_salas[indice_fila])):
            if (indice_col == 2 and amigos_por_salas[indice_fila][indice_col] == 0) or (indice_col != 2 and amigos_por_salas[indice_fila][indice_col] != 0):
                sala_actual_valida = False
        
        if sala_actual_valida: 
            res.append(indice_fila)

    return res