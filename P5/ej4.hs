-- 1) Definir las siguientes funciones sobre listas de caracteres, interpretando una palabra como una secuencia de caracteres sin blancos:

-- a) sacarBlancosRepetidos :: [Char] -> [Char], que reemplaza cada subsecuencia de blancos contiguos de la primera lista por un solo blanco en la lista resultado

sacarBlancosRepetidos :: [Char] -> [Char]
sacarBlancosRepetidos [] = []
sacarBlancosRepetidos (' ' : ' ' : xs) = sacarBlancosRepetidos (' ' : xs)
sacarBlancosRepetidos (x : xs) = x : sacarBlancosRepetidos xs

-- b) contarPalabras :: [Char] -> Integer, que dada una lista de caracteres devuelve la cantidad de palabras que tiene.
contarPalabras :: [Char] -> Integer
contarPalabras [] = 0
contarPalabras (' ' : xs) = contarPalabras xs
contarPalabras [x] = 1
contarPalabras (x : ' ' : xs) = 1 + contarPalabras xs
contarPalabras (x : xs) = contarPalabras xs

-- c) palabras :: [Char] -> [[Char]], que dada una lista arma una nueva lista con las palabras de la lista original.

palabras :: [Char] -> [[Char]]
palabras [] = []
palabras (' ' : xs) = palabras xs
palabras str = primerPalabra str : palabras (quitarHasta str (length (primerPalabra str) + 1))

primerPalabra :: [Char] -> [Char]
primerPalabra [] = []
primerPalabra (' ' : xs) = primerPalabra xs
primerPalabra (x : ' ' : xs) = [x]
primerPalabra (x : xs) = x : primerPalabra xs

quitarHasta :: [Char] -> Int -> [Char]
quitarHasta [] _ = []
quitarHasta str 0 = str
quitarHasta (fstLetter : otherLetters) i = quitarHasta otherLetters (i - 1)

-- d) palabraMasLarga :: [Char] -> [Char], que dada una lista de caracteres devuelve su palabra mas larga.
palabraMasLarga :: [Char] -> [Char]
palabraMasLarga xs = elementoMasLargo (palabras xs)

elementoMasLargo :: (Eq t) => [[t]] -> [t]
elementoMasLargo [] = []
elementoMasLargo [x] = x
elementoMasLargo (x:y:xs) 
    | length x >= length y = elementoMasLargo (x:xs) 
    | otherwise = elementoMasLargo (y:xs) 

-- e) aplanar :: [[Char]] -> [Char], que a partir de una lista de palabras arma una lista de caracteres concatenandolas.
aplanar :: [[Char]] -> [Char]
aplanar [] = []
aplanar [x] = x
aplanar (x:xs) = x ++ aplanar xs

-- f ) aplanarConBlancos :: [[Char]] -> [Char], que a partir de una lista de palabras, arma una lista de caracteres concatenandolas e insertando un blanco entre cada palabra.
aplanarConBlancos :: [[Char]] -> [Char]
aplanarConBlancos [] = []
aplanarConBlancos [x] = x
aplanarConBlancos (x:xs) = x ++ [' '] ++ aplanarConBlancos xs

-- g) aplanarConNBlancos :: [[Char]] -> Integer -> [Char], que a partir de una lista de palabras y un entero n, arma una lista de caracteres concatenandolas e insertando n blancos entre cada palabra (n debe ser no negativo)
aplanarConNBlancos :: [[Char]] -> Integer -> [Char]
aplanarConNBlancos [] _ = []
aplanarConNBlancos [x] _ = x
aplanarConNBlancos (x:xs) n = x ++ nBlancos n ++ aplanarConNBlancos xs n

nBlancos :: Integer -> [Char]
nBlancos 0 = []
nBlancos n = ' ' : nBlancos (abs n - 1)

-- 2) ¿Como cambian los ejercicios si agregamos el renombre de tipos: type Texto = [Char]?
-- Imaginatelo compa, es lo mismo usar Texto a usar String, saludos.