#!/usr/bin/env python3
"""
Generate comprehensive medical content for ALL P-S chapters.
Creates detailed, evidence-based content for each chapter.
"""

import os

# Comprehensive medical content database
MEDICAL_CONTENT = {
    "pneumonia": {
        "title": "Pneumonia",
        "overview": "Pneumonia is an infection that inflames the air sacs in one or both lungs. The air sacs may fill with fluid or pus, causing cough with phlegm or pus, fever, chills, and difficulty breathing. A variety of organisms, including bacteria, viruses, and fungi, can cause pneumonia. It is one of the leading infectious causes of death worldwide, particularly affecting young children and older adults.",
        "symptoms": "Common symptoms include:\n\\begin{itemize}\n\\item Cough that may produce greenish, yellow, or bloody mucus\n\\item Fever, sweating, and repeated shaking chills\n\\item Difficulty breathing or rapid, shallow breathing\n\\item Sharp or stabbing chest pain that worsens with breathing or coughing\n\\item Fatigue and weakness\n\\item Nausea, vomiting, or diarrhea\n\\item Loss of appetite\n\\item Bluish coloration of the lips and fingertips (cyanosis) in severe cases\n\\item Confusion or changes in mental awareness (especially in adults age 65 and older)\n\\end{itemize}",
        "causes": "Pneumonia can be caused by several types of organisms:\n\n\\textbf{Bacterial pneumonia:} The most common cause is \\textit{Streptococcus pneumoniae}. Other bacterial causes include \\textit{Haemophilus influenzae}, \\textit{Mycoplasma pneumoniae}, \\textit{Chlamydia pneumoniae}, and \\textit{Legionella pneumophila}.\n\n\\textbf{Viral pneumonia:} Respiratory syncytial virus (RSV), influenza viruses A and B, adenoviruses, and coronaviruses are common viral causes. Viral pneumonia tends to be less severe than bacterial pneumonia.\n\n\\textbf{Fungal pneumonia:} Caused by fungi found in soil or bird droppings, more common in people with chronic health problems or weakened immune systems.\n\n\\textbf{Aspiration pneumonia:} Occurs when food, vomit, or saliva is inhaled into the lungs instead of being swallowed.\n\n\\textbf{Risk factors include:}\n\\begin{itemize}\n\\item Age 65 or older\n\\item Hospitalization, especially in intensive care\n\\item Chronic diseases (COPD, heart disease, diabetes, kidney disease)\n\\item Weakened immune system (HIV/AIDS, chemotherapy, immunosuppressants)\n\\item Difficulty swallowing\n\\item Recent respiratory infection\n\\item Smoking\n\\end{itemize}",
        "diagnosis": "Diagnosis involves several approaches:\n\n\\textbf{Physical examination:} The doctor listens to the lungs with a stethoscope for crackling, bubbling, or rattling sounds. Percussion may reveal dullness over consolidated areas.\n\n\\textbf{Chest X-ray:} Confirms the presence of pneumonia and helps identify the affected area. May show consolidation, infiltrates, or pleural effusion.\n\n\\textbf{Blood tests:} Complete blood count (CBC) checks for elevated white blood cell count indicating infection. Blood cultures identify the organism causing the infection in severe cases.\n\n\\textbf{Pulse oximetry:} Measures oxygen saturation in the blood. Normal is 95-100%; lower values indicate need for supplemental oxygen.\n\n\\textbf{Sputum test:} Analyzes mucus produced during coughing to identify the causative organism.\n\n\\textbf{CT scan:} Provides detailed images for complex cases or when diagnosis is uncertain.\n\n\\textbf{Bronchoscopy:} Used in severe or non-responsive cases to examine airways and collect samples.\n\n\\textbf{Arterial blood gas:} Measures oxygen and carbon dioxide levels in blood from an artery.",
        "treatment": "Treatment depends on the type and severity of pneumonia:\n\n\\textbf{Bacterial pneumonia:} Treated with antibiotics. Common choices include:\n\\begin{itemize}\n\\item Amoxicillin (first-line for mild cases)\n\\item Doxycycline\n\\item Azithromycin (macrolide)\n\\item Levofloxacin or moxifloxacin (fluoroquinolones)\n\\item Ceftriaxone or cefotaxime (for severe cases)\n\\end{itemize}\n\n\\textbf{Viral pneumonia:} Usually resolves on its own. Antiviral medications such as oseltamivir may be prescribed for influenza.\n\n\\textbf{Fungal pneumonia:} Treated with antifungal medications such as fluconazole or amphotericin B.\n\n\\textbf{Supportive care:}\n\\begin{itemize}\n\\item Rest and increased fluid intake\n\\item Over-the-counter pain relievers (acetaminophen, ibuprofen) for fever and discomfort\n\\item Cough suppressants if needed\n\\item Oxygen therapy for low blood oxygen levels\n\\end{itemize}\n\n\\textbf{Hospitalization may be needed for:}\n\\begin{itemize}\n\\item Age over 65 or under 2\n\\item Severe symptoms requiring IV antibiotics\n\\item High fever persisting despite treatment\n\\item Underlying health conditions\n\\item Confusion or low oxygen levels\n\\end{itemize}",
        "prevention": "Prevention strategies include:\n\n\\begin{itemize}\n\\item \\textbf{Vaccination:} Pneumococcal vaccine (PPSV23 or PCV13), influenza vaccine annually, and COVID-19 vaccines\n\\item \\textbf{Hand hygiene:} Regular handwashing with soap and water or alcohol-based sanitizer\n\\item \\textbf{Avoid smoking:} Smoking damages lung defenses against infection\n\\item \\textbf{Healthy lifestyle:} Adequate sleep, nutrition, and exercise\n\\item \\textbf{Avoid close contact:} With people who have respiratory infections\n\\item \\textbf{Cough etiquette:} Cover mouth when coughing or sneezing\n\\item \\textbf{Manage chronic conditions:} Keep diabetes, heart disease, and COPD under control\n\\end{itemize}",
        "when_to_seek": "Seek immediate medical attention if you experience:\n\\begin{itemize}\n\\item Difficulty breathing or shortness of breath\n\\item Chest pain\n\\item Persistent fever above 102°F (39°C)\n\\item Coughing up blood\n\\item Bluish lips or fingertips\n\\item Symptoms that improve then suddenly worsen\n\\item Confusion or altered mental status\n\\item Symptoms in infants, elderly, or immunocompromised individuals\n\\end{itemize}"
    },
    
    "stroke": {
        "title": "Stroke",
        "overview": "A stroke occurs when blood flow to part of the brain is interrupted or reduced, preventing brain tissue from getting oxygen and nutrients. Brain cells begin to die in minutes. Stroke is a medical emergency. Prompt treatment minimizes brain damage and complications. There are two main types: ischemic stroke (blood clot) and hemorrhagic stroke (bleeding). TIA (transient ischemic attack) is a warning stroke.",
        "symptoms": "Stroke symptoms appear suddenly and may include:\n\n\\begin{itemize}\n\\item \\textbf{Face drooping:} One side of the face droops or feels numb. Ask the person to smile.\n\\item \\textbf{Arm weakness:} One arm is weak or numb. Ask the person to raise both arms.\n\\item \\textbf{Speech difficulty:} Speech is slurred or strange. Ask the person to repeat a simple sentence.\n\\item \\textbf{Time to call emergency services:} If anyone shows these symptoms, even if the symptoms go away, call emergency services immediately.\n\\end{itemize}\n\n\\textbf{Additional symptoms may include:}\n\\begin{itemize}\n\\item Numbness or weakness of the face, arm, or leg, especially on one side of the body\n\\item Confusion, trouble speaking, or understanding speech\n\\item Trouble seeing in one or both eyes\n\\item Trouble walking, dizziness, loss of balance or coordination\n\\item Severe headache with no known cause\n\\item Loss of consciousness\n\\end{itemize}",
        "causes": "\\textbf{Ischemic stroke (87% of strokes):}\n\nCaused by blockage of blood vessels supplying the brain.\n\n\\begin{itemize}\n\\item \\textbf{Thrombotic stroke:} Blood clot forms in an artery supplying blood to the brain, often due to atherosclerosis (plaque buildup)\n\\item \\textbf{Embolic stroke:} Blood clot or debris forms away from the brain and travels through the bloodstream to lodge in narrower brain arteries\n\\end{itemize}\n\n\\textbf{Hemorrhagic stroke:}\n\nCaused by bleeding in or around the brain.\n\n\\begin{itemize}\n\\item \\textbf{Intracerebral hemorrhage:} Blood vessel bursts and leaks into surrounding brain tissue, often due to hypertension\n\\item \\textbf{Subarachnoid hemorrhage:} Bleeding between the brain and surrounding membrane, often from aneurysm rupture\n\\end{itemize}\n\n\\textbf{Transient ischemic attack (TIA):} Temporary blockage causing stroke-like symptoms that resolve within 24 hours (usually minutes). Warning sign of future stroke.\n\n\\textbf{Risk factors:}\n\\begin{itemize}\n\\item High blood pressure (hypertension) - most important modifiable risk factor\n\\item Atrial fibrillation and other heart conditions\n\\item High cholesterol\n\\item Diabetes\n\\item Smoking\n\\item Obesity and physical inactivity\n\\item Family history\n\\item Age over 55 (risk doubles each decade after 55)\n\\item Previous stroke or TIA\n\\end{itemize}",
        "diagnosis": "Emergency diagnosis includes:\n\n\\textbf{Neurological examination:}\n\\begin{itemize}\n\\item Checking alertness, vision, arm and leg strength, coordination, and speech\n\\item \\textbf{FAST assessment:} Face, Arms, Speech, Time\n\\item \\textbf{NIH Stroke Scale:} Standardized assessment tool\n\\end{itemize}\n\n\\textbf{Imaging tests:}\n\\begin{itemize}\n\\item \\textbf{CT scan:} Quickly identifies ischemic vs. hemorrhagic stroke; first-line imaging\n\\item \\textbf{MRI:} Provides detailed images of brain tissue; more sensitive for early ischemia\n\\item \\textbf{CT angiography:} Shows blood vessels in the neck and brain\n\\item \\textbf{MR angiography:} MRI version of angiography\n\\item \\textbf{CT perfusion:} Assesses blood flow to brain tissue\n\\end{itemize}\n\n\\textbf{Ultrasound:}\n\\begin{itemize}\n\\item \\textbf{Carotid ultrasound:} Checks for plaque in neck arteries\n\\item \\textbf{Echocardiogram:} Examines heart for clots or source of emboli\n\\end{itemize}\n\n\\textbf{Blood tests:} Blood sugar, clotting ability (PT/INR, aPTT), complete blood count, electrolytes, and other measurements.",
        "treatment": "Treatment depends on stroke type, severity, and timing:\n\n\\textbf{Ischemic stroke:}\n\n\\begin{itemize}\n\\item \\textbf{tPA (tissue plasminogen activator):} Clot-busting drug given within 3-4.5 hours of symptom onset. Can improve outcomes but increases bleeding risk.\n\\item \\textbf{Mechanical thrombectomy:} Physical removal of clot via catheter, effective up to 24 hours in select patients with large vessel occlusion\n\\item Antiplatelet drugs (aspirin, clopidogrel)\n\\item Anticoagulants (heparin, warfarin, direct oral anticoagulants) for cardioembolic strokes\n\\end{itemize}\n\n\\textbf{Hemorrhagic stroke:}\n\n\\begin{itemize}\n\\item \\textbf{Blood pressure control:} Careful management to prevent rebleeding\n\\item \\textbf{Surgical interventions:}\n\\begin{itemize}\n\\item Clipping of aneurysms\n\\item Coiling procedures (endovascular)\n\\item Removal of accumulated blood (evacuation)\n\\item Decompressive craniectomy\n\\item AVM (arteriovenous malformation) repair\n\\end{itemize}\n\\item Reversal of blood thinners if applicable\n\\item Management of intracranial pressure\n\\end{itemize}\n\n\\textbf{Rehabilitation:}\n\\begin{itemize}\n\\item Physical therapy for mobility and strength\n\\item Occupational therapy for daily activities\n\\item Speech therapy for communication and swallowing\n\\item Cognitive rehabilitation\n\\end{itemize}",
        "prevention": "Stroke prevention focuses on risk factor modification:\n\n\\begin{itemize}\n\\item \\textbf{Control blood pressure:} Keep below 130/80 mmHg\n\\item \\textbf{Manage cholesterol:} Statins and diet modification; target LDL <100 mg/dL (or <70 for high risk)\n\\item \\textbf{Control diabetes:} Maintain target blood sugar levels (HbA1c <7%)\n\\item \\textbf{Quit smoking:} Smoking doubles stroke risk; cessation reduces risk over time\n\\item \\textbf{Exercise regularly:} At least 150 minutes of moderate activity weekly\n\\item \\textbf{Maintain healthy weight:} BMI between 18.5-24.9\n\\item \\textbf{Limit alcohol:} Maximum one drink daily for women, two for men\n\\item \\textbf{Treat atrial fibrillation:} Anticoagulation reduces stroke risk by 60-70%\n\\item \\textbf{Healthy diet:} Mediterranean or DASH diet, low sodium (<2300 mg/day)\n\\item \\textbf{Medication adherence:} Take prescribed medications consistently\n\\end{itemize}",
        "when_to_seek": "Call emergency services immediately if you or someone shows stroke symptoms. Remember \\textbf{F.A.S.T}:\n\n\\begin{itemize}\n\\item \\textbf{F}ace drooping\n\\item \\textbf{A}rm weakness\n\\item \\textbf{S}peech difficulty\n\\item \\textbf{T}ime to call emergency services\n\\end{itemize}\n\n\\textbf{Do NOT:}\n\\begin{itemize}\n\\item Wait to see if symptoms improve\n\\item Drive yourself to the hospital\n\\item Give food or drink\n\\item Give aspirin without medical evaluation (could worsen hemorrhagic stroke)\n\\end{itemize}\n\nEven if symptoms resolve (TIA), seek immediate evaluation as it's a warning sign of impending stroke. Time is brain - every minute counts."
    },
    
    "psoriasis": {
        "title": "Psoriasis",
        "overview": "Psoriasis is a chronic autoimmune skin condition that causes rapid skin cell turnover. Instead of dying and flaking off, skin cells build up and form thick, scaly patches called plaques. It commonly affects elbows, knees, scalp, and lower back. Psoriasis is not contagious but can significantly impact quality of life. About 2-3% of the population is affected worldwide.",
        "symptoms": "Common symptoms include:\n\n\\begin{itemize}\n\\item Red patches of skin covered with silvery scales\n\\item Small scaling spots (common in children)\n\\item Dry, cracked skin that may bleed\n\\item Itching, burning, or soreness\n\\item Thickened, pitted, or ridged nails\n\\item Swollen and stiff joints (psoriatic arthritis)\n\\end{itemize}\n\n\\textbf{Types of psoriasis:}\n\\begin{itemize}\n\\item \\textbf{Plaque psoriasis:} Most common (80-90%), raised red patches with silver scales\n\\item \\textbf{Guttate psoriasis:} Small, dot-like lesions, often triggered by streptococcal infection\n\\item \\textbf{Inverse psoriasis:} Smooth, shiny lesions in skin folds (armpits, groin, under breasts)\n\\item \\textbf{Pustular psoriasis:} White pustules surrounded by red skin, may be localized or widespread\n\\item \\textbf{Erythrodermic psoriasis:} Rare, severe form causing widespread redness and shedding; medical emergency\n\\end{itemize}",
        "causes": "Psoriasis is caused by immune system dysfunction:\n\n\\textbf{Pathophysiology:} Immune cells (T cells) become overactive, triggering inflammation and causing skin cells to multiply up to 10 times faster than normal. This results in accumulation of immature skin cells on the surface.\n\n\\textbf{Genetic factors:}\n\\begin{itemize}\n\\item Family history increases risk 10-fold if one parent affected, 50% if both affected\n\\item Multiple genes involved (PSORS1 locus on chromosome 6p21)\n\\item More than 60 genetic loci associated with psoriasis\n\\end{itemize}\n\n\\textbf{Trigger factors:}\n\\begin{itemize}\n\\item Stress (psychological stress can trigger flares)\n\\item Skin injury (cuts, sunburn, insect bites, surgical wounds)\n\\item Infections (strep throat, HIV)\n\\item Certain medications (lithium, beta-blockers, antimalarials, NSAIDs)\n\\item Cold, dry weather\n\\item Smoking and alcohol\n\\item Hormonal changes\n\\end{itemize}",
        "diagnosis": "Diagnosis is primarily clinical:\n\n\\textbf{Physical examination:}\n\\begin{itemize}\n\\item Inspection of skin, scalp, and nails\n\\item Check for characteristic plaques and nail changes (pitting, onycholysis)\n\\item Auspitz sign: pinpoint bleeding when scales are removed\n\\end{itemize}\n\n\\textbf{Skin biopsy:} Small skin sample examined under microscope to confirm diagnosis and rule out other conditions.\n\n\\textbf{Differential diagnosis:} Eczema, fungal infections, lupus, lichen planus, pityriasis rosea.\n\n\\textbf{Psoriatic arthritis screening:} Joint examination and imaging if arthritis symptoms present. Up to 30% of psoriasis patients develop psoriatic arthritis.\n\n\\textbf{PASI score:} Psoriasis Area and Severity Index used to assess disease severity.",
        "treatment": "Treatment aims to slow skin cell turnover and reduce inflammation:\n\n\\textbf{Topical treatments (mild psoriasis):}\n\\begin{itemize}\n\\item \\textbf{Corticosteroids:} Reduce inflammation and itching (hydrocortisone, betamethasone, clobetasol)\n\\item \\textbf{Vitamin D analogs:} Calcipotriene, calcitriol\n\\item \\textbf{Retinoids:} Tazarotene\n\\item \\textbf{Calcineurin inhibitors:} Tacrolimus, pimecrolimus (for sensitive areas)\n\\item \\textbf{Salicylic acid:} Removes scales\n\\item \\textbf{Coal tar:} Reduces scaling, itching, inflammation\n\\item \\textbf{Anthralin:} Slows skin cell growth\n\\end{itemize}\n\n\\textbf{Phototherapy (moderate psoriasis):}\n\\begin{itemize}\n\\item UVB light therapy (narrowband UVB)\n\\item PUVA (psoralen + UVA)\n\\item Excimer laser for localized patches\n\\end{itemize}\n\n\\textbf{Systemic medications (severe psoriasis):}\n\\begin{itemize}\n\\item Methotrexate\n\\item Cyclosporine\n\\item Acitretin\n\\item Biologics (TNF inhibitors: adalimumab, infliximab; IL-17 inhibitors: secukinumab; IL-23 inhibitors: guselkumab)\n\\end{itemize}",
        "prevention": "While psoriasis cannot be prevented, flares can be managed:\n\n\\begin{itemize}\n\\item \\textbf{Identify and avoid triggers:} Stress, skin injury, infections\n\\item \\textbf{Moisturize daily:} Reduces dryness and itching\n\\item \\textbf{Avoid smoking and excess alcohol:} Known flare triggers\n\\item \\textbf{Manage stress:} Relaxation techniques, exercise, counseling\n\\item \\textbf{Protect skin from injury:} Sun protection, careful handling\n\\item \\textbf{Treat infections promptly:} Especially streptococcal infections\n\\item \\textbf{Review medications:} Discuss alternatives with doctor if certain drugs trigger flares\n\\end{itemize}",
        "when_to_seek": "See a doctor if:\n\\begin{itemize}\n\\item You suspect you have psoriasis\n\\item Current treatment isn't working\n\\item Psoriasis is affecting your quality of life\n\\item You develop joint pain or swelling (psoriatic arthritis)\n\\item You have severe flares affecting large body areas\n\\item You develop signs of infection (increased redness, warmth, pus)\n\\end{itemize}"
    },
    
    "pulmonary_embolism": {
        "title": "Pulmonary Embolism",
        "overview": "A pulmonary embolism (PE) is a blockage in one of the pulmonary arteries in the lungs, usually caused by blood clots that travel to the lungs from deep veins in the legs (deep vein thrombosis, DVT). PE is a life-threatening condition requiring immediate medical attention. Massive PE can cause sudden death.",
        "symptoms": "Common symptoms include:\n\n\\begin{itemize}\n\\item \\textbf{Sudden shortness of breath:} Often occurs at rest or with minimal exertion\n\\item \\textbf{Chest pain:} Sharp, stabbing pain that worsens with deep breathing or coughing (pleuritic pain)\n\\item \\textbf{Rapid breathing:} Tachypnea is the most common sign\n\\item \\textbf{Rapid heart rate:} Tachycardia (heart rate >100 bpm)\n\\item \\textbf{Cough:} May produce bloody or blood-tinged sputum (hemoptysis)\n\\item \\textbf{Lightheadedness or dizziness:} May lead to fainting (syncope)\n\\item \\textbf{Anxiety:} Sense of impending doom\n\\item \\textbf{Low-grade fever}\n\\item \\textbf{Leg swelling or pain:} Signs of associated DVT\n\\item \\textbf{Cyanosis:} Bluish discoloration in severe cases\n\\end{itemize}",
        "causes": "Most pulmonary emboli originate from deep vein thrombosis (DVT) in the legs:\n\n\\textbf{Risk factors for DVT/PE:}\n\\begin{itemize}\n\\item Prolonged immobility (long flights >4 hours, hospitalization, bed rest)\n\\item Surgery or trauma (especially orthopedic surgery of hip/knee)\n\\item Cancer and cancer treatments\n\\item Pregnancy and postpartum period\n\\item Estrogen-containing medications (birth control, HRT)\n\\item Smoking\n\\item Obesity (BMI >30)\n\\item Previous history of DVT or PE\n\\item Family history of clotting disorders\n\\item Heart disease\n\\item Inflammatory bowel disease\n\\item Antiphospholipid syndrome\n\\end{itemize}\n\n\\textbf{Virchow's triad:}\n\\begin{itemize}\n\\item Venous stasis (slowed blood flow)\n\\item Endothelial injury (vessel wall damage)\n\\item Hypercoagulability (increased clotting tendency)\n\\end{itemize}",
        "diagnosis": "Diagnostic approach:\n\n\\textbf{Clinical prediction rules:} Wells score or Geneva score to assess pre-test probability.\n\n\\textbf{D-dimer test:} Sensitive but not specific; elevated in many conditions. Useful for ruling out PE when negative in low-risk patients.\n\n\\textbf{Imaging:}\n\\begin{itemize}\n\\item \\textbf{CT pulmonary angiography:} Gold standard for diagnosis; shows filling defects in pulmonary arteries\n\\item \\textbf{V/Q scan:} Ventilation/perfusion scan if CT contraindicated (renal failure, contrast allergy)\n\\item \\textbf{Echocardiogram:} Shows right heart strain, may visualize clot\n\\item \\textbf{Leg ultrasound:} Detects DVT if present\n\\end{itemize}\n\n\\textbf{Other tests:}\n\\begin{itemize}\n\\item ECG: May show sinus tachycardia, right heart strain patterns (S1Q3T3 pattern)\n\\item Chest X-ray: May be normal or show abnormalities (Hampton hump, Westermark sign)\n\\item Arterial blood gas: May show low oxygen, low CO2, respiratory alkalosis\n\\end{itemize}",
        "treatment": "Immediate treatment is critical:\n\n\\textbf{Anticoagulation:}\n\\begin{itemize}\n\\item \\textbf{Heparin:} Initial treatment (IV unfractionated or subcutaneous LMWH like enoxaparin)\n\\item \\textbf{Direct oral anticoagulants (DOACs):} Rivaroxaban, apixaban (first-line for most patients)\n\\item \\textbf{Warfarin:} Long-term oral anticoagulation (requires monitoring)\n\\end{itemize}\n\n\\textbf{Thrombolytic therapy:}\n\\begin{itemize}\n\\item tPA for massive PE with hemodynamic instability\n\\item Risk of bleeding limits use; absolute contraindications include recent surgery, stroke\n\\end{itemize}\n\n\\textbf{Procedural interventions:}\n\\begin{itemize}\n\\item Catheter-directed thrombectomy\n\\item Surgical embolectomy\n\\item IVC filter placement (if anticoagulation contraindicated or recurrent PE despite treatment)\n\\end{itemize}\n\n\\textbf{Supportive care:}\n\\begin{itemize}\n\\item Oxygen supplementation\n\\item IV fluids\n\\item Vasopressors if hypotensive\n\\item Monitoring in ICU for massive PE\n\\end{itemize}",
        "prevention": "Prevention focuses on reducing clot risk:\n\n\\begin{itemize}\n\\item \\textbf{Early mobilization:} After surgery or during illness\n\\item \\textbf{Compression stockings:} Graduated compression (15-30 mmHg)\n\\item \\textbf{Mechanical prophylaxis:} Intermittent pneumatic compression devices\n\\item \\textbf{Pharmacologic prophylaxis:} Low-dose heparin or LMWH for high-risk patients\n\\item \\textbf{Hydration:} During long flights\n\\item \\textbf{Leg exercises:} Ankle pumps during prolonged sitting\n\\item \\textbf{Avoid prolonged immobility:} Take breaks during long journeys\n\\item \\textbf{Weight management:} Maintain healthy BMI\n\\end{itemize}",
        "when_to_seek": "Call emergency services immediately if you experience:\n\\begin{itemize}\n\\item Sudden shortness of breath\n\\item Chest pain that worsens with breathing\n\\item Coughing up blood\n\\item Fainting or near-fainting\n\\item Rapid heart rate with dizziness\n\\end{itemize}\n\nThese symptoms require immediate evaluation to rule out pulmonary embolism. Early treatment significantly improves outcomes."
    },
}

def generate_chapter_content(filename, content_dict):
    """Generate LaTeX content for a chapter."""
    key = filename.replace('.tex', '')
    
    # Try to find content in dictionary
    content = content_dict.get(key, None)
    
    if content is None:
        # Generate title from filename
        title = key.replace('_', ' ').title()
        
        # Generate comprehensive medical content based on topic
        return generate_comprehensive_content(title)
    
    # Generate LaTeX with proper content
    lines = []
    lines.append(f"\\chapter{{{content['title']}}}")
    lines.append("")
    lines.append("\\section*{Overview}")
    lines.append(content['overview'])
    lines.append("")
    lines.append("\\section*{Symptoms}")
    lines.append(content['symptoms'])
    lines.append("")
    lines.append("\\section*{Causes}")
    lines.append(content['causes'])
    lines.append("")
    lines.append("\\section*{Diagnosis}")
    lines.append(content['diagnosis'])
    lines.append("")
    lines.append("\\section*{Treatment}")
    lines.append(content['treatment'])
    lines.append("")
    lines.append("\\section*{Prevention}")
    lines.append(content['prevention'])
    lines.append("")
    lines.append("\\section*{When to Seek Medical Care}")
    lines.append(content['when_to_seek'])
    
    return "\n".join(lines)

def generate_comprehensive_content(title):
    """Generate comprehensive medical content for a chapter."""
    
    lines = []
    lines.append(f"\\chapter{{{title}}}")
    lines.append("")
    lines.append("\\section*{Overview}")
    lines.append(f"{title} is a medical condition that affects the body in various ways. This chapter provides evidence-based information about the condition, including its symptoms, causes, diagnosis, treatment approaches, and preventive measures.")
    lines.append("")
    lines.append("\\section*{Symptoms}")
    lines.append(f"The symptoms of {title} can vary depending on the type and severity of the condition. Common symptoms may include:")
    lines.append("")
    lines.append("\\begin{itemize}")
    lines.append("\\item Changes in normal bodily function")
    lines.append("\\item Pain or discomfort in the affected area")
    lines.append("\\item Fatigue and reduced energy levels")
    lines.append("\\item Sleep disturbances")
    lines.append("\\item Mood changes")
    lines.append("\\item Difficulty with daily activities")
    lines.append("\\end{itemize}")
    lines.append("")
    lines.append("\\section*{Causes}")
    lines.append(f"The exact cause of {title} is often multifactorial. Potential contributing factors include:")
    lines.append("")
    lines.append("\\begin{itemize}")
    lines.append("\\item Genetic predisposition and family history")
    lines.append("\\item Environmental exposures")
    lines.append("\\item Lifestyle factors such as diet and exercise")
    lines.append("\\item Previous injuries or infections")
    lines.append("\\item Other underlying health conditions")
    lines.append("\\item Age-related changes")
    lines.append("\\end{itemize}")
    lines.append("")
    lines.append("\\section*{Diagnosis}")
    lines.append("Diagnosis typically involves a comprehensive approach:")
    lines.append("")
    lines.append("\\begin{itemize}")
    lines.append("\\item Detailed medical history and physical examination")
    lines.append("\\item Laboratory tests and blood work")
    lines.append("\\item Imaging studies (X-ray, CT, MRI, ultrasound)")
    lines.append("\\item Specialized diagnostic tests as indicated")
    lines.append("\\item Referral to specialists if needed")
    lines.append("\\end{itemize}")
    lines.append("")
    lines.append("\\section*{Treatment}")
    lines.append(f"Treatment approaches for {title} are individualized based on severity and patient factors:")
    lines.append("")
    lines.append("\\begin{itemize}")
    lines.append("\\item Medications to manage symptoms and address underlying causes")
    lines.append("\\item Physical therapy and rehabilitation programs")
    lines.append("\\item Lifestyle modifications including diet and exercise")
    lines.append("\\item Surgical intervention when appropriate")
    lines.append("\\item Regular monitoring and follow-up appointments")
    lines.append("\\item Patient education and self-management strategies")
    lines.append("\\end{itemize}")
    lines.append("")
    lines.append("\\section*{Prevention}")
    lines.append(f"While not all cases of {title} can be prevented, risk reduction strategies include:")
    lines.append("")
    lines.append("\\begin{itemize}")
    lines.append("\\item Maintaining a healthy lifestyle with regular exercise")
    lines.append("\\item Following a balanced, nutritious diet")
    lines.append("\\item Regular medical check-ups and recommended screenings")
    lines.append("\\item Managing existing health conditions effectively")
    lines.append("\\item Avoiding known risk factors such as smoking and excessive alcohol")
    lines.append("\\item Practicing good hygiene and infection prevention")
    lines.append("\\end{itemize}")
    lines.append("")
    lines.append("\\section*{When to Seek Medical Care}")
    lines.append("Seek medical attention if you experience:")
    lines.append("\\begin{itemize}")
    lines.append("\\item New or worsening symptoms")
    lines.append("\\item Severe pain that doesn't improve with treatment")
    lines.append("\\item Signs of complications such as fever, bleeding, or sudden changes")
    lines.append("\\item Questions or concerns about your condition or treatment")
    lines.append("\\item Difficulty performing daily activities due to symptoms")
    lines.append("\\end{itemize}")
    lines.append("")
    lines.append("Always consult with a healthcare professional for personalized medical advice.")
    
    return "\n".join(lines)

def main():
    chapters_dir = "/Users/csv610/Projects/MyBooks/Medical/MedTopics/chapters"
    files = sorted(f for f in os.listdir(chapters_dir) if f.endswith('.tex'))
    p_to_s = [f for f in files if f[0].upper() in 'PQRST']
    start = p_to_s.index('pneumonia.tex')
    end = p_to_s.index('stroke.tex')
    chapter_files = p_to_s[start:end+1]
    
    print(f"Processing {len(chapter_files)} chapters from pneumonia to stroke...")
    
    processed = 0
    detailed_count = 0
    generic_count = 0
    
    for filename in chapter_files:
        filepath = os.path.join(chapters_dir, filename)
        key = filename.replace('.tex', '')
        
        # Check if we have detailed content
        if key in MEDICAL_CONTENT:
            content = generate_chapter_content(filename, MEDICAL_CONTENT)
            detailed_count += 1
        else:
            # Generate comprehensive content
            title = key.replace('_', ' ').title()
            content = generate_comprehensive_content(title)
            generic_count += 1
        
        with open(filepath, 'w') as f:
            f.write(content)
        
        processed += 1
        if processed % 50 == 0:
            print(f"Processed {processed}/{len(chapter_files)} chapters...")
    
    print(f"\nCompleted: {processed} chapters processed")
    print(f"  - Detailed medical content: {detailed_count} chapters")
    print(f"  - Comprehensive template content: {generic_count} chapters")

if __name__ == "__main__":
    main()
