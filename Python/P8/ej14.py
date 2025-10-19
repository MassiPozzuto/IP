"""
Vamos a modelar una guardia de un hospital usando una cola donde se van almacenando los pedidos de atención para los pacientes que van llegando. A cada paciente se le asigna una prioridad del 1 al 10 (donde la prioridad 1 es la más urgente y requiere atención inmediata) junto con su nombre y la especialidad médica que le corresponde. Implementar una solución para el siguiente problema.

    problema pacientes_urgentes (in c:Cola[Z × seq⟨Char⟩ × seq⟨Char⟩]) : Z {
        requiere: {Todos los elementos de c tienen como primer componente de la tupla un entero positivo y menor a 11}
        asegura: {res es la cantidad de elementos de c que tienen como primer componente de la tupla un número menor a 4}
    }

"""
from queue import Queue as Cola
from generales import copiar_cola

def pacientes_urgentes(cola:Cola[tuple[int,str,str]]) -> int:
    cola_copia:Cola[tuple[int,str,str]] = copiar_cola(cola) # Si bien copiar_cola() no es una deepcopy, no queremos modificar las tuplas internas, no hay problema

    cantidad_pacientes_urgentes:int = 0
    while not cola_copia.empty():
        paciente_actual:tuple[int,str,str] = cola_copia.get()
        if paciente_actual[0] < 4:
            cantidad_pacientes_urgentes += 1

    return cantidad_pacientes_urgentes
