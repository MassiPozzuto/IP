"""
Veterinaria - Tabla turnos

Las personas responsables de los turnos están anotadas en una matriz donde las columnas representan los días, en orden de
lunes a domingo, y cada fila un rango de una hora. Hay cuatro filas para los turnos de la mañana (9, 10, 11 y 12 hs) y otras
cuatro para la tarde (14, 15, 16 y 17).

Para hacer más eficiente el trabajo del personal de una veterinaria, se necesita analizar si quienes quedan de responsables,
están asignadas de manera continuada en los turnos de cada día.

Para ello se pide desarrollar una función en Python que, dada la matriz de turnos, devuelva una lista de tuplas de bool, una
por cada día. Cada tupla debe contener dos elementos. El primer elemento debe ser True si y solo si todos los valores de los
turnos de la mañana para ese día son iguales entre sí. El segundo elemento debe ser True si y solo si todos los valores de los
turnos de la tarde para ese día son iguales entre sí.

Siempre hay una persona responsable en cualquier horario de la veterinaria.

    problema un_responsable_por_turno (in grilla_horaria : seq⟨seq⟨str⟩⟩) : seq⟨Bool × Bool⟩ {
        requiere: {|grilla_horaria| = 8.}
        requiere: {Todos los elementos de grilla_horaria tienen el mismo tamaño (mayor a 0 y menor 8).}
        requiere: {No hay cadenas vacías en las listas de grilla_horaria.}
        asegura: {|res| = |grilla_horaria[0]|.}
        asegura: {El primer valor de la tupla en res [i], con i:Z, 0 res| es igual a True los primeros 4 valores de la columna i de grilla_horaria son iguales entre sí.}
        asegura: {El segundo valor de la tupla en res [i], con i:Z, 0 res| es igual a True los últimos 4 valores de la columna i de grilla_horaria son iguales entre sí.}
    }
"""

from typing import Any


def un_responsable_por_turno(grilla_horaria:list[list[str]]) -> list[tuple[bool, bool]]:
    res:list[tuple[bool, bool]] = []

    grilla_traspuesta:list[list[str]] = trasponer_matriz(grilla_horaria)
    
    for i in range(len(grilla_traspuesta)):
        turno_maniana:bool = True
        turno_noche:bool = True

        for j in range(0, 3):
            if grilla_traspuesta[i][j] != grilla_traspuesta[i][j + 1]:
                turno_maniana = False

        for k in range(4, 7):
            if grilla_traspuesta[i][k] != grilla_traspuesta[i][k + 1]:
                turno_noche = False

        res.append((turno_maniana, turno_noche))

    return res


def trasponer_matriz(matriz:list[list[Any]]) -> list[list[Any]]:
    
    fila_default_traspuesta:list[Any] = [ matriz[0][0] for _ in range(len(matriz)) ]
    matriz_traspuesta:list[list[Any]] = [ fila_default_traspuesta.copy() for _ in range(len(matriz[0]))]
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz_traspuesta[j][i] = matriz[i][j]

    return matriz_traspuesta
