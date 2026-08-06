#!/usr/bin/env python3
"""Generate real medical content for T-Z chapter tex files."""

import os
import re

chapters_dir = "/Users/csv610/Projects/MyBooks/Medical/MedTopics/chapters"

# Medical content templates for T-Z chapters
CHAPTERS = {
    "tadalafil_cialis": """\\chapter{Tadalafil (Cialis)}

\\section{Overview}
Tadalafil, sold under the brand name Cialis, is a medication used to treat erectile dysfunction (ED) and benign prostatic hyperplasia (BPH). It belongs to a class of drugs called phosphodiesterase type 5 (PDE5) inhibitors. Unlike sildenafil (Viagra), tadalafil can remain effective for up to 36 hours, earning it the nickname "the weekend pill."

\\section{Symptoms}
Tadalafil is indicated for:
\\begin{itemize}
    \\item Erectile dysfunction in men
    \\item Symptoms of benign prostatic hyperplasia (BPH)
    \\item Pulmonary arterial hypertension (under brand name Adcirca)
\\end{itemize}

\\section{Causes}
Erectile dysfunction can result from:
\\begin{itemize}
    \\item Vascular disease and atherosclerosis
    \\item Diabetes mellitus
    \\item Neurological disorders
    \\item Psychological factors (stress, anxiety, depression)
    \\item Hormonal imbalances
    \\item Medication side effects
\\end{itemize}

\\section{Diagnosis}
Diagnosis of ED involves:
\\begin{itemize}
    \\item Medical and sexual history
    \\item Physical examination
    \\item Blood tests (testosterone, glucose, lipids)
    \\item Urine tests
    \\item Penile ultrasound (if needed)
\\end{itemize}

\\section{Treatment}
Tadalafil is taken orally:
\\begin{itemize}
    \\item \\textbf{As-needed dose:} 10 mg taken at least 30 minutes before sexual activity
    \\item \\textbf{Daily dose:} 2.5-5 mg taken once daily
    \\item \\textbf{BPH dose:} 5 mg once daily
\\end{itemize}

Maximum recommended dose is 20 mg per day. Do not combine with nitrates.

\\section{Prevention}
To reduce ED risk:
\\begin{itemize}
    \\item Maintain healthy weight
    \\item Exercise regularly
    \\item Quit smoking
    \\item Limit alcohol
    \\item Manage stress
    \\item Control blood sugar and blood pressure
\\end{itemize}

\\section{When to Seek Medical Care}
Seek care for:
\\begin{itemize}
    \\item Priapism (erection lasting more than 4 hours)
    \\item Sudden vision or hearing loss
    \\item Chest pain during sexual activity
    \\item Allergic reactions (rash, difficulty breathing)
\\end{itemize}
""",

    "tai_chi": """\\chapter{Tai Chi}

\\section{Overview}
Tai chi is an ancient Chinese martial art practiced as a gentle form of exercise. It involves slow, deliberate movements combined with deep breathing and meditation. Tai chi is considered a moving meditation and offers numerous health benefits, particularly for balance, flexibility, and stress reduction.

\\section{Symptoms}
Tai chi is recommended for:
\\begin{itemize}
    \\item Balance problems and fall prevention
    \\item Chronic back pain
    \\item Osteoarthritis
    \\item Fibromyalgia
    \\item Anxiety and depression
    \\item High blood pressure
    \\item COPD symptoms
\\end{itemize}

\\section{Causes}
Conditions that benefit from tai chi include age-related balance decline, chronic pain conditions, and stress-related disorders.

\\section{Diagnosis}
Assessment before starting tai chi includes:
\\begin{itemize}
    \\item Balance evaluation
    \\item Joint health assessment
    \\item Cardiovascular screening
    \\item Current activity level evaluation
\\end{itemize}

\\section{Treatment}
Standard practice involves:
\\begin{itemize}
    \\item 10-30 minute sessions, 2-3 times per week
    \\item Focus on slow, flowing movements
    \\item Deep, diaphragmatic breathing
    \\item Mindful awareness of body position
    \\item Gradual progression to more complex forms
\\end{itemize}

Classes are available at community centers, yoga studios, and online.

\\section{Prevention}
Regular tai chi practice can prevent:
\\begin{itemize}
    \\item Falls in older adults
    \\item Balance-related injuries
    \\item Stress and anxiety disorders
    \\item Joint stiffness and reduced mobility
\\end{itemize}

\\section{When to Seek Medical Care}
Consult a doctor before starting if you have:
\\begin{itemize}
    \\item Recent surgery
    \\item Severe osteoporosis
    \\item Acute injuries
    \\item Uncontrolled high blood pressure
\\end{itemize}
""",

    "tailbone_coccyx_pain_and_injury": """\\chapter{Tailbone (Coccyx) Pain and Injury}

\\section{Overview}
Coccydynia is pain in the coccyx (tailbone) area, located at the base of the spine. The pain can be acute or chronic and is often worsened by sitting. Common causes include falls, childbirth, and prolonged sitting on hard surfaces.

\\section{Symptoms}
\\begin{itemize}
    \\item Pain and discomfort in the tailbone area
    \\item Pain when sitting, especially on hard surfaces
    \\item Pain during bowel movements
    \\item Pain during sexual intercourse
    \\item Localized tenderness
    \\item Visibility of bruising after trauma
\\end{itemize}

\\section{Causes}
\\begin{itemize}
    \\item Direct trauma (falls onto buttocks)
    \\item Repetitive strain (cycling, rowing)
    \\item Childbirth (especially vaginal delivery)
    \\item Poor posture while sitting
    \\item Degenerative joint changes
    \\item Rarely: tumors or infections
\\end{itemize}

\\section{Diagnosis}
\\begin{itemize}
    \\item Physical examination with palpation
    \\item X-rays (seated and standing views)
    \\item MRI or CT scan (if fracture or tumor suspected)
    \\item Digital rectal exam (internal palpation)
\\end{itemize}

\\section{Treatment}
\\begin{itemize}
    \\item Cushioned seating (donut pillows)
    \\item Ice or heat application
    \\item NSAIDs for pain relief
    \\item Physical therapy
    \\item Steroid injections (in severe cases)
    \\item Surgery (coccygectomy) - rarely needed
\\end{itemize}

\\section{Prevention}
\\begin{itemize}
    \\item Maintain good sitting posture
    \\item Use cushioned seats
    \\item Strengthen core muscles
    \\item Avoid prolonged sitting
    \\item Wear protective gear during sports
\\end{itemize}

\\section{When to Seek Medical Care}
Seek care for:
\\begin{itemize}
    \\item Severe pain after a fall
    \\item Pain lasting more than a few weeks
    \\item Numbness or weakness in legs
    \\item Bowel or bladder changes
    \\item Unexplained weight loss with pain
\\end{itemize}
""",

    "tetanus": """\\chapter{Tetanus}

\\section{Overview}
Tetanus, also known as lockjaw, is a serious bacterial infection caused by Clostridium tetani. The bacteria produce toxins that cause painful muscle contractions, particularly in the jaw and neck. Tetanus can be fatal if it affects the muscles that control breathing.

\\section{Symptoms}
\\begin{itemize}
    \\item Jaw cramping and lockjaw
    \\item Stiff neck muscles
    \\item Difficulty swallowing
    \\item Abdominal muscle rigidity
    \\item Painful body spasms (often triggered by minor stimuli)
    \\item Fever and sweating
    \\item Elevated blood pressure
    \\item Rapid heart rate
\\end{itemize}

Symptoms typically appear 3-21 days after infection.

\\section{Causes}
C. tetani spores enter the body through:
\\begin{itemize}
    \\item Puncture wounds (nails, splinters)
    \\item Crush injuries
    \\item Burns
    \\item Surgical wounds
    \\item Animal bites
    \\item Umbilical cord stumps in newborns
\\end{itemize}

Spores are found in soil, dust, and animal feces.

\\section{Diagnosis}
\\begin{itemize}
    \\item Clinical examination based on symptoms
    \\item History of wound contamination
    \\item Culture (often negative - organisms may not grow)
    \\item No specific lab test confirms diagnosis
\\end{itemize}

\\section{Treatment}
\\begin{itemize}
    \\item \\textbf{Tetanus immune globulin (TIG):} Neutralizes unbound toxin
    \\item \\textbf{Antibiotics:} Metronidazole or penicillin
    \\item \\textbf{Wound care:} Cleaning and removal of dead tissue
    \\item \\textbf{Muscle relaxants:} For spasms control
    \\item \\textbf{Respiratory support:} Ventilator if needed
    \\item \\textbf{Vaccination:} Tdap vaccine after recovery
\\end{itemize}

\\section{Prevention}
\\begin{itemize}
    \\item DTaP vaccine (children): 5 doses by age 6
    \\item Tdap booster (adolescents and adults): every 10 years
    \\item Tdap during each pregnancy
    \\item Wound cleaning and tetanus shot for dirty wounds
\\end{itemize}

\\section{When to Seek Medical Care}
Seek immediate care for:
\\begin{itemize}
    \\item Jaw stiffness after injury
    \\item Muscle spasms following a wound
    \\item Difficulty swallowing
    \\item Any deep or dirty wound if vaccination is not up to date
\\end{itemize}
""",

    "zoster_shingles": """\\chapter{Zoster (Shingles)}

\\section{Overview}
Shingles, also known as herpes zoster, is a viral infection that causes a painful rash. It is caused by reactivation of the varicella-zoster virus, the same virus that causes chickenpox. After chickenpox resolves, the virus remains dormant in nerve tissue and can reactivate decades later.

\\section{Symptoms}
\\begin{itemize}
    \\item Pain, burning, or tingling on one side of the body
    \\item Red rash that develops into fluid-filled blisters
    \\item Rash typically forms a band or strip on one side
    \\item Fever and chills
    \\item Headache
    \\item Sensitivity to light
    \\item Fatigue
\\end{itemize}

Rash usually appears 1-5 days after pain begins and heals in 2-4 weeks.

\\section{Causes}
\\begin{itemize}
    \\item Reactivation of latent varicella-zoster virus
    \\item Weakened immune system (age, HIV, cancer treatment)
    \\item Stress and illness
    \\item Previous chickenpox infection
\\end{itemize}

\\section{Diagnosis}
\\begin{itemize}
    \\item Clinical examination of rash
    \\item PCR testing of blister fluid
    \\item Viral culture
    \\item Tzanck smear (less common)
\\end{itemize}

\\section{Treatment}
\\begin{itemize}
    \\item \\textbf{Antiviral medications:} Acyclovir, valacyclovir, famciclovir (start within 72 hours)
    \\item \\textbf{Pain management:} NSAIDs, acetaminophen
    \\item \\textbf{Topical treatments:} Calamine lotion, cool compresses
    \\item \\textbf{Neuropathic pain:} Gabapentin, pregabalin for postherpetic neuralgia
    \\item \\textbf{Antibiotics:} If secondary bacterial infection occurs
\\end{itemize}

\\section{Prevention}
\\begin{itemize}
    \\item Shingrix vaccine (recommended for adults 50+ and immunocompromised 19+)
    \\item Two doses given 2-6 months apart
    \\item Maintaining immune health
    \\item Avoiding close contact with those who have active shingles or chickenpox
\\end{itemize}

\\section{When to Seek Medical Care}
Seek care for:
\\begin{itemize}
    \\item Rash near eyes or ears
    \\item Widespread rash
    \\item Fever with rash
    \\item Signs of infection (increased redness, warmth, pus)
    \\item Severe pain
\\end{itemize}
""",

    "zinc": """\\chapter{Zinc}

\\section{Overview}
Zinc is an essential trace mineral involved in numerous biological processes including immune function, wound healing, DNA synthesis, and cell division. It is found in many foods and available as a dietary supplement.

\\section{Symptoms}
Zinc deficiency can cause:
\\begin{itemize}
    \\item Impaired immune function
    \\item Delayed wound healing
    \\item Hair loss
    \\item Diarrhea
    \\item Loss of appetite
    \\item Impaired sense of taste and smell
    \\item Growth retardation in children
    \\item Eye and skin lesions
\\end{itemize}

\\section{Causes}
Deficiency risk factors include:
\\begin{itemize}
    \\item Vegetarian or vegan diets (phytates reduce absorption)
    \\item Chronic kidney disease
    \\item Liver cirrhosis
    \\item Sickle cell disease
    \\item Alcoholism
    \\item Malabsorption syndromes
    \\item Extreme stress or trauma
\\end{itemize}

\\section{Diagnosis}
\\begin{itemize}
    \\item Serum zinc level (most common test)
    \\item Plasma zinc level
    \\item Hair zinc analysis (less reliable)
    \\item Alkaline phosphatase (zinc-dependent enzyme)
\\end{itemize}

\\section{Treatment}
\\begin{itemize}
    \\item \\textbf{Dietary changes:} Oysters, red meat, poultry, beans, nuts
    \\item \\textbf{Supplements:} Zinc gluconate, zinc acetate, zinc sulfate
    \\item \\textbf{RDA:} 11 mg/day for men, 8 mg/day for women
    \\item Upper limit: 40 mg/day for adults
\\end{itemize}

Excessive zinc can cause nausea, vomiting, loss of appetite, abdominal cramps, and copper deficiency.

\\section{Prevention}
\\begin{itemize}
    \\item Consume zinc-rich foods regularly
    \\item Soak legumes to reduce phytates
    \\item Consider supplementation if at risk
    \\item Avoid excessive copper supplementation
\\end{itemize}

\\section{When to Seek Medical Care}
Seek care for:
\\begin{itemize}
    \\item Signs of deficiency (recurrent infections, poor wound healing)
    \\item GI side effects from supplements
    \\item Metallic taste or nausea with zinc
\\end{itemize}
""",
}

# Write all prepared chapters
written = []
for filename, content in CHAPTERS.items():
    filepath = os.path.join(chapters_dir, filename)
    with open(filepath, 'w') as f:
        f.write(content)
    written.append(filename)
    print(f"Written: {filename}")

print(f"\\nTotal written: {len(written)}")
