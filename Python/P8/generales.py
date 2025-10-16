from queue import LifoQueue as Pila
from queue import Queue as Cola

def copiar_pila(pila:Pila[any]) -> Pila[any]:
    pila_aux:Pila[any] = Pila()
    pila_copia:Pila[any] = Pila()

    while not pila.empty():
        pila_aux.put(pila.get())
    
    while not pila_aux.empty():
        actual:int = pila_aux.get()
        pila.put(actual)
        pila_copia.put(actual)

    return pila_copia

def copiar_cola(cola:Cola[any]) -> Cola[any]:
    cola_aux:Cola[any] = Cola()
    cola_copia:Cola[any] = Cola()

    while not cola.empty():
        cola_aux.put(cola.get())
    
    while not cola_aux.empty():
        actual:int = cola_aux.get()
        cola.put(actual)
        cola_copia.put(actual)

    return cola_copia