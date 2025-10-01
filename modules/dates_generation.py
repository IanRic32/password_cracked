from datetime import date, timedelta
#Colocar solamente el año
def generar_fechas_completas_optimizada(inicio: int, fin: int) -> list[str]:
    """
    Genera formatos comunes de fechas (DDMM, DDMMYY, DDMMYYYY) para el rango de años dado.
    :param inicio: Año de inicio (ej. 2020).
    :param fin: Año de fin (ej. 2025).
    :return: Lista de strings con variaciones de fechas.
    """
    #Definir el rango de fechas a generar (desde el 1 de enero del año de inicio hasta el 31 de diciembre del año de fin)
    fecha_actual = date(inicio, 1, 1)
    fecha_fin = date(fin, 12, 31)
    
    variaciones = set()
    
    #Iterar día por día
    while fecha_actual <= fecha_fin:
        # Formatos clave de la fecha actual
        dd = fecha_actual.strftime("%d")  # Día: 01, 15, 31
        mm = fecha_actual.strftime("%m")  # Mes: 01, 09, 12
        yy = fecha_actual.strftime("%y")  # Año corto: 20, 24
        yyyy = fecha_actual.strftime("%Y")# Año largo: 2020, 2024
        # Generar las combinaciones de formato de fecha
        variaciones.add(f"{dd}{mm}")  # Ej: 0512
        variaciones.add(f"{mm}{dd}")  # Ej: 1205
        
        # Formato con año corto (YY)
        variaciones.add(f"{dd}{mm}{yy}") # Ej: 051224
        variaciones.add(f"{mm}{dd}{yy}") # Ej: 120524
        
        # Formato con año largo (YYYY)
        variaciones.add(f"{dd}{mm}{yyyy}") # Ej: 05122024
        variaciones.add(f"{mm}{dd}{yyyy}") # Ej: 12052024
        variaciones.add(f"{yyyy}{mm}{dd}") # Ej: 20241205

        # Pasar al siguiente día
        fecha_actual += timedelta(days=1)
    
    # También incluimos los años por separado, si no se incluyeron en la función original
    for anio in range(inicio, fin + 1):
        variaciones.add(str(anio))
        variaciones.add(str(anio)[2:])

    return sorted(list(variaciones))
