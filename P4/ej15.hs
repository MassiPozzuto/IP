-- Implementar una funcion sumaRacionales :: Integer ->Integer ->Float que dados dos naturales n, m sume todos los numeros racionales de la forma p/q con 1 ≤ p ≤ n y 1 ≤ q ≤ m
-- Ver especificacion en el apunte

sumaRacionales :: Integer -> Integer -> Float
sumaRacionales 0 _ = 0
sumaRacionales n m = sumaInternaRacionales n m + sumaRacionales (n - 1) m

sumaInternaRacionales :: Integer -> Integer -> Float
sumaInternaRacionales _ 0 = 0
sumaInternaRacionales n m = (fromInteger n / fromInteger m) + sumaInternaRacionales n (m - 1)