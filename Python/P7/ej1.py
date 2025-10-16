"""
Codificar en Python las siguientes funciones sobre secuencias:
Nota: Cada problema puede tener más de una implementación. Probar utilizando distintas formas de recorrido sobre secuencias, y distintas funciones de Python. No te conformes con una solución, recordar que siempre conviene consultar con tus docentes.
"""

""""
1. 
    problema pertenece (in s:seq⟨Z⟩, in e: Z) : Bool {
        requiere: { True }
        asegura: { (res = true) ↔ (existe un i ∈ Z tal que 0 ≤ i < |s| ∧ s[i] = e) }
    }
Implementar al menos de 3 formas distintas éste problema.
"""
def pertenece1(lista:list[int], el_buscado:int) -> bool :
    res:bool = False
    for el in lista:
        if el == el_buscado:
            res = True
            break
    return res

def pertenece2(lista:list[int], el_buscado:int) -> bool :
    res:bool = False
    i:int = 0
    while(i < len(lista)):
        if lista[i] == el_buscado:
            res = True
            break
        i += 1
    return res

def pertenece3(lista:list[int], el_buscado:int) -> bool :
    res:bool = lista.count(el_buscado) > 0      # Probablemente no este permitida usar en el parcial, je.
    return res

def pertenece4(lista:list[int], el_buscado:int) -> bool :
    res:bool = el_buscado in lista
    return res

"""
2. 
    problema divide_a_todos (in s:seq⟨Z⟩, in e: Z) : Bool {
        requiere: { e ̸= 0 }
        asegura: { (res = true) ↔ (para todo i ∈ Z si 0 ≤ i < |s| → s[i] mod e = 0) }
    }
"""
def divide_a_todos(lista:list[int], el: int) -> bool:
    res:bool = True
    for el_lista in lista:
        if el_lista % el != 0:
            res = False
            break
    return res

"""
3. 
    problema suma_total (in s:seq⟨Z⟩) : Z {
        requiere: { T rue }
        asegura: { res es la suma de todos los elementos de s }
    }
Nota: no utilizar la función sum() nativa.
"""
def suma_total(lista:list[int]) -> int:
    res:int = 0
    for el in lista:
        res += el
    return res

"""
4. 
    problema maximo (in s:seq⟨Z⟩) : Z {
        requiere: { |s| > 0 }
        asegura: { res = al mayor de todos los números que aparece en s }
    }
Nota: no utilizar la función max() nativa
"""
def maximo(lista:list[int]) -> int:
    res:int = lista.pop(0)
    for el in lista:
        if el > res:
            res = el
    return res

"""
5. 
    problema minimo (in s:seq⟨Z⟩) : Z {
        requiere: { |s| > 0 }
        asegura: { res = al menor de todos los números que aparece en s }
    }
Nota: no utilizar la función min() nativa.
"""
def minimo(lista:list[int]) -> int:
    res:int = lista.pop(0)
    for el in lista:
        if el < res:
            res = el
    return res

"""
6. 
    problema ordenados (in s:seq⟨Z⟩) : Bool {
        requiere: { T rue }
        asegura: { res = true ↔(para todo i ∈ Z si 0 ≤ i < (|s| - 1) → s[i] < s[i + 1] }
    }
"""
def ordenados (lista:list[int]) -> bool :
    res:bool = True
    for i in range(len(lista) - 1):
        if lista[i] >= lista[i+1]:
            res = False
            break
    return res

"""
7. 
    problema pos_maximo (in s:seq⟨Z⟩) : Z {
        requiere: { T rue }
        asegura: { (Si |s| = 0, entonces res = -1; si no, res = al índice de la posición donde aparece el mayor elemento de s (si hay varios es la primera aparición) }
    }
"""
def pos_maximo(lista:list[int]) -> int:
    res:int = -1 if len(lista) == 0 else 0
    for i in range(len(lista)):
        if lista[res] < lista[i]:
            res = i
    return res


"""
8. 
    problema pos_minimo (in s:seq⟨Z⟩) : Z {
        requiere: { T rue }
        asegura: { (Si |s| = 0, entonces res = -1; si no, res = al índice de la posición donde aparece el menor elemento de s (si hay varios es la última aparición) }
    }
"""
def pos_minimo(lista:list[int]) -> int:
    res:int = -1 if len(lista) == 0 else 0
    for i in range(len(lista)):
        if lista[res] > lista[i]:
            res = i
    return res


"""
9. Dada una lista de palabras (seq⟨seq⟨Char⟩⟩), devolver verdadero si alguna palabra tiene longitud mayor a 7. Ejemplo: [“termo”, “gato”, “tener”, “jirafas”], devuelve falso.
    problema long_mayor_a_siete (in s:seq⟨seq⟨Char⟩⟩) : Bool {
        requiere: { T rue }
        asegura: { (res = true) ↔ (existe i ∈ Z tal que (0 ≤ i < (|s| - 1)) y (|s[i]| > 7) }
    }
"""
def long_mayor_a_siete(lista:list[str]) -> bool:
    res:bool = False
    for el in lista:
        if len(el) > 7:
            res = True
            break
    return res

"""
10. Dado un texto en formato string, devolver verdadero si es palíndromo (se lee igual en ambos sentidos), falso en caso contrario. Las cadenas de texto vacías o con 1 sólo elemento son palíndromo.
    problema es_palindroma (in s:seq⟨Char⟩) : Bool {
        requiere: { T rue }
        asegura: { (res = true) ↔ (s es igual a su reverso) }
    }
"""
def es_palindroma(palabra: str) -> bool:
    res:bool = palabra == reverso_palabra(palabra)
    return res

def reverso_palabra(palabra:str) -> str:
    res:str = ""
    for i in range(len(palabra) - 1, -1, -1):
        res += palabra[i]
    return res

"""
11. Recorrer una seq⟨Z⟩ y devolver verdadero si hay 3 números iguales consecutivos, en cualquier posición y False en caso
contrario.
    problema iguales_consecutivos (in s:seq⟨Z⟩) : Bool {
        requiere: { T rue }
        asegura: { (res = true) ↔ (existe i, j, k ∈ Z tal que (0 ≤ i, j, k < (|s| - 1)) y (i + 2 = j + 1 = k) y (s[i] = s[j] = s[k])) }
    }
"""
def iguales_consecutivos(lista:list[int]) -> bool:
    res:bool = False
    for i in range(len(lista) - 2):
        if lista[i] == lista[i+1] and lista[i] == lista[i+2]:
            res = True
            break
    return res

"""
12. Recorrer una palabra en formato string y devolver True si ésta tiene al menos 3 vocales distintas y False en caso
contrario.
    problema vocales_distintas (in s:seq⟨Char⟩) : Bool {
        requiere: { T rue }
        asegura: { (res = true) ↔ (existe i, j, k ∈ Z tal que (0 ≤ i, j, k < (|s| - 1)) y (s[i] ̸= s[j] ̸= s[k]) y (s[i], s[j], s[k] ∈ {'a', 'e', 'i', 'o', 'u'})) }
    }
"""
def vocales_distintas(palabra:str) -> bool:
    vocales_distintas:list[str] = []
    for letra in palabra:
        if letra in ['a', 'e', 'i', 'o', 'u'] and letra not in vocales_distintas:
            vocales_distintas.append(letra)
    
    res:bool = len(vocales_distintas) > 2
    return res

"""
13. Recorrer una seq⟨Z⟩ y devolver la posición donde inicia la secuencia de números ordenada más larga. Si hay dos subsecuencias de igual longitud devolver la posición donde empieza la primera. La secuencia de entrada es no vacía.
    problema pos_secuencia_ordenada_mas_larga (in s:seq⟨Z⟩) : Z {
        requiere: { |s| > 0 }
        asegura: { (res = i) ↔ (existe i, j ∈ Z tal que (0 ≤ i, j < (|s| - 1)) y i ≤ j y (para todo k tal que i ≤ k < j → s[k] ≤ s[k + 1]) y j-i+1 es máximo e i es el mínimo valor que lo cumple) }
    }
"""
def pos_secuencia_ordenada_mas_larga(lista:list[int]) -> int:
    lista_secuencias_ordenadas_pos:list[list[int]] = extraer_secuencias_ordenadas_pos(lista)
    lista_mas_larga:list[int] = lista_secuencias_ordenadas_pos[0]

    for sub_lista in lista_secuencias_ordenadas_pos:
        if len(sub_lista) > len(lista_mas_larga):
            lista_mas_larga = sub_lista
    
    return lista_mas_larga[0]

def extraer_secuencias_ordenadas_pos(lista:list[int]) -> list[list[int]]:
    res:list[list[int]] = []
    lista_pos_aux:list[int] = [0]

    for i in range(len(lista) - 1):
        if len(lista_pos_aux) == 0: lista_pos_aux.append(i)
        if lista[i] <= lista[i+1]:
            lista_pos_aux.append(i+1)
        else:
            res.append(lista_pos_aux.copy())
            if i == len(lista) - 2: res.append([i+1])
            lista_pos_aux.clear()

    if len(lista_pos_aux) != 0: res.append(lista_pos_aux.copy())
    return res

"""
14. Cantidad de dígitos impares.
    problema cantidad_digitos_impares (in s:seq⟨Z⟩) : Z {
        requiere: { Todos los elementos de números son mayores o iguales a 0 }
        asegura: { res es la cantidad total de dígitos impares que aparecen en cada uno de los elementos de números }
    }
Por ejemplo, si la lista de números es [57, 2383, 812, 246], entonces el resultado esperado sería 5 (los dígitos impares
son 5, 7, 3, 3 y 1).
"""
def cantidad_digitos_impares(lista:list[int]) -> int:
    res:int = 0
    for num in lista:
        num_str = str(num)
        for digit in num_str:
            if digit in ['1', '3', '5', '7', '9']:
                res += 1

    return res
