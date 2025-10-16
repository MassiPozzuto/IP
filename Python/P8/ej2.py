"""
Implementar una solución para el siguiente problema.
    problema cantidad_elementos (in p: Pila) : Z {
        requiere: {True}
        asegura: {res es igual a la cantidad de elementos que contiene p}
    }
No se puede utilizar la función LifoQueue.qsize(). Tener en cuenta que, al usar get() para recorrer la pila, se modifica el parámetro de entrada, ya que los elementos se eliminan al accederse. Dado que la especificación lo define como de tipo in, debe restaurarse posteriormente.

"""
from queue import LifoQueue as Pila
from generales import copiar_pila

def cantidad_elementos(pila:Pila[int]) -> int:
    pila_copia:Pila[int] = copiar_pila(pila)
    cantidad:int = 0
    while not pila_copia.empty():
        pila_copia.get()
        cantidad += 1

    return cantidad
