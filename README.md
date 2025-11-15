# [AA]Practica_ArbolDecision_202304221

**Universidad Da Vinci de Guatemala**
**Facultad de Ingeniería Industria y Tecnología**
**Análisis de algoritmos**
**Ing.César Sazo**

> PRÁCTICA 3: Árbol de Decisión

**Autor:** William Cardona
**Carnet:** 202304221
**Fecha:** 15 de noviembre de 2025

---

## Objetivos

### Objetivo General

Construir y ejecutar un árbol de decisión simple en Python (sin librerías externas) para clasificar números como "Alto" o "Bajo" a partir de un umbral, aplicando de forma rigurosa el flujo de trabajo Gitflow (ramas, commits, PRs, merges y versionado).

### Objetivos Específicos

* Implementar un árbol de decisión minimalista con 1 solo nodo de decisión (umbral) y 2 hojas ("Bajo" / "Alto").
* Leer un archivo TXT con 1000 números y clasificarlos. 
* Generar salidas claras en consola.
* Aplicar Gitflow con ramas `feature/*`, `hotfix/*` o `bugfix/*`, commits significativos, PRs y merge hacia `develop` y luego a `main`.
* Documentar con docstrings (PEP-257) y un `README.md` claro. 

---

## Descripción del Árbol

El programa implementa un árbol de decisión minimalista de un solo nivel. Este árbol utiliza un único criterio (un **umbral numérico**) para tomar una decisión.

* **Nodo de Decisión:** Compara un número con el umbral (por defecto, 50).
* **Hoja 1 (Alto):** Si el número es mayor o igual al umbral (`>= 50`), se clasifica como "Alto".
* **Hoja 2 (Bajo):** Si el número es menor al umbral (`< 50`), se clasifica como "Bajo".

---

## Metodología

### Flujo del Script (main.py)

El script `main.py` sigue un flujo de ejecución orquestado:

1.  **Iniciar Cronómetro:** Se registra el tiempo de inicio para medir el rendimiento.
2.  **Verificar/Generar Datos:** El script comprueba si `data/numeros_1000.txt` existe. Si no, lo genera con 1000 números aleatorios (1-100).
3.  **Cargar Números:** Se leen los 1000 números del archivo TXT a una lista.
4.  **Clasificar:** Se pasa la lista de números a la función del árbol de decisión, que retorna las clasificaciones y los conteos.
5.  **Imprimir Resultados:** Se muestran en consola los primeros 10 ejemplos y los conteos totales.
6.  **Detener Cronómetro:** Se calcula el tiempo total de ejecución y se imprime en segundos.

### Flujo de Versionado (Gitflow)

Se siguió un flujo de trabajo `git flow` riguroso para la gestión del proyecto:

1.  Se inicializó Gitflow en el repositorio, creando las ramas `main` y `develop`.
2.  Todo el desarrollo del código se realizó en una rama `feature/implementacion_arbol`, acumulando 4 commits significativos.
3.  Se realizó un **Pull Request** para fusionar la rama `feature` en `develop`, simulando la integración del desarrollo.
4.  Se simuló un "lanzamiento" fusionando `develop` en `main`.
5.  Se creó una rama `hotfix/cambiar_nombre_readme` para corregir un "error" en producción (cambiar el nombre del autor a uno ficticio).
6.  El `hotfix` se fusionó automáticamente en `main` (con un tag) y de vuelta en `develop` para mantener la consistencia.
7.  Finalmente, se realizó un último **Pull Request** de `develop` a `main` para publicar la versión final `v1.0.0`.

---

## Resultados

Resultados de la ejecución del script (`python main.py`):

```bash
--- Iniciando Práctica 3: Árbol de Decisión ---
Generando archivo en: ...\data\numeros_1000.txt
Semilla usada para la generación: 7882

Usando UMBRAL = 50

--- Resultados de Clasificación ---
Primeros 10 ejemplos:
89 -> Alto, 91 -> Alto, 70 -> Alto, 26 -> Bajo, 84 -> Alto, 65 -> Alto, 4 -> Bajo, 62 -> Alto, 73 -> Alto, 61 -> Alto

Conteos totales:
  - Altos (>= 50): 524
  - Bajos (< 50):  476
  - Total:         1000

--- Ejecución Finalizada ---
Tiempo total de ejecución: 0.011165 segundos