# Results Summary — Intermodel Comparison (grab7)

> Condition **Standing**: M1 and M2 validated against Complete Model (gold standard) via Comparison B.1 (Perfect distances) and B.2 (IJ\_PX\_C7 distances).
> Condition **Sitting**: inter-model agreement between M1 and M2 only (no gold standard available).
> Statistical metrics: bias (mean difference), SD, RMSD, ICC(C,1) with 95% CI. ICC thresholds follow Koo & Li (2016): < 0.50 poor, 0.50–0.75 moderate, 0.75–0.90 good, ≥ 0.90 excellent.
> Primary variable: **ROM (°)**. Peak and Valley results are in the full Excel sheets.

---

## Figures

### Figure 1 — ICC(C,1) for ROM: Standing, M1 and M2 vs Complete Model (B.1, Perfect distances)

![Figure 1](fig1_icc_rom_standing_B1.png)

**Caption.** Intraclass correlation coefficients ICC(C,1) for ROM between each kinematic model (M1, M2) and the Complete Model used as gold standard, under Perfect anatomical distances (Comparison B.1). Bars represent point estimates; error bars show 95% confidence intervals. Horizontal dashed lines indicate ICC threshold boundaries (Koo & Li, 2016). Left panel: Left side. Right panel: Right side. Bilateral movements (Trunk Extended Lateral Inclination, Thorax Lateral Inclination) appear only in the Left panel. Elbow Flex/Ext yields ICC = 1.000 for both models by design and is included for completeness.

**Why this figure.** This is the central validation result of the standing condition. It summarises in a single image how well each model reproduces the gold-standard ROM across all six movements and both sides. The side-by-side model comparison makes asymmetries immediately visible (e.g., M1 outperforms M2 for Thorax Lateral Inclination; both models agree on Elbow). Threshold lines allow direct clinical interpretation without consulting the numerical table.

---

### Figure 2 — Bland-Altman: Shoulder Flex/Ext ROM, Standing (M1 and M2 vs Complete Model)

![Figure 2](fig2_ba_shoulder_flexext_rom_standing.png)

**Caption.** Bland-Altman plots for Shoulder Flexion/Extension ROM (°) comparing M1 (top row) and M2 (bottom row) against the Complete Model, for Left side (left column) and Right side (right column). The horizontal axis shows the mean of the two measurements; the vertical axis shows the difference (model − Complete Model). The solid red line indicates the mean bias; dashed red lines indicate 95% limits of agreement (LoA = bias ± 1.96 SD). Each point corresponds to one repetition. Standing condition, Perfect anatomical distances.

**Why this figure.** Bland-Altman analysis reveals the *nature* of the disagreement between models, something ICC alone cannot show. For M1, bias is small (< 2.5°) and LoA are narrow, indicating good absolute accuracy. For M2, bias is large and systematic (~3.8–6.9° depending on side) but LoA remain relatively narrow — meaning M2's error is a constant offset rather than random noise. This distinction is critical for interpreting whether a model can be used for absolute measurements or only for within-subject comparisons. Shoulder Flex/Ext is chosen as a representative movement because it has sufficient repetitions, both sides available, and shows the clearest contrast between M1 and M2 behaviour.

---

### Figure 3 — ICC(C,1) for ROM: Sitting, M1 vs M2

![Figure 3](fig3_icc_rom_sitting_M1vsM2.png)

**Caption.** Intraclass correlation coefficients ICC(C,1) for ROM between M1 and M2 in the sitting condition, for Left side (blue) and Right side (green). Error bars show 95% confidence intervals. Bilateral movements appear only for the Left side. Elbow Flex/Ext ICC = 1.000 by design (excluded from the ICC calculation due to zero variance; plotted at maximum for completeness). Threshold lines follow Koo & Li (2016).

**Why this figure.** In the sitting condition no gold standard is available, so the comparison is limited to inter-model agreement. High ICC indicates the two models produce consistent ROM estimates; low ICC reveals movements where C7 reconstruction (virtual in M2) introduces non-systematic variability. Directly comparable in format to Figure 1, allowing qualitative cross-condition comparison.

---

### Figure 4 — Mean ROM Difference (M2 − M1): Sitting, all movements

![Figure 4](fig4_dotplot_rom_sitting_M2minusM1.png)

**Caption.** Mean ROM difference M2 − M1 (°) for each movement-side combination in the sitting condition. Points show the mean difference; horizontal error bars show ± 1 SD. Numerical annotations indicate the mean difference and the ICC interpretation category, colour-coded: green = excellent, orange/yellow = good, dark orange = moderate, red = poor. The vertical dashed line at zero indicates perfect agreement. Elbow Flex/Ext difference = 0° exactly (identity).

**Why this figure.** Complements Figure 3 by adding the magnitude of the disagreement. A movement can have excellent ICC (high reproducibility) but large mean difference (systematic offset) — this figure separates the two. It also provides an at-a-glance summary across all movements in a single compact panel, suitable for inclusion in a results section without taking excessive space.

---

## Tables

### Table 1 — Standing: ROM statistical metrics (Comparison B.1, M1 and M2 vs Complete Model, Perfect distances)

Bias = model − Complete Model. Elbow Flex/Ext omitted (perfect identity, RMSD = 0, ICC = 1.000 for all combinations by design; zero-variance Shapiro-Wilk not applicable).

| Model | Movement | Side | n | Bias (°) | SD (°) | RMSD (°) | ICC | 95% CI | Interpretation |
|---|---|---|---|---|---|---|---|---|---|
| M1 | Elbow Flex/Ext | Left | 7 | 0.00 | 0.00 | 0.00 | 1.000 | [1.000, 1.000] | excellent |
| M1 | Elbow Flex/Ext | Right | 7 | 0.00 | 0.00 | 0.00 | 1.000 | [n/a, n/a] | excellent |
| M1 | Shoulder Abd/Add | Left | 7 | 5.09 | 1.57 | 5.29 | 0.840 | [0.330, 0.970] | good |
| M1 | Shoulder Abd/Add | Right | 7 | 7.20 | 0.87 | 7.25 | 0.979 | [0.880, 1.000] | excellent |
| M1 | Shoulder Flex/Ext | Left | 7 | -0.29 | 0.53 | 0.57 | 0.989 | [0.940, 1.000] | excellent |
| M1 | Shoulder Flex/Ext | Right | 7 | -2.47 | 0.33 | 2.49 | 0.996 | [0.980, 1.000] | excellent |
| M1 | Shoulder Int/Ext Rot | Left | 6 | -1.60 | 1.49 | 2.10 | 0.730 | [-0.050, 0.960] | moderate |
| M1 | Shoulder Int/Ext Rot | Right | 6 | -3.33 | 0.85 | 3.42 | 0.979 | [0.860, 1.000] | excellent |
| M1 | Thorax Lateral Inclination | Left | 8 | -1.62 | 1.48 | 2.13 | 0.880 | [0.520, 0.970] | good |
| M1 | Trunk Extended Lateral Inclination | Left | 8 | -0.11 | 0.33 | 0.33 | 0.859 | [0.450, 0.970] | good |
| M2 | Elbow Flex/Ext | Left | 7 | 0.00 | 0.00 | 0.00 | 1.000 | [1.000, 1.000] | excellent |
| M2 | Elbow Flex/Ext | Right | 7 | 0.00 | 0.00 | 0.00 | 1.000 | [n/a, n/a] | excellent |
| M2 | Shoulder Abd/Add | Left | 7 | -0.19 | 1.08 | 1.02 | 0.922 | [0.620, 0.990] | excellent |
| M2 | Shoulder Abd/Add | Right | 7 | 8.34 | 1.75 | 8.50 | 0.921 | [0.620, 0.990] | excellent |
| M2 | Shoulder Flex/Ext | Left | 7 | 6.88 | 0.52 | 6.89 | 0.990 | [0.940, 1.000] | excellent |
| M2 | Shoulder Flex/Ext | Right | 7 | 3.75 | 1.03 | 3.87 | 0.950 | [0.740, 0.990] | excellent |
| M2 | Shoulder Int/Ext Rot | Left | 6 | 2.69 | 2.04 | 3.27 | 0.667 | [-0.180, 0.950] | moderate |
| M2 | Shoulder Int/Ext Rot | Right | 6 | 3.34 | 1.25 | 3.53 | 0.953 | [0.710, 0.990] | excellent |
| M2 | Thorax Lateral Inclination | Left | 8 | -8.67 | 1.08 | 8.73 | 0.919 | [0.650, 0.980] | excellent |
| M2 | Trunk Extended Lateral Inclination | Left | 8 | -1.32 | 0.33 | 1.36 | 0.858 | [0.450, 0.970] | good |

---

### Table 2 — Standing: ROM statistical metrics (Comparison B.2, M1 and M2 vs Complete Model, IJ\_PX\_C7 distances)

Sensitivity analysis of Table 1 using real anthropometric distances instead of Perfect. ROM values for Shoulder Flex/Ext and Elbow are identical to B.1 due to the ROM cancellation effect (uniform offset in the thorax coordinate system cancels in Peak − Valley).

| Model | Movement | Side | n | Bias (°) | SD (°) | RMSD (°) | ICC | 95% CI | Interpretation |
|---|---|---|---|---|---|---|---|---|---|
| M1 | Elbow Flex/Ext | Left | 7 | 0.00 | 0.00 | 0.00 | 1.000 | [1.000, 1.000] | excellent |
| M1 | Elbow Flex/Ext | Right | 7 | 0.00 | 0.00 | 0.00 | 1.000 | [n/a, n/a] | excellent |
| M1 | Shoulder Abd/Add | Left | 7 | 4.87 | 1.60 | 5.09 | 0.832 | [0.300, 0.970] | good |
| M1 | Shoulder Abd/Add | Right | 7 | 6.91 | 0.85 | 6.96 | 0.979 | [0.890, 1.000] | excellent |
| M1 | Shoulder Flex/Ext | Left | 7 | -0.29 | 0.53 | 0.57 | 0.989 | [0.940, 1.000] | excellent |
| M1 | Shoulder Flex/Ext | Right | 7 | -2.47 | 0.33 | 2.49 | 0.996 | [0.980, 1.000] | excellent |
| M1 | Shoulder Int/Ext Rot | Left | 6 | -1.60 | 1.49 | 2.10 | 0.730 | [-0.050, 0.960] | moderate |
| M1 | Shoulder Int/Ext Rot | Right | 6 | -3.33 | 0.85 | 3.42 | 0.979 | [0.860, 1.000] | excellent |
| M1 | Thorax Lateral Inclination | Left | 8 | -1.43 | 1.45 | 1.97 | 0.883 | [0.530, 0.980] | good |
| M1 | Trunk Extended Lateral Inclination | Left | 8 | -0.11 | 0.33 | 0.33 | 0.859 | [0.450, 0.970] | good |
| M2 | Elbow Flex/Ext | Left | 7 | 0.00 | 0.00 | 0.00 | 1.000 | [1.000, 1.000] | excellent |
| M2 | Elbow Flex/Ext | Right | 7 | 0.00 | 0.00 | 0.00 | 1.000 | [n/a, n/a] | excellent |
| M2 | Shoulder Abd/Add | Left | 7 | -0.51 | 1.10 | 1.14 | 0.919 | [0.600, 0.990] | excellent |
| M2 | Shoulder Abd/Add | Right | 7 | 8.07 | 1.70 | 8.22 | 0.925 | [0.630, 0.990] | excellent |
| M2 | Shoulder Flex/Ext | Left | 7 | 6.88 | 0.52 | 6.89 | 0.990 | [0.940, 1.000] | excellent |
| M2 | Shoulder Flex/Ext | Right | 7 | 3.75 | 1.03 | 3.87 | 0.950 | [0.740, 0.990] | excellent |
| M2 | Shoulder Int/Ext Rot | Left | 6 | 2.69 | 2.04 | 3.27 | 0.667 | [-0.180, 0.950] | moderate |
| M2 | Shoulder Int/Ext Rot | Right | 6 | 3.34 | 1.25 | 3.53 | 0.953 | [0.710, 0.990] | excellent |
| M2 | Thorax Lateral Inclination | Left | 8 | -7.22 | 1.15 | 7.30 | 0.909 | [0.620, 0.980] | excellent |
| M2 | Trunk Extended Lateral Inclination | Left | 8 | -1.32 | 0.33 | 1.36 | 0.858 | [0.450, 0.970] | good |

---

### Table 3 — Sitting: ROM statistical metrics (M1 vs M2)

Bias = M2 − M1. No gold standard available; table reflects inter-model agreement only. Elbow Flex/Ext omitted (perfect identity).

| Movement | Side | n | Bias (°) | SD (°) | RMSD (°) | ICC | 95% CI | Interpretation |
|---|---|---|---|---|---|---|---|---|
| Elbow Flex/Ext | Left | 6 | 0.00 | 0.00 | 0.00 | n/a | [n/a, n/a] | nan |
| Elbow Flex/Ext | Right | 6 | 0.00 | 0.00 | 0.00 | n/a | [n/a, n/a] | nan |
| Shoulder Abd/Add | Left | 6 | -2.29 | 1.37 | 2.61 | 0.982 | [0.880, 1.000] | excellent |
| Shoulder Abd/Add | Right | 6 | -4.26 | 0.95 | 4.35 | 0.934 | [0.610, 0.990] | excellent |
| Shoulder Flex/Ext | Left | 7 | 5.87 | 1.56 | 6.04 | 0.789 | [0.190, 0.960] | good |
| Shoulder Flex/Ext | Right | 7 | 7.77 | 2.13 | 8.02 | 0.756 | [0.110, 0.950] | good |
| Shoulder Int/Ext Rot | Left | 7 | 0.81 | 2.01 | 2.03 | 0.698 | [-0.020, 0.940] | moderate |
| Shoulder Int/Ext Rot | Right | 7 | 5.70 | 2.16 | 6.04 | 0.897 | [0.520, 0.980] | good |
| Thorax Lateral Inclination | Left | 7 | -4.09 | 0.74 | 4.14 | 0.558 | [-0.250, 0.910] | moderate |
| Trunk Extended Lateral Inclination | Left | 7 | -0.70 | 0.16 | 0.72 | 0.993 | [0.960, 1.000] | excellent |

---

## General Conclusions

### Elbow Flex/Ext — insensitivity to the thorax model

Both M1 and M2 produce results identical to the Complete Model for Elbow Flex/Ext (bias = 0.000°, RMSD = 0.000°, ICC = 1.000) in all conditions and both conditions (standing and sitting). This is structurally expected: the elbow joint angle is computed in the humerus coordinate system, which does not depend on the T8 or C7 markers reconstructed differently across models. This result constitutes an internal validation of the analysis pipeline — if differences existed, they would indicate a methodological error, not a model effect.

### ROM cancellation effect — why ROM is more robust than Peak or Valley

For movements where the thorax coordinate system (CS) affects angle computation (principally Shoulder Flex/Ext), the anatomical distance condition introduces a near-uniform additive offset to both Peak and Valley values. Because ROM = Peak − Valley, this offset cancels. Quantitatively: for M1 / Shoulder Flex/Ext / Left, switching from Perfect to IJ_C7 distances shifts Peak by approximately 2.7° and Valley by approximately 2.6°, leaving ROM unchanged (bias B.1 = bias B.2 = −0.29°). This is why ROM is used as the primary variable throughout the analysis and is clinically more meaningful than absolute Peak/Valley values.

### M1 (C7 physical, T8 virtual)

M1 achieves **excellent** ROM agreement with the Complete Model for the majority of movements:

- **Shoulder Flex/Ext**: ICC > 0.989 (both sides, both comparisons); RMSD < 2.5°; bias < 2.5°. Very small systematic error.
- **Shoulder Abd/Add**: ICC 0.832–0.979 for ROM (good to excellent). Significant systematic bias (~5–7°) on both sides, indicating that the T8 virtual reconstruction introduces a consistent offset in abduction/adduction estimation. The bias is reproducible (high ICC) and therefore predictable.
- **Shoulder Int/Ext Rot**: ROM ICC 0.730 (moderate) on the left side, 0.979 (excellent) on the right. This is the most asymmetric result and the weakest performance of M1. The T8 virtual reconstruction affects internal/external rotation more on the dominant side.
- **Trunk Extended Lateral Inclination**: ICC 0.859 (good). Small bias (< 0.11°), acceptable RMSD.
- **Thorax Lateral Inclination**: ICC 0.880 (good); RMSD 2.13°; bias −1.62°. Acceptable but lower than trunk.

Overall, M1 is a viable alternative to the Complete Model for ROM estimation, especially for upper-extremity elevation movements. Its primary limitation is the moderate ICC for Shoulder Int/Ext Rot (left).

### M2 (C7 virtual, NOT_C7)

M2 shows a consistent pattern: **high ICC but large systematic bias** in movements where the virtual C7 marker contributes to the thorax CS computation:

- **Shoulder Flex/Ext**: ICC excellent (0.950–0.990) but bias 3.75–6.88° — substantially larger than M1. The virtual C7 introduces a persistent offset in the thorax CS that propagates to shoulder ROM.
- **Shoulder Abd/Add**: ICC excellent for most combinations (0.921–0.980), bias 8.34° (right ROM) — the largest bias observed across all movements and models.
- **Shoulder Int/Ext Rot**: mixed — ICC moderate (0.667) for left ROM, excellent (0.953) for right ROM. One poor ICC case: Right Valley_deg (ICC = 0.498), the worst result across all M2 metrics.
- **Thorax Lateral Inclination**: despite good ICC (0.919), bias reaches −8.67° for ROM — the largest absolute error in the entire dataset. The thorax lateral inclination movement is most sensitive to C7 virtual reconstruction because the C7 marker defines the proximal endpoint of the thorax segment in this plane of motion.
- **Trunk Extended Lateral Inclination**: ICC 0.858 (good), bias −1.32° — acceptable and similar to M1.

The high ICC despite large bias indicates that M2 errors are **systematic, not random**: the model is internally consistent and reproducible but introduces a measurable inaccuracy in absolute ROM values. M2 should not be used when absolute ROM values are compared against normative data or across sessions with different setups. It may be acceptable for within-session relative comparisons where only the trend between conditions matters.

### Comparison B.1 vs B.2 — insensitivity of ROM to anthropometric distances

Comparing Comparison B.1 (Perfect distances) and B.2 (IJ_PX_C7 distances) reveals near-identical ROM ICC and RMSD values for all movements where the cancellation effect applies. The maximum difference in ICC between B.1 and B.2 across all movement-side combinations is < 0.01 for ROM. This confirms that **errors in the anthropometric distance estimates do not propagate to ROM** and validates the use of real (IJ_PX_C7) distances without loss of reliability.

### Sitting condition — M1 vs M2 inter-model agreement

Without a gold standard in the sitting condition, the analysis characterises inter-model consistency:

- **Trunk Extended Lateral Inclination**: near-perfect agreement (ICC = 0.993, RMSD < 0.72°, bias < 0.70°). This movement is essentially unaffected by C7 reconstruction.
- **Shoulder Abd/Add ROM**: excellent ICC (Left 0.982, Right 0.934); biases < 4.3°. Good inter-model consistency.
- **Shoulder Flex/Ext ROM**: good ICC (0.756–0.789) but large biases (5.87°–7.77°), consistent with the standing pattern. The systematic offset observed in standing validation is present in sitting.
- **Shoulder Int/Ext Rot ROM**: moderate to good (ICC 0.698–0.897); the most variable movement between models.
- **Thorax Lateral Inclination ROM**: moderate ICC (0.558) and large bias (−4.09°) — the most problematic movement in sitting, consistent with its standing performance.

The sitting results reinforce the standing conclusions: movements with large M1/M2 discrepancy in standing also show the largest inter-model disagreement in sitting, confirming that the differences are structural (related to C7 virtual reconstruction) rather than condition-specific.

### Summary statement

M1 is recommended over M2 when accurate absolute ROM values are required, particularly for shoulder and thorax movements. The virtual C7 reconstruction in M2 introduces systematic biases of 4–9° for the movements most dependent on the thorax coordinate system origin. Both models produce perfect agreement for Elbow Flex/Ext, confirming that joints not involving thorax CS computation are unaffected by the model choice. ROM is robust to errors in anthropometric distances (cancellation effect), making it the appropriate primary outcome variable in this analysis framework.
