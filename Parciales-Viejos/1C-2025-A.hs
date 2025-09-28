{--
\* Ejercicio 1

    problema hayPrimosGemelos (d: Z,h: Z) : Bool {
        requiere: {0 < d ≤ h}
        asegura: {res = true <=> existen dos números p1 y p2 contenidos en el rango [d..h] tales que p1 y p2 son primos gemelos}
    }

Aclaración: Se dice que p1 y p2 son primos gemelos si ambos son primos y además |p2-p1| = 2
--}

hayPrimosGemelos :: Integer -> Integer -> Bool
hayPrimosGemelos d h = hayPrimosGemelosAux [d .. h]

hayPrimosGemelosAux :: [Integer] -> Bool
hayPrimosGemelosAux [] = False
hayPrimosGemelosAux (x : xs) = (esPrimo x && tienePrimoGemelo x xs) || hayPrimosGemelosAux xs

tienePrimoGemelo :: Integer -> [Integer] -> Bool
tienePrimoGemelo _ [] = False
tienePrimoGemelo n lst = estaEnLaLista (n + 2) lst && esPrimo (n + 2)

estaEnLaLista :: (Eq t) => t -> [t] -> Bool
estaEnLaLista _ [] = False
estaEnLaLista el (x : xs) = el == x || estaEnLaLista el xs

esPrimo :: Integer -> Bool
esPrimo n = esPrimoAux n 2

esPrimoAux :: Integer -> Integer -> Bool
esPrimoAux 1 _ = False
esPrimoAux n i
  | i * i > n = True
  | mod n i == 0 = False
  | otherwise = esPrimoAux n (i + 1)

-- Aclaracion primer guarda:
--  No hace falta revisar todos los divisores para saber si un numero es primo... Si no tiene un divisor hasta √n, entonces es primo.
--  Si un numero es compuesto, entonces existe al menos un a y un b enteros tales que: n = a*b
--  Si a > √n y b > √n, entonces a*b > √n * √n, pero √n * √n = n, entonces esto es un absurdo ya que sabemos que a*b=n
--  En consecuencia, al menos uno de los factores, a o b, debe ser menor o igual a √n
--  Por ejemplo: para el 97, solo recorreriamos hasta i = 10 y ya sabriamos que es primo, de la otra forma recorreriamos hasta i = 97

{--
\* Ejercicio 2

Representaremos un día de cursada de cierta materia con una tupla String x String x Z x Z, donde:

    La primera componente de la tupla contiene el nombre de una materia
    La segunda componente de la tupla contiene el día de cursada (lunes, martes, etc)
    La tercera componente de la tupla contiene el horario de inicio de la cursada de ese día
    La cuarta componente de la tupla contiene el horario de fin de la cursada de ese día

Se pide implementar materiasTurnoTarde, que dada una lista de cursadas devuelva aquellas materias que se cursan en el turno tarde (14 a 17hs)

    problema materiasTurnoTarde (s: seq⟨String x String x Z x Z⟩) :seq⟨String⟩ {
        requiere: { s[i]1 es alguno de los siguientes valores: "Lunes", "Martes", "Miércoles", "Jueves", "Viernes"}
        requiere: { s[i]2 ≥ 8 para todo i tal que 0 ≤ i < |s|}
        requiere: { s[i]3 ≤ 22 para todo i tal que 0 ≤ i < |s|}
        requiere: { s[i]2 < s[i]3 para todo i tal que 0 ≤ i < |s|}
        asegura: { res no tiene elementos repetidos}
        asegura: { res contiene solamente los nombre las materias incluídas en s tales el horario de cursada de dichas materias se superpone (total o parcialmente) con el rango (14..17)}
    }

--}
type Materia = String

type Dia = String

type Hora = Integer

type CursadaMateria = (Materia, Dia, Hora, Hora)

cursadaEj :: [CursadaMateria]
cursadaEj = [("Algebra I", "Lunes", 9, 14), ("PLP", "Martes", 15, 20), ("IP", "Miercoles", 18, 21), ("Analisis", "Jueves", 14, 17), ("Algo 2", "Viernes", 9, 15)]

materiasTurnoTarde :: [CursadaMateria] -> [Materia]
materiasTurnoTarde [] = []
materiasTurnoTarde ((materia, _, inicio, fin) : otrasMaterias)
  | (inicio >= 8 && fin <= 14) || (inicio >= 17 && fin <= 22) = materiasTurnoTarde otrasMaterias
  | otherwise = materia : materiasTurnoTarde otrasMaterias

-- Entiendo por lo del rango (14..17) que si termina a las 14 o si arranca a las 17 no se incluye (porque son parentesis) en el horario del turno tarde , de lo contrario, simplmenete habria que sacar 2 iguales, en fin <= 14 y en inicio >= 17

{--
\* Ejercicio 3

    problema maximaSumaDeTresConsecutivos (s: seq⟨Z⟩) : Z {
        requiere: { |s| ≥ 3}
        asegura: { res es la suma de tres elementos que se encuentran en posiciones consecutivas de s }
        asegura: {Para cualquier i en el rango 1 ≤ i < |s|-1, se cumple que s[i-1]+s[i]+s[i+1] ≤ res}
    }
--}
maximaSumaDeTresConsecutivos :: [Integer] -> Integer
maximaSumaDeTresConsecutivos [x, y, z] = x + y + z
maximaSumaDeTresConsecutivos (x : y : z : xs)
  | x + y + z >= maximaSumaDeTresConsecutivos (y : z : xs) = x + y + z
  | otherwise = maximaSumaDeTresConsecutivos (y : z : xs)

{--
\* Ejercicio 4

    problema sumaIesimaColumna (matriz: seq⟨seq⟨Integer⟩⟩, col: Integer) : Integer⟩{
        requiere: {Todos los elementos de la secuencia matriz tienen la misma longitud}
        requiere: {|matriz| > 0}
        requiere: {|matriz[0]| > 0}
        requiere: {1 ≤ col ≤ |matriz[0]| }
        asegura: {res es la sumatoria de los elementos matriz[i][col-1] para todo i tal que 0 ≤ i < |matriz| }
    }
--}

sumaIesimaColumna :: [[Integer]] -> Integer -> Integer
sumaIesimaColumna [] _ = 0
sumaIesimaColumna (fila : otrasFilas) col = iesimoElemento fila (col - 1) + sumaIesimaColumna otrasFilas col

iesimoElemento :: [Integer] -> Integer -> Integer
iesimoElemento (el : otrosEl) 0 = el
iesimoElemento (el : otrosEl) i = iesimoElemento otrosEl (i - 1)

{--
\* Ejercicio 5

Conteste marcando la opción correcta.
Sean e1 y e2 dos especificaciones con la misma postcondición. Si la precondición de e1 es más débil que la de e2, entonces:
[ ] Para que un programa sea correcto respecto de e2, debe considerar mayor cantidad de valores de entrada que un programa que busca satisfacer e1.
[X] Para que un programa sea correcto respecto de e1, debe considerar mayor cantidad de valores de entrada que un programa que busca satisfacer e2.
[ ] No es posible afirmar ninguna de las opciones sin conocer en detalle ambas precondiciones.

\* Ejercicio 6

Conteste marcando la opción correcta.
Dado un problema con parámetros x e y, cuya precondición es (x>0 ∨ esPar(y)):
[ ] Todos los casos de test deben tener inputs que cumplan x>0 ∧ esPar(y)
[ ] Independientemente de la precondición, debo testear todas las combinaciones de valores x e y
[X] No tiene sentido tener un caso de test con x=0, y=1

--}
