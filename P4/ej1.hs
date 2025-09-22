{-
Implementar la funcion fibonacci :: Integer -> Integer que devuelve el i-esimo numero de Fibonacci.

    problema fibonacci (n: Z) : Z {
        requiere: { n ≥ 0 }
        asegura: { resultado = fib(n) }
    }
-}
fibonacci :: Integer -> Integer
fibonacci 0 = 0
fibonacci 1 = 1
fibonacci n = fibonacci (n - 1) + fibonacci (n - 2)
