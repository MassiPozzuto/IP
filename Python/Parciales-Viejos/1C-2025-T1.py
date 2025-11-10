from queue import LifoQueue as Pila
from typing import Any

# Ejercicio 1 -----------------------------------------------------------------
"""
Implementar la función prefijo_que_mas_suma:

    problema prefijo_que_mas_suma (in s: seq⟨Z⟩) : Z {
        requiere: { |s| > 0 }
        asegura: { res = ∑ ki=0 s[i] para algún k tal que 0 ≤ k < |s|}
        asegura: { res ≥ ∑ ki=0 s[i] para todos los k tales que 0 ≤ k < |s|}
    }
"""
def prefijo_que_mas_suma(s: list[int]) -> int:
    res:int = s[0]

    sumatoria:int = 0 
    for num in s:
        sumatoria += num

        if sumatoria > res:
            res = sumatoria

    return res


# Ejercicio 2 -----------------------------------------------------------------
"""
Todavía existen materias en la cuales los exámenes se entregan en papel. A medida que los estudiantes van entregando, van apoyando (apilando!) sobre el escritorio del docente sus exámenes, y en la primera hoja indican su nombre y la cantidad de hojas entregadas (además del enunciado). Esta información se almacena en una Pila de String x Z. Nos intersa conocer el nombre de la primera persona que entregó un examen en blanco (es decir, entregó 0 hojas además del enunciado).

    problema primera_entrega_en_blanco (in examenes: Pila⟨ String x Z ⟩) : String {
        requiere:{ Las primeras componentes de examenes son strings no vacíos y todos distintos entre sí }
        requiere:{ Existe al menos un elemento p dentro de la pila examenes tal que p1=0 }
        asegura: { Sea p el primer elemento insertado en la pila examenes tal que p1=0. Entonces, res = p0 }
    }
"""

def primera_entrega_en_blanco(examenes: Pila[tuple[str, int]]) -> str:
    examenes_copia: Pila[tuple[str, int]] = copiar_pila(examenes)
    res:str = ""
    while not examenes_copia.empty(): # Si hay dos examenes en blanco agarramos el ultimo que salga de la pila, ya que seria el primero que fue entregado
        examen_actual:tuple[str, int] = examenes_copia.get()
        if examen_actual[1] == 0:
            res = examen_actual[0]

    return res

def copiar_pila(pila: Pila[Any]) -> Pila[Any]:
    pila_copia:Pila[Any] = Pila()

    pila_aux:Pila[Any] = Pila()
    while not pila.empty():
        pila_aux.put(pila.get())

    while not pila_aux.empty():
        actual: Any = pila_aux.get()
        pila.put(actual)
        pila_copia.put(actual)

    return pila_copia


# Ejercicio 3 -----------------------------------------------------------------
"""
Implementar la función desplazar_columna_hacia_arriba:

    problema desplazar_columna_hacia_arriba(inout A: seq⟨seq⟨Z⟩⟩, in col: Z) {
        requiere: { Todas las filas de A tienen la misma longitud (estrictamente positiva)}
        requiere: { |A| > 0}
        requiere: { 0 ≤ col < |A[0]| }
        modifica: { A }
        asegura: { A tiene exactamente las mismas dimensiones que A@pre }
        asegura: { A[i][j] = A@pre[i][j] para todo i, j en rango tal que col ≠ j }
        asegura: { A[i][col] = A@pre[i+1][col] para todo i tal que 0 ≤ i < |A|-1 }
        asegura: { A[|A|-1][col] = A@pre[0][col] }
    }
"""

def desplazar_columna_hacia_arriba(A: list[list[int]], col:int) -> None:
    primer_elemento: int = A[0][col]
    
    for i in range(len(A) - 1):
        A[i][col] = A[i+1][col]
    
    A[len(A) - 1][col] = primer_elemento


# Ejercicio 4 -----------------------------------------------------------------
"""
A lo largo del año se realizaron diversas competencias de programación, las cuales van otorgando puntos y permiten generar un ranking entre los competidores, con el objetivo de entregar premios al final del año. En cada una de las competencias se selecciona a los 3 participantes con mejor desempeño, y se define el podio para cada una. Luego, se asignan los puntajes de la siguiente manera:

    Quien sale en primer puesto recibe 3 puntos
    Quien sale en segundo puesto recibe 2 puntos
    Quien sale en tercer puesto recibe 1 punto

Nuestro objetivo es, dada una lista de competencias y sus resultados, conocer el ranking actual.

    problema armar_ranking (in podios: seq⟨Diccionario⟨Z,String⟩⟩): Diccionario⟨String,Z⟩ {
        requiere: { Cada diccionario de podios tiene como claves los valores 1, 2 y 3 (o algún subconjunto de los mismos)}
        requiere: { Sea d un diccionario de la secuencia podios , entonces d no contiene valores repetidos }
        asegura: { nom es clave de res si y sólo si existe un diccionario en podios tal que nom es valor de dicho diccionario}
        asegura: { Cada clave c de res tiene como valor la sumatoria de los puntos obtenidos por c en cada una de las competencias de podios (suma 3 puntos si salió primero, 2 puntos si salió segundo, 1 punto si salió tercero y 0 puntos si no estuvo en el podio de esa competencia)}
    }

"""
def armar_ranking(podios: list[dict[int, str]]) -> dict[str, int]:
    res:dict[str, int] = {}
    for podio in podios:
        for puesto, nombre in podio.items():
            if nombre not in res.keys():
                res[nombre] = 0

            if puesto == 1:
                res[nombre] += 3
            elif puesto == 2:
                res[nombre] += 2
            else:
                res[nombre] += 1

    return res

# Ejercicio 5 -----------------------------------------------------------------
"""
Dada la siguiente especificación y una posible implementación de la misma, conteste marcando la opción correcta.

problema sumar_o_restar_uno (in n: Z): Z {
  requiere: { True }
  asegura: { Si n > 0, res = n+1}
  asegura: { Si n = 0, res = n}
  asegura: { Si n < 0, res = n-1}
}

def sumar_o_restar_uno(n: int) -> int:
   res: int = n
   if n > 0:
        res += 1
   else:
        res -= 1
   return res

[ ] El código es correcto, calcula lo pedido en la especificación para cualquier input
[ ] El código tiene un bug, y si hacemos un test suite que cubra todas las líneas lo detectaremos
[X] El código tiene un bug, pero es posible hacer un test suite que cubra todas las líneas y no detectar dicho bug

"""

# Ejercicio 6 -----------------------------------------------------------------
"""
Seleccione la opción correcta.

[ ] Si tengo 2 programas y los ejecuto con los mismos parámetros, el programa que tiene mayor cantidad de líneas de código ejecutará más operaciones que el que tiene menos líneas de código.
[ ] Dado un programa p que recibe una secuencia como parámetro, p([1]) ejecutará menos operaciones que p([0,1,2,3,4,5])
[X] No es posible afirmar ninguna de las opciones anteriores sin conocer el código de la/las función/funciones
"""