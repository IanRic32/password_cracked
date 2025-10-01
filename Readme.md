

# 🛠️ Generador Avanzado de Diccionarios (Wordlist Generator)

Este proyecto es un script de Python diseñado para generar diccionarios (wordlists) personalizados y avanzados. Se enfoca en técnicas de permutación comunes para el *cracking* de contraseñas, como la aplicación de **LeetSpeak**, la combinación de múltiples palabras con separadores y la adición de variaciones de fechas y años.

## ✨ Características Principales

* **Sustituciones LeetSpeak/Capitalización:** Genera variantes de la palabra clave utilizando combinaciones de mayúsculas/minúsculas y sustituciones numéricas/simbólicas comunes (ej: 'a' por '4' o '@').
* **Combinación de Frases:** Permite ingresar frases (múltiples palabras) y las combina usando varios separadores (ej: `palabra1-palabra2`, `palabra1.palabra2`, `palabra1_palabra2`).
* **Fechas y Años:** Añade combinaciones con años (rango configurable) y formatos de fecha completa (DDMM, DDMMYY, DDMMYYYY) como prefijos y sufijos.
* **Caracteres Finales:** Incluye caracteres especiales (`!`, `?`, `$`, `*`, `#`) al final de las palabras clave.

## 🚀 Instalación

Este script solo requiere la instalación de **Python 3**. No se necesitan librerías externas adicionales más allá de las incluidas en la instalación estándar de Python (`itertools`, `datetime`, `argparse`).


```bash
# Simplemente clona el repositorio (asumiendo que está en uno) o guarda los archivos.
git clone "https://github.com/IanRic32/password_cracked.git"
cd <NOMBRE_DEL_DIRECTORIO>
```

## ⚙️ Uso

El script principal se ejecuta a través de la línea de comandos (`main.py`) y acepta varios argumentos para personalizar la generación del diccionario.

### Sintaxis

```bash
python main.py -p <PALABRA_O_FRASE> [OPCIONES]
```

### Argumentos

| Argumento Corto | Argumento Largo | Requerido | Descripción | Defecto (Ejemplo) |
| :---: | :---: | :--- | :--- | :--- |
| `-p` | `--palabra` | **Sí** | Palabra o frase base para generar variantes (ej: `'Sams club'`, `'contrasena'`). | N/A |
| `-o` | `--output` | No | Nombre del archivo de salida. | `diccionario.txt` |
| | `--inicio` | No | Año inicial para las combinaciones de fechas/años. | Año actual - 5 (ej: `2020`) |
| | `--fin` | No | Año final para las combinaciones de fechas/años. | Año actual (ej: `2025`) |
| | `--fechas` | No | Si está presente, añade formatos de fecha completa (DDMM, DDMMYY, DDMMYYYY) para el rango de años. | Ausente |

### Ejemplos de Uso

#### Ejemplo 1: Palabra simple con rango de años por defecto

Genera todas las variantes LeetSpeak/capitalización de "super" y les añade los años del `2020` al `2025` (si el año actual es 2025).

```bash
python main.py -p super -o mi_diccionario_simple.txt
```

#### Ejemplo 2: Frase con separadores, fechas completas y rango de años específico

Genera variantes para "Casa Blanca", combinando las dos palabras con separadores (`_`, `-`, `.`, etc.), y añade formatos de fecha completa desde el año `2018` hasta el `2023`.

```bash
python main.py -p "Casa Blanca" --inicio 2018 --fin 2023 --fechas -o dic_casa_blanca.txt
```

## 📂 Estructura de Módulos (Resumen del Código)

El código se organiza en varios módulos para manejar tareas específicas:

  * `main.py`: Función principal, parseo de argumentos de línea de comandos.
  * `modules/utils.py`: Contiene constantes de sustituciones (`sustituciones`), separadores (`separadores`), caracteres finales (`caracteres_finales`) y la función auxiliar para generar años (`generar_anios`).
  * `modules/variantes_words.py`: Maneja la lógica de aplicar las sustituciones LeetSpeak/capitalización a una sola palabra (`generar_variantes_palabra`).
  * `modules/dates_generation.py`: Contiene la lógica para generar todos los formatos comunes de fechas (`generar_fechas_completas_optimizada`) dentro de un rango de años.
  * `modules/diccionario_palabras.py`: Contiene la función central (`generar_diccionario_final`) que orquesta todas las combinaciones: junta las variantes de las palabras, aplica los separadores y mezcla con los elementos de tiempo (años y fechas).

## ⚠️ Advertencia

La complejidad (y el tamaño del archivo de salida) **crece exponencialmente** con la longitud de la palabra clave y el rango de años, especialmente cuando se activan las `--fechas`.
