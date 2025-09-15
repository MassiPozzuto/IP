-- A partir de las siguientes implementaciones en Haskell, describir en lenguaje natural que hacen y especificarlas.

-- a)
f1 :: Float -> Float
f1 n
  | n == 0 = 1
  | otherwise = 0

{-
    problema f1(n: R): R {
        requiere: { True }
        asegura: { (n = 0 → res = 1) ∧ (n /= 0 → res = 0)}
    }
-}-- b)
f2 :: Float -> Float
f2 n
  | n == 1 = 15
  | n == -1 = -15

{-
    problema f2(n: R): R {
        requiere: { n = 1 ∨  n = -1}
        asegura: { (n = 1 → res = 15) ∧ (n = -1 → res = -15)}
    }
-}

-- c)
f3 :: Float -> Float
f3 n
  | n <= 9 = 7
  | n >= 3 = 5

{-
    problema f2(n: R): R {
        requiere: { True }
        asegura: { (n <= 9 → res = 7) ∨ (n >= 3 → res = 5)}
    }
-}

-- d)
f4 :: Float -> Float -> Float
f4 x y = (x + y) / 2

{-
    problema f4(x: R, y: R): R {
        requiere: { True }
        asegura: { res = La mitad de la suma entre x e y}
    }
-}

-- e)
f5 :: (Float, Float) -> Float
f5 (x, y) = (x + y) / 2

{-
    problema f5(t: R × R): R {
        requiere: { True }
        asegura: { res = La mitad de la suma entre los elementos de t}
    }
-}

-- f)
f6 :: Float -> Int -> Bool
f6 a b = truncate a == b

{-
    problema f6(x: R, z: Z): Bool {
        requiere: { True }
        asegura: { (res = true) ↔  ((z) es el valor entero mas cercano a (x) entre 0 y (x)) }
    }
-}
