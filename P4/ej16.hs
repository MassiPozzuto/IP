import Distribution.Simple.Setup (trueArg)
import GHC.Base (TrName (TrNameD))

-- Recordemos que un entero p > 1 es primo si y solo si no existe un entero k tal que 1 < k < p y k divida a p

-- a) Implementar menorDivisor :: Integer ->Integer que calcule el menor divisor (mayor que 1) de un natural n pasado como parametro.

menorDivisor :: Integer -> Integer
menorDivisor n = divisorMayorMasCercano n 2

divisorMayorMasCercano :: Integer -> Integer -> Integer
divisorMayorMasCercano 1 i = 1
divisorMayorMasCercano n i
  | (i > 1) && (mod n i == 0) = i
  | otherwise = divisorMayorMasCercano n (i + 1)

-- b) Implementar la funcion esPrimo :: Integer ->Bool que indica si un numero natural pasado como parametro es primo
esPrimo :: Integer -> Bool
esPrimo n = menorDivisor n == n

-- c) Implementar la funcion sonCoprimos :: Integer ->Integer ->Bool que dados dos numeros naturales indica si no tienen algun divisor en comun mayor estricto que 1.
sonCoprimos :: Integer -> Integer -> Bool
sonCoprimos n m = algoDeEuclides n m == 1

algoDeEuclides :: Integer -> Integer -> Integer
algoDeEuclides n 0 = abs n
algoDeEuclides n m = algoDeEuclides m (mod n m)

-- d) Implementar la funcion nEsimoPrimo :: Integer ->Integer que devuelve el n-esimo primo (n ≥ 1). Recordar que el primer primo es el 2, el segundo es el 3, el tercero es el 5, etc.
nEsimoPrimo :: Integer -> Integer
nEsimoPrimo 1 = 2
nEsimoPrimo n = proximoPrimo (nEsimoPrimo (n - 1))

proximoPrimo :: Integer -> Integer
proximoPrimo 1 = 2
proximoPrimo n
  | esPrimo (n + 1) = n + 1
  | otherwise = proximoPrimo (n + 1)
