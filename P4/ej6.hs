import System.Win32 (xBUTTON1)

{-
Implementar la funcion todosDigitosIguales :: Integer ->Bool que determina si todos los digitos de un numero natural son iguales, es decir:

    problema todosDigitosIguales (n: Z) : B {
        requiere: { n > 0 }
        asegura: { resultado = true ↔ todos los digitos de n son iguales }
    }

Especifico otra funcion que me ayude a solucionar el problema principal:

    problema extraerUltimoDigito (n: Z) : B {
        requiere: { n > 0 }
        asegura: { resultado = ultimo digito de n }
    }
-}

todosDigitosIguales :: Integer -> Bool
todosDigitosIguales n
  | n < 10 = True
  | not ultDosDigIguales = False
  | ultDosDigIguales = todosDigitosIguales (div n 10)
  where
    ultDosDigIguales = extraerUltimoDigito n == extraerUltimoDigito (div n 10)

extraerUltimoDigito :: Integer -> Integer
extraerUltimoDigito n
  | n < 10 = n
  | otherwise = mod n 10