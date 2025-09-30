{-
Ejercicio 1 (2, 5 puntos)
Se dice que n es un número abundante si la suma de sus divisores propios es mayor que n. Los divisores propios de un número son todos los divisores sin contar al número mismo. Por ejemplo, los divisores propios de 12 son 1, 2, 3, 4 y 6. La suma de los divisores propios de 12 es 1 + 2 + 3 + 4 + 6 = 16, que es mayor que 12. Por lo tanto, 12 es un número abundante.
Se pide implementar cantidadNumerosAbundantes:

    problema cantidadNumerosAbundantes (d: Z,h: Z) : Z {
        requiere: {0 < d ≤ h}
        asegura: {res es la cantidad de números abundantes en el rango [d..h]}
    }

Ejemplo : cantidadNumerosAbundantes 12 24 debe devolver 4
-}
--
cantidadNumerosAbundantes :: Integer -> Integer -> Integer
cantidadNumerosAbundantes d h = cantidadNumerosAbundantesAux [d .. h]

cantidadNumerosAbundantesAux :: [Integer] -> Integer
cantidadNumerosAbundantesAux [] = 0
cantidadNumerosAbundantesAux (x : xs)
  | esAbundante x = 1 + cantidadNumerosAbundantesAux xs
  | otherwise = cantidadNumerosAbundantesAux xs

esAbundante :: Integer -> Bool
esAbundante n = sumaDivisores n > n

sumaDivisores :: Integer -> Integer
sumaDivisores n = sumaDivisoresAux n 1

sumaDivisoresAux :: Integer -> Integer -> Integer
sumaDivisoresAux n i
  | i * 2 > n = 0
  | mod n i == 0 = i + sumaDivisoresAux n (i + 1)
  | otherwise = sumaDivisoresAux n (i + 1)

{-
Ejercicio 2 (2 puntos)
Representaremos una cursada aprobada con una tupla String x Z x Z, donde:
    ◦ La primera componente de la tupla contiene el nombre de una materia
    ◦ La segunda componente de la tupla contiene el año de aprobación de la cursada
    ◦ La tercera componente de la tupla contiene el cuatrimestre de aprobación de la cursada (el valor 0 representa un curso de verano)
Se pide implementar cursadasVencidas, que dada una lista de cursadas devuelva aquellas materias cuya aprobación de la cursada ya venció, y por lo tanto ya no se puede rendir el final

    problema cursadasVencidas (s: seq⟨String x Z x Z⟩) :seq⟨String⟩ {
        requiere: { s[i]1 ≥ 1993 para todo i tal que 0 ≤ i < |s|}
        requiere: { 0 ≤ s[i]2 ≤ 2 para todo i tal que 0 ≤ i < |s|}
        asegura: { res no tiene elementos repetidos}
        asegura: { res contiene los nombres de todas las materias incluídas en s tales que la materia fue aprobada a más tardar en el primer cuatrimestre de 2021, inclusive}
        asegura: { res contiene solamente los nombres de las materias incluídas en s tales que la materia fue aprobada a más tardar en el primer cuatrimestre de 2021, inclusive}
    }

Ejemplo : cursadasVencidas [("Algoritmos y Estructuras de Datos I", 2020, 2), ("Algoritmos y Estructuras de Datos II", 2022, 1)] debe devolver ["Algoritmos y Estructuras de Datos I"]
-}
type Materia = String

type Anio = Integer

type Cuatrimestre = Integer

type CursadaAprobada = (Materia, Anio, Cuatrimestre)

cursadasVencidas :: [CursadaAprobada] -> [String]
cursadasVencidas [] = []
cursadasVencidas ((materia, anio, cuatri) : otrasCursadas)
  | (anio == 2021 && cuatri <= 1) || anio < 2021 = materia : cursadasVencidas otrasCursadasSinLaActual
  | otherwise = cursadasVencidas otrasCursadasSinLaActual
  where
    otrasCursadasSinLaActual = quitarCursada materia otrasCursadas

quitarCursada :: String -> [CursadaAprobada] -> [CursadaAprobada]
quitarCursada _ [] = []
quitarCursada materiaAQuitar ((materia, anio, cuatri) : otrasCursadas)
  | materiaAQuitar == materia = quitarCursada materiaAQuitar otrasCursadas
  | otherwise = (materia, anio, cuatri) : quitarCursada materiaAQuitar otrasCursadas

{-
Ejercicio 3 (2 puntos)
    problema saturarEnUmbralHastaNegativo (s: seq⟨Z⟩, u: Z) : seq⟨Z⟩ {
        requiere: {u > 0}
        asegura: { La longitud de res es igual a la cantidad de elementos no negativos consecutivos desde el inicio de s }
        asegura: {Para cualquier i en el rango 0 ≤ i < |res| tal que 0 ≤ s[i] ≤ u, se cumple que res[i] = s[i]}
        asegura: {Para cualquier i en el rango 0 ≤ i < |res| tal que s[i] > u, se cumple que res[i] = u}
    }

Ejemplo : saturarEnUmbralHastaNegativo [3, 8, 5, 0, 7, -2, 4] 5 debe devolver [3, 5, 5, 0, 5]
-}
saturarEnUmbralHastaNegativo :: [Integer] -> Integer -> [Integer]
saturarEnUmbralHastaNegativo [] _ = []
saturarEnUmbralHastaNegativo (x : xs) u
  | x >= 0 && x <= u = x : saturarEnUmbralHastaNegativo xs u
  | x >= 0 && x > u = u : saturarEnUmbralHastaNegativo xs u
  | otherwise = []

{-
Ejercicio 4 (2 puntos)
    problema cantidadParesColumna (matriz: seq⟨seq⟨Z⟩⟩, col: Z) : Z{
        requiere: {Todos los elementos de la secuencia matriz tienen la misma longitud}
        requiere: {|matriz| > 0}
        requiere: {|matriz[0]| > 0}
        requiere: {1 ≤ col ≤ |matriz[0]| }
        asegura: {res es la cantidad de números pares de los elementos matriz[i][col-1] para todo i tal que 0 ≤ i < |matriz| }
    }

Ejemplo : cantidadParesColumna [[-9, 8, 2, 3], [2, 7, -5, 3], [-1, 0, 5, 6]] 2 debe devolver 2
-}
cantidadParesColumna :: [[Integer]] -> Integer -> Integer
cantidadParesColumna [] _ = 0
cantidadParesColumna (fila : otrasFilas) col
  | mod posicionActualFilaCol 2 == 0 = 1 + cantidadParesColumna otrasFilas col
  | otherwise = cantidadParesColumna otrasFilas col
  where
    posicionActualFilaCol = iesimoElemento fila (col - 1)

iesimoElemento :: [Integer] -> Integer -> Integer
iesimoElemento (x : xs) 0 = x
iesimoElemento (x : xs) i = iesimoElemento xs (i - 1)

{-
Ejercicio 5 (0,75 puntos)

Conteste marcando la opción correcta.
¿Qué ocurre si una definición por pattern matching no contempla todos los casos posibles?
[ ] El programa no compila.
[ ] Haskell elige un valor por defecto automáticamente.
[X] El programa puede lanzar un error en tiempo de ejecución si se invoca con un patrón no contemplado.

Ejercicio 6 (0,75 puntos)
Conteste marcando la opción correcta.
Dado un problema con parámetros c (de tipo Char) y s (de tipo String), cuya única precondición es (esVocal(c) ∨ longitud(s) > 3):
[ ] La precondición garantiza que siempre se trabajará con strings no vacíos.
[X] Si c es una consonante y s tiene longitud igual a 2, no se garantiza el comportamiento correcto del programa.
[ ] Cualquier combinación de valores de c y s es válida, porque la precondición es una disyunción en vez de una conjunción.

-}
