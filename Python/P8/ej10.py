"""
Implementar una solución para el siguiente problema.
    problema buscar_el_maximo (in c: Cola[Z]) : Z {
        requiere: {c no está vacía}
        asegura: {res es un elemento de c}
        asegura: {res es mayor o igual a todos los elementos de c}
    }
Comparar con la versión usando pila
"""
from queue import Queue as Cola
from generales import copiar_cola

def buscar_el_maximo(cola:Cola[int]) -> int:
    cola_copia: Cola[int] = copiar_cola(cola)

    maximo:int = copiar_cola.get()
    while not cola_copia.empty():
        actual:int = cola_copia.get()
        if actual > maximo: 
            maximo = actual
    
    return maximo

# Sucede que la implementacion es la misma, lo unico que cambia es la copia.