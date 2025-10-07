-- Especificar e implementar la funcion esDivisible :: Integer -> Integer ->Bool que dados dos numeros naturales determinar si el primero es divisible por el segundo. No esta permitido utilizar las funciones mod ni div.

{-
    problema esDivisible (x: Z, y:Z): Bool {
        requiere: { y > 0}
        asegura: { res = x es divisible por y }
    }

Utilizo otra funcion para poder resolver el problema
    problema esMultiplo (x: Z, y:Z, i:Z): Bool {
        requiere: { y /= 0}
        requiere: { i = x }
        asegura: { res = True <=> x es un multiplo de y }
    }
-}

esDivisible :: Integer -> Integer -> Bool
esDivisible x 0 = False
esDivisible x y = esMultiplo x y x

esMultiplo :: Integer -> Integer -> Integer -> Bool
esMultiplo x y 0 = False
esMultiplo x y i
  | x == i * y = True
  | otherwise = esMultiplo x y (i - 1)

-- Forma de Mati (un poco modificada)

esDivisible' :: Integer -> Integer -> Bool
esDivisible' _ 0 = False
esDivisible' 0 _ = True
esDivisible' x y
  | x < 0 = False
  | otherwise = esDivisible' (x - abs y) y

-- El abs no hace falta ya que la especificacion pide numero naturales, pero no me importa
