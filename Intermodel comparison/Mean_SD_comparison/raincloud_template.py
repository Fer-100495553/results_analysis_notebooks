"""
raincloud_template.py
---------------------
Template para generar raincloud plots de ROM a partir de archivos .c3d
de grabaciones continuas unilaterales o bilaterales (SULM / Vicon Nexus).

Flujo:
  1. Leer uno o varios C3D.
  2. Extraer la curva angular del label SULM deseado (por lado si bilateral).
  3. Segmentar repeticiones automáticamente (peaks/valleys) o por eventos.
  4. Calcular estadísticas por rep (ROM, peak, valley).
  5. Generar raincloud plot y guardarlo / mostrarlo.

Requisitos:
    pip install ezc3d numpy scipy matplotlib

Ejecución:
    python raincloud_template.py

_________________________________________________________________________________
Estructura del template
Sección CONFIG (única parte que hay que tocar para cada caso):

C3D_FILES — uno o varios archivos; si hay varios, sus repeticiones se acumulan en una sola distribución
VARIABLE_NAME — label SULM sin prefijo de lado ("HumerothoracicAngles", "ElbowAngles", etc.)
COMPONENT_INDEX — 0=X, 1=Y, 2=Z según el componente Euler que interese
SIDES — ["Left", "Right"] bilateral, ["Left"] o ["Right"] unilateral, ["—"] si el label no tiene prefijo
Parámetros de segmentación (prominence, min_distance, dirección del semiciclo)
Flujo interno:

Reutiliza read_c3d() y compute_extended_stats_array() del proyecto directamente
Segmenta con auto_segment() (misma lógica que la app)
Dibuja con matplotlib.pyplot (no el backend GUI), así funciona standalone con plt.show() y fig.savefig()
Salida: 3 subgráficas side-by-side — ROM · Máximo · Mínimo — misma estética que la app (rojo izquierda, verde derecha).
"""
from __future__ import annotations

import sys
import os
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Rectangle
from scipy.stats import gaussian_kde

# ── Importar funciones del proyecto (mismo directorio) ────────────────────
# Si este script está fuera de ROM_analyzer, ajusta esta ruta:
sys.path.insert(0, str(Path(__file__).parent))
from data_processing import read_c3d, compute_extended_stats_array
from segmentation import auto_segment


# ══════════════════════════════════════════════════════════════════════════
#  CONFIGURACIÓN  ← editar aquí para cada caso concreto
# ══════════════════════════════════════════════════════════════════════════

# -- Archivos C3D ----------------------------------------------------------
# Un solo archivo → lista con un elemento.
# Varios archivos → se combinan todas las reps en una sola distribución.
C3D_FILES: list[str] = [
    r"C:\ruta\al\archivo1.c3d",
    # r"C:\ruta\al\archivo2.c3d",
]

# -- Variable SULM a analizar ----------------------------------------------
# Nombre del label tal como aparece en el C3D, SIN prefijo de lado.
# Ejemplos: "HumerothoracicAngles", "ElbowAngles", "LThoraxAngles"
VARIABLE_NAME = "HumerothoracicAngles"

# Componente Euler: 0 = X (Rot1), 1 = Y (Rot2), 2 = Z (Rot3)
COMPONENT_INDEX = 0

# -- Lados -----------------------------------------------------------------
# Unilateral: ["Left"] o ["Right"]
# Bilateral:  ["Left", "Right"]
# Si el label no tiene prefijo de lado (ej. "ThoraxAngles"): ["—"]
SIDES: list[str] = ["Left", "Right"]

# -- Segmentación ----------------------------------------------------------
# Prominencia mínima de pico/valle (°). Aumentar si detecta demasiados.
PROMINENCE = 15.0
# Distancia mínima entre picos consecutivos (frames).
MIN_DISTANCE = 60
# Dirección del semiciclo: "peak_to_valley" o "valley_to_peak"
HALFCYCLE_DIRECTION = "peak_to_valley"

# -- Salida ----------------------------------------------------------------
MOVEMENT_LABEL = "Humerothoracic — Plano de elevación"  # título del plot
OUTPUT_PATH = "raincloud_output.png"                     # None → solo muestra
DPI = 150

# ══════════════════════════════════════════════════════════════════════════


# ── Paleta (igual que la app) ─────────────────────────────────────────────
_COLOR      = {"Left": "#E74C3C", "Right": "#2ECC71", "—": "#4A90D9"}
_COLOR_DARK = {"Left": "#922B21", "Right": "#1A7A3C", "—": "#1A5276"}

_V_AMP  = 0.30   # semi-ancho máximo del violín (unidades x)
_BW     = 0.035  # semi-ancho del boxplot
_SC_OFF = 0.10   # offset del scatter respecto al centro
_SC_JIT = 0.03   # magnitud del jitter


# ══════════════════════════════════════════════════════════════════════════
#  LECTURA Y PROCESAMIENTO
# ══════════════════════════════════════════════════════════════════════════

def _label_for_side(variable: str, side: str) -> str:
    """Construye el label completo añadiendo prefijo de lado si corresponde."""
    if side == "—":
        return variable
    return side + variable   # ej. "Left" + "HumerothoracicAngles"


def load_and_segment(
    c3d_files: list[str],
    variable: str,
    component: int,
    side: str,
    prominence: float,
    min_distance: int,
    direction: str,
) -> dict:
    """
    Lee todos los C3D, extrae la curva angular para un lado y segmenta.

    Devuelve un dict con:
        {
            "extended": {"rom": {...}, "peak": {...}, "valley": {...}},
            "angle_data": np.ndarray,   # curva completa del último archivo
            "frame_rate": int,
        }
    """
    all_roms:    list[float] = []
    all_peaks:   list[float] = []
    all_valleys: list[float] = []
    last_angle:  np.ndarray | None = None
    last_fr:     int = 100

    for path in c3d_files:
        print(f"  Leyendo: {path}")
        c3d = read_c3d(path)
        fr  = c3d["frame_rate"]
        last_fr = fr

        label = _label_for_side(variable, side)
        mo = c3d["model_outputs"]

        if label not in mo:
            available = [k for k in mo if variable in k or side in k]
            raise KeyError(
                f"Label '{label}' no encontrado en {Path(path).name}.\n"
                f"Labels con coincidencia parcial: {available}\n"
                f"Todos los labels: {list(mo.keys())}"
            )

        angle = mo[label][component, :].astype(float)
        last_angle = angle

        cycle_from = f"halfcycle_{direction}"
        segments, _, _ = auto_segment(angle, prominence, min_distance,
                                       cycle_from=cycle_from)

        if not segments:
            print(f"    AVISO: sin segmentos detectados en {Path(path).name}")
            continue

        stats = compute_extended_stats_array(angle, segments)
        all_roms    += stats["rom"]["values"]
        all_peaks   += stats["peak"]["values"]
        all_valleys += stats["valley"]["values"]

    def _agg(values: list[float]) -> dict:
        valid = np.array([v for v in values if not np.isnan(v)])
        return {
            "values": values,
            "mean": float(np.mean(valid))        if valid.size > 0 else float("nan"),
            "sd":   float(np.std(valid, ddof=1)) if valid.size > 1 else 0.0,
            "min":  float(np.min(valid))          if valid.size > 0 else float("nan"),
            "max":  float(np.max(valid))          if valid.size > 0 else float("nan"),
        }

    return {
        "extended": {
            "rom":    _agg(all_roms),
            "peak":   _agg(all_peaks),
            "valley": _agg(all_valleys),
        },
        "angle_data": last_angle,
        "frame_rate": last_fr,
    }


# ══════════════════════════════════════════════════════════════════════════
#  RAINCLOUD PLOT
# ══════════════════════════════════════════════════════════════════════════

def _draw_raincloud_series(
    ax: plt.Axes,
    vals: np.ndarray,
    x_c: float,
    color: str,
    color_dark: str,
    rng: np.random.Generator,
) -> None:
    """Dibuja violín (izq) + boxplot (centro) + scatter jittered (der)."""
    if vals.size == 0:
        return

    # 1. Semi-violín a la izquierda de x_c
    if vals.size >= 2:
        kde     = gaussian_kde(vals, bw_method="scott")
        spread  = max(float(vals.std()) * 0.5, 0.5)
        y_grid  = np.linspace(vals.min() - spread, vals.max() + spread, 300)
        density = kde(y_grid)
        peak_d  = density.max()
        if peak_d > 0:
            kde_x = x_c - (density / peak_d) * _V_AMP
            ax.fill_betweenx(y_grid, kde_x, x_c,
                             color=color, alpha=0.40, zorder=2)
            ax.plot(kde_x, y_grid, color=color, alpha=0.70,
                    linewidth=1.0, zorder=3)

    # 2. Boxplot vertical
    q1, q2, q3 = np.percentile(vals, [25, 50, 75])
    iqr      = q3 - q1
    fence_lo = q1 - 1.5 * iqr
    fence_hi = q3 + 1.5 * iqr
    w_lo = vals[vals >= fence_lo].min() if np.any(vals >= fence_lo) else q1
    w_hi = vals[vals <= fence_hi].max() if np.any(vals <= fence_hi) else q3

    ax.plot([x_c, x_c], [w_lo, q1], color=color, lw=1.2, zorder=4)
    ax.plot([x_c, x_c], [q3, w_hi], color=color, lw=1.2, zorder=4)
    for wy in (w_lo, w_hi):
        ax.plot([x_c - _BW, x_c + _BW], [wy, wy], color=color, lw=1.2, zorder=4)
    ax.add_patch(Rectangle(
        (x_c - _BW, q1), 2 * _BW, q3 - q1,
        facecolor="white", edgecolor=color, linewidth=1.5, zorder=5,
    ))
    ax.plot([x_c - _BW, x_c + _BW], [q2, q2], color=color, lw=2.0, zorder=6)

    mean_val = float(vals.mean())
    ax.text(x_c, w_hi, f"{mean_val:.1f}°",
            ha="center", va="bottom", fontsize=10,
            fontweight="bold", color=color_dark, zorder=7)

    outliers = vals[(vals < w_lo) | (vals > w_hi)]
    if outliers.size:
        ax.scatter(np.full(outliers.size, x_c), outliers,
                   color=color, s=25, marker="D", alpha=0.85, zorder=7)

    # 3. Scatter jittered a la derecha
    jitter = rng.uniform(-_SC_JIT, _SC_JIT, size=vals.size)
    ax.scatter(x_c + _SC_OFF + jitter, vals,
               color=color, s=35, alpha=0.85, zorder=3,
               edgecolors=color_dark, linewidths=0.4)


def plot_raincloud(
    sides_data: dict[str, dict],
    title: str,
) -> plt.Figure:
    """
    Genera el raincloud plot con 3 subgráficas (ROM / Máximo / Mínimo).

    Args:
        sides_data: {side_label: result_dict}
                    result_dict es el retornado por load_and_segment().
        title:      Título superior de la figura.

    Returns:
        matplotlib Figure.
    """
    METRICS = [
        ("rom",    "ROM (°)"),
        ("peak",   "Máximo (°)"),
        ("valley", "Mínimo (°)"),
    ]

    n_sides = len(sides_data)
    rng = np.random.default_rng(42)

    fig, axes = plt.subplots(1, 3, figsize=(10, 5))
    fig.subplots_adjust(wspace=0.38, top=0.82)
    fig.suptitle(title, fontsize=13, fontweight="bold")

    # Posiciones x: bilateral → izq/der; unilateral → centrado
    side_positions: dict[str, float] = {}
    side_list = list(sides_data.keys())
    if n_sides == 1:
        side_positions[side_list[0]] = 0.0
    else:
        for i, s in enumerate(side_list):
            side_positions[s] = -0.22 if i == 0 else 0.22

    for m_idx, (metric_key, metric_label) in enumerate(METRICS):
        ax = axes[m_idx]
        ax.set_title(metric_label, fontsize=10, fontweight="bold")

        x_ticks: list[float] = []
        x_tick_labels: list[str] = []

        for side, result in sides_data.items():
            raw = result["extended"].get(metric_key, {}).get("values", [])
            vals = np.array(
                [v for v in raw if v is not None and not np.isnan(float(v))],
                dtype=float,
            )
            if vals.size == 0:
                continue

            x_c        = side_positions[side]
            color      = _COLOR.get(side, "#4A90D9")
            color_dark = _COLOR_DARK.get(side, "#1A5276")

            _draw_raincloud_series(ax, vals, x_c, color, color_dark, rng)
            x_ticks.append(x_c)
            x_tick_labels.append(side)

        if x_ticks:
            ax.set_xticks(x_ticks)
            ax.set_xticklabels(x_tick_labels, fontsize=9)

        ax.set_xlim(-0.65, 0.65)
        ax.tick_params(axis="x", length=0)
        ax.margins(y=0.2)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.yaxis.grid(True, linestyle="--", alpha=0.4, zorder=0)

    # Leyenda si bilateral
    if n_sides > 1:
        handles = [
            mpatches.Patch(facecolor=_COLOR.get(s, "#4A90D9"), label=s)
            for s in sides_data
        ]
        axes[2].legend(handles=handles, fontsize=8, loc="upper right")

    return fig


# ══════════════════════════════════════════════════════════════════════════
#  MAIN
# ══════════════════════════════════════════════════════════════════════════

def main() -> None:
    sides_data: dict[str, dict] = {}

    for side in SIDES:
        print(f"\nProcesando lado: {side}")
        result = load_and_segment(
            c3d_files    = C3D_FILES,
            variable     = VARIABLE_NAME,
            component    = COMPONENT_INDEX,
            side         = side,
            prominence   = PROMINENCE,
            min_distance = MIN_DISTANCE,
            direction    = HALFCYCLE_DIRECTION,
        )
        sides_data[side] = result

        ext = result["extended"]
        for metric in ("rom", "peak", "valley"):
            m = ext[metric]
            n = len([v for v in m["values"] if not np.isnan(v)])
            print(f"  {metric:7s}: n={n}  mean={m['mean']:.1f}°  "
                  f"sd={m['sd']:.1f}°  "
                  f"[{m['min']:.1f}° – {m['max']:.1f}°]")

    fig = plot_raincloud(sides_data, title=MOVEMENT_LABEL)

    if OUTPUT_PATH:
        fig.savefig(OUTPUT_PATH, dpi=DPI, bbox_inches="tight")
        print(f"\nGuardado: {OUTPUT_PATH}")

    plt.show()


if __name__ == "__main__":
    main()
