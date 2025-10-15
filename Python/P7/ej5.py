# Analizando parámetros in y out vs. resultado:

"""
1. 
    problema pertenece_a_cada_uno_version1 (in s:seq⟨seq⟨Z⟩⟩, in e:Z, out res: seq⟨Bool⟩) {
        requiere: { T rue }
        asegura: { |res| ≥ |s| }
        asegura: { Para todo i ∈ Z si 0 ≤ i < |s| → (res[i] = true ↔ pertenece(s[i], e)) }
    }
Nota: Reutilizar la función pertenece() implementada previamente para listas.
"""
def pertenece_a_cada_uno_version1(matriz:list[list[int]], el:int) -> list[bool]:
    res:list[bool] = []
    for i in range(len(matriz)):
        res.append(i)
        res[i] = el in matriz[i]    # En vez de usar pertenece uso in
    return res

"""
2. 
    problema pertenece_a_cada_uno_version2 (in s:seq⟨seq⟨Z⟩⟩, in e:Z, out res: seq⟨Bool⟩) {
        requiere: { T rue }
        asegura: { |res| = |s| }
        asegura: { Para todo i ∈ Z si 0 ≤ i < |s| → (res[i] = true ↔ pertenece(s[i], e)) }
    }
"""
def pertenece_a_cada_uno_version2(matriz:list[list[int]], el:int) -> list[bool]:
    res:list[bool] = []
    for i in range(len(matriz)):
        res.append(i)
        res[i] = el in matriz[i]    # En vez de usar pertenece uso in
    return res

"""
3. 
    problema pertenece_a_cada_uno_version3 (in s:seq⟨seq⟨Z⟩⟩, in e:Z) : seq⟨Bool⟩ {
        requiere: { T rue }
        asegura: { |res| = |s| }
        asegura: { Para todo i ∈ Z si 0 ≤ i < |s| → (res[i] = true ↔ pertenece(s[i], e)) }
    }
"""
def pertenece_a_cada_uno_version3(matriz:list[list[int]], el:int) -> list[bool]:
    res:list[bool] = []
    for i in range(len(matriz)):
        res.append(i)
        res[i] = el in matriz[i]    # En vez de usar pertenece uso in
    return res

"""
4. Pensar: 
    - ¿Cómo cambia este problema respecto de la versión 1? 
    - Pensar en relación de fuerza entre: implementación en Python y las especificaciones. 
        - ¿Se puede usar la implementación del ejercicio 2 para la especificación del 1? 
        - ¿Se puede usar la implementación del ejercicio 1 para la especificación del 2? 
    Justificar su respuesta.

Rta: 
    De la v1 a la v2 lo unico que cambia es un asegura, de (|res| ≥ |s|) a (|res| = |s|)
    El segundo asegura coincide en ambos y dice: { Para todo i ∈ Z si 0 ≤ i < |s| → (res[i] = true ↔ pertenece(s[i], e)) }
    Entonces, ambas versiones van a coincidir en los indices de s, pero el res de la v1, podria tener mas indices agregados, los cuales seguirian respetando la especificacion

    De la v2 a la v3 el parametro out res: seq⟨Bool⟩ no aparece, sin embargo, este aparece como lo que devuelve el problema, lo cual son distintas formas de decir lo mismo.

    Por lo tanto, v2 → v3 y v3 → v2 son tautologias. Ademas, v2 o v3 → v1, pero no vale que v1 → v2 ni v3.
    Por ejemplo: si tenemos s=[[1,2,3],[4,5,6],[7,8,9]] y e=1. 
        Para v2 o v3 (unica posibilidad): res = [True, False, False]
            asegura: { |res| = |s| } ✅
            asegura: { Para todo i ∈ Z si 0 ≤ i < |s| → (res[i] = true ↔ pertenece(s[i], e)) } ✅
        
        Para v1 (una de las posibilidades): res = [True, False, False, True, False]
            asegura: { |res| ≥ |s| } ✅
            asegura: { Para todo i ∈ Z si 0 ≤ i < |s| → (res[i] = true ↔ pertenece(s[i], e)) } ✅

        El res de v2 o v3 sirve para v1? res = [True, False, False]
                asegura: { |res| ≥ |s| } ✅
                asegura: { Para todo i ∈ Z si 0 ≤ i < |s| → (res[i] = true ↔ pertenece(s[i], e)) } ✅
            Si, cumple.
        El res de v1 sirve para v2 o v3? res = [True, False, False, True, False]
                asegura: { |res| = |s| } ❌
                asegura: { Para todo i ∈ Z si 0 ≤ i < |s| → (res[i] = true ↔ pertenece(s[i], e)) } ✅
            No, no cumple.
        
        
    Entonces, sacamos que v2 = v3 y que cualquier implementacion de v2 o v3 sirve para v1, pero no toda implementacion de v1 sirve para v2 ni v3.
        Vale que: v2 o v3 → v1. Pero no vale: v1 → v2 ni v3
    Por lo tanto, v2 y v3 son igual de fuertes e igual de debiles, que a su vez son mas fuertes que v1 
"""