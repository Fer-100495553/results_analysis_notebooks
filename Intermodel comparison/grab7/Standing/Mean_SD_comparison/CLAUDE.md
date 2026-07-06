# Mean SD Comparison — Instrucciones para Claude Code

## Descripción del proyecto

Análisis de comparación de estadísticos por repetición entre tres modelos biomecánicos (**Complete**, **C7**, **NOT_C7**) a partir de archivos `.csv` exportados. Cada CSV contiene los valores pico, valle y ROM por repetición, modelo, lado (Left/Right) y movimiento. No contienen forma de onda completa.

## Estado actual

| Archivo | Descripción |
|---|---|
| `raincloud_intermodel.ipynb` | Raincloud plots (violín + boxplot + scatter) de ROM, Maximum y Minimum por modelo y lado para los 6 movimientos de `Comparacion_Modelos_De pie.csv` |
| `raincloud_template.py` | Template original de referencia (lee C3D, no usar directamente) |
| `Comparacion_Modelos_De pie.csv` | Datos condición de pie — 6 movimientos, 3 modelos, Left/Right |
| `Comparacion_Modelos_De pie.xlsx` | Versión Excel del mismo archivo |
| `Comparacion_Modelos_Sentado.xlsx` | Datos condición sentado — pendiente de procesar |

### Estructura del CSV

El CSV es multi-sección: cada movimiento ocupa un bloque separado por líneas vacías encabezado con el nombre del movimiento. Las columnas varían según si el movimiento es Unilateral (Left + Right) o Bilateral (solo Left):

- **Unilateral**: `Model`, `Rep`, `Left Peak (°)`, `Left Valley (°)`, `ROM (°)` [Left], `Right Peak (°)`, `Right Valley (°)`, `ROM (°)` [Right] — hay dos columnas con el mismo nombre `ROM (°)`
- **Bilateral**: `Model`, `Rep`, `Left Peak (°)`, `Left Valley (°)`, `ROM (°)`

Los tres modelos en el CSV se llaman `Complete`, `C7`, `NOT_C7`.

### Paletas de colores por movimiento

| Movimiento | Paleta |
|---|---|
| Shoulder y Elbow | Left = familia roja, Right = familia verde |
| Thorax Lateral Inclination | Morado |
| Trunk Extended Lateral Inclination | Azul |

Dentro de cada familia: Complete = tono oscuro, C7 = tono medio, NOT_C7 = tono claro.

## Trabajo pendiente

### 1. Añadir cálculo de diferencias entre pares de modelos

Para cada articulación y lado calcular **ΔROM max** y **ΔROM min** entre los 3 pares:
- `Complete − C7`
- `Complete − NOT_C7`
- `C7 − NOT_C7`

Presentar como tabla de resultados o bar chart / dot plot con intervalo de confianza.

### 2. Procesar la condición Sentado

Extender el análisis a `Comparacion_Modelos_Sentado.xlsx`. Opciones:
- Parametrizar `raincloud_intermodel.ipynb` para cambiar entre `De pie` y `Sentado`
- O crear `raincloud_intermodel_sentado.ipynb` con la misma estructura

## Convención de nombres para métricas

Usar estos nombres de forma consistente en código, variables, títulos de gráficas y outputs:

| Nombre | Significado |
|---|---|
| `ΔROM max` | Diferencia en el valor máximo del ROM entre dos modelos |
| `ΔROM min` | Diferencia en el valor mínimo del ROM entre dos modelos |

> Las métricas de forma de onda (RMSD, MAD, Pearson r, ICC) **no aplican** en esta carpeta — los CSV solo contienen escalares por repetición, no series temporales. Esas métricas se calculan en `Temporal_comparison/`.

## Pares de modelos

Siempre calcular y mostrar los **3 pares**:
- `Complete − C7`
- `Complete − NOT_C7`
- `C7 − NOT_C7`

## Notas técnicas importantes

- Al crear DataFrames desde el CSV usar `dtype=object` para evitar que pandas infiera `StringArray` en columnas mixtas
- Convertir columnas numéricas por índice (`df.iloc[:, i]`) y no por nombre, ya que `ROM (°)` aparece duplicado en movimientos unilaterales
- No guardar figuras automáticamente — el usuario las descarga manualmente cuando está satisfecho con el resultado
