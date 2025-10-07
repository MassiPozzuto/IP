{-
Implementar la funcion esSumaInicialDePrimos :: Integer ->Bool segun la siguiente especificacion:

problema esSumaInicialDePrimos (n: Z) : B {
    requiere: { n ≥ 0 }
    asegura: { resultado = true ↔ n es igual a la suma de los m primeros numeros primos, para algun m.}
}

-}

esSumaInicialDePrimos :: Integer -> Bool
esSumaInicialDePrimos n = esSumaDeIPrimos n 1

esSumaDeIPrimos :: Integer -> Integer -> Bool
esSumaDeIPrimos n i
  | n < sumaDeIPrimos i = False
  | n == sumaDeIPrimos i = True
  | otherwise = esSumaDeIPrimos n (i + 1)

sumaDeIPrimos :: Integer -> Integer
sumaDeIPrimos 1 = 2
sumaDeIPrimos n = nEsimoPrimo n + sumaDeIPrimos (n - 1)

--

menorDivisor :: Integer -> Integer
menorDivisor n = divisorMayorMasCercano n 2

divisorMayorMasCercano :: Integer -> Integer -> Integer
divisorMayorMasCercano 1 i = 1
divisorMayorMasCercano n i
  | (i > 1) && (mod n i == 0) = i
  | otherwise = divisorMayorMasCercano n (i + 1)

esPrimo :: Integer -> Bool
esPrimo n = menorDivisor n == n

nEsimoPrimo :: Integer -> Integer
nEsimoPrimo 1 = 2
nEsimoPrimo n = proximoPrimo (nEsimoPrimo (n - 1))

proximoPrimo :: Integer -> Integer
proximoPrimo 1 = 2
proximoPrimo n
  | esPrimo (n + 1) = n + 1
  | otherwise = proximoPrimo (n + 1)