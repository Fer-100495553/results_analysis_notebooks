# Métricas de comparación entre modelos biomecánicos

Todas las métricas se calculan sobre la **señal continua completa** (frame a frame), comparando dos modelos A y B a lo largo del tiempo. La diferencia en cada instante es `d[t] = A[t] − B[t]`.

---

## RMSD — Root Mean Square Deviation

**Fórmula:**

$$\text{RMSD} = \sqrt{\frac{1}{N} \sum_{t=1}^{N} d[t]^2}$$

**Qué mide:** El error cuadrático medio entre las dos señales. Penaliza de forma desproporcionada los errores grandes porque eleva al cuadrado cada diferencia antes de promediarlas. Un pico puntual de discrepancia grande inflará el RMSD más de lo que inflaría el MAD.

**Interpretación práctica:** Si el RMSD es mucho mayor que el MAD, hay picos de discrepancia puntual entre los modelos (spikes). Si son similares, la discrepancia está distribuida de forma uniforme a lo largo del tiempo.

**Unidades:** grados (°)

---

## MAD — Mean Absolute Deviation

**Fórmula:**

$$\text{MAD} = \frac{1}{N} \sum_{t=1}^{N} |d[t]|$$

**Qué mide:** La diferencia media absoluta entre las dos señales. A diferencia del RMSD, trata todos los errores de forma proporcional (sin elevar al cuadrado), por lo que es más resistente a valores atípicos.

**Interpretación práctica:** Representa el error "típico" esperado en cualquier instante de tiempo. Es la métrica más directa para responder: *"¿cuántos grados de media se desvían los modelos entre sí?"*

**Unidades:** grados (°)

---

## max_diff — Diferencia absoluta máxima

**Fórmula:**

$$\text{max\_diff} = \max_t |d[t]|$$

**Qué mide:** El peor caso — la mayor discrepancia puntual observada entre los dos modelos en toda la señal.

**Interpretación práctica:** Útil para detectar si hay algún instante concreto donde los modelos divergen de forma extrema, aunque en la mayor parte del tiempo sean similares. Un max_diff muy superior al RMSD/MAD indica un spike puntual.

**Unidades:** grados (°)

---

## mean_bias — Sesgo medio

**Fórmula:**

$$\text{mean\_bias} = \frac{1}{N} \sum_{t=1}^{N} d[t]$$

**Qué mide:** La diferencia media con signo entre los dos modelos (A − B). A diferencia del MAD, los errores positivos y negativos se cancelan entre sí.

**Interpretación práctica:**
- Un valor cercano a 0 indica que no hay sesgo sistemático: los modelos se desvían hacia ambos lados de forma equilibrada.
- Un valor positivo indica que el modelo A tiende a dar valores más altos que B de forma consistente (y viceversa si es negativo).
- Es posible tener un bias bajo con un RMSD alto: los modelos oscilan alrededor del mismo valor medio pero con mucho error puntual.

**Unidades:** grados (°)

---

## Pearson r — Coeficiente de correlación de Pearson

**Fórmula:**

$$r = \frac{\sum_{t=1}^{N} (A[t] - \bar{A})(B[t] - \bar{B})}{\sqrt{\sum (A[t]-\bar{A})^2 \cdot \sum (B[t]-\bar{B})^2}}$$

**Qué mide:** La similitud en la *forma* de las dos señales, ignorando diferencias de escala o offset. Evalúa si los dos modelos suben y bajan al mismo tiempo y con la misma proporción relativa.

**Rango:** −1 a +1
- `r ≈ 1`: las señales tienen la misma forma (correlación perfecta positiva).
- `r ≈ 0`: no hay relación lineal entre las formas.
- `r ≈ −1`: las señales son simétricamente opuestas.

**Interpretación práctica:** Un r alto con RMSD alto indica que los modelos coinciden en la forma del movimiento pero tienen un offset o diferencia de escala. Un r alto con RMSD bajo indica acuerdo tanto en forma como en magnitud.

**Limitación importante:** El Pearson r no detecta diferencias de offset ni de escala — dos señales pueden tener `r = 1` y un RMSD grande si una está sistemáticamente desplazada respecto a la otra.

---

## ICC(3,1) — Intraclass Correlation Coefficient

**Modelo utilizado:** ICC(3,1) — dos factores fijos (modelos como "evaluadores"), medida única, consistencia.

**Fórmula (ANOVA de dos vías):**

$$\text{ICC}(3,1) = \frac{MS_{between} - MS_{error}}{MS_{between} + (k-1) \cdot MS_{error}}$$

Donde:
- $MS_{between}$: varianza entre instantes de tiempo (entre "sujetos" en la formulación ANOVA)
- $MS_{error}$: varianza residual (interacción tiempo × modelo)
- $k = 2$: número de modelos comparados

**IC 95%** se calcula mediante la distribución F:

$$\text{IC\_inf} = \frac{F/F_{crit} - 1}{F/F_{crit} + k - 1}, \quad \text{IC\_sup} = \frac{F \cdot F_{crit}' - 1}{F \cdot F_{crit}' + k - 1}$$

**Qué mide:** El acuerdo global entre dos señales, teniendo en cuenta tanto la correlación de su forma como su variabilidad relativa. A diferencia del Pearson r, el ICC sí es sensible a diferencias sistemáticas entre modelos (offset o escala), lo que lo hace más estricto.

**Rango:** −1 a +1 (en la práctica 0 a 1 para señales biomecánicas)

| ICC | Interpretación habitual |
|-----|------------------------|
| < 0.50 | Acuerdo pobre |
| 0.50 – 0.75 | Acuerdo moderado |
| 0.75 – 0.90 | Acuerdo bueno |
| > 0.90 | Acuerdo excelente |

*(Koo & Mae, 2016)*

**Diferencia clave frente a Pearson r:** El Pearson r mide correlación lineal de la forma; el ICC mide acuerdo absoluto. Una señal con offset constante tendrá `r = 1` pero `ICC < 1`. Por eso el ICC es el estándar en estudios de fiabilidad entre instrumentos o modelos.

**El IC 95%** indica la precisión de la estimación del ICC. Con señales muy largas (muchos frames) el intervalo es estrecho; con señales cortas, el intervalo es amplio y la estimación es menos fiable.

---

## Comparación rápida entre métricas

| Métrica | Sensible a offset | Sensible a escala | Sensible a spikes | Tiene dirección (signo) |
|---|:---:|:---:|:---:|:---:|
| RMSD | ✓ | ✓ | Mucho | No |
| MAD | ✓ | ✓ | Poco | No |
| max_diff | ✓ | ✓ | Es el spike | No |
| mean_bias | ✓ | No | No | **Sí** |
| Pearson r | No | No | Poco | No |
| ICC(3,1) | ✓ | ✓ | Poco | No |

---

## Referencia

Koo, T. K., & Mae, M. Y. (2016). A guideline of selecting and reporting intraclass correlation coefficients for reliability research. *Journal of Chiropractic Medicine*, 15(2), 155–163.
