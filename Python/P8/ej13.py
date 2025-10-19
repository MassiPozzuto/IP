"""
Bingo: un cartón de bingo contiene 12 números al azar en el rango [0, 99]. Implementar una solución para cada uno de los siguientes problemas.
    1. 
        problema armar_secuencia_de_bingo () : Cola[Z] {
            requiere: {True}
            asegura: {res solo contiene 100 números del 0 al 99 inclusive, sin repetidos}
            asegura: {Los números de res están ordenados al azar}
        }
        Para generar números pseudoaleatorios pueden usar la función random.randint(< desde >, < hasta >) que devuelve un número en el rango indicado. Recuerden importar el módulo random con import random.
        
    2. 
        problema jugar_carton_de_bingo (in carton: seq⟨Z⟩, in bolillero: Cola[Z]) : Z {
            requiere: {carton solo contiene 12 números, sin repetidos, con valores entre 0 y 99, ambos inclusive}
            requiere: {bolillero solo contiene 100 números, ordenados al azar, del 0 al 99, ambos inclusive, sin repetidos}
            asegura: {res es la cantidad mínima de jugadas necesarias para que todos los números del carton hayan salido del bolillero}
        }
"""
import random
from queue import Queue as Cola
from generales import copiar_cola

def armar_secuencia_de_bingo() -> Cola[int]:
    lista:list[int] = [i for i in range(100)]
    random.shuffle(lista)
    
    bolillero:Cola[int] = Cola()
    for num in lista:
        bolillero.put(num)
    return bolillero

def jugar_carton_de_bingo(carton:list[int], bolillero:Cola[int]) -> int:
    bolillero_copia:Cola[int] = copiar_cola(bolillero)
    carton_copia:list[int] = carton.copy()

    cantidad_de_jugadas:int = 0
    while len(carton_copia) > 0:
        numero_actual:int = bolillero_copia.get()
        if numero_actual in carton_copia: 
            carton_copia.remove(numero_actual)
        cantidad_de_jugadas += 1

    return cantidad_de_jugadas
