# Temporal Comparison — Instrucciones para Claude Code

## Descripción del proyecto

Análisis de comparación temporal entre tres modelos biomecánicos (**Complete**, **C7**, **NOT_C7**) a partir de archivos `.c3d` con series temporales completas de ángulos articulares (frame a frame), eventos de movimiento y metadatos de grabación.

## Estado actual

Existen 4 notebooks con la siguiente estructura común:
- Waveform overlay de los 3 modelos superpuestos
- Difference waveform: Complete−C7 y Complete−NOT_C7
- Métricas por par: RMSD, MAD, diferencia máxima absoluta, mean bias
- Detección de spikes (umbral MAD + 2σ)

| Notebook | Articulación |
|---|---|
| `Shoulder_flex_ext_comparison.ipynb` | Shoulder Flex/Ext |
| `Shoulder_abd_add_comparison.ipynb` | Shoulder Abd/Add |
| `Shoulder_rotac_int_ext_comparison.ipynb` | Shoulder Int/Ext Rot |
| `Elbow_flex_ext_comparison.ipynb` | Elbow Flex/Ext |

## Trabajo pendiente

### 1. Modificar los 4 notebooks existentes

- Añadir el **par C7 vs NOT_C7** en métricas y difference waveform (actualmente solo existen Complete−C7 y Complete−NOT_C7)
- Añadir **Pearson r** de la forma de onda completa para los 3 pares
- Añadir **ICC con IC 95%** para los 3 pares — usar ICC(2,1) o ICC(3,1) según diseño single-subject
- Renombrar variables internas `rmse` → `rmsd` y `mae` → `mad` en el código

### 2. Crear 2 notebooks nuevos (misma estructura que los existentes)

- `Trunk_extended_lateral_inclination_comparison.ipynb`
- `Thorax_lateral_inclination_comparison.ipynb`

### 3. Crear notebook de resumen

- `summary_comparison.ipynb`: RMSD bar chart agrupado por articulación y par de modelos (Complete−C7, Complete−NOT_C7, C7−NOT_C7)

## Convención de nombres para métricas

Usar estos nombres de forma consistente en código, variables, títulos de gráficas y outputs:

| Nombre | Significado | Prohibido usar |
|---|---|---|
| `rmsd` | Root Mean Square Deviation | `rmse` |
| `mad` | Mean Absolute Deviation | `mae` |
| `pearson_r` | Coeficiente de correlación de Pearson | `r`, `corr` |
| `icc` | Intraclass Correlation Coefficient — reportar modelo (2,1) o (3,1) e IC 95% | — |
| `max_diff` | Diferencia absoluta máxima entre señales | `max_error` |
| `mean_bias` | Sesgo medio (media de A−B, con signo) | `mean_error` |

## Pares de modelos

Siempre calcular y mostrar los **3 pares**:
- `Complete − C7`
- `Complete − NOT_C7`
- `C7 − NOT_C7`

## Fuente de datos

Archivos `.c3d` — las métricas se calculan sobre la **señal continua completa** (todos los frames). No usar los CSV de `Mean_SD_comparison` para cálculos de forma de onda.
