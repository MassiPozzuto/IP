{-
Especificar e implementar la funcion tomaValorMax :: Integer ->Integer ->Integer que dado un numero entero n1 ≥ 1 y un n2 ≥ n1 devuelve algun m entre n1 y n2 tal que sumaDivisores(m) = max{sumaDivisores(i) | n1 ≤ i ≤ n2}
-}

{-

problema tomaValorMax (n1: Z, n2: Z):Z {
    requiere: { n1 > 0 }
    requiere: { n2 >= n1}
    asegura: { (n2 >= res) ∧ (res >= n1) }
    asegura: { res = el numero el cual tenga la mayor suma de sus divisores }
}

-}

tomaValorMax :: Integer -> Integer -> Integer
tomaValorMax n1 n2
  | n1 == n2 = n1
  | sumaDeDivisores n2 >= sumaDeDivisores n1 = tomaValorMax (n1 + 1) n2
  | otherwise = tomaValorMax n1 (n2 - 1)

sumaDeDivisores :: Integer -> Integer
sumaDeDivisores m = sumaDeDivisoresDesde m 1

sumaDeDivisoresDesde :: Integer -> Integer -> Integer
sumaDeDivisoresDesde m i
  | i == m = i
  | mod m i == 0 = i + sumaDeDivisoresDesde m (i + 1)
  | otherwise = sumaDeDivisoresDesde m (i + 1)