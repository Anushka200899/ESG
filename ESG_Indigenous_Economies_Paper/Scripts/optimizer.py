#!/usr/bin/env python3
"""
run_optimizer.py  –  pick highest-scoring practices within budget.

Usage:
    python run_optimizer.py 40 100        # budgets: ₹40 L capital, 100 workers
    # if you omit numbers it defaults to 25, 80
"""

import sys
import itertools
import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOOLS = ROOT / "tools"

# ------- 1. load data -------------------------------------------------------
score_df = pd.read_excel(TOOLS / "ESG_Scoring_Rubric.xlsx",
                         sheet_name=0, usecols="A:G")  # assumes a tidy sheet
cost_df  = pd.read_excel(TOOLS / "TRI_ESG_Cost_Input_Template.xlsx")

# Merge on Practice name
df = cost_df.merge(score_df, left_on="Practice", right_on="Indicator")
# If your rubric uses different sheet structure, adjust merge keys.

# Pick the MODE columns for capital & labour
df["Capital"] = df["Capital_Mode"]
df["Labor"]   = df["Labor_Mode"]

# Compute composite M_i
w_E, w_S, w_G = 0.40, 0.35, 0.25   # <- replace with AHP weights
df["M_i"] = (w_E*df["E_i"] + w_S*df["S_i"] + w_G*df["G_i"]).round(2)

# ------- 2. budgets from CLI ------------------------------------------------
try:
    CAP_BUDGET = float(sys.argv[1])
    LAB_BUDGET = float(sys.argv[2])
except (IndexError, ValueError):
    CAP_BUDGET, LAB_BUDGET = 25, 80  # default

# ------- 3. brute-force select best combo ----------------------------------
best_score, best_combo = 0, []
for r in range(1, len(df)+1):
    for idxs in itertools.combinations(df.index, r):
        sub = df.loc[list(idxs)]
        if sub["Capital"].sum() <= CAP_BUDGET and sub["Labor"].sum() <= LAB_BUDGET:
            total = sub["M_i"].sum()
            if total > best_score:
                best_score, best_combo = total, idxs

df["Selected"] = 0
df.loc[list(best_combo), "Selected"] = 1

# ------- 4. print results ---------------------------------------------------
print(f"\nBudget: ₹{CAP_BUDGET} L  |  {LAB_BUDGET} workers")
print(df[["Practice", "M_i", "Capital", "Labor", "Selected"]])
print(f"\nTOTAL SCORE: {best_score}")
print(f"TOTAL CAPITAL: {df.loc[best_combo,'Capital'].sum()}  |  "
      f"TOTAL LABOUR: {df.loc[best_combo,'Labor'].sum()}")
