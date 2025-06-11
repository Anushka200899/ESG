# ESG Indigenous Economies – TRI‑ESG Model Repository  
_A complete, reproducible package for the paper  
“ESG Investing and Indigenous Economies: A Path to Ethical and Scalable Development.”_

---

## 📚  What This Repo Is For
* Turn **tribal practices** (Mahua harvesting, bamboo crafts, etc.) into **ESG scores**.  
* Pick the **best mix** of practices under **capital & labour budgets**.  
* Use only **desk research + RTI replies** (no expensive fieldwork).  
* Everything here is open-source, version-controlled, and traceable for reviewers.

---

## 🗂️  Folder Guide

| Path | What you’ll find | Why it matters |
|------|------------------|----------------|
| **tools/** | **All Excel & helper templates**<br>• `ESG_Scoring_Rubric.xlsx` – fill indicator values  <br>• `AHP_weight_template.xlsx` – derive E/S/G weights  <br>• `TRI_ESG_Cost_Input_Template.xlsx` – capital & labour ranges  <br>• `Governance_Proxy_Table.xlsx` – measurable G proxies | Edit these first; the model reads them directly. |
| **03_RTI_Tracking/** | `Filed_RTIs_Final_Format.xlsx` + `Responses/` | Track every RTI question + paste replies. |
| **02_Model_Design/** | `Math_Model.md` (equations) & `Variables_List.xlsx` | The math spec and variable glossary. |
| **docs/** | Narrative appendices: <br>• `Triangulation_Protocol.md`  <br>• `Field_Validation_Plan.md`  <br>• `portability_note.md`  <br>• `scalability_externalities.md` | Copy-paste these into the manuscript’s appendix. |
| **scripts/** | `run_optimizer.py` (tiny knapsack engine) | Calculates the best set of practices under your budgets. |
| **data/** (you create) | `raw/RTI/` (PDFs) → `processed/` (clean CSV) | Keeps raw vs cleaned data separate. |
| **README.md** | You’re here! | Always 😄 |

---

## 🚀 Quick‑Start (Reproduce the Model)

```bash
git clone <repo‑url>
cd ESG_Indigenous_Economies_Paper
# 1. Fill missing values
open tools/ESG_Scoring_Rubric.xlsx          # add indicator data
open tools/TRI_ESG_Cost_Input_Template.xlsx # add capital & labour ranges
# 2. Derive weights (optional)
open tools/AHP_weight_template.xlsx         # type three pairwise values
# 3. Run optimisation
python scripts/run_optimizer.py 40 100      # budgets: ₹40 L & 100 workers
```

---

## 🔄  Updating with New RTI Responses

1. Save each PDF reply in `data/raw/RTI/` using the naming convention `RTI2025-MoTA-01.pdf`.  
2. Log the response date in `03_RTI_Tracking/Filed_RTIs_Final_Format.xlsx`.  
3. Pull indicator numbers into `tools/ESG_Scoring_Rubric.xlsx`.  
4. Re‑run the optimiser; commit changes with message:  
   ```
   data: update indicators – RTI2025-MoTA-01 incorporated
   ```

---

## 🗺️ Field Validation Workflow

1. Follow `docs/Field_Validation_Plan.md`.  
2. Store photos & audio in `data/field/<practice>/`.  
3. Update `Field_Validation_Log.xlsx`; flag “Validated”.  
4. Rerun optimisation if any indicator deviates >10 %.

---

## 🛠️ Customising Further

* **More practices?**  Add rows in both cost template & rubric, re-run.  
* **Different budgets?**  Pass new numbers to `run_optimizer.py`.  
* **Sensitivity analysis?**  Duplicate the script, loop over budget/weight ranges, store CSV outputs.  

---

## 📑  Citation

> Nair, H. & Joshi, A. (2025). *ESG Investing and Indigenous Economies: A Path to Ethical and Scalable Development.* Working Paper.  

MIT‑style License © 2025.

_Last updated: 2025‑06‑11_
