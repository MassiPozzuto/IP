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