import random
import os
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / "data"
FILE_PATH = DATA_DIR / "numeros_1000.txt"

def verificar_y_generar_archivo():
    """
    Verifica si el archivo de datos existe. Si no, lo genera.
    
    El archivo 'numeros_1000.txt' se crea en la carpeta 'data'
    con 1000 números aleatorios (1-100), uno por línea[cite: 27].
    """
    if not DATA_DIR.exists():
        os.makedirs(DATA_DIR)

    if not FILE_PATH.exists():
        print(f"Generando archivo en: {FILE_PATH}")
        # Usamos una semilla fija para reproducibilidad, aunque no es requisito
        semilla = random.randint(1000, 9999)
        random.seed(semilla)
        print(f"Semilla usada para la generación: {semilla}")
        
        with open(FILE_PATH, 'w') as f:
            for _ in range(1000):
                f.write(f"{random.randint(1, 100)}\n")
    else:
        print(f"Archivo encontrado en: {FILE_PATH}")

def cargar_numeros():
    """
    Carga los números desde el archivo 'numeros_1000.txt'[cite: 28].
    
    Returns:
        list: Una lista de enteros cargados desde el archivo.
    """
    try:
        with open(FILE_PATH, 'r') as f:
            # Leemos las líneas, quitamos espacios en blanco y convertimos a entero
            numeros = [int(line.strip()) for line in f.readlines()]
        return numeros
    except FileNotFoundError:
        print("Error: Archivo no encontrado. Ejecute de nuevo para generarlo.")
        return []
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
        return []