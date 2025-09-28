{-

Implementar la funcion esFibonacci :: Integer ->Bool segun la siguiente especificacion:

    problema esFibonacci (n: Z) : B {
        requiere: { n ≥ 0 }
        asegura: { resultado = true ↔ n es algun valor de la secuencia de Fibonacci definida en el ejercicio 1}
    }

-}

esFibonacci :: Integer -> Bool
esFibonacci n = estaEnFib n 0

estaEnFib :: Integer -> Integer -> Bool
estaEnFib n i
  | fibonacci i > n = False
  | fibonacci i == n = True
  | otherwise = estaEnFib n (i + 1)

fibonacci :: Integer -> Integer
fibonacci 0 = 0
fibonacci 1 = 1
fibonacci n = fibonacci (n - 1) + fibonacci (n - 2)
