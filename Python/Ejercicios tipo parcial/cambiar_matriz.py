"""
    problema cambiar_matriz (inout A: seq⟨seq⟨Z⟩⟩) {
        requiere: {Todas las filas de A tienen la misma longitud}
        requiere: {El mínimo número que aparece en A es igual a 1}
        requiere: {El máximo número que aparece en A es igual a #filas de A por #columnas de A}
        requiere: {No hay enteros repetidos en A}
        requiere: {Existen al menos dos enteros distintos en A} 
        modifica: {A}
        asegura: {A tiene exactamente las mismas dimensiones que A@pre}
        asegura: {El conjunto de elementos que aparecen en A es igual al conjunto de elementos que aparecen en A@pre}
        asegura: {A[i][j] != A@pre[i][j] para todo i, j en rango}
    }
Ejemplo: dada la entrada A = [[1,2,3], [4,5,6]], una posible solución es A = [[4,5,6], [1,2,3]].
"""


def cambiar_matriz(matriz:list[list[int]]) -> None:
    # Voy a enfocarlo de manera de mover cada posicion en uno, entonces: A = [[1,2,3], [4,5,6]] ==> [[6,1,2], [3,4,5]]
    cant_filas:int = len(matriz)
    cant_columnas:int = len(matriz[0])
    
    valor_anterior:int = matriz[cant_filas - 1][cant_columnas - 1] # Ultimo valor
    for i in range(cant_filas):
        for j in range(cant_columnas):
            valor_actual:int = matriz[i][j]
            matriz[i][j] = valor_anterior
            valor_anterior = valor_actual
