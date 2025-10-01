import argparse
from datetime import date
from modules.utils import sustituciones, separadores, caracteres_finales, generar_anios
from modules.dates_generation import generar_fechas_completas_optimizada as generar_fechas_completas
from modules.variantes_words import generar_variantes_palabra
from modules.diccionario_palabras import generar_diccionario_final

def main():
    """
    Función principal que maneja el parseo de argumentos.
    """
    
    # Obtenemos el año actual una sola vez para usarlo en los valores por defecto.
    current_year = date.today().year
    
    parser = argparse.ArgumentParser(
        description="Generador de diccionarios con LeetSpeak, separadores y fechas/años.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    # --- Argumentos Requeridos y de Salida ---
    parser.add_argument(
        "-p", "--palabra", 
        required=True, 
        help="Palabra o frase base (ej: 'Sams club' o 'contrasena')"
    )
    parser.add_argument(
        "-o", "--output", 
        default="diccionario.txt", 
        help="Nombre del archivo de salida (defecto: diccionario.txt)"
    )
    
    # --- Argumentos para el Rango de Años (Uso de 'current_year') ---
    parser.add_argument(
        "--inicio", 
        type=int, 
        default=current_year - 5, 
        help=f"Año inicial para generar combinaciones (defecto: {current_year - 5})"
    )
    # Se usa el año actual como el valor por defecto para el año final.
    parser.add_argument(
        "--fin", 
        type=int, 
        default=current_year, 
        help=f"Año final para generar combinaciones (defecto: {current_year})"
    )

    # --- Bandera para Fechas ---
    parser.add_argument(
        "--fechas", 
        action='store_true', 
        help="Si está presente, añade formatos de fecha completa (DDMM, DDMMYY)."
    )

    args = parser.parse_args()

    # La validación se hace justo después del parseo.
    if args.inicio > args.fin:
        # En lugar de solo 'return', se usa SystemExit para una terminación más limpia
        # y para mostrar un mensaje de error más claro al usuario.
        raise SystemExit("Error: El año de inicio no puede ser mayor al año final.")

    # Generar la lista de años
    # Asumimos la existencia de 'generar_anios'
    anios = generar_anios(args.inicio, args.fin)
    
    # Llamar a la función principal
    # Asumimos la existencia de 'generar_diccionario_final'
    generar_diccionario_final(
        args.palabra, 
        anios, 
        args.output, 
        args.fechas
    )

# La función 'generar_anios' y 'generar_diccionario_final' deben estar definidas 
# en el script principal para que este código funcione.
if __name__ == "__main__":
    main()