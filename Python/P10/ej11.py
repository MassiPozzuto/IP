"""
Sufijos que son palíndromos

Decimos que una palabra es palíndromo si se lee igual de izquierda a derecha que de derecha a izquierda. Se nos pide programar en python la siguiente función:

    problema cuantos_sufijos_son_palindromos (in texto: str) : Z {
        requiere: {True}
        asegura: {res es igual a la cantidad de palíndromos que hay en el conjunto de sufijos de texto.}
    }

Nota: un sufijo es una subsecuencia de texto que va desde una posición cualquiera hasta el al final de la palabra. Ej: ”Diego”, el conjunto de sufijos es: ”Diego”, ”iego”,”ego”,”go”, ”o”. Para este ejercicio no consideraremos a ”” como sufijo de ningún texto.

"""

def cuantos_sufijos_son_palindromos(texto: str) -> int:
    res:int = 0
    sufijos:list[str] = obtener_sufijos(texto)
    for sufijo in sufijos:
        if sufijo == reverso(sufijo):
            res += 1
    
    return res

def obtener_sufijos(string: str) -> list[str]:
    res:list[str] = []

    acumulador:str = ""
    for i in range(len(string) - 1, -1, -1):
        acumulador = string[i] + acumulador
        res.append(acumulador)
    
    return res

def reverso(string: str) -> str:
    res:str = ""
    for i in range(len(string) - 1, -1, -1):
        res += string[i]

    return res

print(cuantos_sufijos_son_palindromos("diegog"))