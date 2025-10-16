"""
Implementar una solución, que use pila, para el siguiente problema.
problema esta_bien_balanceada (in s: seq⟨Char⟩) : Bool {
    requiere: {s solo puede tener números enteros, espacios y los símbolos '(', ')', '+', '-', '*', '/'}
    asegura: {res = true ↔ (La cantidad de paréntesis de apertura '(és igual a la de cierre ')') y (Para todo prefijo de 's', la cantidad de paréntesis de cierre no supera a la de apertura)}
}
Por cada paréntesis de cierre debe haber uno de apertura correspondiente antes de él. Las fórmulas pueden tener:
    - números enteros
    - operaciones básicas +, -, * y /
    - paréntesis
    - espacios

Entonces las siguientes son fórmulas aritméticas con sus paréntesis bien balanceados:
1 + ( 2 x 3 = ( 20 / 5 ) )
10 * ( 1 + ( 2 * (-1)))
Y la siguiente es una fórmula que no tiene los paréntesis bien balanceados:
1 + ) 2 x 3 ( ( )
"""
from queue import LifoQueue as Pila

def esta_bien_balanceada(formula: str) -> bool:
    res:bool = True
    pila_aux: Pila[str] = Pila()

    for char in formula:
        if char == '(': 
            # Agrego a la pila el parentesis agregado
            pila_aux.put('(')
        if char == ')':
            if pila_aux.empty():
                # Si la pila esta vacia, entonces estoy intentando cerrar un parentesis cuando no esta el de apertura
                res = False
                break # Sin el break sigue funcionando, pero nos ahorramos iteraciones
            else:
                # Si no esta vacia, entonces estoy intentando cerrar el ultimo parentesis que agregue, lo saco:
                pila_aux.get()
    
    if not pila_aux.empty(): res = False
    return res

print(esta_bien_balanceada("1 + ( 2 x 3 - ( 2 0 / 5 ) )"))
print(esta_bien_balanceada("10 * ( 1 + ( 2 * (-1)))"))
print(esta_bien_balanceada("1 + ) 2 x 3 ( ( )"))