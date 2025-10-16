"""
Implementar una solución para el siguiente problema.
    problema buscar_el_maximo (in p: Pila[Z]) : Z {
        requiere: {p no está vacía}
        asegura: {res es un elemento de p}
        asegura: {res es mayor o igual a todos los elementos de p}
    }
"""

from queue import LifoQueue as Pila
from generales import copiar_pila

def buscar_el_maximo(pila:Pila[int]) -> int:
    pila_copia:Pila[int] = copiar_pila(pila)

    maximo:int = pila_copia.get()
    while not pila_copia.empty():
        actual:int = pila_copia.get()
        if actual > maximo: 
            maximo = actual

    return maximo