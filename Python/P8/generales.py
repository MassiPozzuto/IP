from queue import LifoQueue as Pila
from queue import Queue as Cola
from typing import Any

def copiar_pila(pila:Pila[Any]) -> Pila[Any]:
    pila_aux:Pila[Any] = Pila()
    pila_copia:Pila[Any] = Pila()

    while not pila.empty():
        pila_aux.put(pila.get())
    
    while not pila_aux.empty():
        actual:int = pila_aux.get()
        pila.put(actual)
        pila_copia.put(actual)

    return pila_copia

def copiar_cola(cola:Cola[Any]) -> Cola[Any]:
    cola_aux:Cola[Any] = Cola()
    cola_copia:Cola[Any] = Cola()

    while not cola.empty():
        cola_aux.put(cola.get())
    
    while not cola_aux.empty():
        actual:int = cola_aux.get()
        cola.put(actual)
        cola_copia.put(actual)

    return cola_copia