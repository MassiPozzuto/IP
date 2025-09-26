-- Definir las siguientes funciones sobre listas de enteros:

-- 1. sumatoria :: [Integer] -> Integer segun la siguiente especificacion: (Ver en el apunte)
sumatoria :: [Integer] -> Integer
sumatoria [] = 0
sumatoria (x : xs) = x + sumatoria xs

-- 2. productoria :: [Integer] -> Integer segun la siguiente especificacion: (Ver en el apunte)
productoria :: [Integer] -> Integer
productoria [] = 1
productoria (x : xs) = x * productoria xs

-- 3. maximo :: [Integer] -> Integer segun la siguiente especificacion:
{-
    problema maximo (s: seq⟨Z⟩) : Z {
        requiere: { |s| > 0 }
        asegura: { resultado ∈ s ∧ todo elemento de s es menor o igual a resultado }
    }
-}

maximo :: [Integer] -> Integer
maximo [x] = x
maximo (x : y : xs)
  | x >= y = maximo (x : xs)
  | otherwise = maximo (y : xs)

-- 4. sumarN :: Integer -> [Integer] -> [Integer] segun la siguiente especificacion:
{-
    problema sumarN (n: Z, s: seq⟨Z⟩) : seq⟨Z⟩ {
        requiere: { True }
        asegura: {|resultado| = |s| ∧ cada posicion de resultado contiene el valor que hay en esa posicion en s sumado n }
    }
-}
sumarN :: Integer -> [Integer] -> [Integer]
sumarN _ [] = []
sumarN n (x : xs) = (x + n) : sumarN n xs

-- 5. sumarElPrimero :: [Integer] -> [Integer] segun la siguiente especificacion:
{-
    problema sumarElPrimero (s: seq⟨Z⟩) : seq⟨Z⟩ {
        requiere: { |s| > 0 }
        asegura: {resultado = sumarN(s[0], s) }
    }

Por ejemplo sumarElPrimero [1,2,3] da [2,3,4]
-}
sumarElPrimero :: [Integer] -> [Integer]
sumarElPrimero (x : xs) = sumarN x (x : xs)

-- 6. sumarElUltimo :: [Integer] -> [Integer] segun la siguiente especificacion:
{-
    problema sumarElUltimo (s: seq⟨Z⟩) : seq⟨Z⟩ {
        requiere: { |s| > 0 }
        asegura: {resultado = sumarN(s[|s| − 1], s) }
    }
Por ejemplo sumarElUltimo [1,2,3] da [4,5,6]
-}
sumarElUltimo :: [Integer] -> [Integer]
sumarElUltimo lista = sumarN (ultimoElemento lista) lista

ultimoElemento :: [t] -> t
ultimoElemento [x] = x
ultimoElemento (x : xs) = ultimoElemento xs

-- 7. pares :: [Integer] -> [Integer] segun la siguiente especificacion:
{-
    problema pares (s: seq⟨Z⟩) : seq⟨Z⟩ {
        requiere: { True }
        asegura: {resultado solo tiene los elementos pares de s en el orden dado, respetando las repeticiones}
    }
Por ejemplo pares [1,2,3,5,8,2] da [2,8,2]
-}
pares :: [Integer] -> [Integer]
pares [] = []
pares (x : xs)
  | mod x 2 == 0 = x : pares xs
  | otherwise = pares xs

-- 8. multiplosDeN :: Integer -> [Integer] -> [Integer] que dado un numero n y una lista xs, devuelve una lista con los elementos de xs multiplos de n.
multiplosDeN :: Integer -> [Integer] -> [Integer]
multiplosDeN _ [] = []
multiplosDeN n (x : xs)
  | mod x n == 0 = x : multiplosDeN n xs
  | otherwise = multiplosDeN n xs

-- 9. ordenar :: [Integer] -> [Integer] que ordena los elementos de la lista en forma creciente. Sugerencia: Pensar como pueden usar la funcion maximo para que ayude a generar la lista ordenada necesaria.

ordenar :: [Integer] -> [Integer]
ordenar [] = []
ordenar lst = ordenar listaSinSuMax ++ [maximo lst]
  where
    listaSinSuMax = quitar (maximo lst) lst

quitar :: (Eq t) => t -> [t] -> [t]
quitar e [] = []
quitar e (x : xs)
  | e == x = xs
  | otherwise = x : quitar e xs
