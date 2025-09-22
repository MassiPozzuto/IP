-- Especificar e implementar la funcion sumaDigitos :: Integer ->Integer que calcula la suma de digitos de un numero natural. Para esta funcion pueden utilizar div y mod.

{-
    problema sumaDigitos (n: Z): Z {
        requiere: { n > 0 }
        asegura: { res = la suma de los digitos de n }
    }
-}

sumaDigitos :: Integer -> Integer
sumaDigitos n
  | n < 10 = n
  | otherwise = mod n 10 + sumaDigitos (div n 10)