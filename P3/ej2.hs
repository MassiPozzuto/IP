-- Especificar e implementar las siguientes funciones, incluyendo su signatura.

-- a) absoluto: calcula el valor absoluto de un numero entero.
{-
    problema absoluto (n: Z): Z {
        requiere: { True }
        asegura: { (n >= 0 → res = n) ∧ (n < 0 → res = -n)  }
    }
-}
absoluto :: Integer -> Integer
absoluto n
  | n >= 0 = n
  | n < 0 = -n

-- b) maximoAbsoluto: devuelve el maximo entre el valor absoluto de dos numeros enteros.
{-
    problema maximoAbsoluto (x: Z, y: Z): Z {
        requiere: { True }
        asegura: { (absoluto (x) >= absoluto (y) → res = x) ∧ (absoluto (x) < absoluto (y) → res = y)  }
    }
-}
maximoAbsoluto :: Integer -> Integer -> Integer
maximoAbsoluto x y
  | absoluto x >= absoluto y = absoluto x
  | otherwise = absoluto y

-- c) maximo3: devuelve el maximo entre tres numeros enteros.
{-
    problema maximo3 (x: Z, y: Z, z: Z): Z {
        requiere: { True }
        asegura: { res = maximo2 x (maximo2 y z)  }
    }

    problema maximo2 (x: Z, y: Z): Z {
        requiere: { True }
        asegura: { (x >= y → res = x) ∧ (x < y → res = y)  }
    }
-}
maximo3 :: Integer -> Integer -> Integer -> Integer
maximo3 x y z = maximo2 x (maximo2 y z)

maximo2 :: Integer -> Integer -> Integer
maximo2 x y
  | x >= y = x
  | otherwise = y

-- d) algunoEsCero: dados dos numeros racionales, decide si alguno es igual a 0 (resolverlo con y sin pattern matching).
{-
    problema algunoEsCero (x: R, y: R): Bool {
        requiere: { x e y pueden expresarse como el cociente de dos números enteros }
        asegura: { res = (x=0 ∨ y=0)  }
    }
-}
algunoEsCero :: Float -> Float -> Bool
algunoEsCero x y = (x == 0) || (y == 0)

-- algunoEsCero 0 y = True
-- algunoEsCero x 0 = True
-- algunoEsCero x y = False

-- e) ambosSonCero: dados dos numeros racionales, decide si ambos son iguales a 0 (resolverlo con y sin pattern matching).
{-
    problema ambosSonCero (x: R, y: R): Bool {
        requiere: { x e y pueden expresarse como el cociente de dos números enteros }
        asegura: { res = (x=0 ∧ y=0)  }
    }
-}
ambosSonCero :: Float -> Float -> Bool
ambosSonCero 0 0 = True
ambosSonCero x y = False

-- ambosSonCero x y = (x == 0) && (y == 0)

-- f) enMismoIntervalo: dados dos numeros reales, indica si estan relacionados por la relacion de equivalencia en R cuyas clases de equivalencia son: (−∞, 3],(3, 7] y (7, ∞), o dicho de otra manera, si pertenecen al mismo intervalo.
{-
    problema enMismoIntervalo (x: R, y: R): Bool {
        requiere: { True }
        asegura: { res = ((x <= 3 ∧ y <= 3) ∨ (x > 7 ∧ y > 7) ∨ ((x > 3 ∧ x <=7) ∧ (y > 3 ∧ y <=7))) }
    }
-}
enMismoIntervalo :: Float -> Float -> Bool
enMismoIntervalo x y
  | x <= 3 = y <= 3
  | x > 7 = y > 7
  | (x > 3) && (x <= 7) = (y > 3) && (y <= 7)
  | otherwise = False

-- g) sumaDistintos: que dados tres numeros enteros calcule la suma sin sumar repetidos (si los hubiera)
{-
    problema sumaDistintos (x: Z, y: Z, z: Z): Z {
        requiere: { True }
        asegura: { res = sumaDistintos2 x (sumaDistintos2 y z)}
    }

    x = y = z
    x = y
    x = z
    y = z
-}
sumaDistintos :: Integer -> Integer -> Integer -> Integer
sumaDistintos x y z
  | (x == y) && (x == z) = x
  | x == y = x + z
  | (x == z) || (y == z) = x + y
  | otherwise = x + y + z

-- h) esMultiploDe: dados dos numeros naturales, decide si el primero es multiplo del segundo
{-
    problema esMultiploDe (x: Z, y: Z): Bool {
        requiere: { x,y > 0 }
        asegura: { res = mod x y == 0}
    }
-}
esMultiploDe :: Integer -> Integer -> Bool
esMultiploDe x 0 = False
esMultiploDe x y = mod x y == 0

-- i) digitoUnidades: dado un numero entero, extrae su dıgito de las unidades.
{-
    problema digitoUnidades (x: Z): Bool {
        requiere: { True }
        asegura: { res = mod (absoluto x) 10}
    }
-}
digitoUnidades :: Integer -> Integer
digitoUnidades x = mod (absoluto x) 10

-- j) digitoDecenas: dado un numero entero mayor a 9, extrae su dıgito de las decenas.
{-
    problema digitoDecenas (x: Z): Bool {
        requiere: { x > 9 }
        asegura: { (x > 99 → res = digitoUnidades (div x 10)) ∧ (x < 100 → res = div x 10) }
    }
-}
digitoDecenas :: Integer -> Integer
digitoDecenas x
  | x > 99 = digitoUnidades (div x 10)
  | otherwise = div x 10