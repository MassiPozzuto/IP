{-
Implementar una funcion parteEntera :: Float -> Integer segun la siguiente especificacion:

    problema parteEntera (x: R) : Z {
        requiere: { x ≥ 0 }
        asegura: { resultado ≤ x < resultado + 1 }
    }
-}

parteEntera :: Float -> Integer
parteEntera x
  | x < 1 = 0
  | otherwise = 1 + parteEntera (x - 1)