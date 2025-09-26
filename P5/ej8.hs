{-
En este ejercicio vamos a trabajar con matrices.

Vamos a representar una matriz como una secuencia de secuencias. Si m es nuestra secuencia de secuencias que representa una matriz: La secuencia i-esima de m representa la i-esima fila de la matriz, y el elemento j-´esimo dentro de la secuencia i-esima representa el elemento en la fila i, columna j de la matriz.
Por ejemplo, a la matriz identidad de R3 la podemos definir como la lista de listas: [[1, 0, 0], [0, 1, 0], [0, 0, 1]] en Haskell.

Usando esta representacion, definir las siguientes funciones sobre matrices:
-}
--
-- 1. sumaTotal :: [[Integer]] -> Integer segun la siguiente especificacion: (Ver en el apunte)
sumaTotal :: [[Integer]] -> Integer
sumaTotal [] = 0
sumaTotal (x : xs) = sumatoria x + sumaTotal xs

-- Funcion del ejercicio 3
sumatoria :: [Integer] -> Integer
sumatoria [] = 0
sumatoria (x : xs) = x + sumatoria xs

--
-- 2. cantDeAparicionesMatriz :: Integer -> [[Integer]] -> Integer segun la siguiente especificacion: (Ver en el apunte)
cantDeAparicionesMatriz :: Integer -> [[Integer]] -> Integer
cantDeAparicionesMatriz _ [] = 0
cantDeAparicionesMatriz e (x : xs) = cantDeAparicionesLista e x + cantDeAparicionesMatriz e xs

cantDeAparicionesLista :: (Eq t) => t -> [t] -> Integer
cantDeAparicionesLista el [] = 0
cantDeAparicionesLista el (x : xs)
  | el == x = 1 + cantDeAparicionesLista el xs
  | otherwise = cantDeAparicionesLista el xs

--
-- 3. contarPalabras :: String ->[[String]] ->Int segun la siguiente especificacion:
{-
    problema contarPalabras (p: String, m: seq⟨seq⟨String⟩⟩) : Z {
        requiere: { |m| > 0 }
        requiere: { |m[0]| > 0 }
        requiere: { Todos los elementos de la secuencia m tienen la misma longitud }
        asegura: { El resultado es la cantidad de veces que p aparece exactamente igual en los elementos de m }
    }
-}
contarPalabras :: String -> [[String]] -> Integer
contarPalabras _ [] = 0
contarPalabras p (x : xs) = cantDeAparicionesLista p x + contarPalabras p xs

--
-- 4. cantDeAparicionesGen :: (Eq a) => a -> [[a]] -> Integer tal que pueda usarlo para resolver los dos ejercicios anteriores.
-- Je, medio que ya lo hice
cantDeAparicionesGen :: (Eq a) => a -> [[a]] -> Integer
cantDeAparicionesGen _ [] = 0
cantDeAparicionesGen p (x : xs) = cantDeAparicionesLista p x + cantDeAparicionesGen p xs

--
-- 5. prodPorEscalarMatriz :: Integer -> [[Integer]] -> [[Integer]] segun la siguiente especificacion:
{-
    problema prodPorEscalarMatriz (lambda: Z, m: seq⟨seq⟨Z⟩⟩) : seq⟨seq⟨Z⟩⟩ {
        requiere: { |m| > 0 }
        requiere: { |m[0]| > 0 }
        requiere: { Todos los elementos de la secuencia m tienen la misma longitud }
        asegura: { |resultado| = m }
        asegura: { Para todo 0 ≤ i < |m|, |resultado[i]| = |m[i]| }
        asegura: { Para toda posicion valida i, j de m, resultado[i][j] = lambda × m[i][j]}
    }
-}
prodPorEscalarMatriz :: Integer -> [[Integer]] -> [[Integer]]
prodPorEscalarMatriz _ [] = []
prodPorEscalarMatriz lambda (m : ms) = prodPorEscalarLista lambda m : prodPorEscalarMatriz lambda ms

prodPorEscalarLista :: Integer -> [Integer] -> [Integer]
prodPorEscalarLista _ [] = []
prodPorEscalarLista lambda (x : xs) = lambda * x : prodPorEscalarLista lambda xs

--
-- 6. concatenarFilas :: [[String]] ->[String] segun la siguiente especificacion:
{-
    problema concatenarFilas (m: seq⟨seq⟨String⟩⟩) : seq⟨String⟩ {
        requiere: { |m| > 0 }
        requiere: { |m[0]| > 0 }
        requiere: { Todos los elementos de la secuencia m tienen la misma longitud }
        asegura: { |resultado| = |m| }
        asegura: { Para todo 0 ≤ i < |m|, resultado[i] = concatenacion de todos los strings en m[i] }
    }
-}
concatenarFilas :: [[String]] -> [String]
concatenarFilas [] = []
concatenarFilas (x : xs) = x ++ concatenarFilas xs

--
-- 7. iesimaFila :: Integer -> [[a]] -> [a] segun la siguiente especificacion:
{-
    problema iesimaFila (i: Z, m: seq⟨seq⟨T⟩⟩) : seq⟨T⟩ {
        requiere: { |m| > 0 }
        requiere: { |m[0]| > 0 }
        requiere: { Todos los elementos de la secuencia m tienen la misma longitud }
        requiere: { 0 ≤ i < |m| }
        asegura: { |resultado| = |m[i]| }
        asegura: { Para todo 0 <= j < |m[i]|, resultado[j] = m[i][j] }
    }
-}
iesimaFila :: Integer -> [[a]] -> [a]
iesimaFila i [] = [] -- Realmente solo entra aca cuando no se cumple el requiere, pero me gusta abarcarlo igual
iesimaFila 0 (row : _) = row
iesimaFila i (_ : otherRows) = iesimaFila (i - 1) otherRows

--
-- 8. iesimaColumna :: Integer -> [[a]] -> [a] segun la siguiente especificacion:
{-
    problema iesimaColumna (i: Z, m: seq⟨seq⟨T⟩⟩) : seq⟨T⟩ {
        requiere: { |m| > 0 }
        requiere: { |m[0]| > 0 }
        requiere: { Todos los elementos de la secuencia m tienen la misma longitud }
        requiere: { 0 ≤ i < |m[0]| }
        asegura: { |resultado| = |m| }
        asegura: { Para todo 0 <= f < |m|, resultado[f] = m[f][i] }
    }
-}
-- Falla cuando no es una matriz (o sea, no se cumple el requiere)
iesimaColumna :: Integer -> [[a]] -> [a]
iesimaColumna i [] = []
iesimaColumna i (x : xs) = iesimoElemento i x : iesimaColumna i xs

iesimoElemento :: Integer -> [a] -> a
iesimoElemento 0 (elem : _) = elem
iesimoElemento i (_ : otherElem) = iesimoElemento (i - 1) otherElem

--
-- 9. matrizIdentidad :: Integer -> [[Integer]] segun la siguiente especificacion:
{-
    problema matrizIdentidad (n: Z) : seq⟨seq⟨Z⟩⟩ {
        requiere: { n > 0 }
        asegura: { |resultado| = n }
        asegura: { Para todo 0 <= i < n, |resultado[i]| = n}
        asegura: { Para todo 0 <= i < n, resultado[i][i] = 1 }
        asegura: { Para todo 0 ≤ i, j < n, si i es distinto de j entonces resultado[i][j] = 0 }
    }
Sugerencia: Pensar en una funcion auxiliar que genere la i-esima fila de la matriz identidad de tamaño n.
-}
matrizIdentidad :: Integer -> [[Integer]]
matrizIdentidad n = matrizIdentidadAux n n

matrizIdentidadAux :: Integer -> Integer -> [[Integer]]
matrizIdentidadAux _ 0 = []
matrizIdentidadAux n i = filaIdentidad n i : matrizIdentidadAux n (i - 1)

filaIdentidad :: Integer -> Integer -> [Integer]
filaIdentidad 0 _ = []
filaIdentidad n i
  | n == i = 1 : filaIdentidad (n - 1) i
  | otherwise = 0 : filaIdentidad (n - 1) i

--
-- 10. cantidadParesColumna :: Integer -> [[Integer]] -> Integer segun la siguiente especificacion: (Ver en el apunte)
-- Basicamente, contar la cantidad de pares que tiene la columna i
cantidadParesColumna :: Integer -> [[Integer]] -> Integer
cantidadParesColumna _ [] = 0
cantidadParesColumna i (x : xs)
  | esPosicionPar i x = 1 + cantidadParesColumna i xs
  | otherwise = cantidadParesColumna i xs

esPosicionPar :: Integer -> [Integer] -> Bool
esPosicionPar _ [] = False
esPosicionPar 0 (x : xs) = mod x 2 == 0
esPosicionPar i (x : xs) = esPosicionPar (i - 1) xs