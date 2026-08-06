# Real Content Progress

Tracking conversion of the 2,816 boilerplate chapters in `medical_topics.tex` to real, cited medical content.

**Total chapters:** 2,663 (after two dedup passes) · **Completed:** 181 · **Remaining (under review):** 2,482

Progress is also measurable automatically: real chapters are those whose files do **not** contain the boilerplate sentence `is a medical condition that requires proper diagnosis`.

## Batch 1 — Pilot (10 chapters, research-backed)
anaphylaxis, heart_attack, sepsis, stroke, appendicitis, melanoma, depression, meningitis, opioid_overdose, suicide_prevention

## Batch 2 — High-priority common conditions (22 chapters)
asthma, covid_19, flu_influenza, pneumonia, bronchitis, copd, diabetes_type_2, diabetes_type_1, hypertension, high_cholesterol, epilepsy, migraine, anxiety, schizophrenia, bipolar_disorder, osteoarthritis, rheumatoid_arthritis, osteoporosis, kidney_stones, urinary_tract_infection_uti, tuberculosis_tb, hepatitis_b

## Batch 3+ — additional converted chapters (100 chapters, 2026-08-05/06)
acne, ocd, ptsd, eating_disorders, carpal_tunnel_syndrome, chronic_kidney_disease, rsv, sepsis, stroke, melanoma, suicide_prevention, gout, dvt, spinal_cord_injury, and ~88 more (see the master include list for the full set; real chapters are those whose files lack the boilerplate sentence)

## Batch 4 — 40 chapters converted 2026-08-06 (research-verified, curl-checked)
allergic_rhinitis_hay_fever, allergies, asthma_attack_management, asthma_medication, asthma_treatment, altitude_sickness, asbestosis, aspergillosis, abdominal_pain, abscesses, achalasia, anal_fissure, bad_breath, bloating, bowel_cancer, botulism, acoustic_neuroma, agoraphobia, als, amnesia, anosmia_loss_of_smell, bells_palsy, blackouts, blepharospasm, aortic_aneurysm, aortic_dissection, aortic_stenosis, arrhythmia, blood_clots, blood_pressure_low, blood_thinners, heart_murmur, acne_treatments, boils, basal_cell_carcinoma, blepharitis, blisters, benign_tumours, bites_and_stings, balanitis_and_balanoposthitis
(All 144 cited URLs verified HTTP 200; every `\cite` resolves to a `\bibitem`; built cleanly: 0 errors / 0 undefined / 0 warnings.)

## Batch 5 — 6 cardiovascular/metabolic chapters converted 2026-08-06
pre_diabetes, gestational_diabetes, diabetes_medicines, blood_pressure_medicines, triglycerides, cholesterol_what_is
(All cited URLs verified; every `\cite` resolves to a `\bibitem`; built cleanly.)

## Batch 6 — 3 common conditions converted 2026-08-06
a_guide_to_menopause, abdominal_aortic_aneurysm, abdominal_pain_in_children
(All cited URLs verified; every `\cite` resolves to a `\bibitem`; built cleanly.)

## Chapter conventions (per batch)
- Structure: Definition · What Is Happening in Your Body · Common Causes/Triggers · Symptoms · When to Seek Medical Care (red flags + 000) · Diagnosis · Treatment Options · Prevention and Self-Care · Prognosis · References
- In-text `\cite{}` markers resolving to a per-chapter `thebibliography` of real, specific pages (healthdirect, NHS, WHO fact sheets, CDC, Cancer Council AU, Heart Foundation, etc.) with access dates
- Australian context (000, GP, National Immunisation Program) consistent with the book's other content
- Every cited URL is link-checked (curl); unverifiable links are replaced or dropped
- Validated by compiling all completed chapters in a test harness (0 errors, 0 undefined citations)

## Known issues tracked separately
- 115 boilerplate duplicates removed 2026-08-06 (2,816 → 2,701), then a further 35 duplicate pairs removed (2,701 → 2,666), keeping the REAL/natural-phrasing chapter in each pair. The two fabricated glossary chapter files were deleted (2,666 → 2,663). All 150 removed slugs are listed in `removed_slugs.txt` so `create_master.py` never reintroduces them.
- All 1,748+4 mangled boilerplate titles fixed to clean `topics.txt` titles (2026-08-06); fabricated References blocks (`Mayo/NIH/CDC/WHO` homepages) stripped from 2,683 boilerplate chapters and replaced with a `\section*{Under Review}` marker.
- Generation scripts (`generate_chapters.py`, `generate_500_chapters.py`) patched so any regeneration uses clean `topics.txt` titles, clean slugs, and the Under Review marker instead of fabricated references. `create_master.py` now regenerates `medical_topics.tex` in place, preserving the curated include list and index entries.
- `.gov.au` (health.gov.au, immunisationhandbook) unreachable from this network via curl — cited only when verifiable, otherwise omitted
