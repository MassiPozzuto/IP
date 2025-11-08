"""
Hospital - Atención por Guardia

Desde el Hospital Fernandez nos pidieron solucionar una serie de problemas relacionados con la información que maneja sobre los pacientes y el personal de salud. En primer lugar debemos resolver en qué orden se deben atender los pacientes que llegan a la guardia. En enfermería, hay una primera instancia que clasifica en dos colas a los pacientes: una urgente y otra postergable (esto se llama hacer triage). A partir de dichas colas que contienen la identificación del paciente, se pide devolver una nueva cola según la siguiente especificación.

    problema orden_de_atencion (in urgentes: Cola<Z>, in postergables: Cola<Z>) : Cola<Z> {
        requiere: {No hay elementos repetidos en urgentes.}
        requiere: {No hay elementos repetidos en postergables.}
        requiere: {La intersección entre postergables y urgentes es vacía.}
        requiere: {|postergables| = |urgentes|.}
        asegura: {No hay repetidos en res.}
        asegura: {res es permutación de la concatenación de urgentes y postergables.}
        asegura: {Si urgentes no es vacía, en la cabeza de res hay un elemento de urgentes.}
        asegura: {En res no hay dos seguidos de urgentes.}
        asegura: {En res no hay dos seguidos de postergables.}
        asegura: {Para todo c1 y c2 de tipo ”urgente” pertenecientes a urgentes si c1 aparece antes que c2 en urgentes entonces c1 aparece antes que c2 en res.}
        asegura: {Para todo c1 y c2 de tipo ”postergable” pertenecientes a postergables si c1 aparece antes que c2 en postergables entonces c1 aparece antes que c2 en res.}
    }
"""
from typing import Any
from queue import Queue as Cola

def orden_de_atencion(urgentes: Cola[int], postergables: Cola[int]) -> Cola[int]:
    res: Cola[int] = Cola()
    urgentes_copia: Cola[int] = copiar_cola(urgentes)
    postergables_copia: Cola[int] = copiar_cola(postergables)

    i:int = 0
    while not urgentes_copia.empty() or not postergables_copia.empty():
        if i % 2 == 0 or postergables_copia.empty(): # Esto es por si |postergables| != |urgentes| aunque lo pida el requiere, no me importa, me gusta abarcar mas
            res.put(urgentes_copia.get())
        else:
            res.put(postergables_copia.get())
        
        i += 1

    return res

def copiar_cola(cola: Cola[Any]) -> Cola[Any]:
    res: Cola[Any] = Cola()

    cola_aux: Cola[Any] = Cola()
    while not cola.empty():
        cola_aux.put(cola.get())

    while not cola_aux.empty():
        actual:Any = cola_aux.get()
        cola.put(actual)
        res.put(actual)

    return res

urgentes = Cola()
urgentes.put(1)
urgentes.put(5)
urgentes.put(2)
urgentes.put(4)
urgentes.put(3)

postergables = Cola()
postergables.put(50)
postergables.put(80)
postergables.put(90)
postergables.put(70)

print(orden_de_atencion(urgentes, postergables).queue)