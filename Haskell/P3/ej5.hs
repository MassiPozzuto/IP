-- Implementar la funcion todosMenores :: (Integer, Integer, Integer) -> Bool

{-
    problema todosMenores (t : Z × Z × Z) : Bool {
        requiere: {True}
        asegura: {(res = true) ↔ ((f(t0) > g(t0)) ∧ (f(t1) > g(t1)) ∧ (f(t2) > g(t2)))}
    }

    problema f (n : Z) : Z {
        requiere: {True}
        asegura: {(n ≤ 7 → res = n²) ∧ (n > 7 → res = 2n − 1)}
    }

    problema g (n : Z) : Z {
        requiere: {True}
        asegura: {Si n es un numero par entonces res = n/2, en caso contrario, res = 3n + 1}
    }
-}
todosMenores :: (Integer, Integer, Integer) -> Bool
todosMenores (a, b, c) = (f a > g a) && (f b > g b) && (f c > g c)

f :: Integer -> Integer
f n
  | n > 7 = 2 * n - 1
  | otherwise = n * n

g :: Integer -> Integer
g n
  | even n = div n 2
  | otherwise = 3 * n + 1