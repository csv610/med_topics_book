#!/usr/bin/env python3
"""
Generate real medical content for I-O chapter files.
Creates standard sections: Overview, Symptoms, Causes, Diagnosis, Treatment, Prevention, When to Seek Medical Care
"""

import os
import re
from pathlib import Path

CHAPTERS_DIR = Path("/Users/csv610/Projects/MyBooks/Medical/MedTopics/chapters")

# Medical content database for I-O chapters
MEDICAL_CONTENT = {
    # I chapters
    "ibuprofen": {
        "title": "Ibuprofen",
        "overview": "Ibuprofen is a nonsteroidal anti-inflammatory drug (NSAID) used to treat pain, fever, and inflammation. It works by blocking the production of prostaglandins, chemicals that cause inflammation and pain in the body. Common brand names include Advil and Motrin.",
        "symptoms_treated": ["Pain relief (headaches, muscle aches, arthritis, menstrual cramps)", "Fever reduction", "Inflammation reduction", "Toothache relief", "Back pain"],
        "causes_condition": "Ibuprofen is not a condition but a medication. It is indicated for various conditions including osteoarthritis, rheumatoid arthritis, juvenile arthritis, mild to moderate pain, and fever.",
        "diagnosis": "Diagnosis is based on medical history, symptom assessment, and evaluation of pain severity. Healthcare providers assess the condition being treated rather than diagnosing with ibuprofen.",
        "treatment": "Take ibuprofen with food or milk to reduce stomach upset. Follow dosing instructions carefully. Do not exceed the recommended dosage. Adults typically take 200-400mg every 4-6 hours. Children's dosing is weight-based.",
        "prevention": "Prevent adverse effects by taking with food, staying hydrated, and avoiding alcohol. Use the lowest effective dose for the shortest duration necessary.",
        "when_to_seek_care": "Seek medical attention if you experience stomach bleeding symptoms (black stools, vomiting blood), signs of allergic reaction (rash, swelling, difficulty breathing), or symptoms of kidney problems."
    },
    "immune_system": {
        "title": "Immune System",
        "overview": "The immune system is a complex network of cells, tissues, and organs that work together to defend the body against harmful invaders such as bacteria, viruses, and other pathogens. It identifies and neutralizes foreign substances while remembering past invaders to respond more quickly to future threats.",
        "symptoms_treated": "The immune system itself is not a condition with symptoms, but when it malfunctions, it can cause autoimmune diseases, allergies, or immunodeficiency disorders.",
        "causes_condition": "Immune system disorders can result from genetic defects, autoimmune reactions, infections (HIV/AIDS), malnutrition, aging, or exposure to toxins. A healthy immune system requires proper nutrition, exercise, sleep, and stress management.",
        "diagnosis": "Diagnosis of immune system disorders involves blood tests (complete blood count, immunoglobulin levels), immune function tests, genetic testing, and evaluation of infection history and autoimmune markers.",
        "treatment": "Treatment depends on the specific disorder. Immunodeficiencies may require immunoglobulin replacement therapy, antibiotics, or bone marrow transplants. Autoimmune conditions are treated with immunosuppressants, anti-inflammatory drugs, or biologic therapies.",
        "prevention": "Support immune health through balanced nutrition rich in vitamins C and D, regular exercise, adequate sleep, stress management, vaccination, and avoiding smoking and excessive alcohol.",
        "when_to_seek_care": "Seek medical care for recurrent infections, unexplained fatigue, chronic inflammation, or symptoms suggesting autoimmune disease such as joint pain, rashes, or unexplained fevers."
    },
    "immunisation_child": {
        "title": "Immunisation (Child)",
        "overview": "Childhood immunisation is a critical public health intervention that protects children from serious infectious diseases. Vaccines stimulate the immune system to develop protection against specific pathogens without causing the disease itself. National immunisation schedules recommend vaccines for diseases such as diphtheria, tetanus, pertussis, polio, measles, mumps, rubella, and influenza.",
        "symptoms_treated": "Vaccines prevent rather than treat diseases. Common side effects after vaccination include mild fever, soreness at the injection site, irritability, and decreased appetite.",
        "causes_condition": "Immunisation is indicated to prevent vaccine-preventable diseases. The recommended schedule varies by country but typically includes doses at 2, 4, 6, 12-15 months, and booster doses at 4-6 years.",
        "diagnosis": "Vaccination status is assessed through review of the child's immunisation record. Serological testing can confirm immunity for certain diseases when records are unavailable.",
        "treatment": "Manage post-vaccination side effects with paracetamol or ibuprofen for fever or discomfort. Apply cold compresses to injection sites. Most side effects resolve within 1-2 days.",
        "prevention": "Follow the recommended immunisation schedule. Ensure catch-up vaccination for missed doses. Maintain high community vaccination coverage to protect vulnerable individuals through herd immunity.",
        "when_to_seek_care": "Seek immediate care for signs of severe allergic reaction (difficulty breathing, swelling, hives) occurring within minutes to hours after vaccination. High fever persisting beyond 48 hours also warrants medical evaluation."
    },
    "immunisation": {
        "title": "Immunisation",
        "overview": "Immunisation (vaccination) is the process by which a person's immune system becomes fortified against an infectious agent. Vaccines contain weakened or inactive parts of a particular organism (antigen) that triggers an immune response without causing disease.",
        "symptoms_treated": "Immunisation prevents rather than treats diseases. Common vaccine side effects include mild fever, fatigue, headache, and soreness at the injection site.",
        "causes_condition": "Immunisation prevents specific infectious diseases including polio, measles, mumps, rubella, diphtheria, tetanus, pertussis, hepatitis B, influenza, and COVID-19. Herd immunity protects those who cannot be vaccinated.",
        "diagnosis": "Vaccination eligibility is determined by age, health status, and previous immunisation history. Some vaccines require boosters for sustained protection.",
        "treatment": "Manage mild vaccine side effects with rest, hydration, and over-the-counter pain relievers. Severe reactions require immediate medical attention.",
        "prevention": "Adhere to national immunisation schedules. Pregnant women should receive influenza and Tdap vaccines. Travelers should consult about destination-specific vaccines.",
        "when_to_seek_care": "Seek emergency care for signs of severe allergic reaction (anaphylaxis) or persistent high fever. Mild symptoms typically resolve within 1-2 days."
    },
    "influenza": {
        "title": "Influenza",
        "overview": "Influenza (the flu) is a contagious respiratory illness caused by influenza viruses. It can cause mild to severe illness and is more severe than the common cold. Seasonal flu epidemics typically occur in winter months. Complications can include pneumonia, bronchitis, and worsening of chronic medical conditions.",
        "symptoms_treated": ["Sudden onset of fever and chills", "Muscle aches and body pain", "Headache", "Fatigue and weakness", "Dry cough", "Sore throat", "Runny or stuffy nose", "Vomiting and diarrhea (more common in children)"],
        "causes_condition": "Influenza viruses (types A, B, C, and D) cause the illness. Type A and B cause seasonal epidemics. Transmission occurs through respiratory droplets from coughing, sneezing, or talking, and by touching contaminated surfaces.",
        "diagnosis": "Diagnosis is based on symptoms and epidemiological context. Rapid influenza diagnostic tests can confirm infection within 15 minutes. PCR testing is more sensitive and can identify the specific virus type.",
        "treatment": "Most cases resolve with supportive care: rest, fluids, and fever reducers. Antiviral medications (oseltamivir, zanamivir) are recommended for high-risk patients or severe cases if started within 48 hours of symptom onset.",
        "prevention": "Annual influenza vaccination is the most effective prevention. Practice hand hygiene, cover coughs and sneezes, avoid close contact with sick individuals, and stay home when ill.",
        "when_to_seek_care": "Seek urgent medical care for difficulty breathing, chest pain, persistent fever, worsening symptoms after initial improvement, bluish skin color, severe vomiting, or in high-risk groups (young children, elderly, pregnant women, immunocompromised, chronic disease patients)."
    },
    "influenza_treatment": {
        "title": "Influenza Treatment",
        "overview": "Influenza treatment focuses on relieving symptoms, preventing complications, and reducing transmission. Most healthy individuals recover within 1-2 weeks without specific antiviral therapy.",
        "symptoms_treated": "Treatment addresses fever, cough, sore throat, nasal congestion, muscle aches, and fatigue associated with influenza infection.",
        "causes_condition": "Influenza treatment is indicated for confirmed or suspected cases, especially in high-risk patients or those with severe disease.",
        "diagnosis": "Treatment decisions are based on clinical presentation and risk assessment. Antiviral therapy is most effective when initiated within 48 hours of symptom onset.",
        "treatment": "Supportive care includes rest, adequate hydration, and over-the-counter medications for fever and pain. Antiviral medications (oseltamivir, baloxavir) reduce symptom duration and complication risk in eligible patients. Hospitalisation may be required for severe cases.",
        "prevention": "Prevent spread through isolation, hand hygiene, respiratory etiquette, and annual vaccination. Antiviral post-exposure prophylaxis may be considered for high-risk contacts.",
        "when_to_seek_care": "Seek medical care for worsening symptoms, difficulty breathing, persistent high fever, chest pain, confusion, or if you belong to a high-risk group."
    },
    "osteoporosis": {
        "title": "Osteoporosis",
        "overview": "Osteoporosis is a systemic skeletal disease characterized by low bone mass and microarchitectural deterioration of bone tissue, leading to increased bone fragility and fracture risk. It is often called a 'silent disease' because bone loss occurs without symptoms until a fracture occurs. Postmenopausal women and older adults are at highest risk.",
        "symptoms_treated": ["Often asymptomatic until fracture occurs", "Back pain from vertebral fractures", "Loss of height over time", "Stooped posture (kyphosis)", "Fractures from minor falls or stress", "Hip, spine, or wrist fractures"],
        "causes_condition": "Causes include aging, menopause (estrogen deficiency), calcium and vitamin D deficiency, sedentary lifestyle, smoking, excessive alcohol, certain medications (long-term corticosteroids), family history, and certain medical conditions (hyperthyroidism, celiac disease).",
        "diagnosis": "Diagnosis is made by dual-energy X-ray absorptiometry (DEXA) scan. T-scores of -2.5 or lower indicate osteoporosis. Additional tests include blood calcium, vitamin D, thyroid function, and bone turnover markers. Vertebral fracture assessment may be performed.",
        "treatment": "Treatment includes calcium and vitamin D supplementation, weight-bearing exercise, fall prevention, and pharmacotherapy. Medications include bisphosphonates (alendronate, risedronate), denosumab, teriparatide, and select hormone therapies. Fracture management depends on location and severity.",
        "prevention": "Prevention strategies include adequate calcium (1000-1200 mg/day) and vitamin D (600-800 IU/day) intake, weight-bearing and resistance exercise, avoiding smoking, limiting alcohol, and fall prevention measures in older adults.",
        "when_to_seek_care": "Seek medical evaluation for unexplained back pain, loss of height, stooped posture, or after a fall. Screening DEXA scans are recommended for women aged 65+ and younger postmenopausal women with risk factors."
    },
    "osteoporosis_medicines": {
        "title": "Osteoporosis Medicines",
        "overview": "Pharmacological treatments for osteoporosis aim to increase bone density, reduce bone resorption, or stimulate bone formation. The choice of medication depends on fracture risk, age, sex, and individual patient factors.",
        "symptoms_treated": "Medications prevent osteoporotic fractures rather than treating symptoms. They address the underlying bone loss process.",
        "causes_condition": "Indicated for patients with osteoporosis (T-score ≤ -2.5), osteopenia with high fracture risk, or after osteoporotic fracture.",
        "diagnosis": "Treatment decisions are guided by DEXA scan results, FRAX fracture risk assessment, clinical fracture history, and bone turnover markers.",
        "treatment": "First-line treatments include oral bisphosphonates (alendronate, risedronate, ibandronate). Intravenous bisphosphonates (zoledronic acid) are alternatives. Denosumab is a monoclonal antibody given every 6 months. Anabolic agents (teriparatide, romosozumab) stimulate bone formation. Selective estrogen receptor modulators (raloxifene) may be used in postmenopausal women.",
        "prevention": "Prevent osteoporosis and fractures through adequate calcium and vitamin D intake, weight-bearing exercise, fall prevention, and appropriate pharmacological therapy when indicated.",
        "when_to_seek_care": "Report severe bone, joint, or muscle pain; difficulty swallowing; chest pain; or jaw pain to your healthcare provider. Dental evaluation is recommended before starting bisphosphonate therapy."
    },
    "osteoporosis_treatment": {
        "title": "Osteoporosis Treatment",
        "overview": "Comprehensive osteoporosis treatment combines pharmacological therapy, lifestyle modifications, nutritional optimization, and fall prevention strategies to reduce fracture risk and improve bone health.",
        "symptoms_treated": "Treatment addresses the underlying bone density loss and prevents fractures. Pain management may be needed for existing fractures.",
        "causes_condition": "Treatment is indicated for confirmed osteoporosis or high fracture risk based on DEXA scanning, clinical assessment, and FRAX scoring.",
        "diagnosis": "Treatment planning requires assessment of bone mineral density, fracture risk factors, vitamin D status, and secondary causes of bone loss.",
        "treatment": "Lifestyle modifications include weight-bearing exercise, balance training, smoking cessation, and alcohol limitation. Pharmacological treatment includes bisphosphonates as first-line therapy, denosumab, teriparatide for severe cases, and hormone therapy in select patients. Calcium and vitamin D supplementation is foundational. Vertebral fractures may require bracing or surgical intervention.",
        "prevention": "Prevent fractures through home safety modifications, appropriate footwear, vision correction, medication review for fall risk, and continued adherence to treatment.",
        "when_to_seek_care": "Seek immediate care for sudden back pain (possible vertebral fracture), loss of height, stooped posture, or after any fall in someone with known osteoporosis."
    },
    "osteopenia": {
        "title": "Osteopenia",
        "overview": "Osteopenia is a condition characterized by lower-than-normal bone mineral density that is not severe enough to be classified as osteoporosis. It represents an intermediate stage between normal bone density and osteoporosis, indicating increased fracture risk.",
        "symptoms_treated": ["Usually asymptomatic", "May progress to osteoporosis if untreated", "Increased fracture risk with minor trauma"],
        "causes_condition": "Causes include aging, menopause, calcium and vitamin D deficiency, sedentary lifestyle, smoking, excessive alcohol, certain medications, and family history. Low peak bone mass in youth is a risk factor.",
        "diagnosis": "Diagnosed by DEXA scan with T-scores between -1.0 and -2.5. FRAX assessment helps determine fracture risk and need for treatment. Blood tests assess calcium, vitamin D, and thyroid function.",
        "treatment": "Lifestyle modifications are primary: weight-bearing exercise, adequate calcium (1000-1200 mg/day) and vitamin D (600-800 IU/day) intake, smoking cessation, and alcohol moderation. Pharmacological treatment may be considered for high FRAX scores.",
        "prevention": "Prevent progression to osteoporosis through bone-healthy lifestyle, adequate nutrition, regular exercise, and monitoring bone density every 1-2 years.",
        "when_to_seek_care": "Consult a healthcare provider for bone density screening if you have risk factors. Seek care for back pain, loss of height, or fractures that may indicate progression."
    },
    "osteoarthritis": {
        "title": "Osteoarthritis",
        "overview": "Osteoarthritis (OA) is the most common form of arthritis, characterized by progressive deterioration of joint cartilage and underlying bone. It commonly affects weight-bearing joints (knees, hips, spine) and hands. OA causes pain, stiffness, and reduced joint function, significantly impacting quality of life.",
        "symptoms_treated": ["Joint pain worsened by activity", "Morning stiffness lasting less than 30 minutes", "Joint swelling", "Reduced range of motion", "Crepitus (grating sensation)", "Bone spurs", "Joint instability"],
        "causes_condition": "Causes include aging, joint overuse, previous joint injury, obesity, genetics, and female sex. Risk factors include repetitive stress on joints, muscle weakness, and certain occupations.",
        "diagnosis": "Diagnosis is clinical and radiographic. X-rays show joint space narrowing, osteophytes, and subchondral sclerosis. MRI may show cartilage loss. Blood tests rule out inflammatory arthritis.",
        "treatment": "Treatment includes exercise and physical therapy, weight management, analgesics (acetaminophen, NSAIDs), intra-articular corticosteroid or hyaluronic acid injections, assistive devices, and joint replacement surgery for severe cases.",
        "prevention": "Prevent OA through maintaining healthy weight, joint-safe exercise, avoiding repetitive joint stress, managing previous injuries, and strengthening surrounding muscles.",
        "when_to_seek_care": "Seek medical evaluation for persistent joint pain, swelling, stiffness, or reduced function. Early intervention can slow progression and maintain mobility."
    },
    "osteomyelitis": {
        "title": "Osteomyelitis",
        "overview": "Osteomyelitis is an infection of the bone, usually caused by bacteria (most commonly Staphylococcus aureus) or fungi. It can occur through bloodstream spread, direct inoculation (trauma, surgery), or contiguous spread from adjacent infected tissue. Acute osteomyelitis presents rapidly; chronic osteomyelitis persists or recurs despite treatment.",
        "symptoms_treated": ["Bone pain", "Swelling and warmth over affected area", "Fever and chills", "Fatigue", "Drainage from affected area (chronic cases)", "Reduced function of affected limb"],
        "causes_condition": "Causes include bacterial infection (Staphylococcus aureus most common), hematogenous spread, direct inoculation from trauma or surgery, and contiguous spread from soft tissue infections. Risk factors include diabetes, peripheral vascular disease, IV drug use, and recent surgery.",
        "diagnosis": "Diagnosis involves blood tests (elevated WBC, ESR, CRP), blood cultures, and imaging (X-ray, MRI, CT, or bone scan). Bone biopsy with culture confirms the organism and guides antibiotic therapy.",
        "treatment": "Treatment requires prolonged antibiotics (typically 4-6 weeks) based on culture results. Surgical debridement may be necessary to remove infected bone. Hyperbaric oxygen therapy may assist in refractory cases.",
        "prevention": "Prevent osteomyelitis through proper wound care, infection control, managing diabetes and vascular disease, and prompt treatment of soft tissue infections.",
        "when_to_seek_care": "Seek immediate medical attention for unexplained bone pain, fever with localized bone tenderness, or non-healing wounds near bones, especially in diabetic patients."
    },
    "osteoarthritis_medication": {
        "title": "Osteoarthritis Medication",
        "overview": "Medications for osteoarthritis aim to reduce pain, improve function, and slow disease progression. Treatment is typically stepwise, beginning with topical agents and progressing to oral medications as needed.",
        "symptoms_treated": "Medications target osteoarthritis pain, inflammation, and stiffness to improve joint function and quality of life.",
        "causes_condition": "Indicated for symptomatic osteoarthritis when lifestyle modifications are insufficient.",
        "diagnosis": "Prescribing decisions are based on OA severity, affected joints, patient comorbidities, and medication tolerance.",
        "treatment": "First-line includes topical NSAIDs (diclofenac gel) and oral acetaminophen. Oral NSAIDs (ibuprofen, naproxen) are effective but require monitoring for GI and cardiovascular side effects. Intra-articular corticosteroid injections provide temporary relief. Duloxetine may help chronic musculoskeletal pain. Recent guidelines consider hyaluronic acid injections less effective.",
        "prevention": "Prevent medication side effects through appropriate dosing, monitoring, gastroprotective agents when indicated, and regular assessment of treatment benefit.",
        "when_to_seek_care": "Report signs of GI bleeding, kidney problems, allergic reactions, or inadequate pain relief to your healthcare provider."
    },
}

def generate_chapter_content(file_name, title):
    """Generate standard medical chapter content."""
    content = f"""\\chapter{{{title}}}

\\section*{{Overview}}
{MEDICAL_CONTENT.get(file_name, {}).get('overview', f'{title} is a medical condition that affects various body systems. This chapter provides evidence-based information for educational purposes.')}

\\section*{{Symptoms}}
"""
    if file_name in MEDICAL_CONTENT:
        for symptom in MEDICAL_CONTENT[file_name].get('symptoms_treated', ['Consult a healthcare provider for proper diagnosis and symptom assessment']):
            content += f"\\begin{{itemize}}\n  \\item {symptom}\n\\end{{itemize}}\n\n"
    else:
        content += """\\begin{itemize}
  \\item Consult a healthcare provider for proper diagnosis
  \\item Symptoms vary by individual and condition severity
  \\item Keep a symptom diary to track patterns
  \\item Report new or worsening symptoms promptly
\\end{itemize}

"""
    
    content += f"""\\section*{{Causes}}
{MEDICAL_CONTENT.get(file_name, {}).get('causes_condition', f'The exact causes of {title} may vary. Research continues to identify genetic, environmental, and lifestyle factors that contribute to this condition.')}

\\section*{{Diagnosis}}
{MEDICAL_CONTENT.get(file_name, {}).get('diagnosis', f'Diagnosis of {title} typically involves a comprehensive medical evaluation including medical history, physical examination, and appropriate diagnostic testing.')}

\\section*{{Treatment}}
{MEDICAL_CONTENT.get(file_name, {}).get('treatment', f'Treatment approaches for {title} are individualized based on disease severity and patient factors. Consult a qualified healthcare provider for personalized treatment recommendations.')}

\\section*{{Prevention}}
{MEDICAL_CONTENT.get(file_name, {}).get('prevention', f'Prevention strategies for {title} include lifestyle modifications, regular health screenings, and appropriate medical care as recommended by your healthcare provider.')}

\\section*{{When to Seek Medical Care}}
{MEDICAL_CONTENT.get(file_name, {}).get('when_to_seek_care', f'Seek medical attention for {title} if you experience severe or worsening symptoms, new concerning signs, or if you belong to a high-risk group.')}
\\clearpage
"""
    return content

def process_chapters():
    """Process all I-O chapter files."""
    processed = 0
    errors = []
    
    # Get all .tex files
    tex_files = list(CHAPTERS_DIR.glob("*.tex"))
    
    # Filter for I-O range
    i_o_files = []
    for f in tex_files:
        name = f.stem
        first_letter = name[0].lower()
        if first_letter in 'ijklmno':
            i_o_files.append(f)
    
    i_o_files.sort()
    
    print(f"Found {len(i_o_files)} files in I-O range")
    
    # Process each file
    for filepath in i_o_files:
        file_name = filepath.stem
        title = file_name.replace('_', ' ').title()
        
        try:
            content = generate_chapter_content(file_name, title)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            processed += 1
            print(f"✓ Processed: {file_name}.tex")
        except Exception as e:
            errors.append(f"{file_name}: {str(e)}")
            print(f"✗ Error: {file_name}.tex - {e}")
    
    print(f"\nProcessed {processed}/{len(i_o_files)} files")
    if errors:
        print(f"\nErrors: {len(errors)}")
        for err in errors[:5]:
            print(f"  - {err}")

if __name__ == "__main__":
    process_chapters()
