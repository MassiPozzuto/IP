{-
a) Implementar la función parcial f :: Integer -> Integer definida por extensión de la siguiente manera:
    f(1) = 8
    f(4) = 131
    f(16) = 16

y cuya especificación es:
    problema f (n : Z) : Z {
        requiere: {n = 1 ∨ n = 4 ∨ n = 16}
        asegura: {(n = 1 → res = 8) ∧ (n = 4 → res = 131) ∧ (n = 16 → res = 16)}
    }
-}
f :: Integer -> Integer
f 1 = 8
f 4 = 131
f 16 = 16

{-
b) Análogamente, especificar e implementar la función parcial g :: Integer -> Integer
    g(8) = 16
    g(16) = 4
    g(131) = 1
-}
{-
    problema g (n : Z) : Z {
        requiere: {n = 8 ∨ n = 16 ∨ n = 131}
        asegura: {(n = 8 → res = 16) ∧ (n = 16 → res = 4) ∧ (n = 131 → res = 1)}
    }
-}
g :: Integer -> Integer
g 8 = 16
g 16 = 4
g 131 = 1

{-
c) A partir de las funciones definidas en los ıtems a) y b), implementar las funciones parciales h = f ◦ g y k = g ◦ f
-}
h :: Integer -> Integer
h x = f (g x)

k :: Integer -> Integer
k x = g (f x)