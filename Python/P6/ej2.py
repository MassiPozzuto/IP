import math


def imprimir_saludo(nombre: str) -> None :
    print(f"Hola {nombre}")


def raiz_cuadrada_de(numero: int) -> float :
    res:float = math.sqrt(numero)
    return res

def fahrenheit_a_celsius(temp_far: float)-> float:
    res:float = ((temp_far -32) * 5) / 9
    return res

def imprimir_dos_veces(estribillo:str) -> None:
    print(estribillo * 2)

def es_multiplo_de(n:int, m:int) -> bool:
    res:bool = n % m == 0
    return res

def es_par(numero: int) -> bool:
    res:bool = es_multiplo_de(numero, 2)
    return res

def cantidad_de_pizzas(comensales:int, min_cant_de_porciones:int) -> int :
    res:int = math.ceil((comensales * min_cant_de_porciones) / 8)
    return res
