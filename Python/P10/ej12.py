"""
Ta-Te-Ti-Facilito

Ana y Beto juegan al Ta-Te-Ti-Facilito. El juego es en un tablero cuadrado de lado entre 5 y 10. Cada jugador va poniendo su ficha en cada turno. Juegan intercaladamente y comienza Ana. Ana pone siempre una ”X” en su turno y Beto pone una ”O” en el suyo. Gana la persona que logra poner 3 fichas suyas consecutivas en forma vertical. Si el tablero está completo y no ganó nadie, entonces se declara un empate. El tablero comienza vacío, representado por ” ” en cada posición. Notar que dado que juegan por turnos y comienza Ana poniendo una ”X” se cumple que la cantidad de ”X” es igual a la cantidad de ”O” o bien la cantidad de ”X” son uno más que la cantidad de ”O”. Se nos pide implementar una función en python quien gano el tateti facilito que determine si ganó alguno, o si Beto hizo trampa (puso una ”O” cuando Ana ya había ganado).

    problema quien_gano_el_tateti_facilito (in tablero:seq⟨seq⟨Char⟩⟩) : Z {
        requiere: {tablero es una matriz cuadrada.}
        requiere: {5 ≤ |tablero[0]| ≤ 10.}
        requiere: {tablero sólo tiene ”X”, ”O” y ”” (espacio vacío) como elementos.}
        requiere: {En tablero la cantidad de ”X” es igual a la cantidad de ”O” o bien la cantidad de ”X” es uno más que la cantidad de ”O”.}
        asegura: {res = 1 ⇔ hay tres ”X” consecutivas en forma vertical(misma columna) y no hay tres ”O” consecutivas en forma vertical(misma columna).}
        asegura: {res = 2 ⇔ hay tres ”O” consecutivas en forma vertical (misma columna) y no hay tres ”X” consecutivas en forma vertical(misma columna).}
        asegura: {res = 0 ⇔ no hay tres ”O” ni hay tres ”X” consecutivas en forma vertical.}
        asegura: {res = 3 ⇔ hay tres ”X” y hay tres ”O” consecutivas en forma vertical (evidenciando que beto hizo trampa).}
    }
"""

from ej4 import trasponer_matriz


def quien_gano_el_tateti_facilito(tablero: list[list[str]]) -> int :

    tablero_traspuesto:list[list[str]] = trasponer_matriz(tablero)

    ganador_X:bool = False
    ganador_O:bool = False
    for i in range(len(tablero_traspuesto)):
        for j in range(len(tablero_traspuesto[0]) - 2):
            if tablero_traspuesto[i][j] == tablero_traspuesto[i][j + 1] and tablero_traspuesto[i][j] == tablero_traspuesto[i][j + 2]:
                if tablero_traspuesto[i][j] == "X": ganador_X = True
                elif tablero_traspuesto[i][j] == "O": ganador_O = True

    res:int = 0
    if ganador_X and not ganador_O:
        res = 1
    elif not ganador_X and ganador_O:
        res = 2
    elif ganador_X and ganador_O:
        res = 3
    
    return res



print(quien_gano_el_tateti_facilito([
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "],
        [" ", "O", " ", " ", " "],
        ["X", "O", " ", " ", " "],
        ["X", "O", "X", " ", " "],
    ]))

