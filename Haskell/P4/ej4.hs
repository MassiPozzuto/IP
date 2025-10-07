-- Especificar e implementar la funcion sumaImpares :: Integer -> Integer que dado n ∈ N sume los primeros n numeros impares.
-- Por ejemplo : sumaImpares 3 = 1 + 3 + 5 ⇝ 9

{-

    problema sumaImpares (n: Z): Z {
        requiere: { n > 0 }
        asegura: { res = la suma de los primeros n numeros impares }
    }

-}

sumaImpares :: Integer -> Integer
sumaImpares 1 = 1
sumaImpares n = (2 * n - 1) + sumaImpares (n - 1)