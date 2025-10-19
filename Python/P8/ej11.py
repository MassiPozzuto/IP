"""
Implementar una solución para el siguiente problema.
    problema buscar_nota_minima (in c: Cola[(Char × Z)]) : (Char × Z) {   # Cambie la especificacion porque pareceria estar mal
        requiere: {c no está vacía}
        requiere: {los elementos de c no tienen valores repetidos en la segunda componente de las tuplas}
        asegura: {res es una tupla de c}
        asegura: {No hay ningún elemento en c cuya segunda componente sea menor que la de res }
    }

"""
from queue import Queue as Cola
from generales import copiar_cola

def buscar_nota_minima(cola:Cola[tuple[str, int]]) -> tuple[str, int]:
    cola_copia: Cola[tuple[str, int]] = copiar_cola(cola) # Si bien copiar_cola() no es una deepcopy, no queremos modificar las tuplas internas, no hay problema

    nota_minima:tuple[str, int] = cola_copia.get()
    while not cola_copia.empty():
        nota_actual:tuple[str, int] = cola_copia.get()
        if nota_actual[1] < nota_minima[1]:
            nota_minima = nota_actual
    
    return nota_minima