from typing import TextIO
"""
Implementar una solución para el siguiente problema.
    problema listar_textos_de_archivo (in nombre_archivo: seq⟨Char⟩ ) : seq⟨seq⟨Char⟩⟩ {
        requiere: {nombre_archivo es el path de un archivo existente y accesible}
        asegura: {res contiene exactamente los textos legibles que aparecen en el archivo nombre_archivo}
    }
Definimos un texto como legible si:
    - solo contiene secuencias de carácteres legibles (números, letras mayúsculas/minúsculas, espacios o '_'(guión bajo)
    - tienen longitud >= 5

(Para resolver este ejercicio se puede abrir un archivo en modo binario 'b'. Al hacer read() vamos a obtener una secuencia de bytes, que al hacer chr(byte) nos va a devolver un carácter correspondiente al byte leído.)
"""
def listar_textos_de_archivo(nombre_archivo:str) -> list[str]:
    res:list[str] = []
    
    archivo:TextIO = open(nombre_archivo, "rb")
    contenido:list[str] = archivo.read()
    archivo.close()
    
    texto_actual:str = ""
    for byte in contenido:
        es_mayus:bool = byte > 64 and byte < 91
        es_minus:bool = byte > 96 and byte < 123
        es_num:bool = byte > 47 and byte < 58
        es_con_acento:bool = byte in [130, 160, 161, 162, 163, 144, 181, 214, 224, 233]
        es_especial:bool = byte in [32, 95, 164, 165] # 32 = espacio, 95 = _, 164 = ñ, 165 = Ñ
        
        if es_mayus or es_minus or es_num or es_con_acento or es_especial:
            texto_actual += chr(byte)
        elif len(texto_actual) > 4:
            res.append(texto_actual)
            texto_actual = ""
        else:
            texto_actual = ""

    if len(texto_actual) > 4: res.append(texto_actual)

    return res
