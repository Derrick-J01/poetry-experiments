"""Compare the poetry-ranking variants against the baseline submission F.

Usage (from this directory):  python compare_submissions.py
Needs: pandas, scipy
"""
import pandas as pd
from scipy.stats import spearmanr

base = pd.read_csv("submissions/submission_F.csv").set_index("id")["label"]

print(f"{'variant':<22}{'rows':>6}{'changed':>9}{'max |diff|':>12}{'spearman (changed rows)':>26}")
for name in ["submission_F_style", "submission_F_raidar"]:
    v = pd.read_csv(f"submissions/{name}.csv").set_index("id")["label"]
    assert (v.index == base.index).all(), "id mismatch"
    changed = (v != base)
    diff = (v - base).abs()
    rho = spearmanr(base[changed], v[changed])[0] if changed.any() else float("nan")
    print(f"{name:<22}{len(v):>6}{changed.sum():>9}{diff.max():>12.5f}{rho:>26.4f}")
