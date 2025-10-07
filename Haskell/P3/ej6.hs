{-
Usando los siguientes tipos:
    type Anio = Integer
    type EsBisiesto = Bool

Programar la funcion bisiesto :: Anio -> EsBisiesto segun la siguiente especificacion:
    problema bisiesto (año : Z) : Bool {
        requiere: {True}
        asegura: {(res = false) ↔ (año no es multiplo de 4, o bien, año es multiplo de 100 pero no de 400)}
    }

Por ejemplo:
    bisiesto 1900 ⇝ False
    bisiesto 1901 ⇝ False
    bisiesto 1904 ⇝ True
    bisiesto 2000 ⇝ True
-}
type Anio = Integer

type EsBisiesto = Bool

bisiesto :: Anio -> EsBisiesto
bisiesto anio
  | mod anio 400 == 0 = True
  | mod anio 4 == 0 && mod anio 100 /= 0 = True
  | otherwise = False