{-
En este ejercicio trabajaremos con lockers de una facultad.
Para resolverlo usaremos un tipo MapaDelockers que sera una secuencia de locker.
Cada locker es una tupla con la primera componente correspondiente al numero de identificacion, y la segunda componente
el estado.
El estado es a su vez una tupla cuya primera componente dice si esta ocupado (False) o libre (True), y la segunda
componente es un texto con el codigo de ubicacion del locker.
-}
type Identificacion = Integer
type Disponibilidad = Bool
type Ubicacion = String
type Estado = (Disponibilidad, Ubicacion)
type Locker = (Identificacion, Estado)
type MapaDeLockers = [Locker]

lockers = [ (100,(False,"ZD39I")), (103,(True,"IQSA9")), (105,(True,"QOTSA")), (109,(False,"893JJ")), (110,(False,"99292")) ]

-- 1. Implementar existeElLocker :: Identificacion -> MapaDeLockers -> Bool, una funcion para saber si un locker existe en la facultad.
existeElLocker :: Identificacion -> MapaDeLockers -> Bool
existeElLocker _ [] = False
existeElLocker idLocker ((idPrimerLocker, _) : otrosLockers)
    | idLocker == idPrimerLocker = True
    | otherwise = existeElLocker idLocker otrosLockers

-- 2. Implementar ubicacionDelLocker :: Identificacion ->MapaDeLockers ->Ubicacion, una funcion que dado un locker que existe en la facultad, me dice la ubicacion del mismo.
ubicacionDelLocker :: Identificacion -> MapaDeLockers -> Ubicacion
ubicacionDelLocker _ [] = []
ubicacionDelLocker idLocker ((idPrimerLocker, (_, ubiPrimerLocker)) : otrosLockers) 
    | idLocker == idPrimerLocker = ubiPrimerLocker
    | otherwise = ubicacionDelLocker idLocker otrosLockers

-- 3. Implementar estaDisponibleElLocker :: Identificacion ->MapaDeLockers ->Bool, una funcion que dado un locker que existe en la facultad, me devuelve Verdadero si esta libre.
estaDisponibleElLocker :: Identificacion -> MapaDeLockers -> Bool
estaDisponibleElLocker _ [] = False
estaDisponibleElLocker idLocker ((idPrimerLocker, (dispoPrimerLocker, _)) : otrosLockers) 
    | idLocker == idPrimerLocker = dispoPrimerLocker
    | otherwise = estaDisponibleElLocker idLocker otrosLockers

-- 4. Implementar ocuparLocker :: Identificacion ->MapaDeLockers ->MapaDeLockers, una funcion que dado un locker que existe en la facultad, y esta libre, lo ocupa
ocuparLocker :: Identificacion -> MapaDeLockers -> MapaDeLockers
ocuparLocker _ [] = []
ocuparLocker idLocker ((idPrimerLocker, (dispoPrimerLocker, ubiPrimerLocker)) : otrosLockers)
    | idLocker == idPrimerLocker = lockerActualizado : otrosLockers
    | otherwise = lockerAnalizado : (ocuparLocker idLocker otrosLockers)
    where
        lockerAnalizado = (idPrimerLocker, (dispoPrimerLocker, ubiPrimerLocker))
        lockerActualizado = (idPrimerLocker, (True, ubiPrimerLocker))
