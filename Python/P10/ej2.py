"""
Veterinaria - Filtrar códigos de barra

El hijo del dueño de la veterinaria, cuya actividad principal es ver tik toks, cree que los productos cuyos códigos de barras terminan en números primos son especialmente auspiciosos y deben ser destacados en la tienda. Luego de convencer a su padre de esta idea, solicita una función en Python que facilite esta gestión. Se pide implementar una función que, dada una secuencia de enteros, cada uno representando un código de barras de un producto, cree y devuelva una nueva lista que contenga únicamente aquellos números de la lista original cuyos últimos tres dígitos formen un número primo (por ejemplo, 101, 002 y 011).

Nota: Un número primo es aquel que solo es divisible por sí mismo y por 1. Algunos ejemplos de números primos de hasta tres dígitos son: 2, 3, 5, 101, 103, 107, etc.

    problema filtrar_codigos_primos (in codigos_barra : seq⟨Z⟩) : seq⟨Z⟩ {
        requiere: {Todos los enteros de codigos_barra tienen, por lo menos, 3 dígitos.}
        requiere: {No hay elementos repetidos en codigos_barra.}
        asegura: {Los últimos 3 dígitos de cada uno de los elementos de res forman un número primo.}
        asegura: {Todos los elementos de codigos_barra cuyos últimos 3 dígitos forman un número primo están en res.}
        asegura: {Todos los elementos de res están en codigos_barra.}
    }
"""

def filtrar_codigos_primos(codigo_barra: list[int]) -> list[int]:
    res:list[int] = []

    for codigo in codigo_barra:
        ultimos_tres_digitos: int = codigo % 1000
        if es_primo(ultimos_tres_digitos):
            res.append(codigo)
    
    return res


def es_primo(n: int) -> bool:
    res:bool = True
    for i in range(2, n):
        if n % i == 0: res = False

    return res

print(filtrar_codigos_primos([7791234562317, 7791234562352, 7791234562389, 7791234562444, 7791234562473, 7791234562491, 7791234562520, 7791234562002]))