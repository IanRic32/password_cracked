from modules.utils import sustituciones, separadores, caracteres_finales
import itertools
from modules.dates_generation import generar_fechas_completas_optimizada as generar_fechas_completas
from modules.variantes_words import generar_variantes_palabra

def generar_diccionario_final(palabra_o_frase, anios, output_file, generar_fechas):
    print(f"Procesando: '{palabra_o_frase}'...")
    
    palabras_individuales = palabra_o_frase.strip().split()
    
    variantes_por_palabra = [generar_variantes_palabra(p) for p in palabras_individuales]
    
    combinadas = set()
    if len(variantes_por_palabra) == 1:
        # Usamos union, no update, para mayor claridad
        combinadas = combinadas.union(variantes_por_palabra[0])
    
    # Caso de múltiples palabras (con separadores)
    else:
        for sep in separadores:
            nuevas_combinaciones = {sep.join(c) for c in itertools.product(*variantes_por_palabra)}
            combinadas.update(nuevas_combinaciones)

    # Si 'combinadas' está vacío aquí (por algún error de input), salimos.
    if not combinadas:
        print("Advertencia: No se generaron combinaciones base. Saliendo.")
        return 
    
    elementos_tiempo = set(anios) # Empezamos con los años (como set para unicidad)
    
    if generar_fechas and anios:
        # Generar fechas completas (asume que la función ya retorna un set/list único)
        primer_anio = int(anios[0])
        ultimo_anio = int(anios[-1])
        fechas_generadas = generar_fechas_completas(primer_anio, ultimo_anio)
        # Unimos los sets para obtener todos los elementos de tiempo de forma única
        elementos_tiempo.update(fechas_generadas)
        
    todas_las_variantes = set(combinadas) 
    
    for base in combinadas:
        # Añadir prefijos y sufijos de tiempo
        for t in elementos_tiempo:
            todas_las_variantes.add(f"{t}{base}")
            todas_las_variantes.add(f"{base}{t}")
        
        # Añadir sufijos especiales y sus combinaciones con tiempo
        for char in caracteres_finales:
            sufijo_base_especial = f"{base}{char}"
            todas_las_variantes.add(sufijo_base_especial)
            
            for t in elementos_tiempo:
                # Variante: base + tiempo + especial
                todas_las_variantes.add(f"{base}{t}{char}") 
                # Variante: tiempo + base + especial
                todas_las_variantes.add(f"{t}{base}{char}")
    lista_final = sorted(list(todas_las_variantes)) 
    with open(output_file, 'w', encoding='utf-8') as f:
        
        f.write('\n'.join(lista_final))
        
        if lista_final:
            f.write('\n')
            
    print(f"\n Diccionario generado con {len(lista_final):4e} combinaciones.")
    print(f"Guardado en: {output_file}")