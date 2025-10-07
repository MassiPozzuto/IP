{-

Especificar e implementar una funcion pitagoras :: Integer ->Integer ->Integer ->Integer que dados m, n , r ∈ N≥0, cuente cuantos pares (p, q) con 0 ≤ p ≤ m y 0 ≤ q ≤ n satisfacen que p^2 + q^2 ≤ r^2.

Por ejemplo:
    pitagoras 3 4 5 ⇝ 20
    pitagoras 3 4 2 ⇝ 6

-}

{-

    problema pitagoras (m: Z, n:Z, r:Z): Z {
        requiere: { (m >= 0) ∧ (n >= 0) ∧ (r >= 0) }
        asegura: {res = la cantidad de pares (p, q) con (0 ≤ p ≤ m) y (0 ≤ q ≤ n) satisfacen: (p^2 + q^2 ≤ r^2) }
    }

-}

pitagoras :: Integer -> Integer -> Integer -> Integer
pitagoras _ (-1) _ = 0
pitagoras m n r = pitagorasAux m n r + pitagoras m (n - 1) r

pitagorasAux :: Integer -> Integer -> Integer -> Integer
pitagorasAux (-1) _ _ = 0
pitagorasAux m n r
  | (m ^ 2) + (n ^ 2) <= (r ^ 2) = 1 + pitagorasAux (m - 1) n r
  | otherwise = pitagorasAux (m - 1) n r