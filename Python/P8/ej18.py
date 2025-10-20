"""
Se debe desarrollar un sistema de gestión de inventario para una tienda de ropa. Este sistema debe permitir llevar un registro de los productos en el inventario y realizar operaciones como agregar nuevos productos, actualizar las existencias y calcular el valor total del inventario.
Para resolver este problema vamos a utilizar un diccionario llamado inventario que almacenará la información de los productos. En este diccionario, cada clave será el nombre de un producto, y su valor asociado será otro diccionario con los atributos del producto. Este segundo diccionario tendrá dos claves posibles: 'precio'y 'cantidad', cuyos valores serán de tipo float e int, respectivamente.
Un ejemplo de inventario, con un solo producto, es: {“remera”: {“precio”: 999.99, “cantidad”: 3}}).
Implementar una solución para cada uno de los siguientes problemas. Agregar en las funciones los tipos de datos correspondientes (ver nota al final de la primera especificación).
"""

"""
1. 
    problema agregar_producto (inout inventario: Diccionario⟨ seq⟨Char⟩, Diccionario⟨ seq⟨Char⟩, T ⟩⟩, in nombre: seq⟨Char⟩, in precio: R, in cantidad: Z) {
        requiere: {T ∈ [Z, R]}
        requiere: {cantidad ≥ 0}
        requiere: {precio ≥ 0}
        requiere: {Ninguno de los Strings de los parámetros es vacío}
        requiere: {nombre no es una clave de inventario }
        asegura: {Todas los pares clave-valor de inventario@pre están tal cual en inventario}
        asegura: {Todas los pares clave-valor de inventario están en inventario@pre y, además, hay una nueva con clave igual a nombre y como valor tendrá un diccionario con los pares clave-valor (“precio”, precio) y (“cantidad”, cantidad)}
    }
Se necesitará un diccionario cuyas claves son de tipo String (“precio” y “cantidad”) y cuyos valores serán de tipo float y enteros respectivamente. Para declarar los tipos de este diccionario mediante anotaciones en Python, se procede de la siguiente manera:
En Python 3.9:
    Es necesario importar Union desde el módulo typing para indicar que los valores pueden ser de más de un tipo.
    from typing import Union
    mi diccionario: dict[str, Union[int, float]]
En Python 3.10 o superior:
    No es necesario importar Union, ya que se puede usar el operador | para representar una unión de tipos.
    mi diccionario: dict[str, int | float]
"""
def agregar_producto(inventario:dict[str, dict[str, int | float]], nombre:str, precio:float, cantidad:int) -> None:
    inventario[nombre] = {
        "precio": precio,
        "cantidad": cantidad
    }

"""
2. 
    problema actualizar_stock (inout inventario: Diccionario ⟨ seq⟨Char⟩, Diccionario⟨ seq⟨Char⟩, T ⟩⟩, in nombre: seq⟨Char⟩, in cantidad: Z) {
        requiere: {T ∈ [Z, R]}
        requiere: {cantidad ≥ 0}
        requiere: {nombre es una clave existente en el inventario}
        requiere: {Ninguno de los Strings de los parámetros es vacío}
        asegura: {Todos los pares clave-valor de inventario@pre están tal cual en inventario, con excepción del que tiene como clave nombre}
        asegura: {Todos los pares clave-valor de inventario están en inventario@pre}
        asegura: {En inventario, el valor asociado a la clave nombre, tendrá el mismo precio que antes y la cantidad será cantidad}
    }
"""
def actualizar_stock(inventario:dict[str, dict[str, int | float]], nombre:str, cantidad:int) -> None:
    inventario[nombre]["cantidad"] = cantidad

"""
3. 
    problema actualizar_precio (inout inventario: Diccionario⟨ seq⟨Char⟩, Diccionario⟨ seq⟨Char⟩, T ⟩⟩, in nombre:seq⟨Char⟩, in precio: R) {
        requiere: {T ∈ [Z, R]}
        requiere: {precio ≥ 0}
        requiere: {nombre es una clave existente en el inventario}
        requiere: {Ninguno de los Strings de los parámetros es vacío}
        asegura: {Todos los pares clave-valor de inventario@pre están tal cual en inventario, con excepción del valor que tiene como clave nombre}
        asegura: {Todos los pares clave-valor de inventario están en inventario@pre}
        asegura: {En inventario el diccionario asociado a nombre, tendrá la misma cantidad que antes y el precio será precio}
    }
"""
def actualizar_precio(inventario:dict[str, dict[str, int | float]], nombre:str, precio:float) -> None:
    inventario[nombre]["precio"] = precio

"""
4. 
    problema calcular_valor_inventario (in inventario: Diccionario ⟨ seq⟨Char⟩, Diccionario ⟨ seq⟨Char⟩, T ⟩⟩) : R {
        requiere: {T ∈ [Z, R]}
        requiere: {Ninguno de los Strings del inventario es vacío}
        asegura: {res es la suma, para cada producto, del precio multiplicado por la cantidad}
    }
"""
def calcular_valor_inventario(inventario:dict[str, dict[str, int | float]]) -> float:
    valor_acumulado:float = 0
    for _, info_prod in inventario.items():
        valor_acumulado += info_prod["precio"] * info_prod["cantidad"]
    
    return round(valor_acumulado, 2)

#Ejemplo de uso:
inventario = {}
agregar_producto(inventario, "Camisa", 20.0, 50)
agregar_producto(inventario, "Pantalón", 30.0, 30)
actualizar_stock(inventario, "Camisa", 10)
valor_total = calcular_valor_inventario(inventario)
print("Valor total del inventario:", valor_total) # Debería imprimir 1100.0