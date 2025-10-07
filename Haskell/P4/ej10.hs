-- Especificar, implementar y dar el tipo de las siguientes funciones (simil Ejercicio 4 Practica 2 de Algebra 1).

-- FALTA ESPECIFICAR

f1 :: Integer -> Integer
f1 0 = 1
f1 n = 2 ^ n + f1 (n - 1)

-- Todos Float ya que como q es Real (Float) para operar debo tener todos los numeros del mismo tipo
f2 :: Float -> Float -> Float
f2 0 q = 1
f2 n q = q ** n + f2 (n - 1) q

f3 :: Float -> Float -> Float
f3 n = f2 (2 * n) -- No esta q porque f3 es una aplicacion parcial de la funcion f2

f4 :: Float -> Float -> Float
f4 0 q = 1
f4 n q = (q ** n) * f2 n q