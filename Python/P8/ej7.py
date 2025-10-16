"""
Implementar una solución para el siguiente problema.
    problema intercalar (in p1: Pila, in p2: Pila) : Pila {
        requiere: {p1 y p2 tienen la misma cantidad de elementos}
        asegura: {res solo contiene los elementos de p1 y p2}
        asegura: {res contiene todos los elementos de p1 y p2, intercalados y respetando el orden original}
        asegura: {El tope de la pila res es el tope de p2}
        asegura: {El tamaño de res es igual al doble del tamaño de p1}
    }
Nota: Ojo que hay que recorrer dos veces para que queden en el orden apropiado al final.
"""

from queue import LifoQueue as Pila
from generales import copiar_pila

def invertir_pila(pila:Pila) -> Pila:
    pila_copia = copiar_pila(pila)
    pila_invertida = Pila()

    while not pila_copia.empty():
        pila_invertida.put(pila_copia.get())
    
    return pila_invertida

def intercalar(p1:Pila, p2: Pila) -> Pila:
    res:Pila = Pila()
    
    p1_copia = invertir_pila(p1) 
    p2_copia = invertir_pila(p2)
    # Seguimos respetando que p1 y p2 sean 'in' ya que el parametro de invertir_pila tambien es 'in'

    i:int = 0
    while (not p1_copia.empty()) or (not p2_copia.empty()):
        if i % 2 == 0: 
            res.put(p1_copia.get())
        else:
            res.put(p2_copia.get())
        i += 1

    return res

pila1 = Pila()
pila1.put(1)
pila1.put(2)
pila1.put(3)

pila2 = Pila()
pila2.put(40)
pila2.put(50)
pila2.put(60)

print(intercalar(pila1, pila2).queue)