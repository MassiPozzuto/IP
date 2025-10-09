"""
Resuelva los siguientes ejercicios utilizando los operadores lógicos and, or, not. Resolverlos sin utilizar
alternativa condicional (if).

    1. alguno_es_0(numero1, numero2): dados dos números racionales, decide si alguno de los dos es igual a 0.
    2. ambos_son_0(numero1, numero2): dados dos números racionales, decide si ambos son iguales a 0.
    3. problema es_nombre_largo (in nombre: String) : Bool {
        requiere: { True }
            asegura: {(res = true) ↔ (3 ≤ |nombre| ≤ 8)}
        }
    4. es_bisiesto(año): que indica si un año tiene 366 días. Recordar que un año es bisiesto si es múltiplo de 400, o bien es múltiplo de 4 pero no de 100.
"""

def  alguno_es_0(numero1: float, numero2: float) -> bool:
    res:bool = numero1 == 0 or numero2 == 0
    return res

def  ambos_son_0(numero1: float, numero2: float) -> bool:
    res:bool = numero1 == 0 and numero2 == 0
    return res

def es_nombre_largo(nombre: str) -> bool:
    res:bool = len(nombre) > 2 and len(nombre) < 9
    return res

def es_bisiesto(anio: int) -> bool:
    res:bool = (anio % 400 == 0) or (anio % 4 == 0 and anio % 100 != 0 )
    return res