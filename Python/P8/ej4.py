"""
Implementar una solución para el siguiente problema.
    problema buscar_nota_maxima (in p: Pila[seq⟨Char⟩ × Z]) : seq⟨Char⟩ × Z {
        requiere: {p no está vacía}
        requiere: {los elementos de p no tienen valores repetidos en la segunda posición de las tuplas}
        asegura: {res es una tupla de p}
        asegura: {No hay ningún elemento en p cuya segunda componente sea mayor que la segunda componente de res }
    }
"""
from queue import LifoQueue as Pila
from generales import copiar_pila

def buscar_nota_maxima(pila:Pila[tuple[str, int]]) -> tuple[str, int]:
    pila_copia: Pila[tuple[str, int]] = copiar_pila(pila)

    nota_maxima:tuple[str, int] = pila_copia.get()
    while not pila_copia.empty():
        nota_actual:tuple[str, int] = pila_copia.get()
        if nota_actual[1] > nota_maxima[1]:
            nota_maxima = nota_actual
    
    return nota_maxima
