-- Especificar e implementar una funcion sumaPotencias :: Integer ->Integer ->Integer ->Integer
-- Que dados tres naturales q, n, m sume todas las potencias de la forma q^(a+b) con 1 ≤ a ≤ n y 1 ≤ b ≤ m

{-

problema sumaPotencias (q: Z, n: Z, m: Z): Z {
    requiere: { (q > 0) ∧ (n > 0) ∧ (m > 0)  }
    asegura : { res =  la suma todas las potencias de la forma q^(a+b) con 1 ≤ a ≤ n y 1 ≤ b ≤ m }
}

problema sumaInternaPotencias (q: Z, n: Z, m: Z): Z {
    requiere: { (q > 0) ∧ (n > 0) ∧ (m > 0)  }
    asegura : { res =  la suma todas las potencias de la forma q^(n+b) con 1 ≤ b ≤ m }
}

-}

sumaPotencias :: Integer -> Integer -> Integer -> Integer
sumaPotencias _ 0 _ = 0
sumaPotencias q n m = sumaInternaPotencias q n m + sumaPotencias q (n - 1) m

sumaInternaPotencias :: Integer -> Integer -> Integer -> Integer
sumaInternaPotencias _ _ 0 = 0
sumaInternaPotencias q n m = q ^ (n + m) + sumaInternaPotencias q n (m - 1)

-- Que pasa con los repetidos? Por ejemplo: 1+3 = 3+1; 4+5 = 5+4