"""
Implementar una solución para el siguiente problema.
    problema intercalar (in c1: Cola, in c2: Cola) : Cola {
        requiere: {c1 y c2 tienen la misma cantidad de elementos}
        asegura: {res solo contiene los elementos de c1 y c2}
        asegura: {res contiene todos los elementos de c1 y c2, intercalados y respetando el orden original}
        asegura: {El primer elemento de res es el primer elemento de c1}
        asegura: {El tamaño de res es igual al doble del tamaño de c1}
    }
"""
from queue import Queue as Cola
from generales import copiar_cola

def intercalar(cola1:Cola, cola2:Cola) -> Cola:
    cola1_copia:Cola = copiar_cola(cola1)
    cola2_copia:Cola = copiar_cola(cola2)
    cola_intercalada:Cola = Cola()

    i:int = 0
    while not cola1_copia.empty() and not cola2_copia.empty():
        if i % 2 == 0:
            cola_intercalada.put(cola1_copia.get())
        else:
            cola_intercalada.put(cola2_copia.get())
        i += 1
    
    return cola_intercalada

# A diferencia del intercalar de pilas, no tenemos que invertir las pilas para respetar el orden pedido