"""
Cola en el Banco

En el banco ExactaBank los clientes hacen cola para ser atendidos por un representante. Los clientes son representados por
las tuplas (nombre, tipo afiliado) donde la primera componente es el nombre y el tipo afiliado puede ser ”común” o ”vip”.

Se nos pide implementar una función en python que dada una cola de clientes del banco, devuelva una nueva cola con los
mismos clientes pero en donde los clientes vip est´an primero que los clientes comunes manteniendo el orden original de los clientes
vips y los comunes entre sí.

    problema reordenar_cola_priorizando_vips (in filaClientes: Cola<str × str>) : Cola<str> {
        requiere: {La longitud de los valores de la primera componente de las tuplas de la cola filaClientes es mayor a 0.}
        requiere: {Los valores de la segunda componente de las tuplas de la cola filaClientes son ”común” o ”vip”.}
        requiere: {No hay dos tuplas en filaClientes que tengan la primera componente iguales entre sí.}
        asegura: {todo valor de res aparece como primera componente de alguna tupla de filaClientes.}
        asegura: {|res| = |filaCliente|.}
        asegura: {res no tiene elementos repetidos.}
        asegura: {No hay ningún cliente ”común” antes que un ”vip” en res.}
        asegura: {Para todo cliente c1 y cliente c2 de tipo ”común” pertenecientes a filaClientes si c1 aparece antes que c2 en filaClientes entonces el nombre de c1 aparece antes que el nombre de c2 en res.}
        asegura: {Para todo cliente c1 y cliente c2 de tipo ”vip” pertenecientes a filaClientes si c1 aparece antes que c2 en filaClientes entonces el nombre de c1 aparece antes que el nombre de c2 en res.}
    }
"""
from typing import Any
from queue import Queue as Cola

def copiar_cola(cola:Cola) -> Cola:
    cola_aux:Cola = Cola()
    cola_copia:Cola = Cola()

    while not cola.empty():
        cola_aux.put(cola.get())
    
    while not cola_aux.empty():
        actual:Any = cola_aux.get()
        cola.put(actual)
        cola_copia.put(actual)
    
    return cola_copia


def reordenar_cola_priorizando_vips(fila_clientes: Cola[tuple[str, str]]) -> Cola[str]:
    # Mi enfoque va a ser dividir la fila en dos, una de vips y otra de comunes, de manera tal que mantenga el orden 
    # Luego agregarle a la lista de vips, los elementos de la lista de comunes y entonces tener lo pedido
    fila_clientes_copia:Cola[tuple[str, str]] = copiar_cola(fila_clientes)  # Como fila_clientes es 'in' debe salir igual que como entró
 
    clientes_priorizando_vips:Cola[str] = Cola()
    clientes_normales:Cola[str] = Cola()
    while not fila_clientes_copia.empty():
        actual:tuple[str, str] = fila_clientes_copia.get()
        if actual[1] == "vip":
            clientes_priorizando_vips.put(actual[0])
        else:
            clientes_normales.put(actual[0])
    
    while not clientes_normales.empty():
        clientes_priorizando_vips.put(clientes_normales.get())
    
    return clientes_priorizando_vips