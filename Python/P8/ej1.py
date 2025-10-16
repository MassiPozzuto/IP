"""
Implementar una solución para el siguiente problema.
    problema generar_nros_al_azar (in cantidad: Z, in desde: Z, in hasta: Z) : Pila[Z] {
        requiere: { cantidad ≥ 0 }
        requiere: { desde ≤ hasta }
        asegura: { El tamaño de res es igual a cantidad }
        asegura: { Todos los elementos de res son valores entre desde y hasta (ambos inclusive), seleccionados aleatoriamente con probabilidad uniforme }
    }
Para generar números en un rango con probabilidad uniforme, pueden usar la función random.randint(< desde >, < hasta >) que devuelve un número en el rango indicado. Recuerden importar el módulo random con import random. Además, pueden usar la clase LifoQueue() que es un ejemplo de una implementación básica de una pila: 
    from queue import LifoQueue as Pila # importa LifoQueue y le asigna el alias Pila
    
    p = Pila () # crea una pila
    p . put (1) # apila un 1
    elemento = p . get () # desapila
    p . empty () # devuelve true si y solo si la pila está vacía
"""
import random
from queue import LifoQueue as Pila

def generar_nros_al_azar(cantidad:int, desde:int, hasta:int) -> Pila[int]:
    pila:Pila[int] = Pila()
    for _ in range(cantidad):
        pila.put(random.randint(desde, hasta))
    
    return pila