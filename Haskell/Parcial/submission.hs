{--
Yo: Massimo Luca Pozzuto
Certifico que el siguiente archivo fue elaborado únicamente por mí, sin ayuda de otras personas o herramientas.
--}

module SolucionT2 where

-- Ejercicio 1 
-- ^
esCuadradoDePrimo :: Integer -> Bool
esCuadradoDePrimo numero = esCuadradoDePrimoAux numero 1

esCuadradoDePrimoAux :: Integer -> Integer -> Bool
esCuadradoDePrimoAux n i 
    | n < (proximoPrimo i)^2 = False
    | n == (proximoPrimo i)^2 = True
    | otherwise = esCuadradoDePrimoAux n (i+1) 

proximoPrimo :: Integer -> Integer
proximoPrimo 1 = 2
proximoPrimo n 
    | esPrimo (n+1) = n+1
    | otherwise = proximoPrimo (n+1)

esPrimo :: Integer -> Bool
esPrimo n = esPrimoAux n 2

esPrimoAux :: Integer -> Integer -> Bool
esPrimoAux n i 
    | n < 2 = False
    | n == i = True
    | mod n i == 0 = False
    | otherwise = esPrimoAux n (i+1)


-- Ejercicio 2
posParesFormanEscalera :: [Integer] -> Bool
posParesFormanEscalera [] = True
posParesFormanEscalera lista = posParesFormanEscaleraAux lista 0

posParesFormanEscaleraAux :: [Integer] -> Integer -> Bool
posParesFormanEscaleraAux [x] _ = True
posParesFormanEscaleraAux [x, y] _ = True
posParesFormanEscaleraAux (x:xs) i
    | not posEsPar = posParesFormanEscaleraAux xs (i+1)
    | (x+1 == iesimoElemento xs 1 ) = posParesFormanEscaleraAux xs (i+1)
    | otherwise = False
    where
        posEsPar = mod i 2 == 0

iesimoElemento :: [t] -> Integer -> t
iesimoElemento (x:xs) 0 = x 
iesimoElemento (x:xs) i = iesimoElemento xs (i-1)


-- Ejercicio 3
listadoDePeliculas :: [(Integer, [String])] -> [(String, Integer)]
listadoDePeliculas [] = []
listadoDePeliculas (primerAnio: otrosAnios) = eliminarRepetidos (listadoDePeliculasDeUnAnio primerAnio ++ listadoDePeliculas otrosAnios)

-- Asumo que las tuplas deben ser exactamente iguales para estar repetidas, por ejemplo: ("Dune", 2021) /= ("Dune", 2019)
eliminarRepetidos :: [(String, Integer)] -> [(String, Integer)]
eliminarRepetidos [] = []
eliminarRepetidos ((peli, anio): otrasPelis)
    | laPeliActualEstaEnLasOtras = eliminarRepetidos otrasPelis
    | otherwise = (peli, anio): eliminarRepetidos otrasPelis
    where
        laPeliActualEstaEnLasOtras = pertenece (peli, anio) otrasPelis

pertenece :: (Eq t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece el (x:xs)
    | el == x = True
    | otherwise = pertenece el xs

quitarPeli :: String -> [(String, Integer)] -> [(String, Integer)]
quitarPeli _ [] = []
quitarPeli peliDeseada ((peli, anio): otrasPelis)
    | peliDeseada == peli = quitarPeli peliDeseada otrasPelis
    | otherwise = (peli, anio) : quitarPeli peliDeseada otrasPelis

listadoDePeliculasDeUnAnio :: (Integer, [String]) -> [(String, Integer)]
listadoDePeliculasDeUnAnio (_, []) = []
listadoDePeliculasDeUnAnio (anio, (peli: otrasPelis)) = (peli, anio) : listadoDePeliculasDeUnAnio (anio, otrasPelis)


-- Ejercicio 4
eliminarFilaQueMasSuma :: [[Integer]] -> [[Integer]]
eliminarFilaQueMasSuma [] = []
eliminarFilaQueMasSuma [fila] = []
eliminarFilaQueMasSuma (fila : otrasFilas) 
    | sumatoria fila >= maximaSumatoriaFilas otrasFilas = otrasFilas
    | otherwise = fila : eliminarFilaQueMasSuma otrasFilas

maximaSumatoriaFilas :: [[Integer]] -> Integer
maximaSumatoriaFilas [fila] = sumatoria fila
maximaSumatoriaFilas (fila : otrasFilas) 
    | sumatoria fila >= maximaSumatoriaFilas otrasFilas = sumatoria fila
    | otherwise = maximaSumatoriaFilas otrasFilas

sumatoria :: (Num t) => [t] -> t 
sumatoria [] = 0
sumatoria (x:xs) = x + sumatoria xs

{--
Siendo la última modificación con la solución final:
01/10/2025 11:22
--}
