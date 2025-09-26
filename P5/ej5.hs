-- Definir las siguientes funciones sobre listas:

-- 1. sumaAcumulada :: (Num t) => [t] -> [t] segun la siguiente especificacion: (Ver en el apunte)
-- Por ejemplo sumaAcumulada [1, 2, 3, 4, 5] es [1, 3, 6, 10, 15].

sumaAcumulada :: (Num t) => [t] -> [t]
sumaAcumulada [] = []
sumaAcumulada [x] = [x]
sumaAcumulada (x : y : xs) = x : sumaAcumulada ((x + y) : xs)

-- 2. descomponerEnPrimos :: [Integer] -> [[Integer]] segun la siguiente especificacion:

{-
    problema descomponerEnPrimos (s: seq⟨Z⟩) : seq⟨seq⟨Z⟩⟩ {
        requiere: { Todos los elementos de s son mayores a 2 }
        asegura: { |resultado| = |s| }
        asegura: {todos los valores en las listas de resultado son numeros primos}
        asegura: {multiplicar todos los elementos en la lista en la posicion i de resultado es igual al valor en la posicion i de s}
    }
Por ejemplo descomponerEnPrimos [2, 10, 6] es [[2], [2, 5], [2, 3]].
-}

descomponerEnPrimos :: [Integer] -> [[Integer]]
descomponerEnPrimos [] = []
descomponerEnPrimos (x : xs) = factorizarNum x 1 : descomponerEnPrimos xs

factorizarNum :: Integer -> Integer -> [Integer]
factorizarNum 1 1 = []
factorizarNum n i
  | i > n = []
  | mod n (nEsimoPrimo i) == 0 = nEsimoPrimo i : factorizarNum (div n (nEsimoPrimo i)) 1
  | otherwise = factorizarNum n (i + 1)

-- En la segunda guara: Si n es divisible por el nEsimoPrimo, entonces lo agrego a la lista y vuelvo a realizar la funcion para la division entre el numero y el primo
-- Ej: factorizarNum 4 1  ==>  2 : factorizarNum 2 1  ==>  2 : 2 : factorizarNum 1 1  ==>  2 : 2 : []  ==>  [2,2]

-- Ej: factorizarNum 10 1  ==>  2 : factorizarNum 5 1  ==>  2 : factorizarNum 5 2  ==>  2 : factorizarNum 5 3  ==>  2 : 5 : factorizarNum 1 1 ==>  2 : 5 : []  ==>  [2,5]

------ Todas funciones del ejercicio 16 de la practica 4 ------
nEsimoPrimo :: Integer -> Integer
nEsimoPrimo 1 = 2
nEsimoPrimo n = proximoPrimo (nEsimoPrimo (n - 1))

proximoPrimo :: Integer -> Integer
proximoPrimo 1 = 2
proximoPrimo n
  | esPrimo (n + 1) = n + 1
  | otherwise = proximoPrimo (n + 1)

esPrimo :: Integer -> Bool
esPrimo n = menorDivisor n == n

menorDivisor :: Integer -> Integer
menorDivisor n = divisorMayorMasCercano n 2

divisorMayorMasCercano :: Integer -> Integer -> Integer
divisorMayorMasCercano 1 i = 1
divisorMayorMasCercano n i
  | (i > 1) && (mod n i == 0) = i
  | otherwise = divisorMayorMasCercano n (i + 1)

---------------------------------------------------------------