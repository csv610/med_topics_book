#!/usr/bin/env python3
"""Generate real medical content for more T-Z chapter tex files."""

import os

chapters_dir = "/Users/csv610/Projects/MyBooks/Medical/MedTopics/chapters"

CHAPTERS = {
    "tapeworm": """\\chapter{Tapeworm}

\\section{Overview}
Tapeworms are parasitic flatworms that live in the intestines of humans and animals. Infection occurs through consumption of contaminated food or water. Most tapeworm infections are treatable and not life-threatening.

\\section{Symptoms}
\\begin{itemize}
    \\item Passing tapeworm segments in stool
    \\item Nausea and weakness
    \\item Diarrhea
    \\item Abdominal pain
    \\item Unexplained weight loss
    \\item Vitamin B12 deficiency
    \\item Appetite changes
\\end{itemize}

Some infections are asymptomatic.

\\section{Causes}
Tapeworms are transmitted through:
\\begin{itemize}
    \\item Undercooked pork (Taenia solium)
    \\item Undercooked beef (Taenia saginata)
    \\item Contaminated water (Diphyllobothrium)
    \\item Poor hygiene and sanitation
\\end{itemize}

\\section{Diagnosis}
\\begin{itemize}
    \\item Stool examination for eggs or segments
    \\item Blood tests for antibodies
    \\item Imaging for complications (cysticercosis)
\\end{itemize}

\\section{Treatment}
\\begin{itemize}
    \\item Praziquantel (first-line)
    \\item Albendazole
    \\item Niclosamide
\\end{itemize}

\\section{Prevention}
\\begin{itemize}
    \\item Cook meat thoroughly
    \\item Freeze meat before consumption
    \\item Wash fruits and vegetables
    \\item Practice good hygiene
    \\item Avoid contaminated water
\\end{itemize}

\\section{When to Seek Medical Care}
Seek care for:
\\begin{itemize}
    \\item Visible worm segments in stool
    \\item Persistent abdominal pain
    \\item Neurological symptoms (possible cysticercosis)
    \\item Seizures or headaches
\\end{itemize}
""",

    "tay_sachs_disease": """\\chapter{Tay-Sachs Disease}

\\section{Overview}
Tay-Sachs disease is a rare inherited disorder that destroys nerve cells in the brain and spinal cord. It is caused by a deficiency of the enzyme hexosaminidase A, leading to accumulation of fatty substances in brain tissue. The disease is most common in people of Ashkenazi Jewish descent.

\\section{Symptoms}
Infantile form (most common):
\\begin{itemize}
    \\item Loss of developmental milestones
    \\item Weakness and muscle wasting
    \\item Cherry-red spot on retina
    \\item Seizures
    \\item Hearing loss
    \\item Blindness
    \\item Increased startle response
\\end{itemize}

Symptoms typically appear around 3-6 months of age.

\\section{Causes}
Autosomal recessive inheritance. Both parents must carry the defective gene. Mutation in the HEXA gene on chromosome 15.

\\section{Diagnosis}
\\begin{itemize}
    \\item Enzyme assay (low hexosaminidase A)
    \\item Genetic testing
    \\item Newborn screening
    \\item Prenatal testing (amniocentesis)
    \\item MRI of brain
\\end{itemize}

\\section{Treatment}
No cure exists. Treatment is supportive:
\\begin{itemize}
    \\item Seizure management
    \\item Physical therapy
    \\item Nutritional support
    \\item Palliative care
\\end{itemize}

\\section{Prevention}
\\begin{itemize}
    \\item Genetic screening before pregnancy
    \\item Carrier testing
    \\item Prenatal diagnosis
    \\item Preimplantation genetic diagnosis
\\end{itemize}

\\section{When to Seek Medical Care}
Seek care for developmental delays, seizures, or if both parents are carriers.
""",

    "tardive_dyskinesia": """\\chapter{Tardive Dyskinesia}

\\section{Overview}
Tardive dyskinesia (TD) is a neurological disorder characterized by involuntary, repetitive body movements. It is typically caused by long-term use of dopamine-blocking medications, particularly antipsychotics.

\\section{Symptoms}
\\begin{itemize}
    \\item Facial grimacing
    \\item Tongue protrusion
    \\item Puckering of lips
    \\item Rapid eye blinking
    \\item Smacking or popping sounds
    \\item Involuntary arm and leg movements
    \\item Choreoathetoid movements
\\end{itemize}

\\section{Causes}
\\begin{itemize}
    \\item Long-term antipsychotic use
    \\item Antiemetic medications (metoclopramide)
    \\item Dopamine receptor hypersensitivity
    \\item Older age
    \\item Longer duration of treatment
\\end{itemize}

\\section{Diagnosis}
\\begin{itemize}
    \\item Clinical assessment using AIMS scale
    \\item History of medication use
    \\item Exclusion of other movement disorders
\\end{itemize}

\\section{Treatment}
\\begin{itemize}
    \\item Discontinue or reduce offending medication
    \\item VMAT2 inhibitors (valbenazine, deutetrabenazine)
    \\item Switch to clozapine or quetiapine
    \\item Benztropine (may worsen symptoms)
\\end{itemize}

\\section{Prevention}
\\begin{itemize}
    \\item Use lowest effective dose
    \\item Regular monitoring with AIMS
    \\item Prefer second-generation antipsychotics
    \\item Limit duration of therapy
\\end{itemize}

\\section{When to Seek Medical Care}
Seek care for involuntary movements, especially if taking antipsychotics or antiemetics.
""",

    "tampon_retained": """\\chapter{Retained Tampon}

\\section{Overview}
A retained tampon occurs when a tampon is left in the vagina longer than recommended. This can lead to infection and toxic shock syndrome (TSS), a rare but potentially fatal condition.

\\section{Symptoms}
\\begin{itemize}
    \\item Foul-smelling vaginal discharge
    \\item Vaginal irritation
    \\item Fever
    \\item Rash (especially on palms and soles)
    \\item Low blood pressure
    \\item Nausea and vomiting
    \\item Diarrhea
    \\item Muscle aches
\\end{itemize}

\\section{Causes}
\\begin{itemize}
    \\item Forgetting to remove tampon
    \\item Using super-absorbent tampons
    \\item Leaving tampon in for more than 8 hours
    \\item Menstrual irregularities
\\end{itemize}

\\section{Diagnosis}
\\begin{itemize}
    \\item Pelvic examination
    \\item Culture of vaginal discharge
    \\item Blood tests for infection
    \\item Toxin detection (rarely needed)
\\end{itemize}

\\section{Treatment}
\\begin{itemize}
    \\item Remove tampon immediately
    \\item Antibiotics for infection
    \\item Hospitalization for TSS
    \\item IV fluids
    \\item Supportive care
\\end{itemize}

\\section{Prevention}
\\begin{itemize}
    \\item Change tampons every 4-8 hours
    \\item Use lowest absorbency needed
    \\item Alternate with pads
    \\item Set phone reminder if prone to forgetting
\\end{itemize}

\\section{When to Seek Medical Care}
Seek immediate care for fever, rash, dizziness, or signs of TSS after tampon use.
""",

    "tapentadol": """\\chapter{Tapentadol}

\\section{Overview}
Tapentadol is an opioid pain medication used for moderate to severe pain. It has a dual mechanism: mu-opioid receptor agonism and norepinephrine reuptake inhibition. Available under brand names Nucynta and Palexia.

\\section{Symptoms}
Indicated for:
\\begin{itemize}
    \\item Acute pain
    \\item Chronic pain
    \\item Neuropathic pain
\\end{itemize}

\\section{Causes}
Pain conditions treated include:
\\begin{itemize}
    \\item Back pain
    \\item Diabetic neuropathy
    \\item Post-surgical pain
    \\item Cancer pain
\\end{itemize}

\\section{Diagnosis}
Proper pain assessment and diagnosis before prescribing.

\\section{Treatment}
\\begin{itemize}
    \\item Immediate-release: 50-100 mg every 4-6 hours
    \\item Extended-release: 50-250 mg every 12 hours
    \\item Start low, titrate slowly
    \\item Monitor for side effects
\\end{itemize}

Side effects: nausea, dizziness, constipation, somnolence. Risk of addiction and respiratory depression.

\\section{Prevention}
\\begin{itemize}
    \\item Use lowest effective dose
    \\item Limit duration
    \\item Monitor for misuse
    \\item Proper storage and disposal
\\end{itemize}

\\section{When to Seek Medical Care}
Seek care for:
\\begin{itemize}
    \\item Signs of overdose (slow breathing, extreme sleepiness)
    \\item Severe constipation
    \\item Allergic reactions
    \\item Mood changes
\\end{itemize}
""",

    "taking_opioid_medicines_safely": """\\chapter{Taking Opioid Medicines Safely}

\\section{Overview}
Opioids are powerful pain medications that carry risks of addiction, overdose, and death. Safe use requires understanding proper dosing, storage, and disposal.

\\section{Symptoms}
Opioids are prescribed for moderate to severe pain when other treatments are insufficient.

\\section{Causes}
Chronic pain, post-surgical pain, cancer pain, and acute trauma.

\\section{Diagnosis}
Proper pain assessment before starting opioids.

\\section{Treatment}
Safe opioid use guidelines:
\\begin{itemize}
    \\item Take exactly as prescribed
    \\item Never share medications
    \\item Store securely away from children
    \\item Do not mix with alcohol
    \\item Dispose of unused medications properly
    \\item Attend regular follow-ups
    \\item Keep medication log
\\end{itemize}

\\section{Prevention}
\\begin{itemize}
    \\item Use non-opioid alternatives when possible
    \\item Set clear treatment goals
    \\item Regular urine drug screening
    \\item Pain contracts
    \\item Monitor prescription drug databases
\\end{itemize}

\\section{When to Seek Medical Care}
Seek emergency care for:
\\begin{itemize}
    \\item Slow or shallow breathing
    \\item Extreme drowsiness
    \\item Confusion
    \\item Unresponsiveness
    \\item Blue lips or fingernails
\\end{itemize}
""",
}

for filename, content in CHAPTERS.items():
    filepath = os.path.join(chapters_dir, filename)
    with open(filepath, 'w') as f:
        f.write(content)
    print(f"Written: {filename}")

print(f"Total: {len(CHAPTERS)}")
