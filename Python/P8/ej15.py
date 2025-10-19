"""
La gerencia de un banco nos pide modelar la atención de los clientes usando una cola donde se van registrando los pedidos de atención. Cada vez que ingresa una persona a la entidad, debe completar sus datos en una pantalla que está a la entrada: Nombre y Apellido, DNI, tipo de cuenta (true si es preferencial o f alse en el caso contrario) y si tiene prioridad (true o f alse) por ser adulto +65, embarazada o con movilidad reducida.
La atención a los clientes se da por el siguiente orden: primero las personas que tienen prioridad, luego las que tienen cuenta bancaria preferencial y por último el resto. Dentro de cada subgrupo de clientes, se respeta el orden de llegada.

    1. Dar una especificación para el problema planteado.
    2. Implementar atencion_a_clientes(in c : Cola[tuple[str, int, bool, bool]]) → Cola[tuple[str, int, bool, bool]] que dada la cola de ingreso de clientes al banco devuelve la cola en la que van a ser atendidos.

"""

"""
    problema atencion_a_clientes(in c : Cola[(seq⟨Char⟩ × Z × Bool × Bool)]) → Cola[(seq⟨Char⟩ × Z × Bool × Bool)]{
        requiere: { True }
        asegura: { |res| = |c| }
        asegura: { res tiene los elementos de c ordenados de la sig. forma: los elementos que tengan la cuarta componente verdadera, luego los elementos que tengan la tercer componente verdadera y por último los otros casos. Dentro de cada uno de estos subgrupo, se respeta el orden original de c  }
    }

"""

from queue import Queue as Cola
from generales import copiar_cola

def atencion_a_clientes(cola: Cola[tuple[str, int, bool, bool]]) -> Cola[tuple[str, int, bool, bool]]:
    cola_inicial: Cola[tuple[str, int, bool, bool]] = copiar_cola(cola)

    cola_ordenada: Cola[tuple[str, int, bool, bool]] = Cola()
    clientes_cuenta_preferencial: Cola[tuple[str, int, bool, bool]] = Cola()
    clientes_normales: Cola[tuple[str, int, bool, bool]] = Cola()
    while not cola_inicial.empty():
        actual_cliente:tuple[str, int, bool, bool] = cola_inicial.get()
        if actual_cliente[3]:
            cola_ordenada.put(actual_cliente)
        elif actual_cliente[2]:
            clientes_cuenta_preferencial.put(actual_cliente)
        else:
            clientes_normales.put(actual_cliente)

    while not clientes_cuenta_preferencial.empty():
        cola_ordenada.put(clientes_cuenta_preferencial.get())

    while not clientes_normales.empty():
        cola_ordenada.put(clientes_normales.get())

    return cola_ordenada

