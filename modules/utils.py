sustituciones = {
    'a': ['a', 'A', '@', '4'],
    'e': ['e', 'E', '3'],
    'i': ['i', 'I', '1', '!', '¡'],
    'o': ['o', 'O', '0'],
    'u': ['u', 'U'],
    's': ['s', 'S', '$', '5'],
    'n': ['n', 'N'],
    'c': ['c', 'C'],
    't': ['t', 'T', '7'],
    'r': ['r', 'R'],
    'l': ['l', 'L', '1'],
    'p': ['p', 'P'],
    'b': ['b', 'B', '8'],
    'd': ['d', 'D'],
    'm': ['m', 'M']
}
# Separadores permitidos para reemplazar espacios en frases
separadores = ['', '_', '-', '.', ',']

# Caracteres especiales para añadir al final de las palabras clave
caracteres_finales = ['!', '?', '$', '*', '#']

def generar_anios(inicio, fin) :
    """Genera una lista de años como strings en el rango dado."""
    return [str(a) for a in range(inicio, fin + 1)]
