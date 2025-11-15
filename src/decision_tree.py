def clasificar_numeros(numeros, umbral):
    """
    Clasifica una lista de números como 'Alto' o 'Bajo' según un umbral[cite: 21, 22].
    
    El árbol de decisión es de un solo nodo:
    - Si numero >= umbral -> "Alto" [cite: 30]
    - Si numero < umbral  -> "Bajo" [cite: 31]

    Args:
        numeros (list): Lista de enteros a clasificar.
        umbral (int): El valor de corte para la decisión.

    Returns:
        tuple: Una tupla conteniendo:
            - (list): Lista de resultados (ej: "23 -> Bajo").
            - (dict): Conteo de "Alto" y "Bajo".
    """
    clasificaciones = []
    conteo = {"Alto": 0, "Bajo": 0}
    
    for num in numeros:
        if num >= umbral:
            clase = "Alto"
            conteo["Alto"] += 1
        else:
            clase = "Bajo"
            conteo["Bajo"] += 1
        clasificaciones.append(f"{num} -> {clase}")
        
    return clasificaciones, conteo