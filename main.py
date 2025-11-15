import time
import argparse
from src.data_loader import verificar_y_generar_archivo, cargar_numeros
from src.decision_tree import clasificar_numeros

# Valor por defecto del umbral [cite: 32, 58]
UMBRAL_POR_DEFECTO = 50

def main(umbral):
    """
    Función principal que orquesta la ejecución del programa.
    
    1. Inicia cronómetro.
    2. Verifica/Genera el archivo de datos.
    3. Carga los números.
    4. Clasifica los números.
    5. Imprime resultados.
    6. Detiene cronómetro e imprime tiempo total.
    """
    print("--- Iniciando Práctica 3: Árbol de Decisión ---")
    start_time = time.perf_counter() # Iniciar cronómetro [cite: 66]

    # 1. Verificar/crear data/numeros_1000.txt [cite: 67]
    verificar_y_generar_archivo()
    
    # 2. Leer números [cite: 68]
    numeros = cargar_numeros()
    
    if not numeros:
        print("No se pudieron cargar los números. Terminando.")
        return

    # 3. Clasificar con el árbol (if/else con umbral) [cite: 69]
    print(f"\nUsando UMBRAL = {umbral}")
    clasificaciones, conteo = clasificar_numeros(numeros, umbral)
    
    # 4. Imprimir resultados y conteos [cite: 70]
    print("\n--- Resultados de Clasificación ---")
    
    # 10 clasificaciones de ejemplo [cite: 34, 62]
    print("Primeros 10 ejemplos:")
    print(", ".join(clasificaciones[:10]))
    
    # Conteo "Alto" / "Bajo" [cite: 37, 63]
    print("\nConteos totales:")
    print(f"  - Altos (>= {umbral}): {conteo['Alto']}")
    print(f"  - Bajos (< {umbral}):  {conteo['Bajo']}")
    print(f"  - Total:     {len(numeros)}")

    # 5. Detener cronómetro e imprimir tiempo total [cite: 71]
    end_time = time.perf_counter()
    tiempo_total = end_time - start_time
    
    print("\n--- Ejecución Finalizada ---")
    print(f"Tiempo total de ejecución: {tiempo_total:.6f} segundos") # [cite: 38, 64]

if __name__ == "__main__":
    # Configuración para permitir cambiar el umbral por argumento [cite: 57, 59]
    parser = argparse.ArgumentParser(description="Clasificador de Árbol de Decisión Simple")
    parser.add_argument(
        "--umbral", 
        type=int, 
        default=UMBRAL_POR_DEFECTO,
        help=f"Umbral para clasificar (default: {UMBRAL_POR_DEFECTO})"
    )
    args = parser.parse_args()
    
    main(args.umbral)