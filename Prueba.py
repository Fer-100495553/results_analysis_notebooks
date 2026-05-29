"""
timeseries_template.py
----------------------
Template para comparar la curva temporal de un ángulo concreto
en tres grabaciones .c3d distintas (misma variable, mismo sujeto o condición).

Flujo:
  1. Leer cada C3D y extraer la curva angular del label SULM indicado.
  2. (Opcional) Normalizar el eje temporal al 0-100 % de la duración.
  3. (Opcional) Segmentar repeticiones y mostrar media ± DE por grabación.
  4. Superponer las tres curvas en un mismo gráfico y guardar/mostrar.

Requisitos:
    pip install ezc3d numpy scipy matplotlib

Ejecución:
    python timeseries_template.py

_________________________________________________________________________________
Sección CONFIG (única parte que hay que tocar para cada caso):

C3D_RECORDINGS — lista de 3 dicts con 'path' y 'label' (nombre en la leyenda)
VARIABLE_NAME  — label SULM sin prefijo de lado
COMPONENT_INDEX— 0=X, 1=Y, 2=Z según el componente Euler que interese
SIDE           — "Left", "Right" o "—" si el label no tiene prefijo
NORMALIZE_TIME — True → eje X en % de duración | False → segundos reales
SHOW_MEAN_BAND — True → segmenta reps y dibuja media ± 1 DE
               False → dibuja la señal cruda completa
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

# ── Importar funciones del proyecto ──────────────────────────────────────────
# Si este script está fuera de ROM_analyzer, ajusta esta ruta:
sys.path.insert(0, str(Path(__file__).parent))
from data_processing import read_c3d
from segmentation import auto_segment


# ══════════════════════════════════════════════════════════════════════════════
#  CONFIGURACIÓN  ← editar aquí para cada caso concreto
# ══════════════════════════════════════════════════════════════════════════════

# -- Grabaciones a comparar ---------------------------------------------------
# Cada elemento necesita 'path' (ruta al .c3d) y 'label' (texto en la leyenda).
# Añade o quita elementos; el script usa los colores de COLORS en el mismo orden.
C3D_RECORDINGS: list[dict] = [
    {"path": r"E:\Universidad_2\Fourth Year\4.2_Practicas y TFG\TFG\Analisis de Resultados\Scripts gráficos\grab 5\Pie_C7_Shoulder_Flex_Ext_Left_Cont01.c3d", "label": "Grabación 1"},
    {"path": r"E:\Universidad_2\Fourth Year\4.2_Practicas y TFG\TFG\Analisis de Resultados\Scripts gráficos\grab 5\Pie_Complete_Shoulder_Flex_Ext_Left_Cont01.c3d", "label": "Grabación 2"},
    {"path": r"E:\Universidad_2\Fourth Year\4.2_Practicas y TFG\TFG\Analisis de Resultados\Scripts gráficos\grab 5\Pie_NOT_C7_Shoulder_Flex_Ext_Left_Cont01.c3d", "label": "Grabación 3"},
]

# -- Variable SULM a analizar -------------------------------------------------
# Nombre del label tal como aparece en el C3D, SIN prefijo de lado.
VARIABLE_NAME = "Humerothoracic_ZXY_Op1"

# Componente Euler: 0 = X (Rot1), 1 = Y (Rot2), 2 = Z (Rot3)
COMPONENT_INDEX = 1

# -- Lado ---------------------------------------------------------------------
# "Left", "Right", o "—" si el label no lleva prefijo de lado
SIDE = "Left"

# -- Eje temporal -------------------------------------------------------------
# True  → normaliza cada señal a 0–100 % de su duración total
# False → eje X en segundos reales (cada grabación puede tener duración distinta)
NORMALIZE_TIME = False

# -- Mostrar media ± DE por repetición en lugar de la señal cruda -------------
# True  → segmenta las reps automáticamente y dibuja media ± 1 DE
# False → dibuja la señal completa sin segmentar
SHOW_MEAN_BAND = False

# Parámetros de segmentación (sólo relevantes si SHOW_MEAN_BAND = True)
PROMINENCE         = 15.0           # prominencia mínima de pico/valle (°)
MIN_DISTANCE       = 60             # distancia mínima entre picos (frames)
HALFCYCLE_DIRECTION = "peak_to_valley"  # "peak_to_valley" o "valley_to_peak"

# -- Apariencia ---------------------------------------------------------------
COLORS = ["#E74C3C", "#2E86C1", "#27AE60"]   # un color por grabación
ALPHA_RAW  = 0.85    # opacidad de la señal cruda
ALPHA_BAND = 0.18    # opacidad de la banda DE
LINE_WIDTH = 1.4

MOVEMENT_LABEL = "Humerothoracic — Plano de elevación"   # título del gráfico
Y_LABEL        = "Ángulo (°)"
OUTPUT_PATH    = "timeseries_output.png"    # None → solo muestra en pantalla
DPI            = 150

# ══════════════════════════════════════════════════════════════════════════════


# ── Helpers ──────────────────────────────────────────────────────────────────

def _label_for_side(variable: str, side: str) -> str:
    return variable if side == "—" else side + variable


def _extract_angle(c3d_path: str, variable: str, component: int, side: str) -> tuple[np.ndarray, int]:
    """Devuelve (señal_angular, frame_rate)."""
    c3d   = read_c3d(c3d_path)
    label = _label_for_side(variable, side)
    mo    = c3d["model_outputs"]

    if label not in mo:
        available = [k for k in mo if variable in k or side in k]
        raise KeyError(
            f"Label '{label}' no encontrado en {Path(c3d_path).name}.\n"
            f"Coincidencias parciales: {available}\n"
            f"Labels disponibles: {list(mo.keys())}"
        )

    angle = mo[label][component, :].astype(float)
    return angle, int(c3d["frame_rate"])


def _build_time_axis(n_frames: int, frame_rate: int, normalize: bool) -> np.ndarray:
    t = np.arange(n_frames) / frame_rate
    if normalize:
        t = t / t[-1] * 100.0
    return t


def _mean_band(angle: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Segmenta las repeticiones, interpola cada una a 101 puntos y devuelve
    (time_norm_0_100, mean_curve, std_curve).
    """
    segments, _, _ = auto_segment(
        angle, PROMINENCE, MIN_DISTANCE,
        cycle_from=f"halfcycle_{HALFCYCLE_DIRECTION}",
    )
    if not segments:
        raise RuntimeError("No se detectaron repeticiones con los parámetros de segmentación actuales.")

    x_norm = np.linspace(0, 100, 101)
    interp_reps = []
    for start, end in segments:
        seg = angle[start:end + 1]
        t_seg = np.linspace(0, 100, len(seg))
        interp_reps.append(np.interp(x_norm, t_seg, seg))

    mat  = np.vstack(interp_reps)
    mean = mat.mean(axis=0)
    std  = mat.std(axis=0, ddof=1) if mat.shape[0] > 1 else np.zeros(101)
    return x_norm, mean, std


# ══════════════════════════════════════════════════════════════════════════════
#  GRÁFICO
# ══════════════════════════════════════════════════════════════════════════════

def plot_timeseries(recordings: list[dict]) -> plt.Figure:
    """
    recordings: lista de dicts con keys 'path', 'label'.
    Dibuja una figura con las curvas superpuestas.
    """
    fig, ax = plt.subplots(figsize=(10, 4.5))
    fig.subplots_adjust(top=0.88)
    fig.suptitle(MOVEMENT_LABEL, fontsize=13, fontweight="bold")

    legend_handles = []

    for i, rec in enumerate(recordings):
        color = COLORS[i % len(COLORS)]
        print(f"  Leyendo: {rec['path']}")

        angle, fr = _extract_angle(rec["path"], VARIABLE_NAME, COMPONENT_INDEX, SIDE)

        if SHOW_MEAN_BAND:
            t, mean, std = _mean_band(angle)
            ax.plot(t, mean, color=color, linewidth=LINE_WIDTH + 0.3, alpha=ALPHA_RAW)
            ax.fill_between(t, mean - std, mean + std, color=color, alpha=ALPHA_BAND)
            n_reps = len(auto_segment(angle, PROMINENCE, MIN_DISTANCE,
                                       cycle_from=f"halfcycle_{HALFCYCLE_DIRECTION}")[0])
            lbl = f"{rec['label']}  (n={n_reps} reps)"
        else:
            t = _build_time_axis(len(angle), fr, NORMALIZE_TIME)
            ax.plot(t, angle, color=color, linewidth=LINE_WIDTH, alpha=ALPHA_RAW)
            lbl = rec["label"]

        legend_handles.append(
            mlines.Line2D([], [], color=color, linewidth=2.2, label=lbl)
        )

    # Eje X
    if SHOW_MEAN_BAND:
        ax.set_xlabel("Ciclo normalizado (%)", fontsize=10)
    elif NORMALIZE_TIME:
        ax.set_xlabel("Tiempo normalizado (%)", fontsize=10)
    else:
        ax.set_xlabel("Tiempo (s)", fontsize=10)

    ax.set_ylabel(Y_LABEL, fontsize=10)
    ax.legend(handles=legend_handles, fontsize=9, framealpha=0.7)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.yaxis.grid(True, linestyle="--", alpha=0.35, zorder=0)
    ax.margins(x=0.01)

    return fig


# ══════════════════════════════════════════════════════════════════════════════
#  MAIN
# ══════════════════════════════════════════════════════════════════════════════

def main() -> None:
    print(f"Variable : {_label_for_side(VARIABLE_NAME, SIDE)}  [componente {COMPONENT_INDEX}]")
    print(f"Modo     : {'media ± DE por rep' if SHOW_MEAN_BAND else 'señal cruda'}")

    fig = plot_timeseries(C3D_RECORDINGS)

    if OUTPUT_PATH:
        fig.savefig(OUTPUT_PATH, dpi=DPI, bbox_inches="tight")
        print(f"\nGuardado: {OUTPUT_PATH}")

    plt.show()


if __name__ == "__main__":
    main()
