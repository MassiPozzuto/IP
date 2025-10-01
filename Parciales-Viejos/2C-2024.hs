{--
EJERCICIO 1 (2 puntos)

    problema mediaMovilN (lista: seq⟨Z⟩, n: Z) : Float {
        requiere: {|lista| > 0}
        requiere: {n > 0 ∧ n ≤ |lista|}
        asegura: {res es el promedio de los últimos n elementos de lista}
    }
--}

mediaMovilN :: [Integer] -> Integer -> Float
mediaMovilN lst n = promedio ultimosNElementosDeLst
  where
    ultimosNElementosDeLst = quitarPrimerosIElementos lst (longitud lst - n)

quitarPrimerosIElementos :: [t] -> Integer -> [t]
quitarPrimerosIElementos lst 0 = lst
quitarPrimerosIElementos (x : xs) i = quitarPrimerosIElementos xs (i - 1)

promedio :: [Integer] -> Float
promedio lst = fromIntegral (sumatoria lst) / fromIntegral (longitud lst)

sumatoria :: (Num t) => [t] -> t
sumatoria [] = 0
sumatoria (x : xs) = x + sumatoria xs

longitud :: [t] -> Integer
longitud [] = 0
longitud (el : otrosEl) = 1 + longitud otrosEl

{--
EJERCICIO 2 (2 puntos)

    problema esAtractivo (n: Z) : Bool {
        requiere: {n > 0}
        asegura: {res = true <=> la cantidad de factores primos de n (distintos o no) es también un número primo.}
    }
Aclaración: los factores primos de 30 son [5,3,2]. Los factores primos de 9 son [3,3].

--}
esAtractivo :: Integer -> Bool
esAtractivo n = esPrimo (longitud (factoresPrimos n))

factoresPrimos :: Integer -> [Integer]
factoresPrimos 0 = []
factoresPrimos n = factoresPrimosAux n 1

factoresPrimosAux :: Integer -> Integer -> [Integer]
factoresPrimosAux 1 _ = []
factoresPrimosAux n i
  | i * i > abs n = [n] -- El abs esta para que tambien sirva para numeros negativos, pero no lo pide la especificacion, por eso tampoco hago un funcion absoluto
  | mod n (proximoPrimo i) == 0 = proximoPrimo i : factoresPrimosAux (div n (proximoPrimo i)) 1
  | otherwise = factoresPrimosAux n (i + 1)

proximoPrimo :: Integer -> Integer
proximoPrimo 1 = 2
proximoPrimo n
  | esPrimo (n + 1) = n + 1
  | otherwise = proximoPrimo (n + 1)

esPrimo :: Integer -> Bool
esPrimo n = esPrimoAux n 2

esPrimoAux :: Integer -> Integer -> Bool
esPrimoAux n i
  | n < 2 = False
  | n == i = True
  | n /= i && mod n i == 0 = False
  | otherwise = esPrimoAux n (i + 1)

{--
EJERCICIO 3 (2 puntos)

    problema palabraOrdenada (palabra: seq⟨Char⟩) : Bool {
        requiere: {True}
        asegura: {res = true <=> cada uno de los elementos no blancos de palabra es mayor o igual al anterior caracter no blanco, si existe alguno.}
    }
Aclaración: 'a' < 'b' es True.

--}
palabraOrdenada :: String -> Bool
palabraOrdenada [] = True
palabraOrdenada [x] = True
palabraOrdenada (' ' : xs) = palabraOrdenada xs
palabraOrdenada (x : ' ' : xs) = palabraOrdenada (x : xs)
palabraOrdenada (x : y : xs)
  | x <= y = palabraOrdenada (y : xs)
  | otherwise = False

{--
EJERCICIO 4 (3 puntos)

    problema similAnagrama (palabra1: seq⟨Char⟩, palabra2: seq⟨Char⟩) : Bool⟩{
        requiere: {True}
        asegura: {res = true <=> (para todo caracter no blanco, la cantidad de apariciones de ese caracter en palabra1 es igual a la cantidad de apariciones en palabra2, y además existe al menos un caracter en palabra1 que tiene una posición distinta en palabra2)}
    }

--}
similAnagrama :: String -> String -> Bool
similAnagrama (x : xs) palabra2 = similAnagramaAux (x : xs) palabra2 1

similAnagramaAux :: (Eq t, Num t) => [Char] -> String -> t -> Bool
similAnagramaAux [] _ _ = True
similAnagramaAux (x : xs) palabra2 i
  | i == 1 && estaIncluidaExactamenteIgual (x : xs) palabra2 = False
  | cantApariciones x (x : xs) /= cantApariciones x palabra2 = False
  | otherwise = similAnagramaAux xs palabra2 (i + 1)

estaIncluidaExactamenteIgual :: String -> String -> Bool
estaIncluidaExactamenteIgual _ [] = False
estaIncluidaExactamenteIgual (x : xs) (y : ys)
  | x == y = primerPalabraCoincide (x : xs) (y : ys)
  | otherwise = estaIncluidaExactamenteIgual (x : xs) ys

primerPalabraCoincide :: String -> String -> Bool
primerPalabraCoincide [] _ = True
primerPalabraCoincide _ [] = False
primerPalabraCoincide (x : xs) (y : ys)
  | x == y = primerPalabraCoincide xs ys
  | otherwise = False

cantApariciones :: (Eq t) => t -> [t] -> Integer
cantApariciones _ [] = 0
cantApariciones el (x : xs)
  | el == x = 1 + cantApariciones el xs
  | otherwise = cantApariciones el xs

{--
EJERCICIO 5 (1 punto)

¿Cuándo se dice que una especificación está sub-especificada?:
    [x] Cuando se da una precondición más restrictiva de lo realmente necesario, o bien una postcondición más débil de la que se necesita.
    [ ] Cuando se da una precondición más débil de lo realmente necesario, o bien una postcondición más restrictiva de la que se necesita.
    [ ] Cuando no hay precondiciones (o la precondición es True).

--}
