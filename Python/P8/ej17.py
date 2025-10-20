# Se debe desarrollar un navegador web muy simple que debe llevar un registro de los sitios web visitados por los usuarios del sistema. El navegador debe permitir al usuario navegar hacia atrás en la historia de navegación.

"""
1. Crea un diccionario llamado historiales que almacenará el historial de navegación para cada usuario. Las claves del
diccionario serán los nombres de usuario y los valores serán pilas de String.
"""
from queue import LifoQueue as Pila
historiales:dict[str, Pila[str]] = {}
historiales['Juan'] = Pila()
historiales['Juan'].put("google.com")
historiales['Juan'].put("kick.com")
historiales['Juan'].put("kick.com/baulo")
historiales['Juan'].put("x.com/home")
historiales['Camila'] = Pila()
historiales['Camila'].put("youtube.com")
historiales['Camila'].put("youtube.com/watch?v=au2MTlth520")
historiales['Camila'].put("instagram.com")
historiales['Pablo'] = Pila()
historiales['Pablo'].put("promiedos.com.ar")
historiales['Pablo'].put("promiedos.com.ar/league/liga-profesional/hc")
historiales['Pablo'].put("chatgpt.com")
historiales['Pablo'].put("github.com")

"""
2. Implementar una solución para el siguiente problema.
    problema visitar_sitio (inout historiales: Diccionario⟨seq⟨Char⟩, Pila[seq⟨Char⟩]⟩, in usuario: seq⟨Char⟩, in sitio: seq⟨Char⟩) {
        requiere: {Ninguno de los Strings de los parámetros es vacío}
        asegura: {Si usuario es una de las claves de historiales@pre, entonces se agrega sitio a su pila de historiales@pre[usuario]}
        asegura: {Si usuario no es una de las claves de historiales@pre, entonces historiales[usuario] es igual a la pila que tiene solo el elemento sitio}
        asegura: {No se modifica ningún otro historial salvo, si existe, el de usuario}
        asegura: {Todos los pares clave-valor de historiales@pre están en historiales}
        asegura: {Todos los pares clave-valor de historiales están en historiales@pre, salvo historiales[usuario] que podría no existir en historiales@pre}
    }
"""
def visitar_sitio(historiales:dict[str: Pila[str]], usuario: str, sitio:str) -> None:
    if not historiales.get(usuario):
        historiales[usuario] = Pila()
    historiales[usuario].put(sitio)

"""
3. Implementar una solución para el siguiente problema.
    problema navegar_atras (inout historiales: Diccionario⟨ seq⟨Char⟩, Pila[ seq⟨Char⟩, in usuario: seq⟨Char⟩⟩) : seq⟨Char⟩ {
        requiere: {Ninguno de los Strings de los parámetros es vacío}
        requiere: {usuario es una clave de historiales}
        requiere: {La pila asociada a usuario no está vacía}
        asegura: {res es igual al tope de historiales@pre[usuario]}
        asegura: {historiales[usuario] es igual a historiales@pre[usuario] quitando el tope de la pila de historiales@pre[usuario]}
        asegura: {En historiales, salvo la pila asociada a usuario, no se modifica ningún otro por clave-valor}
    }
Ejemplo de uso:
    historiales = {}
    visitar_sitio(historiales, "Usuario1", "google.com")
    visitar_sitio(historiales, "Usuario1", "facebook.com")
    navegar_atras(historiales, "Usuario1")
    visitar_sitio(historiales, "Usuario2", "youtube.com")
"""
def navegar_atras(historiales:dict[str, Pila[str]], usuario:str) -> str:
    res:str = historiales[usuario].get()
    return res