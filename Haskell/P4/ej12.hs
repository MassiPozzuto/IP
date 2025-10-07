{-
Para n ∈ N se define recursivamente a[1] = 2, a[n] = 2 + 1 / (a[n-1])

Utilizando esta sucesion, especificar e implementar una funcion raizDe2Aprox :: Integer ->Float que dado n ∈ N devuelva la aproximacion de √2 definida por √2 ≈ a[n] − 1.

Por ejemplo:
    raizDe2Aprox 1 ⇝ 1
    raizDe2Aprox 2 ⇝ 1,5
    raizDe2Aprox 3 ⇝ 1,4
-}

{-
    problema raizDe2Aprox (n: Z): R {
        requiere: { n > 0 }
        asegura: { res = fRecursiva (n) − 1}
    }

    problema fRecursiva (n: Z): R {
        requiere: { n > 0 }
        asegura: { res = 2 + (1 / fRecursiva (n - 1)) }
    }
-}

raizDe2Aprox :: Integer -> Float
raizDe2Aprox n = fRecursiva n - 1

fRecursiva :: Integer -> Float
fRecursiva 1 = 2
fRecursiva n = 2 + (1 / fRecursiva (n - 1))