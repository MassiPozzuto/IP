# Implementar las siguientes funciones sobre secuencias pasadas por par´ametro:

"""
1.
    problema ceros_en_posiciones_pares (inout s:seq⟨Z⟩) {
        requiere: { True }
        modifica: { s }
        asegura: { (|s| = |s@pre|) y (para todo i entero, con 0 <= i < |s|, si i es impar entonces s[i] = s@pre[i] y, si i es par, entonces s[i] = 0) }
    }
"""
def ceros_en_posiciones_pares(lista:list[int]) -> None:
    for i in range(0, len(lista), 2):
        lista[i] = 0

"""
2. 
    problema ceros_en_posiciones_pares2 (in s:seq⟨Z⟩) : seq⟨Z⟩ {
        requiere: { T rue }
        asegura: { (|s| = |res|) y (para todo i entero, con 0 <= i < |res|, si i es impar entonces res[i] = s[i] y, si i espar, entonces res[i] = 0) }
    }
"""
def ceros_en_posiciones_pares2(lista:list[int]) -> list[int]:
    nueva_lista:list[int] = lista.copy()
    for i in range(0, len(nueva_lista), 2):
        nueva_lista[i] = 0
    return nueva_lista

"""
3. Dada una cadena de caracteres devuelva una cadena igual a la anterior, pero sin las vocales. No se agregan espacios, sino que borra la vocal y concatena a continuación.
    problema sin_vocales (in s:seq⟨Char⟩) : seq⟨Char⟩ {
        requiere: { T rue }
        asegura: { res es la subsecuencia de s que se obtiene al quitarle las vocales a s }
    }
Nota: Una subsecuencia de una cadena es una nueva secuencia que se crea eliminando algunos elementos de la cadena original, conservando el orden de los elementos restantes.
"""
def sin_vocales(palabra:str) -> str:
    palabra_sin_vocales:str = ""
    for letra in palabra:
        if letra not in ['a','e','i','o','u']: palabra_sin_vocales += letra
    return palabra_sin_vocales

"""
4. 
    problema reemplaza_vocales (in s:seq⟨Char⟩) : seq⟨Char⟩ {
        requiere: { T rue }
        asegura: { |res| = |s| }
        asegura: { Para todo i ∈ Z, si 0 ≤ i < |res| → (pertenece(<'a','e','i','o','u'>, s[i]) ∧ res[i] = ' ') ∨ (¬ pertenece(<'a','e','i','o','u'>, s[i]) ∧ res[i] = s[i])) }
    }
"""
def reemplaza_vocales(palabra:str) -> str:
    palabra_remplazando_vocales:str = ""
    for letra in palabra:
        if letra not in ['a','e','i','o','u']: palabra_remplazando_vocales += letra
        else: palabra_remplazando_vocales += ' '
    return palabra_remplazando_vocales

"""
5.
    problema da_vuelta_str (in s:seq⟨Char⟩) : seq⟨Char⟩ {
        requiere: { T rue }
        asegura: { |res| = |s| }
        asegura: { Para todo i ∈ Z si 0 ≤ i < |res| → res[i] = s[|s| - i - 1] }
    }
"""
def da_vuelta_str(string:str) -> str:
    reverso_string:str = ""
    for i in range(len(string) - 1, -1, -1):
        reverso_string += string[i]
    return reverso_string

"""
6. 
    problema eliminar_repetidos (in s:seq⟨Char⟩) : seq⟨Char⟩ {
        requiere: { T rue }
        asegura: { (|res| ≤ |s|) ∧ (para todo i ∈ Z si 0 ≤ i < |s| → pertenece(s[i], res)) ∧ (para todo i, j ∈ Z si (0 ≤ i, j < |res| ∧ i ̸= j) → res[i] ̸= res[j]) }
    }
"""
def eliminar_repetidos(string:str) -> str:
    string_sin_repetidos:str = ""
    for char in string:
        if char not in string_sin_repetidos: string_sin_repetidos += char
    return string_sin_repetidos
