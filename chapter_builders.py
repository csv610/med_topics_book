"""Medical content builders for 14 categories, each producing 11 sections."""

def _itemize(items):
    body = "\\begin{itemize}\n"
    for it in items:
        body += f"    \\item {it}\n"
    body += "\\end{itemize}"
    return body

def build_cancer(title):
    return {
        "Definition and Overview": (
            f"{title} is a neoplastic disease characterised by the uncontrolled "
            "proliferation of abnormal cells that have the capacity to invade "
            "surrounding tissues and metastasise to distant sites via the blood "
            "and lymphatic systems. It represents a heterogeneous group of "
            "disorders that can arise in virtually any organ or tissue. The "
            "behaviour, natural history, and response to therapy vary "
            "considerably depending on histological type, grade, stage at "
            "presentation, and host factors."
        ),
        "Epidemiology": (
            "Cancer is a leading cause of morbidity and mortality worldwide. "
            "One in two men and one in three women will be diagnosed with some "
            "form of cancer in their lifetime. Incidence rises steeply with "
            "age, with the majority of new diagnoses occurring in people over "
            "60 years. Geographic and ethnic variation is substantial, "
            "reflecting differences in environmental exposures, screening "
            "practices, and genetic susceptibility. Modifiable risk factors "
            "(tobacco, alcohol, obesity, infection) account for a significant "
            "proportion of cases."
        ),
        "Aetiology and Pathophysiology": (
            "Cancer arises from the accumulation of somatic (and occasionally "
            "inherited) genetic alterations that disrupt normal cellular "
            "regulatory pathways. Key mechanisms include:"
        ) + "\n\n" + _itemize([
            "\\textbf{Activation of oncogenes:} mutations that promote uncontrolled cell division (e.g.\\ RAS, MYC, HER2)",
            "\\textbf{Inactivation of tumour suppressor genes:} loss of genes that normally restrain growth (e.g.\\ TP53, RB1, APC)",
            "\\textbf{Evasion of apoptosis:} cancer cells resist programmed cell death",
            "\\textbf{Angiogenesis:} tumours induce new blood vessel formation to sustain growth",
            "\\textbf{Tissue invasion and metastasis:} altered cell adhesion and motility enable spread to distant organs",
            "\\textbf{Immune evasion:} tumours develop mechanisms to avoid detection and destruction by the immune system",
        ]),
        "Clinical Features": _itemize([
            "A new or changing lump, thickening, or mass",
            "Unexplained weight loss, anorexia, or fatigue",
            "Persistent pain not explained by other causes",
            "Changes in bowel or bladder habits",
            "Unusual bleeding or discharge from any body opening",
            "A sore or ulcer that does not heal",
            "Persistent cough, hoarseness, or dysphagia",
            "Changes in the size, shape, or colour of a skin lesion or mole",
            "Persistent fever or night sweats of unknown cause",
        ]),
        "Differential Diagnosis": _itemize([
            "Benign tumours (e.g.\\ lipomas, fibroadenomas, adenomatous polyps)",
            "Infectious processes (e.g.\\ abscess, granulomatous disease, lymphadenitis)",
            "Inflammatory or autoimmune conditions (e.g.\\ sarcoidosis, vasculitis)",
            "Cysts and developmental anomalies",
            "Reactive lymph node hyperplasia",
            "Other primary or metastatic malignancies",
        ]),
        "When to Seek Medical Care": (
            "Seek prompt medical assessment for any persistent unexplained "
            "symptom, particularly:"
            ) + "\n" + _itemize([
            "A new or enlarging lump",
            "Unexplained weight loss or fatigue",
            "Unusual bleeding from any site",
            "A changing mole or non-healing skin lesion",
            "Persistent cough, dysphagia, or altered bowel habits",
        ]) + "\n\n"
            "\\textbf{Call 000} for acute emergencies related to cancer or its "
            "treatment, such as severe chest pain, difficulty breathing, "
            "neutropenic sepsis, spinal cord compression, or hypercalcaemia.",
        "Diagnosis and Investigations": _itemize([
            "\\textbf{History and examination:} symptom assessment, risk factors, family history, systemic enquiry",
            "\\textbf{Blood tests:} full blood count, liver and renal function, tumour markers where appropriate",
            "\\textbf{Imaging:} X-ray, ultrasound, CT, MRI, PET-CT for localisation and staging",
            "\\textbf{Biopsy:} histopathological examination is the gold standard for definitive diagnosis",
            "\\textbf{Endoscopy:} direct visualisation and sampling of hollow organ lesions (e.g.\\ colonoscopy, bronchoscopy)",
            "\\textbf{Molecular and genetic testing:} to guide targeted therapy (e.g.\\ HER2, EGFR, BRCA status)",
            "\\textbf{Staging:} TNM classification to determine disease extent and guide treatment",
        ]),
        "Management": (
            "Cancer management is coordinated by a multidisciplinary team "
            "(MDT) and depends on type, stage, molecular profile, and patient "
            "fitness. Modalities include:"
        ) + "\n\n" + _itemize([
            "\\textbf{Surgery:} definitive excision for localised disease; also for diagnosis, staging, and palliation",
            "\\textbf{Radiotherapy:} ionising radiation to destroy tumour cells or control local disease",
            "\\textbf{Chemotherapy:} cytotoxic drugs that target rapidly dividing cells, used alone or in combination",
            "\\textbf{Targeted therapy:} drugs that act on specific molecular targets (e.g.\\ tyrosine kinase inhibitors, monoclonal antibodies)",
            "\\textbf{Immunotherapy:} agents that enhance the immune response against cancer cells (e.g.\\ checkpoint inhibitors, CAR-T cells)",
            "\\textbf{Hormone therapy:} for hormone-sensitive tumours (e.g.\\ breast, prostate)",
            "\\textbf{Supportive and palliative care:} symptom control, psychological support, and quality-of-life management at all stages",
        ]),
        "Complications": _itemize([
            "Local: pain, obstruction, compression of adjacent structures, bleeding, infection",
            "Metastatic: organ failure (liver, lung, brain, bone), pathological fractures, spinal cord compression",
            "Paraneoplastic: syndromes not directly caused by the tumour mass (e.g.\\ hypercalcaemia, Cushing syndrome, neuropathies)",
            "Treatment-related: myelosuppression, nausea, fatigue, cardiotoxicity, neuropathy, secondary malignancies, infertility",
            "Psychological: anxiety, depression, body-image disturbance, existential distress",
        ]),
        "Prognosis and Outcomes": (
            "Prognosis depends on cancer type, histological grade, stage at "
            "diagnosis, molecular markers, performance status, and response to "
            "treatment. Early-stage localised cancers are frequently curable "
            "with surgery alone, while advanced or metastatic disease is often "
            "incurable but increasingly manageable with systemic therapies. "
            "Five-year survival varies widely, from over 95\\% for some "
            "early-stage skin cancers to under 10\\% for advanced pancreatic "
            "cancer. Survivorship care addresses long-term physical and "
            "psychological needs."
        ),
        "Prevention and Self-Care": _itemize([
            "Do not smoke; avoid second-hand smoke",
            "Maintain a healthy weight and engage in regular physical activity",
            "Eat a balanced diet rich in vegetables, fruit, and whole grains",
            "Limit or avoid alcohol consumption",
            "Protect skin from UV radiation; avoid solariums",
            "Participate in recommended cancer screening programs (e.g.\\ bowel, breast, cervical)",
            "Vaccinate against cancer-causing infections (HPV, hepatitis B)",
            "Follow occupational health and safety guidance to minimise carcinogen exposure",
        ]),
    }

def build_mental_health(title):
    return {
        "Definition and Overview": (
            f"{title} is a mental health condition that affects cognition, "
            "emotional regulation, or behaviour. Mental health disorders are "
            "defined by clinically significant disturbance in these domains, "
            "associated with distress and/or functional impairment. They are "
            "common, frequently co-morbid with physical illness, and are a "
            "leading cause of disability worldwide. Most are treatable, and "
            "many people recover fully or achieve substantial improvement "
            "with appropriate intervention."
        ),
        "Epidemiology": (
            "Approximately one in five adults experiences a mental health "
            "condition in any given year. Lifetime prevalence is higher, with "
            "anxiety and depressive disorders the most common. Onset is often "
            "in adolescence or early adulthood. Co-morbidity with substance "
            "use disorders and chronic physical conditions is high. Stigma, "
            "delayed help-seeking, and unequal access to care remain "
            "significant barriers to effective treatment."
        ),
        "Aetiology and Pathophysiology": (
            "Mental health conditions arise from a complex interplay of "
            "biological, psychological, and social factors:"
        ) + "\n\n" + _itemize([
            "\\textbf{Genetic predisposition:} family history is a strong risk factor; heritability estimates range from 30\\% to 80\\% depending on the condition",
            "\\textbf{Neurobiological factors:} alterations in neurotransmitter systems (serotonin, dopamine, GABA, noradrenaline), neuroendocrine function, and brain circuitry",
            "\\textbf{Psychological factors:} maladaptive cognitions, coping styles, and personality traits",
            "\\textbf{Early life adversity:} childhood trauma, abuse, and neglect significantly increase lifetime risk",
            "\\textbf{Social determinants:} poverty, social isolation, relationship breakdown, unemployment, and chronic stress",
            "\\textbf{Substance use:} alcohol and other drugs can trigger or exacerbate symptoms",
        ]),
        "Clinical Features": _itemize([
            "Persistent low mood, sadness, emptiness, or irritability",
            "Excessive worry, fear, panic, or apprehension",
            "Anhedonia -- loss of interest or pleasure in usual activities",
            "Sleep disturbance (insomnia or hypersomnia)",
            "Appetite or weight changes",
            "Fatigue or loss of energy",
            "Psychomotor agitation or retardation",
            "Difficulty concentrating, indecisiveness, or memory complaints",
            "Feelings of worthlessness or excessive guilt",
            "Recurrent thoughts of death or suicide",
            "Hallucinations or delusions (in psychotic disorders)",
            "Avoidance behaviour and social withdrawal",
        ]),
        "Differential Diagnosis": _itemize([
            "Other psychiatric disorders (e.g.\\ depression vs.\\ bipolar disorder; anxiety vs.\\ thyroid dysfunction)",
            "Substance-induced mood or anxiety disorder",
            "Medical conditions mimicking psychiatric presentation (hypothyroidism, anaemia, vitamin B12 deficiency, cerebrovascular disease)",
            "Medication side effects (e.g.\\ corticosteroids, beta-blockers)",
            "Normal grief or adjustment reactions",
            "Neurodevelopmental disorders (ADHD, autism spectrum)",
        ]),
        "When to Seek Medical Care": (
            "Consult a GP or mental health professional if symptoms persist "
            "for more than two weeks, cause significant distress, or impair "
            "function at work, school, or in relationships.\n\n"
            "\\textbf{Seek immediate help if there are thoughts of suicide "
            "or self-harm.} Call 000, contact Lifeline on 13 11 14, or go "
            "to the nearest hospital emergency department. Acute mental "
            "health crises are medical emergencies."
        ),
        "Diagnosis and Investigations": _itemize([
            "\\textbf{Clinical interview:} thorough history of presenting complaint, psychiatric review of symptoms, and mental state examination",
            "\\textbf{Risk assessment:} evaluation of suicide risk, self-harm, and risk to others",
            "\\textbf{Physical examination:} to identify medical causes or co-morbidities",
            "\\textbf{Blood tests:} full blood count, thyroid function, B12, folate, and metabolic screen to exclude organic causes",
            "\\textbf{Screening tools:} standardised questionnaires (e.g.\\ PHQ-9 for depression, GAD-7 for anxiety)",
            "\\textbf{Psychometric testing:} where personality or cognitive assessment is needed",
        ]),
        "Management": _itemize([
            "\\textbf{Psychological therapies:} cognitive behaviour therapy (CBT), interpersonal therapy, dialectical behaviour therapy (DBT), or other evidence-based modalities",
            "\\textbf{Pharmacotherapy:} antidepressants, anxiolytics, mood stabilisers, antipsychotics, or other medicines as indicated, prescribed and monitored by a doctor",
            "\\textbf{Lifestyle interventions:} regular exercise, sleep hygiene, reduced alcohol and substance use, and a balanced diet",
            "\\textbf{Social support:} family involvement, peer support groups, and community services",
            "\\textbf{Care coordination:} GP Mental Health Treatment Plan, referral to a psychologist or psychiatrist",
            "\\textbf{Acute and crisis care:} hospital admission or community crisis team involvement for severe presentations",
        ]),
        "Complications": _itemize([
            "Suicide and self-harm -- the most serious complication",
            "Substance use disorders (alcohol, drugs) as self-medication",
            "Social and relationship breakdown, isolation",
            "Occupational impairment and unemployment",
            "Physical health decline (poor diet, inactivity, chronic stress)",
            "Stigma and discrimination affecting quality of life",
            "Treatment-resistant symptoms requiring specialist input",
        ]),
        "Prognosis and Outcomes": (
            "Most people with mental health conditions improve with "
            "appropriate treatment. Early intervention is associated with "
            "better outcomes. Some conditions (e.g.\\ depression, anxiety) "
            "may resolve completely; others (e.g.\\ schizophrenia, bipolar "
            "disorder) typically follow a relapsing-remitting course and "
            "require long-term management. Relapse rates are reduced by "
            "medication adherence, ongoing therapy, and social support. "
            "Approximately 50--70\\% of people achieve significant symptom "
            "reduction with first-line treatment."
        ),
        "Prevention and Self-Care": _itemize([
            "Build and maintain strong social connections",
            "Develop healthy coping strategies for stress (mindfulness, exercise, relaxation)",
            "Maintain a consistent sleep routine",
            "Limit alcohol and avoid recreational drugs",
            "Seek help early when symptoms first appear",
            "Adhere to treatment plans and attend follow-up appointments",
            "Engage in meaningful activities and set realistic goals",
            "Learn to recognise early warning signs of relapse",
        ]),
    }

def build_surgery(title):
    return {
        "Definition and Overview": (
            f"{title} is a surgical procedure performed to diagnose, treat, "
            "correct, or palliate a medical condition. Surgery is one of the "
            "principal therapeutic modalities in medicine and may be classified "
            "as elective, urgent, or emergency; open or minimally invasive "
            "(keyhole); and curative, palliative, or diagnostic. All surgical "
            "interventions carry inherent risks, and the decision to operate "
            "requires careful consideration of benefits, alternatives, and "
            "patient fitness."
        ),
        "Epidemiology": (
            "Hundreds of millions of surgical procedures are performed globally "
            "each year. Surgical volume and complexity have increased with ageing "
            "populations and advances in anaesthesia and perioperative care. "
            "Postoperative complications occur in approximately 10--15\\% of "
            "procedures, with major complications in 2--4\\%. Surgical safety is "
            "improved by standardised checklists, team communication, and "
            "protocol-driven care."
        ),
        "Aetiology and Pathophysiology": (
            "Surgical intervention is indicated for:"
        ) + "\n\n" + _itemize([
            "Removal of diseased or neoplastic tissue",
            "Repair or reconstruction of structures damaged by injury, congenital anomaly, or degeneration",
            "Relief of mechanical obstruction or compression",
            "Correction of anatomical abnormalities",
            "Diagnostic biopsy or staging",
            "Implantation of prosthetic devices or donor organs",
            "Palliation of incurable conditions (e.g.\\ bypass of malignant obstruction)",
        ]),
        "Clinical Features": _itemize([
            "Pre-operative symptoms relate to the underlying condition necessitating surgery",
            "Post-operative: pain and swelling at the operative site",
            "Fatigue and reduced mobility for days to weeks",
            "Mild fever in the first 24--48 hours is common",
            "Reduced appetite and altered bowel function (especially after abdominal surgery)",
            "Wound drainage -- serous or blood-tinged fluid is normal in the early period",
        ]),
        "Differential Diagnosis": (
            "Postoperative complications to distinguish from normal recovery include:"
        ) + "\n\n" + _itemize([
            "Wound infection vs.\\ normal inflammatory response",
            "Deep vein thrombosis vs.\\ postoperative calf pain",
            "Pulmonary embolism vs.\\ postoperative dyspnoea",
            "Atelectasis vs.\\ pneumonia",
            "Ileus vs.\\ mechanical bowel obstruction",
            "Haematoma vs.\\ seroma vs.\\ wound infection",
            "Urinary retention vs.\\ urinary tract infection",
        ]),
        "When to Seek Medical Care": (
            "After surgery, contact the surgical team or seek urgent care if:"
            ) + "\n" + _itemize([
            "Severe or worsening pain not controlled by prescribed analgesia",
            "Heavy or persistent bleeding from the wound",
            "Spreading redness, warmth, swelling, or purulent discharge (wound infection)",
            "Fever above 38 degrees Celsius that does not settle",
            "Chest pain, dyspnoea, or calf pain and swelling (possible thromboembolism)",
            "Inability to pass urine or open the bowels",
            "Wound dehiscence (separation of wound edges)",
        ]) + "\n\n"
            "\\textbf{Call 000} for any life-threatening postoperative emergency.",
        "Diagnosis and Investigations": _itemize([
            "\\textbf{Pre-operative assessment:} full history, examination, and medication review",
            "\\textbf{Blood tests:} full blood count, coagulation, electrolytes, group and save",
            "\\textbf{Cardiac assessment:} ECG; echocardiogram or cardiology review for cardiac patients",
            "\\textbf{Imaging:} X-ray, ultrasound, CT, or MRI to plan the procedure",
            "\\textbf{Anaesthetic assessment:} airway, fitness grading (ASA classification), and discussion of anaesthetic options",
            "\\textbf{Informed consent:} discussion of risks, benefits, alternatives, and expected recovery",
        ]),
        "Management": _itemize([
            "\\textbf{Anaesthesia:} local, regional (e.g.\\ spinal, epidural), or general depending on the procedure",
            "\\textbf{Operative technique:} open or minimally invasive (laparoscopic, robotic, endoscopic)",
            "\\textbf{Perioperative care:} prophylactic antibiotics, VTE prophylaxis, temperature and fluid management",
            "\\textbf{Pain management:} multimodal analgesia (paracetamol, NSAIDs, opioids, regional techniques)",
            "\\textbf{Wound care:} sutures, clips, dressings; removal at appropriate interval",
            "\\textbf{Rehabilitation:} physiotherapy, graded return to activity, and functional restoration",
            "\\textbf{Follow-up:} review to assess healing, histopathology results, and ongoing management",
        ]),
        "Complications": _itemize([
            "\\textbf{Infection:} wound, deep, or organ/space surgical site infection",
            "\\textbf{Bleeding:} intra-operative or postoperative haemorrhage requiring transfusion or re-operation",
            "\\textbf{Thromboembolism:} deep vein thrombosis and pulmonary embolism",
            "\\textbf{Anaesthetic complications:} aspiration, anaphylaxis, malignant hyperthermia (rare)",
            "\\textbf{Organ injury:} inadvertent damage to adjacent structures",
            "\\textbf{Wound dehiscence and hernia:} failure of wound healing",
            "\\textbf{Systemic:} ileus, urinary retention, pneumonia, acute kidney injury",
        ]),
        "Prognosis and Outcomes": (
            "Most elective surgical procedures have excellent outcomes, with "
            "the majority of patients returning to normal function within "
            "weeks to months. Recovery time depends on the procedure, patient "
            "factors (age, co-morbidity, fitness), and the presence of "
            "complications. Minimally invasive techniques generally result in "
            "shorter hospital stays and faster recovery than open surgery. "
            "Major complications, when they occur, can significantly prolong "
            "recovery and increase mortality."
        ),
        "Prevention and Self-Care": _itemize([
            "Stop smoking well before surgery to reduce wound and anaesthetic complications",
            "Maintain a healthy weight and optimise chronic conditions (diabetes, hypertension) pre-operatively",
            "Follow fasting and medication instructions precisely",
            "Mobilise early postoperatively to reduce DVT and pneumonia risk",
            "Perform prescribed breathing exercises and physiotherapy",
            "Attend all follow-up appointments",
            "Report any concerning symptoms promptly",
        ]),
    }

def build_infection(title):
    return {
        "Definition and Overview": (
            f"{title} is an infectious disease caused by a pathogenic "
            "microorganism -- virus, bacterium, fungus, or parasite -- that "
            "invades the host, replicates, and triggers an immune response. "
            "Infections may be localised or systemic, acute or chronic, and "
            "range from subclinical to life-threatening. Transmission occurs "
            "via person-to-person contact, respiratory droplets, faecal-oral "
            "route, vector-borne spread, or environmental exposure."
        ),
        "Epidemiology": (
            "Infectious diseases remain a leading cause of morbidity and "
            "mortality worldwide, particularly in children, older adults, and "
            "immunocompromised individuals. Burden is highest in "
            "resource-limited settings, though globalisation, travel, and "
            "antimicrobial resistance have increased relevance in all "
            "populations. Seasonal epidemics (influenza) and periodic "
            "pandemics (COVID-19) can overwhelm health systems. Vaccination "
            "and sanitation have dramatically reduced the burden of many "
            "vaccine-preventable diseases."
        ),
        "Aetiology and Pathophysiology": (
            "Infectious diseases are caused by four main classes of pathogen:"
        ) + "\n\n" + _itemize([
            "\\textbf{Viruses:} intracellular pathogens that hijack host cell machinery to replicate (e.g.\\ influenza, HIV, SARS-CoV-2)",
            "\\textbf{Bacteria:} single-celled organisms that cause disease through direct tissue damage and toxin production (e.g.\\ \\textit{Staphylococcus}, \\textit{Streptococcus}, \\textit{Mycobacterium tuberculosis})",
            "\\textbf{Fungi:} eukaryotic organisms causing disease primarily in immunocompromised hosts or through superficial skin/nail infection",
            "\\textbf{Parasites:} protozoa or helminths acquired through contaminated food, water, or vector bites (e.g.\\ malaria, schistosomiasis)",
        ]) + "\n\n"
            "Pathogenesis involves pathogen entry, evasion of host defences, "
            "replication, tissue damage, and host inflammatory response. The "
            "severity of disease reflects the balance between pathogen "
            "virulence and host immunity.",
        "Clinical Features": _itemize([
            "Fever, chills, or rigors",
            "Malaise, fatigue, and myalgia",
            "Localising symptoms reflecting the affected organ system (e.g.\\ cough for respiratory, dysuria for urinary, diarrhoea for gastrointestinal)",
            "Lymphadenopathy",
            "Rash or skin eruption",
            "Headache, photophobia, or neck stiffness (meningeal irritation)",
            "Confusion or altered consciousness in severe systemic infection",
        ]),
        "Differential Diagnosis": _itemize([
            "Non-infectious inflammatory conditions (e.g.\\ autoimmune disorders, vasculitis)",
            "Malignancy (e.g.\\ lymphoma presenting with fever and lymphadenopathy)",
            "Drug fever or hypersensitivity reactions",
            "Thromboembolic disease (e.g.\\ DVT/PE presenting with fever)",
            "Other infectious agents producing the same syndrome (e.g.\\ viral vs.\\ bacterial pneumonia)",
            "Heat illness or endocrine causes of fever (thyrotoxic crisis, adrenal crisis)",
        ]),
        "When to Seek Medical Care": (
            "Most mild infections improve with supportive care within a few days. "
            "Seek medical assessment if symptoms are severe, progressive, or not "
            "improving.\n\n"
            "\\textbf{Call 000 or attend an emergency department for:}\n"
            ) + _itemize([
            "Difficulty breathing or chest pain",
            "Confusion, drowsiness, or neck stiffness with a rash",
            "Persistent high fever not responding to treatment, especially in infants, older adults, or immunocompromised patients",
            "Signs of sepsis: rapid breathing, rapid heart rate, mottled skin, or reduced urine output",
            "Continuous vomiting or signs of dehydration",
        ]),
        "Diagnosis and Investigations": _itemize([
            "\\textbf{History and examination:} exposure, travel, vaccination status, immune status, and localising features",
            "\\textbf{Blood tests:} full blood count (leukocytosis or leukopenia), CRP, inflammatory markers",
            "\\textbf{Microbiology:} blood cultures, urine culture, throat swab, stool culture, or wound swab",
            "\\textbf{Molecular testing:} PCR for viral and atypical bacterial pathogens",
            "\\textbf{Imaging:} chest X-ray, CT, or ultrasound to identify the focus of infection",
            "\\textbf{Serology:} antibody testing for certain infections (e.g.\\ hepatitis, HIV, syphilis)",
        ]),
        "Management": _itemize([
            "\\textbf{Antiviral therapy:} for specific viral infections (e.g.\\ oseltamivir for influenza, antiretrovirals for HIV)",
            "\\textbf{Antibiotics:} directed against the suspected or confirmed bacterial pathogen; empirical therapy may be needed before culture results",
            "\\textbf{Antifungal agents:} for confirmed or suspected fungal infection (e.g.\\ fluconazole, amphotericin B)",
            "\\textbf{Anti-parasitic therapy:} for parasitic infections (e.g.\\ antimalarials, anthelmintics)",
            "\\textbf{Supportive care:} rest, hydration, antipyretics (paracetamol, ibuprofen), and monitoring",
            "\\textbf{Source control:} drainage of abscesses, removal of infected devices, or surgical debridement where necessary",
            "\\textbf{Hospitalisation:} for severe infections requiring intravenous therapy, oxygen, or intensive care",
        ]),
        "Complications": _itemize([
            "Sepsis and septic shock -- a life-threatening systemic inflammatory response",
            "Organ failure: respiratory, renal, hepatic, or multi-organ dysfunction",
            "Secondary infections (e.g.\\ bacterial pneumonia following viral influenza)",
            "Chronic infection or carrier state (e.g.\\ chronic hepatitis, latent tuberculosis)",
            "Post-infectious syndromes (e.g.\\ Guillain-Barre syndrome after Campylobacter; rheumatic fever after streptococcal pharyngitis)",
            "Antimicrobial resistance and recurrent infection",
        ]),
        "Prognosis and Outcomes": (
            "Most common infections resolve with appropriate treatment within "
            "days to weeks. Uncomplicated viral upper respiratory infections "
            "typically resolve in 7--10 days. Bacterial infections usually "
            "improve within 48--72 hours of starting effective antibiotics. "
            "Prognosis is worse at extremes of age, in immunocompromised "
            "patients, and when treatment is delayed. Sepsis carries a "
            "mortality of 10--30\\% depending on severity and timeliness of "
            "intervention."
        ),
        "Prevention and Self-Care": _itemize([
            "Maintain up-to-date vaccinations for age, risk group, and travel destination",
            "Practise regular hand hygiene with soap and water or alcohol-based sanitiser",
            "Cover coughs and sneezes; dispose of tissues safely",
            "Ensure safe food preparation, storage, and water supply",
            "Use insect repellent and protective clothing in vector-borne disease areas",
            "Practice safe sex to reduce sexually transmitted infections",
            "Stay home when unwell to avoid transmitting infection",
            "Complete prescribed courses of antibiotics to reduce resistance",
        ]),
    }

def build_injury(title):
    return {
        "Definition and Overview": (
            f"{title} is a physical injury resulting from external force or trauma. "
            "Injuries may affect skin, soft tissue, bone, joints, nerves, blood "
            "vessels, or internal organs, and range from minor (requiring first "
            "aid only) to life-threatening. Trauma is a leading cause of death "
            "and disability globally, particularly in young adults. Prompt "
            "assessment and management follow the Advanced Trauma Life Support "
            "(ATLS) principles of primary survey, resuscitation, and secondary "
            "survey."
        ),
        "Epidemiology": (
            "Trauma is the leading cause of death in people aged 1--44 years "
            "in developed countries. Road traffic accidents, falls, and "
            "interpersonal violence account for the majority of serious "
            "injuries. Fall-related injuries are increasingly common in older "
            "adults. Sports injuries are frequent in adolescents and young "
            "adults. Occupational injuries remain a significant preventable "
            "burden."
        ),
        "Aetiology and Pathophysiology": _itemize([
            "\\textbf{Blunt trauma:} motor vehicle crashes, falls, assaults -- causes tissue compression, shearing, and contusion",
            "\\textbf{Penetrating trauma:} stab wounds, gunshot wounds -- causes direct tissue disruption along the projectile path",
            "\\textbf{Thermal injury:} burns, frostbite -- tissue damage from extreme temperature",
            "\\textbf{Chemical/electrical injury:} corrosive substances, electric current",
            "\\textbf{Overuse:} repetitive stress leading to microtrauma and inflammation",
            "\\textbf{Pathophysiology:} tissue damage triggers inflammation, oedema, haemorrhage, and the systemic inflammatory response syndrome (SIRS) in severe trauma",
        ]),
        "Clinical Features": _itemize([
            "Pain, tenderness, or deformity at the injury site",
            "Swelling, bruising, or haematoma",
            "Loss of function, range of motion, or ability to bear weight",
            "Wound, laceration, or skin break",
            "Numbness, paraesthesia, or weakness (nerve injury)",
            "Pallor, coolness, or absent pulse distal to injury (vascular compromise)",
            "Deformity, shortening, or abnormal mobility (fracture/dislocation)",
            "Signs of internal injury: abdominal tenderness, chest instability, dyspnoea",
        ]),
        "Differential Diagnosis": _itemize([
            "Fracture vs.\\ soft tissue injury (sprain, strain, contusion)",
            "Closed vs.\\ open (compound) fracture",
            "Dislocation vs.\\ subluxation",
            "Tendon rupture vs.\\ tendonitis",
            "Internal organ injury vs.\\ abdominal wall contusion",
            "Spinal injury vs.\\ muscular back pain",
            "Pre-existing lesions unmasked by minor trauma (e.g.\\ pathological fracture through a bone cyst)",
        ]),
        "When to Seek Medical Care": (
            "\\textbf{Call 000 for major trauma, suspected spinal injury, "
            "severe bleeding, suspected fractures that are deformed or "
            "compound, head injury with confusion or loss of consciousness, "
            "or any injury that compromises breathing or circulation.}\n\n"
            "Otherwise seek care if:"
            ) + "\n" + _itemize([
            "Pain and swelling are severe or worsening",
            "The limb looks deformed or cannot be used",
            "There is numbness, tingling, coldness, or colour change below the injury (neurovascular compromise)",
            "A wound is deep, dirty, or has a foreign body",
            "Symptoms do not improve after 48--72 hours of self-care",
        ]),
        "Diagnosis and Investigations": _itemize([
            "\\textbf{Primary survey (ATLS):} Airway, Breathing, Circulation, Disability, Exposure -- to identify immediately life-threatening problems",
            "\\textbf{History:} mechanism of injury, time, loss of consciousness, pre-existing conditions, medications (anticoagulants)",
            "\\textbf{Examination:} inspection, palpation, and neurovascular assessment of the injured region",
            "\\textbf{Imaging:} X-ray for suspected fractures; CT for complex fractures and internal injuries; MRI for soft tissue, spinal cord, or ligamentous injury",
            "\\textbf{Blood tests:} full blood count, coagulation, cross-match; blood gas and lactate in severe trauma",
            "\\textbf{FAST scan:} focused assessment with sonography in trauma to detect intraperitoneal haemorrhage",
        ]),
        "Management": _itemize([
            "\\textbf{First aid:} RICE protocol (Rest, Ice, Compression, Elevation) for soft tissue injuries; control bleeding with direct pressure",
            "\\textbf{Wound management:} cleaning, debridement, suturing/stereostrips, and tetanus prophylaxis",
            "\\textbf{Analgesia:} paracetamol, NSAIDs, or opioids for moderate-to-severe pain",
            "\\textbf{Immobilisation:} splints, plaster casts, slings, or braces to protect and stabilise",
            "\\textbf{Reduction:} manipulation of fractures or dislocations under appropriate analgesia/anaesthesia",
            "\\textbf{Surgery:} internal fixation, wound exploration, repair of vessels/nerves/tendons, or laparotomy for internal injury",
            "\\textbf{Rehabilitation:} physiotherapy and graded return to function",
        ]),
        "Complications": _itemize([
            "Infection (cellulitis, osteomyelitis, septic arthritis) -- especially with open fractures or contaminated wounds",
            "Compartment syndrome -- raised pressure within a muscle compartment causing ischaemia",
            "Fat embolism syndrome -- after long bone fractures",
            "Deep vein thrombosis and pulmonary embolism -- due to immobility",
            "Non-union, malunion, or delayed union of fractures",
            "Chronic pain, stiffness, or post-traumatic arthritis",
            "Nerve or vascular injury with permanent deficit",
            "Tetanus or rabies (if contaminated wound or animal bite)",
        ]),
        "Prognosis and Outcomes": (
            "Most minor injuries heal within 2--6 weeks. Simple fractures "
            "unite in 6--8 weeks (longer in older adults). Soft tissue "
            "injuries recover in days to weeks depending on severity. "
            "Rehabilitation is essential for optimal functional recovery. "
            "Long-term outcomes depend on the severity of injury, adequacy "
            "of treatment, and presence of complications. Post-traumatic "
            "arthritis may develop years after intra-articular fractures."
        ),
        "Prevention and Self-Care": _itemize([
            "Wear seatbelts, helmets, and recommended protective equipment for sport and work",
            "Follow road safety rules and avoid drink-driving",
            "Warm up and cool down when exercising; use correct technique",
            "Keep walkways, stairs, and lighting safe at home, especially for older adults",
            "Take breaks from repetitive tasks; use ergonomic equipment",
            "Maintain physical fitness, strength, and balance",
            "Ensure tetanus vaccination is up to date",
        ]),
    }

def build_womens_health(title):
    return {
        "Definition and Overview": (
            f"{title} relates to women's reproductive and sexual health, "
            "encompassing menstruation, fertility, pregnancy, childbirth, "
            "and menopause, as well as conditions affecting the female "
            "reproductive system. These events and conditions reflect normal "
            "physiology as well as pathology, and management requires "
            "attention to both biomedical and psychosocial factors. Care is "
            "provided by GPs, midwives, obstetricians, and gynaecologists."
        ),
        "Epidemiology": (
            "Menstrual disorders affect up to 25\\% of women of reproductive "
            "age. Endometriosis affects approximately 1 in 10 women. "
            "Polycystic ovary syndrome (PCOS) affects 8--13\\% of "
            "reproductive-aged women. Approximately 10--15\\% of couples "
            "experience infertility. Menopause typically occurs at age "
            "50--52. Cervical cancer incidence has fallen significantly "
            "with screening and HPV vaccination programmes."
        ),
        "Aetiology and Pathophysiology": _itemize([
            "\\textbf{Hormonal changes:} fluctuations in oestrogen, progesterone, FSH, and LH across the menstrual cycle, pregnancy, and menopause",
            "\\textbf{Structural abnormalities:} fibroids, polyps, endometriosis, ovarian cysts, congenital uterine anomalies",
            "\\textbf{Infection:} sexually transmitted infections, pelvic inflammatory disease, vaginal candidiasis",
            "\\textbf{Autoimmune/endocrine:} thyroid disorders, premature ovarian insufficiency",
            "\\textbf{Genetic:} hereditary cancer syndromes (BRCA1/2, Lynch syndrome)",
            "\\textbf{Lifestyle factors:} stress, weight extremes, excessive exercise, smoking",
        ]),
        "Clinical Features": _itemize([
            "Changes in menstrual cycle: heavy, irregular, or absent periods",
            "Dysmenorrhoea (painful periods) or dyspareunia (painful intercourse)",
            "Intermenstrual or postcoital bleeding",
            "Postmenopausal bleeding -- always requires investigation",
            "Abnormal vaginal discharge (colour, odour, or itch)",
            "Pelvic pain, pressure, or a palpable mass",
            "Menopausal symptoms: hot flushes, night sweats, mood changes, vaginal dryness",
            "Subfertility or difficulty conceiving",
        ]),
        "Differential Diagnosis": _itemize([
            "Pregnancy-related: ectopic pregnancy, miscarriage, molar pregnancy",
            "Structural: fibroids, endometrial polyps, ovarian cysts, endometriosis",
            "Hormonal: PCOS, thyroid dysfunction, hyperprolactinaemia",
            "Infective: pelvic inflammatory disease, cervicitis, vaginitis",
            "Neoplastic: cervical, endometrial, or ovarian cancer",
            "Functional: dysfunctional uterine bleeding, primary dysmenorrhoea",
        ]),
        "When to Seek Medical Care": (
            "See a GP for menstrual changes, persistent pelvic pain, "
            "unusual bleeding, or unusual discharge.\n\n"
            "\\textbf{Call 000} for:"
            ) + "\n" + _itemize([
            "Heavy vaginal bleeding soaking pads rapidly, especially in pregnancy",
            "Severe abdominal or pelvic pain",
            "Fever with pelvic pain or discharge (possible pelvic infection or sepsis)",
            "Shoulder tip pain with vaginal bleeding and positive pregnancy test (suspected ectopic pregnancy)",
            "Bleeding or severe pain after miscarriage, abortion, or childbirth",
        ]),
        "Diagnosis and Investigations": _itemize([
            "\\textbf{History:} menstrual, obstetric, gynaecological, sexual, and contraceptive history",
            "\\textbf{Examination:} abdominal and pelvic (bimanual and speculum) examination",
            "\\textbf{Microbiology:} swabs for chlamydia, gonorrhoea, and other STIs; wet mount for candidiasis",
            "\\textbf{Blood tests:} beta-hCG (pregnancy test), full blood count, iron studies, thyroid function, hormone profile (FSH, LH, oestradiol, prolactin, testosterone)",
            "\\textbf{Imaging:} pelvic ultrasound (transvaginal or transabdominal); saline infusion sonography; MRI for complex cases",
            "\\textbf{Histology:} endometrial biopsy, hysteroscopy with biopsy, colposcopy with cervical biopsy",
        ]),
        "Management": _itemize([
            "\\textbf{Lifestyle:} weight management, exercise, stress reduction",
            "\\textbf{Hormonal therapy:} combined oral contraceptive pill, progesterone-only pill, Mirena IUD, hormone replacement therapy (HRT) for menopause",
            "\\textbf{Non-hormonal medications:} NSAIDs for dysmenorrhoea, antifibrinolytics (tranexamic acid) for heavy bleeding",
            "\\textbf{Antimicrobials:} antibiotics for STIs and pelvic inflammatory disease; antifungals for candidiasis",
            "\\textbf{Surgery:} myomectomy or hysterectomy for fibroids; endometrial ablation for heavy menstrual bleeding; laparoscopic surgery for endometriosis",
            "\\textbf{Fertility management:} ovulation induction, intrauterine insemination, IVF",
            "\\textbf{Pelvic floor physiotherapy:} for prolapse or incontinence",
        ]),
        "Complications": _itemize([
            "Iron-deficiency anaemia from heavy menstrual bleeding",
            "Infertility or subfertility",
            "Chronic pelvic pain",
            "Ectopic pregnancy and rupture (life-threatening)",
            "Sepsis from untreated pelvic infection",
            "Endometrial hyperplasia and progression to endometrial cancer (with unopposed oestrogen)",
            "Osteoporosis and cardiovascular disease (postmenopausal)",
            "Psychological impact of menopausal symptoms or infertility",
        ]),
        "Prognosis and Outcomes": (
            "Most menstrual disorders are well controlled with medical or "
            "surgical treatment. Endometriosis may require long-term "
            "management. PCOS is a chronic condition managed with lifestyle "
            "measures and symptom-targeted therapy. Menopausal symptoms "
            "typically resolve over 2--5 years, though bone and "
            "cardiovascular risks persist. Fertility outcomes depend on the "
            "underlying cause and treatment. Early detection and treatment "
            "of reproductive cancers improves survival significantly."
        ),
        "Prevention and Self-Care": _itemize([
            "Participate in cervical screening (HPV test every 5 years for women aged 25--74)",
            "HPV vaccination (ideally before sexual debut)",
            "Maintain a healthy weight and exercise regularly",
            "Use contraception to plan pregnancy and prevent STIs",
            "Take folic acid supplementation before and during early pregnancy",
            "Avoid smoking and limit alcohol, especially in pregnancy",
            "Seek pre-pregnancy care if planning a pregnancy",
            "Discuss HRT risks and benefits with a doctor during menopause transition",
        ]),
    }

def build_paediatric(title):
    return {
        "Definition and Overview": (
            f"{title} is a health matter affecting infants, children, or "
            "adolescents. Children are not merely small adults; their "
            "physiology, pharmacology, psychology, and developmental needs "
            "differ fundamentally from those of adults. Many childhood "
            "conditions are self-limiting, but some require prompt diagnosis "
            "and management. Assessment must always consider the "
            "developmental stage and the family/social context."
        ),
        "Epidemiology": (
            "Children under 5 years account for a disproportionate burden of "
            "global morbidity and mortality, primarily from infectious "
            "diseases. In developed countries, chronic conditions (asthma, "
            "diabetes, obesity, mental health disorders) are increasingly "
            "common. Congenital anomalies remain a leading cause of infant "
            "mortality. Injury is the leading cause of death in children "
            "over 1 year in high-income countries. Immunisation has "
            "dramatically reduced the burden of vaccine-preventable diseases."
        ),
        "Aetiology and Pathophysiology": _itemize([
            "\\textbf{Infections:} viral upper respiratory infections, otitis media, gastroenteritis, bronchiolitis, croup",
            "\\textbf{Developmental:} teething, colic, temper tantrums, pubertal changes",
            "\\textbf{Genetic/congenital:} inherited disorders, chromosomal abnormalities, structural anomalies",
            "\\textbf{Allergic/atopic:} eczema, food allergy, asthma, allergic rhinitis",
            "\\textbf{Behavioural/mental health:} ADHD, autism spectrum disorder, anxiety, depression in older children",
            "\\textbf{Injury:} falls, poisoning, burns, road trauma",
        ]),
        "Clinical Features": _itemize([
            "Fever -- the most common presentation",
            "Lethargy, irritability, or reduced feeding/fluid intake",
            "Respiratory: tachypnoea, wheeze, stridor, chest recession",
            "Gastrointestinal: vomiting, diarrhoea, abdominal pain",
            "Rash -- viral exanthems, allergic, or meningococcal",
            "Altered behaviour: drowsiness, floppiness, or unresponsiveness",
            "Seizures or abnormal movements",
            "Failure to thrive or delayed developmental milestones",
        ]),
        "Differential Diagnosis": _itemize([
            "Viral vs.\\ bacterial infection (e.g.\\ viral vs.\\ bacterial tonsillitis; viral vs.\\ bacterial gastroenteritis)",
            "Serious bacterial infection (meningitis, sepsis, pyelonephritis) vs.\\ self-limiting viral illness",
            "Asthma vs.\\ bronchiolitis vs.\\ pneumonia",
            "Colic vs.\\ organic disease in infants",
            "Behavioural vs.\\ psychiatric disorder in adolescents",
            "Accidental vs.\\ non-accidental injury",
        ]),
        "When to Seek Medical Care": (
            "Seek urgent medical attention for any child who is drowsy, "
            "floppy, breathing rapidly or with effort, very pale, has a "
            "non-blanching rash, has a fit, or is unable to keep fluids "
            "down.\n\n"
            "\\textbf{Call 000 if the child looks seriously ill or you are worried.}\n\n"
            "See a GP for:"
            ) + "\n" + _itemize([
            "Fever in a baby under 3 months old",
            "Symptoms not improving after 48 hours",
            "Ongoing concerns about feeding, growth, or development",
        ]),
        "Diagnosis and Investigations": _itemize([
            "\\textbf{History:} from parent/carer, including onset, progression, feeding, urine output, and behaviour change",
            "\\textbf{Examination:} vital signs (temperature, respiratory rate, heart rate, capillary refill), observation of interaction and alertness",
            "\\textbf{Growth assessment:} weight, height/length, and head circumference plotted on growth charts",
            "\\textbf{Developmental assessment:} milestones and school performance",
            "\\textbf{Investigations:} urine dipstick/culture, throat swab, blood tests, or imaging as indicated",
            "\\textbf{Paediatric early warning scores (PEWS):} to identify deterioration",
        ]),
        "Management": _itemize([
            "\\textbf{Supportive care:} fluids, rest, antipyretics (paracetamol or ibuprofen at weight-appropriate dose)",
            "\\textbf{Specific therapy:} antibiotics for bacterial infection, inhalers for asthma, insulin for diabetes",
            "\\textbf{Fluid management:} oral rehydration solution for gastroenteritis; IV fluids for severe dehydration",
            "\\textbf{Family-centred care:} involve parents in decision-making and care",
            "\\textbf{Multidisciplinary approach:} paediatricians, nurses, allied health, and school liaison",
            "\\textbf{Hospital admission:} for severe illness, dehydration, or conditions requiring specialist care",
        ]),
        "Complications": _itemize([
            "Dehydration and electrolyte disturbance (especially with gastroenteritis)",
            "Sepsis and meningitis -- can be rapidly fatal in young children",
            "Respiratory failure (e.g.\\ severe bronchiolitis, asthma)",
            "Developmental delay or disability",
            "Long-term impact of chronic illness on growth and psychosocial development",
            "Impact on family (financial, psychological, social)",
        ]),
        "Prognosis and Outcomes": (
            "Most childhood illnesses are self-limiting and resolve without "
            "sequelae. Children recover rapidly from most infections. "
            "Chronic conditions such as asthma and diabetes require ongoing "
            "management but most children lead full, active lives. Early "
            "intervention for developmental and mental health concerns "
            "improves long-term outcomes. Mortality is highest in the first "
            "year of life, particularly in the neonatal period."
        ),
        "Prevention and Self-Care": _itemize([
            "Keep vaccinations up to date on the National Immunisation Program schedule",
            "Encourage regular hand washing and healthy eating",
            "Use age-appropriate car seats, helmets, and safety equipment",
            "Create a safe home environment: stair gates, pool fencing, medication lock-up",
            "Supervise young children at all times near water, roads, and heights",
            "Support emotional and mental wellbeing through family and school",
            "Attend regular growth and developmental checks",
        ]),
    }

def build_medication(title):
    return {
        "Definition and Overview": (
            f"{title} is a pharmaceutical agent used to prevent, diagnose, "
            "treat, or manage a health condition. Medicines act through "
            "diverse mechanisms: replacing deficient substances, modifying "
            "physiological processes, destroying pathogens, or relieving "
            "symptoms. Safe and effective medication use requires "
            "understanding the indication, dose, route, adverse effects, "
            "interactions, and contraindications."
        ),
        "Epidemiology": (
            "Approximately half of the adult population takes at least one "
            "prescription medicine, and polypharmacy (5 or more medicines) "
            "is common in older adults. Adverse drug reactions account for "
            "a significant proportion of hospital admissions, particularly "
            "in the elderly. Medication errors are among the most common "
            "preventable causes of patient harm in healthcare. Antimicrobial "
            "resistance, driven by overuse and misuse of antibiotics, is a "
            "growing global threat."
        ),
        "Aetiology and Pathophysiology": _itemize([
            "\\textbf{Pharmacokinetics:} how the body handles the drug -- absorption, distribution, metabolism, and excretion",
            "\\textbf{Pharmacodynamics:} how the drug affects the body -- receptor binding, enzyme inhibition, or channel modulation",
            "\\textbf{Adverse drug reactions:} may be dose-related (Type A) or idiosyncratic/allergic (Type B)",
            "\\textbf{Drug interactions:} pharmacokinetic (altering metabolism) or pharmacodynamic (additive or antagonistic effects)",
            "\\textbf{Tolerance and dependence:} particularly with opioids, benzodiazepines, and other psychoactive agents",
        ]),
        "Clinical Features": _itemize([
            "Adverse effects vary by medicine but commonly include: nausea, headache, dizziness, drowsiness, or gastrointestinal disturbance",
            "Allergic reactions: rash, urticaria, angioedema, or anaphylaxis",
            "Symptoms of overdose: organ-specific toxicity (e.g.\\ hepatotoxicity with paracetamol overdose)",
            "Withdrawal symptoms if certain medicines are stopped abruptly (e.g.\\ opioids, benzodiazepines, corticosteroids)",
            "Therapeutic effect: improvement or resolution of the condition being treated",
        ]),
        "Differential Diagnosis": (
            "When a patient develops new symptoms while taking a medicine, consider:"
        ) + "\n" + _itemize([
            "Adverse drug reaction vs.\\ progression of underlying disease",
            "Drug interaction vs.\\ independent new condition",
            "Allergic reaction vs.\\ non-allergic hypersensitivity",
            "Overdose (intentional or accidental) vs.\\ therapeutic side effect",
            "Withdrawal vs.\\ recurrence of the treated condition",
        ]),
        "When to Seek Medical Care": (
            "\\textbf{Call 000 for signs of a severe allergic reaction "
            "(anaphylaxis): difficulty breathing, swelling of the face or "
            "throat, collapse, or widespread rash with hypotension.}\n\n"
            "Otherwise seek urgent advice if:"
            ) + "\n" + _itemize([
            "You think too much medicine has been taken -- call the Poisons Information Centre on 13 11 26 (Australia)",
            "You develop a rash, yellowing of the skin or eyes, or unusual bleeding",
            "You have severe or persistent side effects",
            "You are pregnant, breastfeeding, or planning pregnancy and are unsure whether a medicine is safe",
        ]),
        "Diagnosis and Investigations": _itemize([
            "\\textbf{Medication review:} comprehensive review of all prescribed, over-the-counter, herbal, and recreational substances",
            "\\textbf{Adherence assessment:} explore whether the medicine is being taken as prescribed",
            "\\textbf{Blood tests:} drug levels (e.g.\\ lithium, phenytoin, warfarin INR), liver and renal function, full blood count",
            "\\textbf{Therapeutic drug monitoring:} for medicines with a narrow therapeutic index",
            "\\textbf{Allergy testing:} for suspected drug allergy",
        ]),
        "Management": _itemize([
            "\\textbf{Prescribing principles:} right drug, right dose, right route, right time, right patient",
            "\\textbf{Take as prescribed:} do not stop or change a dose without medical advice",
            "\\textbf{Read the Consumer Medicines Information (CMI)} for each medicine",
            "\\textbf{Monitor:} for therapeutic effect and adverse reactions",
            "\\textbf{Adjust:} dose for age, renal/hepatic function, and interactions",
            "\\textbf{Deprescribing:} judicious withdrawal of medicines that are no longer needed or causing harm",
            "\\textbf{Adverse reaction management:} dose reduction, switching to an alternative, or symptomatic treatment",
        ]),
        "Complications": _itemize([
            "Adverse drug reactions -- ranging from mild to life-threatening",
            "Anaphylaxis -- a medical emergency",
            "Organ toxicity: hepatotoxicity, nephrotoxicity, cardiotoxicity, bone marrow suppression",
            "Drug interactions leading to treatment failure or toxicity",
            "Medication errors: wrong drug, wrong dose, wrong patient",
            "Antimicrobial resistance -- from inappropriate antibiotic use",
            "Dependence and withdrawal -- with opioids, benzodiazepines, and other agents",
        ]),
        "Prognosis and Outcomes": (
            "Most medicines are safe and effective when used as prescribed. "
            "Adverse reactions are usually mild and reversible on stopping "
            "or adjusting the dose. Serious adverse reactions are uncommon "
            "but can be life-threatening. Medication-related harm is "
            "significantly reduced by reconciliation at care transitions, "
            "regular review, and patient education. Long-term outcomes "
            "depend on the underlying condition being treated and adherence "
            "to therapy."
        ),
        "Prevention and Self-Care": _itemize([
            "Keep an up-to-date list of all medicines and bring it to every appointment",
            "Use one pharmacy where possible so interactions can be checked",
            "Never share prescription medicines",
            "Store medicines out of reach of children; dispose of expired medicines safely",
            "Avoid alcohol if the medicine warns against it",
            "Ask questions: know what each medicine is for and what to expect",
            "Report side effects to a doctor or pharmacist promptly",
        ]),
    }

def build_test(title):
    return {
        "Definition and Overview": (
            f"{title} is a clinical investigation used to diagnose, monitor, "
            "or screen for disease. Investigations may involve analysis of "
            "body samples (blood, urine, tissue), imaging of internal "
            "structures, or measurement of physiological function. The choice "
            "of test depends on the clinical question: is a disease present? "
            "How severe is it? Is treatment working? Is a healthy person at "
            "risk?"
        ),
        "Epidemiology": (
            "Diagnostic and screening tests are among the most frequently "
            "performed medical interventions. Billions of pathology tests "
            "and imaging studies are ordered globally each year. Overuse and "
            "inappropriate testing contribute to unnecessary costs, "
            "false-positive results, and patient anxiety. Evidence-based "
            "guidelines aim to optimise test use. Screening programs "
            "(cervical, breast, bowel) have demonstrably reduced cancer "
            "mortality in eligible populations."
        ),
        "Aetiology and Pathophysiology": _itemize([
            "\\textbf{Diagnostic testing:} performed when a patient has symptoms, to identify or exclude a condition",
            "\\textbf{Screening:} offered to asymptomatic individuals at risk to detect disease at an early, treatable stage",
            "\\textbf{Monitoring:} repeated to track disease progression or treatment response",
            "\\textbf{Pre-operative assessment:} to evaluate fitness for surgery and anaesthesia",
            "\\textbf{Test performance:} characterised by sensitivity, specificity, positive and negative predictive values, and likelihood ratios",
        ]),
        "Clinical Features": _itemize([
            "Most tests cause minimal discomfort",
            "Blood tests: brief sting and possible small bruise at the puncture site",
            "Imaging: some scans require contrast injection, fasting, or lying still in an enclosed space",
            "Procedural tests (e.g.\\ biopsy, endoscopy): may require sedation or local anaesthetic",
            "Anxiety about results is common and should be acknowledged",
        ]),
        "Differential Diagnosis": (
            "Interpretation of test results must always be integrated with "
            "the clinical picture. Consider:"
        ) + "\n" + _itemize([
            "False positives: abnormal result in the absence of disease",
            "False negatives: normal result despite disease being present",
            "Borderline results: may require repeat testing or specialist interpretation",
            "Pre-analytical errors: wrong sample, wrong tube, or delayed transport",
            "Analytical errors: laboratory or equipment malfunction",
        ]),
        "When to Seek Medical Care": _itemize([
            "If you have unexplained symptoms, ask your doctor whether a test is appropriate",
            "If you feel faint, unwell, or have a reaction during a test, tell staff immediately",
            "If results are abnormal, follow up to discuss next steps",
            "Never ignore a recommendation for follow-up after an abnormal screening result",
        ]),
        "Diagnosis and Investigations": _itemize([
            "\\textbf{Test selection:} based on the clinical question, pre-test probability, and test characteristics",
            "\\textbf{Preparation:} some tests require fasting, a full bladder, or medication adjustment",
            "\\textbf{Sample analysis:} performed in accredited laboratories using standardised methods",
            "\\textbf{Imaging interpretation:} by a radiologist, with results communicated to the requesting clinician",
            "\\textbf{Result interpretation:} always in clinical context -- a test result alone is not a diagnosis",
        ]),
        "Management": _itemize([
            "A test itself is not a treatment -- results guide management",
            "Normal results may be reassuring or may require further investigation if clinical suspicion remains high",
            "Abnormal results trigger further evaluation, specialist referral, or treatment initiation",
            "Discussion of results with the patient is essential, including implications and next steps",
            "Incidental findings (unexpected abnormalities) require judgement about further investigation",
        ]),
        "Complications": _itemize([
            "Bleeding, bruising, or infection at puncture or biopsy sites",
            "Allergic reaction to contrast dye (e.g.\\ iodinated contrast in CT)",
            "Radiation exposure -- cumulative dose from repeated imaging (especially CT)",
            "False-positive results leading to unnecessary further testing, anxiety, and overdiagnosis",
            "False-negative results providing false reassurance and delayed diagnosis",
            "Incidental findings causing psychological distress and cascade of investigations",
        ]),
        "Prognosis and Outcomes": (
            "Most tests are safe and well tolerated. The clinical value of "
            "a test lies not in the result itself but in how it changes "
            "management decisions. A test that does not alter management "
            "should be questioned. Screening programs with strong evidence "
            "(cervical, breast, bowel) reduce disease-specific mortality. "
            "Over-investigation can cause harm through false positives, "
            "radiation, and patient anxiety."
        ),
        "Prevention and Self-Care": _itemize([
            "Participate in recommended screening programs for your age, sex, and risk factors",
            "Ask your doctor what a test involves, its risks, and how to prepare",
            "Inform the doctor of allergies, pregnancy, or previous problems with tests",
            "Keep a record of your results and follow-up plans",
            "Ask for an explanation of results in plain language",
            "Do not request tests that are not clinically indicated",
        ]),
    }

def build_symptom(title):
    return {
        "Definition and Overview": (
            f"{title} is a clinical symptom or sign -- a departure from "
            "normal function experienced by the patient or observed on "
            "examination. Symptoms are subjective experiences (e.g.\\ pain, "
            "nausea); signs are objective findings (e.g.\\ fever, rash). "
            "Neither a symptom nor a sign is a diagnosis in itself; rather, "
            "each is a clue that guides differential diagnosis and "
            "investigation."
        ),
        "Epidemiology": (
            "Symptoms are the most common reason people seek medical care. "
            "Pain, fatigue, cough, and digestive complaints are among the "
            "most frequently reported. Most symptoms are transient and "
            "benign, but a minority signal serious disease. The challenge "
            "in clinical practice is distinguishing self-limiting from "
            "progressive conditions using history, examination, and "
            "targeted investigation."
        ),
        "Aetiology and Pathophysiology": _itemize([
            "\\textbf{Infection:} viral, bacterial, or other pathogen triggering inflammation and immune response",
            "\\textbf{Inflammation:} immune-mediated tissue damage (allergic, autoimmune, or reactive)",
            "\\textbf{Mechanical:} injury, obstruction, compression, or overuse",
            "\\textbf{Metabolic/endocrine:} electrolyte disturbance, thyroid dysfunction, diabetes",
            "\\textbf{Neurological:} nerve compression, central or peripheral neuropathy",
            "\\textbf{Psychogenic:} stress, anxiety, depression manifesting as physical symptoms",
            "\\textbf{Neoplastic:} tumour causing direct or paraneoplastic symptoms",
            "\\textbf{Iatrogenic:} medication side effects or post-procedural changes",
        ]),
        "Clinical Features": _itemize([
            "The symptom itself -- its character, severity, and temporal pattern",
            "Onset: sudden, gradual, or episodic",
            "Duration and progression: improving, worsening, or fluctuating",
            "Associated symptoms: fever, weight loss, night sweats, or other systemic features",
            "Triggers and relieving factors",
            "Impact on daily activities and quality of life",
        ]),
        "Differential Diagnosis": _itemize([
            "Common benign causes (e.g.\\ viral infection, muscle strain, dietary indiscretion)",
            "Serious or life-threatening causes (e.g.\\ malignancy, sepsis, cardiovascular event)",
            "Chronic conditions (e.g.\\ inflammatory bowel disease, rheumatoid arthritis, asthma)",
            "Functional or psychosomatic disorders",
            "Medication-related causes",
            "Referred pain or symptoms from adjacent structures",
        ]),
        "When to Seek Medical Care": (
            "Seek medical care if the symptom is severe, persists beyond a "
            "few days, keeps recurring, or is accompanied by warning "
            "signs.\n\n"
            "\\textbf{Call 000 for:}"
            ) + "\n" + _itemize([
            "Chest pain, difficulty breathing, or severe abdominal pain",
            "Sudden weakness, numbness, confusion, or difficulty speaking",
            "Heavy bleeding or major injury",
            "Collapse, fitting, or loss of consciousness",
        ]),
        "Diagnosis and Investigations": _itemize([
            "\\textbf{History:} a detailed description of the symptom -- onset, character, duration, progression, triggers, associated features, and prior episodes",
            "\\textbf{Examination:} systematic physical examination of the relevant system and general examination for systemic signs",
            "\\textbf{Blood tests:} full blood count, CRP, biochemistry, and organ-specific markers",
            "\\textbf{Imaging:} X-ray, ultrasound, CT, or MRI depending on the suspected cause",
            "\\textbf{Specialised tests:} endoscopy, biopsy, nerve conduction studies, or cardiac stress testing as indicated",
        ]),
        "Management": _itemize([
            "\\textbf{Treat the underlying cause:} once identified, direct therapy at the diagnosis, not just the symptom",
            "\\textbf{Symptom relief:} analgesics, antiemetics, antipyretics, or other symptomatic measures",
            "\\textbf{Lifestyle measures:} rest, hydration, dietary modification, or activity adjustment",
            "\\textbf{Monitoring:} review to ensure the symptom is resolving and to detect any new features",
            "\\textbf{Specialist referral:} if the cause is unclear, symptoms persist despite treatment, or specialist investigation is needed",
        ]),
        "Complications": _itemize([
            "Missed or delayed diagnosis of serious underlying disease",
            "Chronic pain or disability if the cause is not addressed",
            "Anxiety and psychological distress from unexplained symptoms",
            "Side effects from empirical treatment",
            "Unnecessary investigation and associated risks",
        ]),
        "Prognosis and Outcomes": (
            "Most symptoms resolve within days to weeks as the underlying "
            "cause is treated or self-resolves. Persistent or recurrent "
            "symptoms require thorough evaluation to exclude serious "
            "disease. Functional symptoms (those without an identified "
            "organic cause) can be challenging to manage and may benefit "
            "from a multidisciplinary approach including psychological "
            "support."
        ),
        "Prevention and Self-Care": _itemize([
            "Maintain a healthy lifestyle with regular exercise, balanced diet, and adequate sleep",
            "Stay up to date with recommended vaccinations and screening",
            "Use protective equipment and safe techniques at work and during sport",
            "Avoid smoking and limit alcohol",
            "Manage stress and seek help for mental health concerns",
            "Keep regular check-ups and manage existing chronic conditions",
        ]),
    }

def build_lifestyle(title):
    return {
        "Definition and Overview": (
            f"{title} concerns lifestyle factors -- diet, physical activity, "
            "sleep, substance use, and social engagement -- that influence "
            "health and disease. Lifestyle medicine is an evidence-based "
            "discipline that addresses these modifiable determinants to "
            "prevent, manage, and sometimes reverse chronic disease. The "
            "cumulative impact of daily habits on long-term health "
            "outcomes is substantial."
        ),
        "Epidemiology": (
            "Modifiable lifestyle factors are responsible for a large "
            "proportion of chronic disease burden globally. Tobacco use "
            "remains the leading preventable cause of death. Physical "
            "inactivity, unhealthy diet, and harmful alcohol use are major "
            "contributors to cardiovascular disease, type 2 diabetes, and "
            "several cancers. Obesity prevalence has tripled in many "
            "countries since 1975. Mental health and social connection "
            "are increasingly recognised as independent determinants of "
            "physical health."
        ),
        "Aetiology and Pathophysiology": _itemize([
            "\\textbf{Diet:} excess energy intake, high sugar/salt/saturated fat, low fibre, and ultra-processed foods drive obesity, metabolic syndrome, and cardiovascular disease",
            "\\textbf{Physical inactivity:} contributes to insulin resistance, sarcopenia, osteoporosis, and cardiovascular deconditioning",
            "\\textbf{Sleep disturbance:} chronic sleep deprivation disrupts hormonal regulation (cortisol, ghrelin, leptin) and immune function",
            "\\textbf{Substance use:} tobacco, alcohol, and other drugs cause direct tissue damage and increase disease risk",
            "\\textbf{Chronic stress:} sustained activation of the HPA axis and sympathetic nervous system",
            "\\textbf{Social isolation:} associated with increased all-cause mortality comparable to smoking",
        ]),
        "Clinical Features": _itemize([
            "Fatigue and low energy",
            "Unintended weight gain or loss",
            "Poor sleep quality or insomnia",
            "Reduced exercise tolerance or muscle weakness",
            "Low mood, irritability, or anxiety",
            "Frequent minor illness (immune suppression)",
            "Reduced productivity and social engagement",
        ]),
        "Differential Diagnosis": _itemize([
            "Underlying medical condition causing the symptom (e.g.\\ hypothyroidism causing fatigue; anaemia causing tiredness)",
            "Depression or anxiety disorder",
            "Substance use disorder",
            "Eating disorder",
            "Chronic fatigue syndrome / ME",
            "Medication side effects",
        ]),
        "When to Seek Medical Care": _itemize([
            "Before starting a new exercise or diet program if you have a long-term health condition",
            "If you have symptoms such as chest pain, dizziness, or persistent low mood",
            "If you are concerned about your weight, alcohol use, or smoking",
            "If lifestyle changes are not improving symptoms despite sustained effort",
        ]),
        "Diagnosis and Investigations": _itemize([
            "\\textbf{Lifestyle assessment:} structured history of diet, activity, sleep, substance use, and social engagement",
            "\\textbf{Anthropometry:} weight, height, BMI, waist circumference",
            "\\textbf{Blood tests:} lipid profile, HbA1c, liver function, thyroid function, vitamin D",
            "\\textbf{Blood pressure:} measurement and monitoring",
            "\\textbf{Mental health screening:} depression and anxiety screening questionnaires",
            "\\textbf{Sleep assessment:} sleep diary, Epworth Sleepiness Scale, or polysomnography if sleep apnoea suspected",
        ]),
        "Management": _itemize([
            "\\textbf{SMART goals:} specific, measurable, achievable, relevant, and time-bound behavioural targets",
            "\\textbf{Diet:} Mediterranean or DASH dietary pattern; increase vegetables, fruit, whole grains; reduce ultra-processed foods, added sugar, and salt",
            "\\textbf{Physical activity:} build up to 150--300 minutes of moderate-intensity activity per week, plus resistance training twice weekly",
            "\\textbf{Sleep:} consistent sleep routine; 7--9 hours per night; address sleep disorders",
            "\\textbf{Smoking cessation:} behavioural support plus nicotine replacement therapy, varenicline, or bupropion",
            "\\textbf{Alcohol reduction:} brief intervention, motivational interviewing, or specialist referral",
            "\\textbf{Stress management:} mindfulness, meditation, cognitive behaviour therapy, or other psychological strategies",
        ]),
        "Complications": _itemize([
            "Cardiovascular disease: coronary artery disease, stroke, hypertension",
            "Metabolic disease: type 2 diabetes, metabolic syndrome, non-alcoholic fatty liver disease",
            "Certain cancers (colorectal, breast, endometrial, kidney)",
            "Mental health disorders: depression, anxiety",
            "Musculoskeletal: osteoarthritis, osteoporosis, sarcopenia",
            "Social and occupational consequences of substance use",
        ]),
        "Prognosis and Outcomes": (
            "Lifestyle modifications can prevent, delay, or improve many "
            "chronic conditions. Even modest weight loss (5--10\\%) improves "
            "metabolic markers. Regular physical activity reduces all-cause "
            "mortality by approximately 30\\%. Smoking cessation reduces "
            "cardiovascular risk within months. Behavioural change is most "
            "sustainable when introduced gradually and supported by social "
            "and environmental structures. Relapse is common and should be "
            "anticipated and managed without judgement."
        ),
        "Prevention and Self-Care": _itemize([
            "Make one change at a time; set realistic goals",
            "Find physical activities you enjoy so they are easier to sustain",
            "Plan meals and movement into your weekly routine",
            "Prioritise sleep as a foundation of health",
            "Build strong social connections; stay engaged with community",
            "Ask for support from family, friends, a GP, or a structured program",
            "Monitor progress and celebrate improvements",
        ]),
    }

def build_body_system(title):
    return {
        "Definition and Overview": (
            f"{title} concerns a body system or anatomical region. "
            "Understanding the normal structure and function of body systems "
            "is fundamental to clinical medicine, as disease processes "
            "disrupt normal anatomy and physiology, and treatments aim to "
            "restore or compensate for that disruption."
        ),
        "Epidemiology": (
            "Diseases of major body systems represent a leading cause of "
            "morbidity and mortality. Cardiovascular disease is the leading "
            "cause of death globally. Respiratory diseases (COPD, asthma, "
            "pneumonia) are a major burden. Musculoskeletal conditions are "
            "the leading cause of disability worldwide. The prevalence of "
            "most system-based diseases increases with age, reflecting "
            "cumulative exposure to risk factors and degenerative processes."
        ),
        "Aetiology and Pathophysiology": _itemize([
            "\\textbf{Degenerative:} age-related wear and tear (e.g.\\ osteoarthritis, atherosclerosis, degenerative disc disease)",
            "\\textbf{Inflammatory/autoimmune:} immune-mediated damage (e.g.\\ rheumatoid arthritis, inflammatory bowel disease)",
            "\\textbf{Infectious:} pathogen invasion of the system",
            "\\textbf{Neoplastic:} benign or malignant tumours arising from the system's tissues",
            "\\textbf{Genetic/congenital:} inherited disorders or developmental anomalies",
            "\\textbf{Traumatic:} injury to the system's structures",
            "\\textbf{Vascular:} impaired blood supply causing ischaemia or infarction",
        ]),
        "Clinical Features": _itemize([
            "Pain, swelling, or tenderness in the affected region",
            "Loss of normal movement, strength, or organ function",
            "Changes in appearance: redness, deformity, lumps, or colour change",
            "Numbness, paraesthesia, or altered sensation",
            "Symptoms specific to the organ or system involved",
            "Systemic symptoms: fever, weight loss, fatigue if inflammation or malignancy is present",
        ]),
        "Differential Diagnosis": _itemize([
            "Inflammatory vs.\\ infective vs.\\ neoplastic processes",
            "Acute vs.\\ chronic presentations",
            "Primary vs.\\ referred symptoms",
            "Structural vs.\\ functional disorder",
            "Localised vs.\\ systemic disease",
            "Other conditions affecting the same anatomical region",
        ]),
        "When to Seek Medical Care": (
            "See a doctor if symptoms are new, severe, persistent, or "
            "interfering with daily life.\n\n"
            "\\textbf{Call 000 for:}"
            ) + "\n" + _itemize([
            "Chest pain, difficulty breathing, or sudden weakness",
            "Loss of consciousness, fitting, or sudden severe pain",
            "Heavy bleeding or major injury",
            "Signs of stroke (FAST: Face, Arms, Speech, Time)",
        ]),
        "Diagnosis and Investigations": _itemize([
            "\\textbf{History and examination:} focused on the relevant system, with full systemic review",
            "\\textbf{Blood tests:} organ-specific markers (e.g.\\ cardiac enzymes, liver function, renal function, inflammatory markers)",
            "\\textbf{Imaging:} X-ray, ultrasound, CT, MRI, or fluoroscopy to visualise structures",
            "\\textbf{Functional tests:} ECG, spirometry, nerve conduction, or manometry as appropriate",
            "\\textbf{Endoscopy:} direct visualisation of hollow organs (e.g.\\ bronchoscopy, colonoscopy, cystoscopy)",
            "\\textbf{Biopsy:} tissue sampling for histopathological diagnosis",
        ]),
        "Management": _itemize([
            "\\textbf{Conservative:} lifestyle modification, physiotherapy, and self-management",
            "\\textbf{Pharmacotherapy:} medicines specific to the condition (e.g.\\ antihypertensives, bronchodilators, anti-inflammatories)",
            "\\textbf{Interventional:} injections, nerve blocks, or minimally invasive procedures",
            "\\textbf{Surgical:} definitive correction or reconstruction when conservative measures fail",
            "\\textbf{Rehabilitation:} structured programs to restore function and prevent recurrence",
            "\\textbf{Ongoing monitoring:} for chronic conditions requiring long-term management",
        ]),
        "Complications": _itemize([
            "Progressive loss of function in the affected system",
            "Secondary effects on other body systems",
            "Chronic pain or disability",
            "Treatment-related complications (medication side effects, surgical complications)",
            "Psychological impact of chronic disease",
            "Reduced quality of life and independence",
        ]),
        "Prognosis and Outcomes": (
            "Outcomes depend on the specific condition, its severity, the "
            "timeliness of diagnosis, and response to treatment. Many "
            "system-based diseases are chronic and require lifelong "
            "management, but good control can prevent complications and "
            "maintain function. Early intervention and adherence to "
            "treatment generally improve prognosis. Rehabilitation plays a "
            "key role in recovery from acute events and in managing chronic "
            "conditions."
        ),
        "Prevention and Self-Care": _itemize([
            "Stay physically active; maintain strength and flexibility",
            "Eat a balanced, nutrient-rich diet",
            "Maintain a healthy weight",
            "Avoid smoking and limit alcohol",
            "Use protective equipment at work and during sport",
            "Keep up to date with screening and check-ups",
            "Manage existing health conditions and follow treatment plans",
        ]),
    }

def build_service(title):
    return {
        "Definition and Overview": (
            f"{title} relates to the organisation, delivery, or accessibility "
            "of health and support services. Effective healthcare requires "
            "understanding what services exist, when to use them, and how to "
            "navigate complex systems. This topic covers the structures, "
            "pathways, and resources available to support health and "
            "wellbeing."
        ),
        "Epidemiology": (
            "Health service utilisation is rising with ageing populations, "
            "increasing chronic disease, and technological advances. "
            "Inequities in access -- geographic, financial, cultural, and "
            "informational -- remain a major barrier to care. Emergency "
            "departments are frequently overused for non-urgent problems, "
            "while preventive and primary care services are underutilised "
            "by those who need them most. Health literacy is a strong "
            "predictor of appropriate service use."
        ),
        "Aetiology and Pathophysiology": _itemize([
            "\\textbf{System complexity:} multiple providers, funding streams, and entry points create confusion",
            "\\textbf{Access barriers:} cost, distance, waiting times, language, and cultural factors",
            "\\textbf{Information gaps:} people do not know what is available or how to access it",
            "\\textbf{Fragmentation:} poor communication between providers and services",
        ]),
        "Clinical Features": _itemize([
            "Uncertainty about which service to use for a given problem",
            "Difficulty obtaining appointments, transport, or affordable care",
            "Feeling that needs are not being met by current care arrangements",
            "Navigating multiple providers and repeated assessments",
        ]),
        "Differential Diagnosis": (
            "When access to care is difficult, consider the barriers:"
        ) + "\n" + _itemize([
            "Structural: no local service, long waiting list",
            "Financial: out-of-pocket cost, no insurance/concession",
            "Informational: not knowing what is available or how to ask",
            "Cultural: language, trust, or stigma barriers",
            "Personal: transport, mobility, or caring responsibilities",
        ]),
        "When to Seek Medical Care": _itemize([
            "\\textbf{Call 000 for emergencies} -- chest pain, severe bleeding, difficulty breathing, collapse, or stroke symptoms",
            "Contact a GP for non-urgent health concerns",
            "Use after-hours services, nurse helplines, or pharmacists for less urgent needs",
            "Ask a community worker or social worker for help navigating services",
        ]),
        "Diagnosis and Investigations": _itemize([
            "\\textbf{Needs assessment:} identify what help is needed and roughly which service fits",
            "\\textbf{Eligibility check:} for programs, benefits, and concessions",
            "\\textbf{Service mapping:} identify available local providers and programs",
            "\\textbf{Documentation:} keep a list of current providers, medicines, and care plans",
        ]),
        "Management": _itemize([
            "\\textbf{Start with a GP:} the usual entry point and coordinator of ongoing care",
            "\\textbf{Use appropriate services:} nurse-led clinics, pharmacist advice, after-hours services for non-urgent needs",
            "\\textbf{Explore community services:} peer support groups, carer support, and community health programs",
            "\\textbf{Plan ahead:} advance care plans, known contacts, and documented preferences",
            "\\textbf{Use emergency services appropriately:} reserve 000 for genuine emergencies",
        ]),
        "Complications": _itemize([
            "Delayed diagnosis and treatment due to access barriers",
            "Inappropriate use of emergency services for non-urgent problems",
            "Fragments of care across multiple uncoordinated providers",
            "Missed preventive care and screening opportunities",
            "Financial hardship from healthcare costs",
            "Disparity in health outcomes for disadvantaged groups",
        ]),
        "Prognosis and Outcomes": (
            "Effective navigation of health services improves health "
            "outcomes, reduces unnecessary costs, and enhances patient "
            "experience. A strong relationship with a regular GP is "
            "associated with better chronic disease management and reduced "
            "hospitalisation. Health literacy and advance planning empower "
            "individuals to make informed decisions and receive care "
            "aligned with their values."
        ),
        "Prevention and Self-Care": _itemize([
            "Find and keep a regular GP",
            "Keep a list of medicines, allergies, and key contacts",
            "Ask about bulk-billing and concession options early",
            "Build support networks before a crisis",
            "Develop a personal health record and advance care plan",
            "Improve health literacy: ask questions and seek reliable information",
        ]),
    }

def build_general(title):
    return {
        "Definition and Overview": (
            f"{title} is a medical topic covered in this reference. This "
            "chapter provides structured information under standard clinical "
            "headings, from definition through to prevention. For advice "
            "specific to an individual, consult a qualified health "
            "professional."
        ),
        "Epidemiology": (
            "The prevalence and demographics of this condition vary with "
            "age, sex, genetic background, environmental exposures, and "
            "access to healthcare. Many common medical conditions are "
            "increasing in prevalence due to ageing populations, lifestyle "
            "changes, and improved survival from other diseases. Accurate "
            "epidemiological data informs resource allocation, screening "
            "strategies, and public health policy."
        ),
        "Aetiology and Pathophysiology": _itemize([
            "Genetic predisposition and family history",
            "Environmental exposures (occupational, dietary, environmental)",
            "Lifestyle factors: diet, physical activity, sleep, substance use",
            "Previous injuries, infections, or medical interventions",
            "Age-related degenerative changes",
            "Other underlying health conditions and their treatments",
            "Psychosocial factors: stress, socioeconomic status, social support",
        ]),
        "Clinical Features": _itemize([
            "Changes in normal bodily function or sensation",
            "Pain, discomfort, or dysfunction in the affected area",
            "Fatigue, reduced energy, or exercise intolerance",
            "Sleep disturbance or mood changes",
            "Difficulty with daily activities and reduced quality of life",
            "Signs observable on examination: swelling, redness, deformity, or altered function",
        ]),
        "Differential Diagnosis": _itemize([
            "Other conditions producing similar symptoms",
            "Variants of the same condition (acute vs.\\ chronic, localised vs.\\ systemic)",
            "Functional vs.\\ structural causes",
            "Primary vs.\\ secondary (referred) presentations",
            "Common vs.\\ rare but serious causes",
        ]),
        "When to Seek Medical Care": (
            "See a doctor if a symptom is new, persistent, severe, or "
            "affecting daily life.\n\n"
            "\\textbf{Call 000 for:}"
            ) + "\n" + _itemize([
            "Chest pain, difficulty breathing, or severe bleeding",
            "Sudden weakness, numbness, confusion, or difficulty speaking",
            "Loss of consciousness or a fit",
            "Any sudden, severe symptom that worries you",
        ]),
        "Diagnosis and Investigations": _itemize([
            "\\textbf{History:} detailed account of the presenting complaint, past medical history, medications, family history, and social context",
            "\\textbf{Examination:} systematic physical examination",
            "\\textbf{Blood tests:} full blood count, biochemistry, inflammatory markers, organ-specific tests",
            "\\textbf{Imaging:} X-ray, ultrasound, CT, or MRI as indicated",
            "\\textbf{Specialist tests:} endoscopy, biopsy, or function studies as appropriate",
            "\\textbf{Referral:} to a specialist for further assessment if needed",
        ]),
        "Management": _itemize([
            "\\textbf{Self-care and lifestyle modification:} diet, exercise, sleep, and stress management",
            "\\textbf{Medication:} to manage symptoms or treat the underlying cause",
            "\\textbf{Physical therapies:} physiotherapy, occupational therapy, or rehabilitation",
            "\\textbf{Procedures or surgery:} when conservative measures are insufficient",
            "\\textbf{Psychological support:} counselling or psychological therapy where indicated",
            "\\textbf{Follow-up:} regular monitoring to assess response and adjust treatment",
        ]),
        "Complications": _itemize([
            "Progression of the underlying condition if untreated",
            "Secondary effects on other body systems",
            "Treatment-related adverse effects",
            "Chronic pain, disability, or reduced quality of life",
            "Psychological consequences: anxiety, depression",
            "Social and economic impact on patient and family",
        ]),
        "Prognosis and Outcomes": (
            "Prognosis depends on the specific condition, its severity, "
            "the timeliness of diagnosis, and response to treatment. Many "
            "conditions are manageable with appropriate intervention, and "
            "outcomes are generally better with early detection and "
            "adherence to treatment. Chronic conditions require ongoing "
            "management to prevent complications and maintain function. "
            "Individual prognosis should be discussed with the treating "
            "clinician."
        ),
        "Prevention and Self-Care": _itemize([
            "Maintain a healthy lifestyle with regular physical activity and a balanced diet",
            "Keep up to date with recommended screening and vaccinations",
            "Avoid smoking, limit alcohol, and use protective equipment as needed",
            "Manage existing health problems and follow treatment plans",
            "Practice good hygiene and infection prevention",
            "Maintain social connections and seek help for mental health concerns",
        ]),
    }
