"""
Implementar una solución para el siguiente problema.
    problema cantidad_elementos (in c: Cola) : Z {
        requiere: {True}
        asegura: {res es igual a la cantidad de elementos que contiene c}
    }
No se puede utilizar la función Queue.qsize().
Comparar el resultado con la implementación utilizando una pila en lugar de una cola
"""
from queue import Queue as Cola
from generales import copiar_cola

def cantidad_elementos(cola: Cola) -> int:
    cola_copia:Cola = copiar_cola(cola)
    cantidad:int = 0
    while not cola_copia.empty():
        cola_copia.get()
        cantidad += 1

    return cantidad

# La implementacion es la misma, lo unico que cambia es que funcion copiar se utiliza (copiar_cola o copiar_pila)