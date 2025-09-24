import Distribution.Simple (earlierVersion)

-- a) Especificar e implementar una funcion eAprox :: Integer ->Float que aproxime el valor del numero e a partir de la sumatoria que va desde i=0 hasta i=n de 1/i!

{-
    problema eAprox (x: Z): R{
        requiere: { x >= 0 }
        asegura: { res = la sumatoria que va desde i=0 hasta i=n de (1/i!) }
    }
-}

eAprox :: Integer -> Float
eAprox 0 = 1
eAprox x = (1 / fromIntegral (factorial x)) + eAprox (x - 1)

factorial :: Integer -> Integer
factorial 0 = 1
factorial n = n * factorial (n - 1)

-- b) Definir la constante e :: Float como la aproximacion de e a partir de los primeros 10 terminos de la serie anterior. ¡Atencion! A veces ciertas funciones esperan un Float y nosotros tenemos un Int. Para estos casos podemos utilizar la funcion fromIntegral :: Int -> Float definida en el Preludio de Haskell.

e :: Float
e = eAprox 10