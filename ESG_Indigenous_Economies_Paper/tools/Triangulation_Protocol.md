# Data Triangulation Protocol  
*(Ensuring reliable ESG indicator values when RTI responses are partial or delayed)*  

## 1. Purpose  
This protocol guarantees that every indicator in the scoring rubric has a **traceable, auditable value** even if primary RTI data are incomplete. It ranks fallback sources so reviewers can see exactly how each number was derived.

## 2. Hierarchy of Sources  

| Rank | Source Type | Typical Documents | Rationale |
|------|-------------|-------------------|-----------|
| **1** | **RTI Response** | MoTA, TRIFED, MoEFCC, MCA letters (PDF) | Primary, government‑certified data |
| **2** | **Official Public Report** | FSI *State of Forest Report*, TRIFED Annual Report, SEBI CSR database | Same ministry; already in public domain |
| **3** | **Peer‑Reviewed or Reputed NGO Study** | PRADAN livelihood surveys, ICFRE biodiversity studies | Independent validation with methodology |
| **4** | **Grey Literature / Media** | District newsletters, newspaper articles | Used only if 1–3 absent; flagged ‘LOW CONFIDENCE’ |

## 3. Step‑by‑Step Procedure  

1. **Check RTI tracker**  
   * If response received, use the exact figure.  
   * Record RTI ID in *Primary Source* column.

2. **No RTI yet?**  
   * Search the ministry’s most recent **official report**.  
   * Record report name + page in *Secondary Source* column.

3. **Still missing?**  
   * Look for a **peer‑reviewed article or reputable NGO publication**.  
   * Note DOI or report URL.

4. **Absolute last resort**  
   * Use grey literature; mark the data cell with suffix “_LC” (low confidence).  
   * Example: `E_ForestCover_LC = 73`.

5. **Document everything**  
   * Add a footnote to the rubric with: `Source Tier`, `Citation`, and retrieval date.

## 4. Quality Flags  

| Tag | Meaning | Action |
|-----|---------|--------|
| ✅ | Primary (RTI) | No action needed |
| ⚠️ | Secondary (official report) | Re‑check annually |
| 🟡 | Tertiary (peer‑review/NGO) | Plan RTI or field validation |
| 🔴 | Low Confidence (grey) | Highlight in limitations section |

## 5. Version Control  

* **Update frequency:** After every new RTI response.  
* **Git commit message:** `data: update indicator values – RTI2025-MoTA-01 received`  
* Store raw PDFs in `/data/raw/RTI/` with filenames `RTI2025-MoTA-01.pdf`, etc.

## 6. Audit Trail Checklist  

1. Can every indicator cell trace back to a file or URL?  
2. Are any ‘🔴’ values older than 12 months?  
3. Do fallback values change the model ranking materially (>5 points)? If yes, rerun optimisation and note change log.

---

**Maintainer:** Harsh Nair & Anushka Joshi  
**Last updated:** 2025-06-11  
