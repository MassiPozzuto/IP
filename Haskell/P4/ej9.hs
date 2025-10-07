-- Especificar e implementar una funcion esCapicua :: Integer -> Bool que dado n ∈ N≥0 determina si n es un numero capicua

{-

    problema esCapicua (n: Z): Bool {
        requiere: {n >= 0}
        asegura: { resultado = true ↔ n es un numero capicua (es el mismo numero escrito de izquierda a derecha que de derecha a izquierda)}
    }

    problema invertirNum (n: Z): Z {
        requiere: {n >= 0}
        asegura: { resultado = el numero n escrito de derecha a izquierda }
    }

    problema cantDigitos (n: Z): Z {
        requiere: {n >= 0}
        asegura: { resultado = la cantidad de digitos que tiene n}
    }
-}

esCapicua :: Integer -> Bool
esCapicua n = n == invertirNum n

invertirNum :: Integer -> Integer
invertirNum n
  | n < 10 = n
  | otherwise = (mod n 10 * (10 ^ (cantDigitos n - 1))) + invertirNum (div n 10)

cantDigitos :: Integer -> Integer
cantDigitos n
  | n < 10 = 1
  | otherwise = 1 + cantDigitos (div n 10)
