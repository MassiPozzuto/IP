"""
Veterinaria - Stock

En la veterinaria "Exactas's pets", al finalizar cada día, el personal registra en papeles los nombres y la cantidad actual de los productos cuyo stock ha cambiado. Para mejorar la gestión, desde la dirección de la veterinaria han pedido desarrollar una solución en Python que les permita analizar las fluctuaciones del stock. Se pide implementar una función, que reciba una lista de tuplas donde cada tupla contiene el nombre de un producto y su stock en ese momento. La función debe procesar esta lista y devolver un diccionario que tenga como clave el nombre del producto y como valor una tupla con su mínimo y máximo stock histórico registrado.

    problema stock_productos (in stock_cambios : seq⟨str × Z⟩) : seq⟨Z⟩ {
        requiere: {Todos los elementos de stock_cambios están formados por un str no vacío y un entero ≥ 0.}
        asegura: {res tiene como claves solo los primeros elementos de las tuplas de stock_cambios (o sea, un producto).}
        asegura: {res tiene como claves todos los primeros elementos de las tuplas de stock_cambios.}
        asegura: {El valor en res de un producto es una tupla de cantidades. Su primer elemento es la menor cantidad de ese producto en stock_cambios y como segundo valor el mayor.}
    }

"""

def stock_productos(stock_cambios:list[tuple[str, int]]) -> dict[str, tuple[int, int]]:
    res:dict[str, tuple[int, int]] = {}

    for nombre_prod, stock in stock_cambios:
        if nombre_prod in res.keys() and res[nombre_prod][0] > stock:
            res[nombre_prod] = (stock, res[nombre_prod][1]) # Las tuplas son inmutables
        elif nombre_prod in res.keys() and res[nombre_prod][1] < stock:
            res[nombre_prod] = (res[nombre_prod][0], stock) # Las tuplas son inmutables 
        else:
            res[nombre_prod] = (stock, stock)

    return res


print(stock_productos([("Coca", 2), ("Papel Higienico", 10), ("Coca", 5), ("Coca", 1)]))