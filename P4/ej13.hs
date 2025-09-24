-- Especificar e implementar la siguiente funcion: (ver del apunte)

{-

La especificacion incluye la escritura de las sumatorias, lo cual es incomodo de hacer en texto

-}

sumatoriaDoble :: Integer -> Integer -> Integer
sumatoriaDoble 1 m = m
sumatoriaDoble n m = sumatoriaInterna n m + sumatoriaDoble (n - 1) m

sumatoriaInterna :: Integer -> Integer -> Integer
sumatoriaInterna n 1 = n
sumatoriaInterna n j = n ^ j + sumatoriaInterna n (j - 1)