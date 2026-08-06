#!/usr/bin/env python3
"""
Medical Chapter Content Generator
Rewrites C-H chapters with real medical content in standard sections.
"""

import os
import re
from pathlib import Path

CHAPTERS_DIR = '/Users/csv610/Projects/MyBooks/Medical/MedTopics/chapters'

# Standard sections for all chapters
STANDARD_SECTIONS = [
    "Overview",
    "Symptoms",
    "Causes",
    "Diagnosis",
    "Treatment",
    "Prevention",
    "When to Seek Medical Care"
]

# Medical content database for C-H chapters
MEDICAL_CONTENT = {
    # C chapters
    "cancer": {
        "title": "Cancer",
        "overview": """Cancer is a group of diseases characterized by the uncontrolled growth and spread of abnormal cells. If not controlled, cancer can spread from its original site into nearby tissue or to other parts of the body. The term refers to a large group of different diseases that can start in almost any organ or tissue of the body when abnormal cells divide uncontrollably and grow into tissue masses, forming tumors.""",
        "symptoms": """Symptoms of cancer depend on where it is located, how big it is, and how many organs it is affecting. General symptoms include:\n\\begin{itemize}
    \\item Persistent fatigue and tiredness
    \\item Unexplained weight loss
    \\item Fever that doesn't go away
    \\item Changes in skin color (yellowing, darkening, redness)
    \\item Changes in bowel or bladder habits
    \\item Persistent cough or hoarseness
    \\item Unusual bleeding or discharge
    \\item Difficulty swallowing
    \\item Lumps or thickening in the breast or elsewhere
    \\item Persistent pain that doesn't go away
\\end{itemize}""",
        "causes": """Cancer is caused by damage to DNA within cells. Several factors can cause this damage:\n\\begin{itemize}
    \\item \\textbf{Tobacco use:} Responsible for about 30\% of cancer deaths
    \\item \\textbf{Unhealthy diet and physical inactivity:} Contribute to about 30-35\% of cancers
    \\item \\textbf{Infections:} Certain viruses and bacteria can cause cancer (HPV, hepatitis B and C, H. pylori)
    \\item \\textbf{Radiation:} Ultraviolet radiation from sun exposure, ionizing radiation
    \\item \\textbf{Occupational exposures:} Asbestos, benzene, certain chemicals
    \\item \\textbf{Genetic factors:} Inherited mutations in genes like BRCA1, BRCA2
    \\item \\textbf{Age:} Risk increases significantly with age due to accumulated genetic damage
\\end{itemize}""",
        "diagnosis": """Cancer diagnosis typically involves multiple steps:\n\\begin{itemize}
    \\item \\textbf{Medical history and physical examination:} Detailed review of symptoms and risk factors
    \\item \\textbf{Laboratory tests:} Blood tests, urine tests, tumor markers
    \\item \\textbf{Imaging studies:} X-rays, CT scans, MRI, PET scans, ultrasound
    \\item \\textbf{Biopsy:} Removal of tissue sample for pathological examination (gold standard)
    \\item \\textbf{Endoscopy:} Visual examination of internal organs using a camera
    \\item \\textbf{Genetic testing:} Identification of hereditary cancer syndromes
\\end{itemize}
Early diagnosis through screening programs significantly improves treatment outcomes.
""",
        "treatment": """Cancer treatment depends on the type, stage, and location of cancer, as well as the patient's overall health:\n\\begin{itemize}
    \\item \\textbf{Surgery:} Removal of tumors and surrounding tissue
    \\item \\textbf{Chemotherapy:} Use of drugs to kill cancer cells throughout the body
    \\item \\textbf{Radiation therapy:} High-energy rays to destroy cancer cells
    \\item \\textbf{Immunotherapy:} Boosting the immune system to fight cancer
    \\item \\textbf{Targeted therapy:} Drugs that target specific molecules involved in cancer growth
    \\item \\textbf{Hormone therapy:} Blocking hormones that fuel certain cancers
    \\item \\textbf{Stem cell transplant:} Replacing damaged bone marrow with healthy stem cells
\\end{itemize}
Treatment is often combined (multimodal therapy) for better outcomes.
""",
        "prevention": """Cancer prevention focuses on reducing risk factors:\n\\begin{itemize}
    \\item Avoid tobacco products and secondhand smoke
    \\item Maintain a healthy weight through regular exercise
    \\item Eat a diet rich in fruits, vegetables, and whole grains
    \\item Limit alcohol consumption
    \\item Protect skin from UV radiation
    \\item Get vaccinated against cancer-causing infections (HPV, hepatitis B)
    \\item Participate in recommended cancer screenings
    \\item Avoid occupational carcinogens when possible
    \\item Practice safe sex to reduce HPV risk
\\end{itemize}
The World Health Organization estimates that 30-50\% of cancers are preventable.
""",
        "when_to_seek_care": """Seek medical attention if you experience:\n\\begin{itemize}
    \\item Unexplained weight loss
    \\item Persistent fatigue
    \\item New lumps or thickening in any part of the body
    \\item Persistent pain that doesn't improve with time
    \\item Changes in bowel or bladder habits lasting more than a few days
    \\item Unusual bleeding or discharge
    \\item Persistent cough or hoarseness
    \\item Difficulty swallowing
    \\item Skin changes (new moles, changes to existing moles)
    \\item Fever or night sweats that persist
\\end{itemize}
Regular screening according to age and risk factors is essential for early detection.
"""
    },
    "chemotherapy": {
        "title": "Chemotherapy",
        "overview": """Chemotherapy is the use of drugs to destroy cancer cells. It is one of the main types of cancer treatment, along with surgery and radiation therapy. Chemotherapy works by targeting rapidly dividing cells, which is a characteristic of cancer cells. The drugs travel through the bloodstream to reach cancer cells throughout the body, making it effective for cancers that have spread or are likely to spread.""",
        "symptoms": """Chemotherapy side effects occur because the drugs also affect healthy cells that divide rapidly. Common side effects include:\n\\begin{itemize}
    \\item Fatigue and weakness
    \\item Nausea and vomiting
    \\item Hair loss (alopecia)
    \\item Mouth sores
    \\item Loss of appetite
    \\item Increased risk of infection (due to low white blood cell count)
    \\item Easy bruising or bleeding (due to low platelet count)
    \\item Anemia (fatigue, shortness of breath)
    \\item Diarrhea or constipation
    \\item Skin and nail changes
    \\item "Chemo brain" (cognitive changes)
\\end{itemize}
Side effects vary depending on the drugs used, dosage, and individual patient factors.
""",
        "causes": """Chemotherapy is prescribed by oncologists to:\n\\begin{itemize}
    \\item \\textbf{Cure cancer:} Eliminate all cancer cells
    \\item \\textbf{Control cancer:} Slow or stop growth of advanced cancer
    \\item \\textbf{Relieve symptoms:} Palliative care to improve quality of life
    \\item \\textbf{Prepare for surgery:} Shrink tumors before operation (neoadjuvant)
    \\item \\textbf{Prevent recurrence:} Kill remaining cells after surgery (adjuvant)
\\end{itemize}
The choice of chemotherapy drugs depends on cancer type, stage, genetic markers, and patient health status.
""",
        "diagnosis": """Before starting chemotherapy, oncologists determine:\n\\begin{itemize}
    \\item Cancer type and stage through biopsy and imaging
    \\item Whether chemotherapy is appropriate for the specific cancer
    \\item Which drug regimen will be most effective
    \\item Patient's ability to tolerate treatment (organ function tests)
    \\item Potential drug interactions with current medications
\\end{itemize}
Genetic testing of tumors helps identify targeted therapies and predict response.
""",
        "treatment": """Chemotherapy can be given in several ways:\n\\begin{itemize}
    \\item \\textbf{Intravenous (IV):} Most common, through a vein
    \\item \\textbf{Oral:} Pills or liquids taken by mouth
    \\item \\textbf{Intramuscular/Subcutaneous:} Injection into muscle or under skin
    \\item \\textbf{Intrathecal:} Directly into spinal fluid
    \\item \\textbf{Topical:} Cream applied to skin
    \\item \\textbf{Intracavitary:} Into body cavities (abdomen, bladder)
\\end{itemize}
Treatment is given in cycles with rest periods to allow healthy cells to recover. Common regimens include combinations of drugs like cyclophosphamide, doxorubicin, cisplatin, and paclitaxel.
""",
        "prevention": """While chemotherapy cannot be prevented, patients can:\n\\begin{itemize}
    \\item Discuss all medications with oncologist to avoid interactions
    \\item Stay hydrated before and after treatment
    \\item Maintain good nutrition to support recovery
    \\item Practice good hygiene to prevent infections
    \\item Report side effects promptly to healthcare team
    \\item Use cold caps to reduce hair loss (where appropriate)
    \\item Avoid pregnancy during treatment (teratogenic risk)
\\end{itemize}
Proper preparation and supportive care minimize complications.
""",
        "when_to_seek_care": """Contact your oncology team immediately if you experience:\n\\begin{itemize}
    \\item Fever above 38°C (100.4°F) - may indicate infection
    \\item Signs of infection (chills, sore throat, cough)
    \\item Uncontrolled vomiting or diarrhea
    \\item Bleeding that won't stop
    \\item Severe pain not relieved by medication
    \\item Shortness of breath
    \\item Confusion or changes in mental status
    \\item Signs of allergic reaction (rash, swelling, difficulty breathing)
    \\item Reduced urine output
\\end{itemize}
Never wait until your next appointment if you have concerning symptoms.
"""
    },
    "heart_attack": {
        "title": "Heart Attack",
        "overview": """A heart attack, or myocardial infarction, occurs when blood flow decreases or stops to a part of the heart, causing damage to the heart muscle. This is usually caused by a blockage in the coronary arteries that supply blood to the heart. Heart attack is a medical emergency that requires immediate treatment to restore blood flow and minimize heart damage.""",
        "symptoms": """Classic symptoms of a heart attack include:\n\\begin{itemize}
    \\item Chest pain or discomfort (pressure, squeezing, fullness)
    \\item Pain radiating to arm, shoulder, neck, jaw, or back
    \\item Shortness of breath
    \\item Cold sweat
    \\item Nausea or vomiting
    \\item Lightheadedness or dizziness
    \\item Unexplained fatigue
\\end{itemize}
Women may experience atypical symptoms including jaw pain, back pain, nausea, and unusual fatigue without classic chest pain.
""",
        "causes": """Most heart attacks are caused by:\n\\begin{itemize}
    \\item \\textbf{Coronary artery disease:} Buildup of plaque (atherosclerosis) in coronary arteries
    \\item \\textbf{Plaque rupture:} Sudden rupture of cholesterol plaque triggering blood clot formation
    \\item \\textbf{Coronary spasm:} Temporary narrowing of coronary artery
    \\item Risk factors include: high blood pressure, high cholesterol, smoking, diabetes, obesity, sedentary lifestyle, family history, age (>45 men, >55 women)
\\end{itemize}""",
        "diagnosis": """Heart attack diagnosis involves:\n\\begin{itemize}
    \\item \\textbf{Electrocardiogram (ECG/EKG):} Shows ST-segment changes indicating heart damage
    \\item \\textbf{Blood tests:} Cardiac enzymes (troponin, CK-MB) elevated when heart muscle damaged
    \\item \\textbf{Echocardiogram:} Ultrasound showing heart wall motion abnormalities
    \\item \\textbf{Coronary angiography:} Visualizes blockages in coronary arteries
    \\item \\textbf{Cardiac MRI:} Detailed imaging of heart damage
\\end{itemize}
Time is critical - faster diagnosis leads to better outcomes.
""",
        "treatment": """Heart attack treatment focuses on restoring blood flow:\n\\begin{itemize}
    \\item \\textbf{Immediate:} Aspirin, oxygen, nitroglycerin, morphine for pain
    \\item \\textbf{Reperfusion therapy:}
        \\begin{itemize}
            \\item Percutaneous coronary intervention (PCI/stent) - preferred if available within 90 minutes
            \\item Thrombolytic therapy ("clot-busting" drugs) if PCI unavailable
        \\end{itemize}
    \\item \\textbf{Medications:} Beta-blockers, ACE inhibitors, statins, anticoagulants
    \\item \\textbf{Surgery:} Coronary artery bypass graft (CABG) for complex blockages
    \\item \\textbf{Cardiac rehabilitation:} Structured exercise and education program
\\end{itemize}""",
        "prevention": """Heart attack prevention includes:\n\\begin{itemize}
    \\item Don't smoke and avoid secondhand smoke
    \\item Control blood pressure (target <140/90 mmHg)
    \\item Manage cholesterol (LDL <100 mg/dL, or <70 for high risk)
    \\item Control diabetes (HbA1c <7\%)
    \\item Maintain healthy weight (BMI 18.5-24.9)
    \\item Exercise regularly (150 minutes moderate activity weekly)
    \\item Eat heart-healthy diet (Mediterranean diet recommended)
    \\item Limit alcohol consumption
    \\item Manage stress
    \\item Regular health screenings
\\end{itemize}""",
        "when_to_seek_care": """Call emergency services immediately if you experience:\n\\begin{itemize}
    \\item Chest pain or pressure lasting more than a few minutes
    \\item Pain spreading to shoulder, arm, neck, jaw, or back
    \\item Shortness of breath with or without chest discomfort
    \\item Cold sweat, nausea, or lightheadedness
    \\item Unexplained extreme fatigue
\\end{itemize}
Do not drive yourself to the hospital. Early treatment saves heart muscle and lives.
"""
    },
    "heart_failure": {
        "title": "Heart Failure",
        "overview": """Heart failure is a chronic condition where the heart doesn't pump blood as well as it should. Despite the name, it doesn't mean the heart has stopped working. Rather, the heart's pumping action is weakened, causing blood to back up in the veins and organs. Over time, the heart muscle weakens and stretches, becoming less efficient at pumping blood throughout the body.""",
        "symptoms": """Common symptoms of heart failure include:\n\\begin{itemize}
    \\item Shortness of breath (dyspnea), especially with activity or when lying flat
    \\item Fatigue and weakness
    \\item Swelling (edema) in legs, ankles, and feet
    \\item Rapid or irregular heartbeat
    \\item Reduced exercise tolerance
    \\item Persistent cough or wheezing with white or pink blood-tinged mucus
    \\item Difficulty breathing when lying flat
    \\item Sudden weight gain from fluid retention
    \\item Impaired thinking or confusion
    \\item Lack of appetite and nausea
\\end{itemize}
Symptoms may be subtle initially and worsen gradually.
""",
        "causes": """Heart failure commonly results from:\n\\begin{itemize}
    \\item \\textbf{Coronary artery disease:} Most common cause, leading to heart attack
    \\item \\textbf{High blood pressure:} Forces heart to work harder
    \\item \\textbf{Cardiomyopathy:} Damage to heart muscle from various causes
    \\item \\textbf{Heart valve disease:} Valves don't work properly
    \\item \\textbf{Congenital heart defects:} Present at birth
    \\item \\textbf{Arrhythmias:} Abnormal heart rhythms
    \\item \\textbf{Diabetes:} Increases cardiovascular risk
    \\item \\textbf{Viral infections:} Can damage heart muscle
    \\item \\textbf{Alcohol and drug abuse:} Toxic to heart muscle
\\end{itemize}""",
        "diagnosis": """Heart failure diagnosis involves:\n\\begin{itemize}
    \\item \\textbf{Physical examination:} Checking for swelling, lung sounds, heart murmurs
    \\item \\textbf{Blood tests:} BNP or NT-proBNP (heart failure markers), complete blood count, kidney function
    \\item \\textbf{Echocardiogram:} Gold standard - measures ejection fraction (EF)
    \\item \\textbf{Chest X-ray:} Shows heart size and fluid in lungs
    \\item \\textbf{Electrocardiogram:} Detects arrhythmias, previous heart attacks
    \\item \\textbf{Cardiac MRI:} Detailed heart structure and function
    \\item \\textbf{Stress test:} Evaluates heart function during exercise
    \\item \\textbf{Coronary angiography:} Checks for blocked arteries
\\end{itemize}
Heart failure with reduced EF (HFrEF) vs preserved EF (HFpEF) guides treatment.
""",
        "treatment": """Heart failure treatment includes:\n\\begin{itemize}
    \\item \\textbf{Medications:}
        \\begin{itemize}
            \\item ACE inhibitors or ARBs (lisinopril, losartan)
            \\item Beta-blockers (metoprolol, carvedilol)
            \\item Diuretics (furosemide) for fluid removal
            \\item Aldosterone antagonists (spironolactone)
            \\item SGLT2 inhibitors (dapagliflozin, empagliflozin)
            \\item ARNI (sacubitril/valsartan) for eligible patients
        \\end{itemize}
    \\item \\textbf{Devices:} Pacemakers, ICDs, biventricular pacemakers
    \\item \\textbf{Surgery:} Coronary bypass, valve repair/replacement, heart transplant
    \\item \\textbf{Lifestyle changes:} Salt restriction, fluid management, exercise
    \\item \\textbf{Cardiac rehabilitation:} Supervised exercise and education
\\end{itemize}""",
        "prevention": """Prevent heart failure by:\n\\begin{itemize}
    \\item Managing high blood pressure
    \\item Controlling diabetes
    \\item Keeping cholesterol in check
    \\item Maintaining healthy weight
    \\item Exercising regularly
    \\item Eating a balanced diet
    \\item Avoiding smoking and excessive alcohol
    \\item Getting adequate sleep
    \\item Managing stress
    \\item Regular health checkups
\\end{itemize}
Early detection and management of cardiovascular disease reduces heart failure risk.
""",
        "when_to_seek_care": """Seek immediate medical attention for:\n\\begin{itemize}
    \\item Difficulty breathing that doesn't improve with rest
    \\item Chest pain or pressure
    \\item Fainting or severe weakness
    \\item Rapid or irregular heartbeat
    \\item Coughing up pink, frothy mucus
    \\item Sudden weight gain (>2 kg in 2 days)
    \\item Increased swelling in legs and abdomen
    \\item Confusion or impaired thinking
\\end{itemize}
Call emergency services if symptoms are severe or worsening rapidly.
"""
    },
    "hypertension": {
        "title": "High Blood Pressure (Hypertension)",
        "overview": """High blood pressure, or hypertension, is a condition where the force of blood against artery walls is consistently too high. Normal blood pressure is below 120/80 mmHg. Hypertension is defined as systolic ≥140 mmHg and/or diastolic ≥90 mmHg. Often called the "silent killer" because it typically has no symptoms but significantly increases risk of heart disease, stroke, and kidney failure.""",
        "symptoms": """Most people with hypertension have no symptoms. When present, they may include:\n\\begin{itemize}
    \\item Headaches (usually occipital, morning)
    \\item Shortness of breath
    \\item Nosebleeds
    \\item Flushing
    \\item Dizziness
    \\item Chest pain
    \\item Visual changes
    \\item Blood in urine
\\end{itemize}
Severe hypertension (hypertensive crisis >180/120) is a medical emergency requiring immediate treatment.
""",
        "causes": """Hypertension is classified as:\n\\begin{itemize}
    \\item \\textbf{Primary (essential) hypertension:} 90-95\% of cases, no identifiable cause, develops gradually over years
    \\item \\textbf{Secondary hypertension:} Caused by underlying conditions including:
        \\begin{itemize}
            \\item Kidney disease
            \\item Obstructive sleep apnea
            \\item Thyroid problems
            \\item Adrenal gland tumors
            \\item Certain medications (NSAIDs, decongestants, oral contraceptives)
            \\item Illegal drugs (cocaine, amphetamines)
            \\item Congenital blood vessel defects
        \\end{itemize}
    \\item Risk factors: family history, age (>60), obesity, physical inactivity, tobacco use, high sodium intake, low potassium intake, excessive alcohol, chronic stress
\\end{itemize}""",
        "diagnosis": """Hypertension diagnosis requires:\n\\begin{itemize}
    \\item \\textbf{Multiple blood pressure measurements:} At least 2 readings on 2+ occasions
    \\item \\textbf{Home monitoring:} To confirm diagnosis and rule out white-coat hypertension
    \\item \\textbf{Blood tests:} Kidney function, blood sugar, cholesterol, thyroid
    \\item \\textbf{Urinalysis:} Check for kidney damage
    \\item \\textbf{ECG:} Assess heart damage from hypertension
    \\item \\textbf{Echocardiogram:} Evaluate heart structure
    \\item \\textbf{Retinal exam:} Check for damage to eye blood vessels
\\end{itemize}
Blood pressure categories: Normal (<120/80), Elevated (120-129/<80), Stage 1 (130-139/80-89), Stage 2 (≥140/≥90).
""",
        "treatment": """Hypertension management includes:\n\\begin{itemize}
    \\item \\textbf{Lifestyle modifications:} Weight loss, DASH diet, sodium restriction (<2.3g/day), exercise, alcohol moderation
    \\item \\textbf{First-line medications:}
        \\begin{itemize}
            \\item ACE inhibitors (lisinopril, enalapril)
            \\item ARBs (losartan, valsartan)
            \\item Calcium channel blockers (amlodipine, diltiazem)
            \\item Thiazide diuretics (hydrochlorothiazide, chlorthalidone)
        \\end{itemize}
    \\item \\textbf{Combination therapy:} Often needed for blood pressure ≥140/90
    \\item \\textbf{Secondary hypertension:} Treat underlying cause
    \\item \\textbf{Target:} <140/90 mmHg for most; <130/80 for diabetes or chronic kidney disease
\\end{itemize}""",
        "prevention": """Prevent hypertension through:\n\\begin{itemize}
    \\item Maintain healthy weight (BMI 18.5-24.9)
    \\item Regular physical activity (150 min/week moderate exercise)
    \\item DASH diet rich in fruits, vegetables, whole grains
    \\item Limit sodium to <2,300 mg daily (ideally 1,500 mg)
    \\item Limit alcohol (≤1 drink/day women, ≤2 men)
    \\item Don't smoke
    \\item Manage stress
    \\item Get adequate sleep
    \\item Regular blood pressure screenings
\\end{itemize}
Lifestyle changes can prevent or delay hypertension by up to 50\%.
""",
        "when_to_seek_care": """Seek medical attention for:\n\\begin{itemize}
    \\item Blood pressure readings consistently above 140/90
    \\item Hypertensive crisis: systolic >180 and/or diastolic >120
    \\item Severe headache with high blood pressure
    \\item Chest pain
    \\item Shortness of breath
    \\item Changes in vision
    \\item Nausea or vomiting
    \\item Anxiety or confusion
\\end{itemize}
Hypertensive crisis requires immediate emergency medical care to prevent stroke, heart attack, or organ damage.
"""
    }
}

def generate_chapter_content(name, content):
    """Generate a properly formatted LaTeX chapter with medical content."""
    lines = []
    lines.append(f"\\chapter{{{content['title']}}}")
    lines.append("")
    
    for section in STANDARD_SECTIONS:
        section_key = section.lower().replace(" ", "_")
        if section_key in content:
            lines.append(f"\\section*{{{section}}}")
            lines.append(content[section_key])
            lines.append("")
    
    lines.append("\\clearpage")
    return "\n".join(lines)

def get_chapter_names():
    """Get all chapter names starting with C-H."""
    chapters_dir = Path(CHAPTERS_DIR)
    files = sorted([f.stem for f in chapters_dir.glob("*.tex")])
    c_to_h = [f for f in files if 'c' <= f[0].lower() <= 'h']
    return c_to_h

def process_chapters():
    """Process and rewrite C-H chapters."""
    chapters = get_chapter_names()
    print(f"Found {len(chapters)} chapters to process")
    
    processed = 0
    skipped = 0
    
    for name in chapters:
        filepath = Path(CHAPTERS_DIR) / f"{name}.tex"
        
        # Check if chapter already has real content (not lorem ipsum)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if 'Lorem ipsum' not in content and len(content) > 500:
            skipped += 1
            continue
        
        # Generate content
        if name in MEDICAL_CONTENT:
            new_content = generate_chapter_content(name, MEDICAL_CONTENT[name])
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            processed += 1
            print(f"  Processed: {name}")
        else:
            # Skip for now - would need content database for all 916 chapters
            pass
    
    print(f"\nProcessed: {processed}, Skipped: {skipped}")
    return processed

if __name__ == "__main__":
    process_chapters()
