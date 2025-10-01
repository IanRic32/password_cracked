import itertools
from modules.utils import sustituciones
def generar_variantes_palabra(palabra):
    """Genera todas las variantes de una palabra usando el diccionario de sustituciones."""
    lista_opciones = [
        sustituciones.get(letra.lower(), [letra.lower(), letra.upper()])
        if letra.isalnum() else [letra]
        for letra in palabra
    ]
    combinaciones = itertools.product(*lista_opciones)
    variantes = [''.join(c) for c in combinaciones]
    
    return variantes