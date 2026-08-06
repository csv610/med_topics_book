#!/usr/bin/env python3
"""
Fill placeholder medical-topic chapter files with plain-English content
in the standard 7-section structure.

- Reads medical_topics.tex for canonical (slug, title) pairs (preserves
  human-readable titles and the book's order).
- Skips files that already contain a real Overview section (preserves
  previously written real content).
- Classifies each remaining topic by keyword and writes category-aware
  English content using:
      Overview / Symptoms / Causes / Diagnosis / Treatment /
      Prevention / When to Seek Medical Care
- No citations (per project decision).  No Lorem ipsum.

Usage:
    python3 generate_all_chapters.py            # write all placeholders
    python3 generate_all_chapters.py --dry-run  # report what would change
"""

import argparse
import os
import re
import sys

HERE          = os.path.dirname(os.path.abspath(__file__))
MASTER_TEX    = os.path.join(HERE, "medical_topics.tex")
CHAPTERS_DIR  = os.path.join(HERE, "chapters")

SECTION_NAMES = [
    "Overview",
    "Symptoms",
    "Causes",
    "Diagnosis",
    "Treatment",
    "Prevention",
    "When to Seek Medical Care",
]

# Escape special LaTeX chars in user-supplied titles.
def tex_escape(s: str) -> str:
    return (s.replace("\\", r"\textbackslash{}")
             .replace("&", r"\&")
             .replace("%", r"\%")
             .replace("$", r"\$")
             .replace("#", r"\#")
             .replace("_", r"\_")
             .replace("{", r"\{")
             .replace("}", r"\}")
             .replace("~", r"\textasciitilde{}")
             .replace("^", r"\textasciicircum{}"))

# ----------------------------------------------------------------------------
# Master parsing — extract (slug, title) pairs in document order.
# ----------------------------------------------------------------------------
PAIR_RE = re.compile(
    r"^\\index\{(?P<title>.+?)\}\s*\n\\include\{chapters/(?P<slug>[^}]+)\}",
    re.MULTILINE,
)

def parse_master(path: str):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    pairs = []
    seen = set()
    for m in PAIR_RE.finditer(text):
        slug  = m.group("slug")
        title = m.group("title")
        if slug in seen:
            continue
        seen.add(slug)
        pairs.append((slug, title))
    return pairs

# ----------------------------------------------------------------------------
# Classification — pick a content template based on the topic title.
# ----------------------------------------------------------------------------
def classify(title: str) -> str:
    t = title.lower()

    # Cancers / oncology
    if any(k in t for k in (
        "cancer", "tumour", "tumor", "carcinoma", "leukaemia", "leukemia",
        "lymphoma", "melanoma", "sarcoma", "myeloma", "mesothelioma",
        "neuroblastoma", "glioma", "leukoplakia", "bowen's disease",
    )):
        return "cancer"

    # Mental health / psychiatric / behavioural
    if any(k in t for k in (
        "anxiety", "depression", "depressive", "bipolar", "schizophren",
        "psychosis", "psychotic", "obsessive", "compulsive", "ocd",
        "ptsd", "post-traumatic", "phobia", "phobic", "panic",
        "addiction", "dependence", "withdrawal", "substance",
        "eating disorder", "anorexia", "bulimia", "binge eating",
        "dysmorph", "personality disorder", "mood disorder",
        "mental health", "mental illness", "behaviour", "behavior",
        "aggression", "anger", "self-harm", "suicide", "grief",
        "bereavement", "stress", "burnout", "trauma", "ptsd",
        "adolescent mental", "child mental", "sleep problem",
        "insomn", "nightmare", "claustrophob", "hoarding",
    )):
        return "mental_health"

    # Surgical / procedural
    if any(k in t for k in (
        "surgery", "surgical", "resection", "ectomy", "oplasty",
        "reconstruction", "replacement", "arthroscopy", "arthrodesis",
        "transplant", "graft", "repair", "fusion", "laminectomy",
        "hysterectomy", "appendectomy", "cesarean", "caesarean",
        "c section", "c-section", "stenting", "angioplasty",
        "laparoscop", "endoscopy", "colonoscopy", "colposcopy",
        "biopsy", "amputation", "incision and drainage", "abdominoplasty",
        "blepharoplasty", "rhinoplasty", "circumcision", "vasectomy",
        "ablation", "angiogram", "delivery", "decompression",
        "craniotomy", "shunt", "stapedectomy", "myringotomy",
        "tonsillectomy", "adenoidectomy", "cholecystectomy",
        "fusion", "fixation", "osteotomy", "arthroplasty",
        "fundoplication", "shunt", " CABG", "bypass",
    )):
        return "surgery"

    # Infections / infectious diseases
    if any(k in t for k in (
        "infection", "infectious", "virus", "viral", "bacterial",
        "fungal", "parasitic", "parasite", "sepsis", "septic",
        "pneumonia", "influenza", "flu ", "covid", "coronavirus",
        " measles", "mumps", "rubella", "chickenpox", "shingles",
        "herpes", "HPV", "HIV", "AIDS", "hepatitis", "tuberculosis",
        "tb ", "meningitis", "encephalitis", "gastroenteritis",
        "dengue", "zika", "ebola", "malaria", "typhoid", "cholera",
        "rabies", "tetanus", "botulism", "anthrax", "plague",
        "leprosy", "syphilis", "gonorrhea", "gonorrhoea",
        "chlamydia", "trichomoniasis", "thrush", "candidiasis",
        "tinea", "ringworm", "impetigo", "cellulitis", "boil",
        "abscess", "osteo", "brucellosis", "lyme", "ricketts",
        "leptospirosis", "toxoplasmosis", "cryptococcosis",
        "aspergillosis", "histoplasmosis", "coccidioidomycosis",
        "blastomycosis", "gangrene", "scarlet fever", "diphtheria",
        "pertussis", "whooping cough", "polio", "rabies",
        "rsv", "croup", "bronchiolitis", "ebola", "monkeypox",
        "smallpox", "syndrome",
    )):
        return "infection"

    # Injuries / trauma / wounds
    if any(k in t for k in (
        "injury", "injuries", "fracture", "broken", "wound", "wounds",
        "sprain", "strain", "dislocation", "dislocated", "burn",
        "burns", "bite", "sting", "concussion", "contusion",
        "laceration", "abrasion", "rupture", "tear", "torn",
        "trauma", "subluxation", "crush", "avulsion", "blister",
        "bruise", "sunburn", "chilblain", "frostbite", "hypothermia",
        "heat stroke", "heat exhaustion", "electric shock",
        "drowning", "near drowning", "fall", "falls", "accident",
        "animal bite", "insect bite",
    )):
        return "injury"

    # Pregnancy / childbirth / gynaecology / women's health
    if any(k in t for k in (
        "pregnan", "antenatal", "prenatal", "postnatal", "postpartum",
        "labour", "labor", "childbirth", "birth", "miscarriage",
        "abortion", "fertility", " conception", "in vitro",
        "IVF", "endometriosis", "adenomyosis", "menopause",
        "menstrual", "periods", "menstruation", "amenorrhoea",
        "amenorrhea", "PCOS", "polycystic ovary", "ovarian",
        "cervical", "vaginal", "vulvar", "pelvic floor",
        "PMS", "premenstrual", "fibroid", "contracept",
        "breastfeed", "lactation", "engorgement",
    )):
        return "womens_health"

    # Paediatric / children
    if any(k in t for k in (
        "child", "children", "childhood", "baby", "babies",
        "infant", "toddler", "newborn", "neonatal", "paediatric",
        "pediatric", "adolescent", "teenager", "teenage",
        "youth", "juvenile", "cradle cap", "colic",
        "bedwetting", "immunisation", "immunization",
        "vaccin",
    )):
        return "paediatric"

    # Medications / drugs / vaccines / supplements
    if any(k in t for k in (
        "medicine", "medication", "medicines", "drug", "drugs",
        "antibiotic", "antiviral", "antifungal", "antihistamine",
        "antidepressant", "antipsychotic", "anti-inflammatory",
        "vaccine", "vaccination", "inhibitor", "blocker",
        "agonist", " Table ", "tablet", "capsule", "dose",
        "supplement", "vitamin", "mineral", "calcium", "iron",
        "magnesium", "potassium", "zinc", "selenium", "iodine",
        "folate", "folic acid", "B12", " vitamin ", "protein",
        "fibre", "fiber", "carbohydrate", "fat ", "nutrition",
        "diet", "caffeine", "alcohol", "nicotine", "opioid",
        "methadone", "buprenorphine", "naloxone", "codeine",
        "morphine", "aspirin", "paracetamol", "ibuprofen",
        "statin", "beta blocker", "steroid", "corticosteroid",
        "hormone", "insulin", "metformin", "warfarin",
        "heparin", "cialis", "tadalafil", "sildenafil",
        "adrenaline", " antacid", "laxative",
    )):
        return "medication"

    # Diagnostic tests / imaging / screening
    if any(k in t for k in (
        "test", "tests", "scan", "x-ray", "xray", "MRI", "CT scan",
        "ultrasound", "sonogram", "biopsy", "endoscopy",
        "colonoscopy", "screening", "ECG", "EKG", "EEG",
        "echocardiogram", "angiogram", "mammogram", "smear",
        "blood test", "blood pressure", "blood glucose",
        "monitoring", "stethoscope", "spirometry", "audiogram",
        "vision test", "eye test",
    )):
        return "test"

    # Symptoms / signs / complaints
    if any(k in t for k in (
        "pain", "ache", "fever", "cough", "headache", "nausea",
        "vomit", "dizziness", "vertigo", "fatigue", "tired",
        "weakness", "numbness", "tingling", "rash", "itch",
        "bleeding", "swelling", "lump", "bump", "redness",
        "discharge", "constipation", "diarrhoea", "diarrhea",
        "bloating", "indigestion", "heartburn", "shortness of breath",
        "breathlessness", "wheeze", "palpitation", "syncope",
        "fainting", "seizure", "tremor", "spasm", "cramp",
        "sore throat", "blocked nose", "runny nose", "congestion",
        "sneezing", " hiccup", "burping", "blurred vision",
        "tinnitus", "loss of smell", "loss of taste",
        "memory", "confusion", "delirium",
    )):
        return "symptom"

    # Nutrition / lifestyle / prevention / wellness (broad)
    if any(k in t for k in (
        "diet", "nutrition", "exercise", "fitness", "yoga",
        "tai chi", "meditation", "mindfulness", "sleep",
        "smoking", "tobacco", "cigarette", "healthy", "wellbeing",
        "well-being", "wellness", "lifestyle", "weight",
        "obesity", "balanced diet", "vegetarian", "vegan",
        "BMI", "detox", "hydration", "water intake",
        "compassion", "kindness", "volunteering", "relationship",
        "anger management", "stress", "relaxation",
    )):
        return "lifestyle"

    # Body systems / anatomy / organs
    if any(k in t for k in (
        "anatomy", " physiology", "body", "system",
        "blood vessel", "heart", "lung", "liver", "kidney",
        "brain", "spinal ", "spine", "bone", "joint", "muscle",
        "tendon", "ligament", "cartilage", "nerve", "skin",
        "eye", "ear", "nose", "throat", "teeth", "tooth",
        "dental", "mouth", "tongue", "stomach", "intestine",
        "bowel", "colon", "rectum", "anus", "bladder",
        "prostate", "uterus", "ovary", "testicle", "penis",
        "breast", "lymph", "spleen", "pancreas", "gallbladder",
        "thyroid", "adrenal", "pituitary", "endocrine",
        "circulatory", "respiratory", "digestive", "nervous",
        "immune", "skeletal", "muscular", "urinary",
        "reproductive", "lymphatic",
    )):
        return "body_system"

    # Health services / system / administrative
    if any(k in t for k in (
        "health service", "healthcare", "health care", "medicare",
        "bulk billing", " hospital", "ambulance", "after-hours",
        "care plan", "caregiver", "carer", "respite",
        "accommodation", " support", "services", "consumer",
        "rights", "advance care", "palliative", "end of life",
        "hospice", "disability", "aged care", "nursing",
        "allied health", "complementary", "alternative medicine",
        "homeopathy", "acupunct", "chiropract", "osteopath",
        "physiotherap", "occupational therap", "speech therap",
        "counselling", "counseling", "psychology", "psychologist",
        "psychiatr", " addiction rehab", "recovery",
        "telehealth", "online health", "buying medicines",
    )):
        return "service"

    return "general"


# ----------------------------------------------------------------------------
# Category-specific content builders.
# Each returns dict: section -> LaTeX string.
# All content is plain English, no citations, no fabricated specifics.
# ----------------------------------------------------------------------------

def _itemize(items):
    body = "\\begin{itemize}\n"
    for it in items:
        body += f"    \\item {it}\n"
    body += "\\end{itemize}"
    return body

def build_cancer(title):
    return {
        "Overview": (
            f"{title} is a condition in which abnormal cells grow and divide "
            "in an uncontrolled way. These cells can form a tumour, invade "
            "nearby tissues, or spread to other parts of the body through "
            "the blood and lymph systems. The behaviour, treatment, and "
            "outlook differ widely depending on the tissue of origin, the "
            "type of cells involved, and how far the disease has spread at "
            "the time of diagnosis."
        ),
        "Symptoms": _itemize([
            "A new lump or thickening in the breast, testicle, skin, or elsewhere",
            "A change in the size, shape, colour, or feel of an existing mole or sore",
            "A sore that does not heal",
            "Persistent cough, hoarseness, or difficulty swallowing",
            "Unexplained weight loss, fevers, or night sweats",
            "Persistent tiredness and loss of appetite",
            "Unusual bleeding or discharge from any body opening",
            "Changes in bowel or bladder habits that persist",
        ]),
        "Causes": (
            "Cancer arises from changes (mutations) in the DNA of cells. "
            "These changes may be inherited or acquired over a lifetime. "
            "Contributing factors include:"
        ) + "\n\n" + _itemize([
            "Tobacco smoking and exposure to second-hand smoke",
            "Excessive alcohol consumption",
            "Ultraviolet radiation from the sun or solariums",
            "Infections such as human papillomavirus, hepatitis B and C, and \\textit{Helicobacter pylori}",
            "An unhealthy diet, physical inactivity, and obesity",
            "Exposure to cancer-causing chemicals such as asbestos, benzene, or certain workplace dusts",
            "Increasing age and a family history of cancer",
        ]),
        "Diagnosis": _itemize([
            "Detailed medical history and physical examination",
            "Blood tests and tumour markers where appropriate",
            "Imaging such as X-ray, ultrasound, CT, MRI, or PET scans",
            "Biopsy, in which a sample of tissue is removed for laboratory examination",
            "Endoscopy or colonoscopy to look inside hollow organs",
            "Staging tests to determine whether, and how far, the disease has spread",
        ]),
        "Treatment": (
            "Treatment is planned by a multidisciplinary team and depends on "
            "the type, stage, location, and the person's overall health. "
            "Common options include:"
        ) + "\n\n" + _itemize([
            "Surgery to remove the tumour and a margin of healthy tissue",
            "Radiation therapy to destroy cancer cells or shrink a tumour",
            "Chemotherapy, which uses drugs to kill cancer cells throughout the body",
            "Targeted therapy and immunotherapy, which act on specific features of cancer cells",
            "Hormone therapy for cancers that are sensitive to hormones",
            "Supportive and palliative care to manage symptoms and maintain quality of life",
        ]),
        "Prevention": _itemize([
            "Do not smoke, and avoid exposure to second-hand smoke",
            "Maintain a healthy weight and be physically active",
            "Eat a balanced diet rich in vegetables, fruit, and whole grains",
            "Limit or avoid alcohol",
            "Protect skin from the sun and avoid solariums",
            "Take part in recommended vaccinations and cancer screening programs",
            "Follow workplace health and safety guidance to avoid carcinogens",
        ]),
        "When to Seek Medical Care": (
            "See a doctor promptly for any persistent, unexplained symptom "
            "such as a new lump, a changing mole, unexplained weight loss, "
            "or unusual bleeding. Take part in the recommended screening "
            "for your age and sex. \\textbf{Call 000} for severe symptoms "
            "such as difficulty breathing, chest pain, or sudden severe "
            "abdominal pain.\\n\\n"
            "Always consult a qualified health professional for diagnosis "
            "and treatment of cancer; no information here replaces "
            "individual medical advice."
        ).replace("\\n\\n", "\n\n"),
    }


def build_mental_health(title):
    return {
        "Overview": (
            f"{title} is a mental health condition that affects the way a "
            "person thinks, feels, or behaves. Mental health conditions are "
            "common and treatable. They can be triggered by a combination "
            "of biological factors (such as genetics and brain chemistry), "
            "psychological factors (such as coping style and past trauma), "
            "and social factors (such as stress, relationships, and life "
            "events). With appropriate support, most people recover or "
            "learn to manage their condition well."
        ),
        "Symptoms": _itemize([
            "Persistent low mood, sadness, or emptiness",
            "Excessive worry, fear, panic, or irritability",
            "Loss of interest in activities once enjoyed",
            "Changes in sleep (too much or too little)",
            "Changes in appetite or weight",
            "Tiredness, low energy, or reduced motivation",
            "Difficulty concentrating, remembering, or making decisions",
            "Thoughts of self-harm or suicide",
            "Withdrawal from family, friends, and usual activities",
        ]),
        "Causes": (
            "Mental health conditions usually arise from several factors "
            "acting together:"
        ) + "\n\n" + _itemize([
            "A family history of mental illness",
            "Long-term stress, trauma, abuse, or significant loss",
            "Physical illness, chronic pain, or substance use",
            "Imbalances in brain chemicals and hormones",
            "Social isolation or relationship breakdown",
        ]),
        "Diagnosis": _itemize([
            "A thorough assessment by a GP, psychologist, or psychiatrist",
            "Discussion of symptoms, thoughts, mood, and behaviour",
            "Questions about medical history, family history, and life events",
            "Physical examination and blood tests to rule out other causes",
            "Use of standard questionnaires to gauge severity",
        ]),
        "Treatment": _itemize([
            "Psychological treatments such as cognitive behaviour therapy (CBT), interpersonal therapy, or counselling",
            "Medication such as antidepressants, anti-anxiety medicines, mood stabilisers, or antipsychotics, prescribed by a doctor",
            "Lifestyle changes including regular exercise, good sleep, and reducing alcohol and other drugs",
            "Social support from family, friends, peer groups, and community services",
            "Hospital or specialist care for severe or crisis presentations",
        ]),
        "Prevention": _itemize([
            "Build strong relationships and social connections",
            "Manage stress with relaxation, mindfulness, or exercise",
            "Maintain a regular sleep routine",
            "Limit alcohol and avoid recreational drugs",
            "Seek help early when symptoms first appear",
            "Follow treatment plans and keep follow-up appointments",
        ]),
        "When to Seek Medical Care": (
            "See a GP or mental health professional if symptoms persist for "
            "more than a couple of weeks or interfere with daily life. "
            "\\textbf{Seek immediate help} if there are thoughts of suicide "
            "or self-harm: call emergency services on 000, contact Lifeline "
            "on 13 11 14, or go to the nearest hospital emergency "
            "department. Mental health crises are medical emergencies and "
            "can be treated."
        ),
    }


def build_surgery(title):
    return {
        "Overview": (
            f"{title} is a surgical procedure used to diagnose or treat a "
            "medical condition. Surgery may be recommended when other "
            "treatments have not worked, when a structural problem needs to "
            "be corrected, or to remove diseased tissue. Surgical "
            "procedures are performed in hospitals by qualified surgeons "
            "and anaesthetists and may be carried out as day surgery or "
            "with a hospital stay, depending on the type and complexity of "
            "the operation."
        ),
        "Symptoms": (
            "After surgery it is common to experience:"
            ) + "\n" + _itemize([
            "Pain, swelling, or bruising around the wound",
            "Tiredness and reduced energy for several days",
            "A mild fever in the first 24--48 hours",
            "Reduced appetite and changes in bowel function",
            "Some clear or blood-tinged fluid from the wound",
        ]),
        "Causes": (
            "Surgery is recommended for reasons such as:"
            ) + "\n" + _itemize([
            "To remove a diseased or damaged structure",
            "To repair or reconstruct a structure after injury or disease",
            "To relieve symptoms such as pain or obstruction",
            "To diagnose a condition through biopsy or direct inspection",
            "To implant or replace a device, such as a joint or a stent",
        ]),
        "Diagnosis": (
            "Before surgery the surgical team usually:"
            ) + "\n" + _itemize([
            "Takes a full medical history and examines you",
            "Orders blood tests, heart tracings (ECG), and other tests as needed",
            "Arranges imaging such as X-ray, ultrasound, CT, or MRI",
            "Reviews current medicines and allergies",
            "Discusses the benefits, risks, and alternatives, and seeks consent",
        ]),
        "Treatment": _itemize([
            "Anaesthesia: local, regional (such as spinal or epidural), or general, depending on the procedure",
            "The operation itself, performed using open or keyhole (minimally invasive) techniques",
            "Pain control with medicines such as paracetamol, anti-inflammatories, or stronger pain relievers",
            "Wound care with stitches, clips, or dressings as appropriate",
            "Rehabilitation, including guided movement, exercises, and physiotherapy",
            "Follow-up review to check healing and remove stitches or dressings",
        ]),
        "Prevention": _itemize([
            "Stop smoking well before the operation to reduce anaesthetic and wound complications",
            "Maintain a healthy weight and manage chronic conditions such as diabetes",
            "Follow pre-operative instructions about fasting and medicines",
            "Arrange help at home for the recovery period",
        ]),
        "When to Seek Medical Care": (
            "After surgery contact the surgical team or seek urgent care if "
            "any of the following occur:"
            ) + "\n" + _itemize([
            "Severe or worsening pain not helped by prescribed medicines",
            "Heavy bleeding from the wound",
            "Spreading redness, warmth, swelling, or pus (signs of infection)",
            "Fever above 38\\textdegree{}C that does not settle",
            "Chest pain, shortness of breath, or calf pain and swelling (possible clot)",
            "Inability to pass urine or open the bowels",
            "Any concern that the wound is not healing",
        ]),
    }


def build_infection(title):
    return {
        "Overview": (
            f"{title} is an infection caused by a microorganism such as a "
            "virus, bacterium, fungus, or parasite. Infections can spread "
            "between people, through contaminated food or water, through "
            "insect or animal bites, or by contact with the environment. "
            "Many infections are mild and resolve on their own, while "
            "others can be serious, especially in young babies, older "
            "people, pregnant women, and people with weakened immune "
            "systems."
        ),
        "Symptoms": _itemize([
            "Fever, chills, or sweats",
            "Tiredness and a general feeling of being unwell",
            "Aches and pains in muscles or joints",
            "Headache",
            "Cough, sore throat, or a runny nose",
            "Nausea, vomiting, or diarrhoea",
            "A rash, swelling, or redness at the site of infection",
        ]),
        "Causes": (
            "Infections are caused by:")
        + "\n\n" + _itemize([
            "\\textbf{Viruses,} such as those that cause the common cold, influenza, COVID-19, and many childhood illnesses",
            "\\textbf{Bacteria,} which can cause throat, skin, chest, urinary, and gut infections",
            "\\textbf{Fungi,} which can affect the skin, nails, mouth, or vagina",
            "\\textbf{Parasites,} spread for example by insects, contaminated water, or undercooked food",
        ]),
        "Diagnosis": _itemize([
            "Medical history and physical examination",
            "Blood, urine, throat, or swab tests to identify the organism",
            "Imaging such as a chest X-ray for chest infections",
            "Stool tests for gut infections",
            "Specific tests such as PCR for certain viruses",
        ]),
        "Treatment": _itemize([
            "Rest and plenty of fluids for most viral infections",
            "Antibiotics for bacterial infections, used only when needed and as prescribed",
            "Antiviral medicines for selected viral infections",
            "Antifungal medicines for fungal infections",
            "Anti-parasitic medicines for parasitic infections",
            "Medicines such as paracetamol or ibuprofen to reduce fever and relieve pain",
            "Hospital care for severe infections, including fluids, oxygen, or intravenous treatment",
        ]),
        "Prevention": _itemize([
            "Hand washing with soap and water, or alcohol-based sanitiser",
            "Covering coughs and sneezes and disposing of tissues carefully",
            "Keeping up to date with recommended vaccinations",
            "Safe food handling, thorough cooking, and clean water",
            "Using insect repellent and protective clothing in risk areas",
            "Staying home when unwell to avoid spreading infection",
        ]),
        "When to Seek Medical Care": (
            "Most mild infections improve within a few days. Seek medical "
            "care if symptoms are severe, last longer than expected, or "
            "are getting worse. \\textbf{Call 000 or go to an emergency "
            "department} for:"
            ) + "\n" + _itemize([
            "Difficulty breathing or chest pain",
            "Confusion, drowsiness, or a stiff neck with a rash",
            "A fever that does not settle, especially in babies, older people, or during pregnancy",
            "Persistent vomiting or signs of dehydration",
            "A rapidly spreading skin redness or a wound that becomes hot and swollen",
        ]),
    }


def build_injury(title):
    return {
        "Overview": (
            f"{title} is an injury that can affect the skin, muscles, "
            "bones, joints, or other tissues. Injuries may result from "
            "accidents, falls, sports, motor vehicle crashes, bites, or "
            "overuse. Most minor injuries recover with simple first aid "
            "and rest, while more serious injuries need medical assessment "
            "and sometimes surgery or rehabilitation."
        ),
        "Symptoms": _itemize([
            "Pain or tenderness at the site",
            "Swelling, bruising, or redness",
            "Loss of movement or strength",
            "Deformity, or a limb that looks out of place",
            "Numbness, tingling, or weakness",
            "Bleeding, cuts, or grazes",
            "Inability to bear weight or use the part normally",
        ]),
        "Causes": _itemize([
            "Falls, trips, and slips",
            "Sports and recreational activities",
            "Motor vehicle and bicycle accidents",
            "Bites, stings, and blows",
            "Repetitive or overuse movements",
            "Hot surfaces, chemicals, or electricity (for burns)",
        ]),
        "Diagnosis": _itemize([
            "History of how the injury happened and physical examination",
            "X-ray to check for broken bones",
            "Ultrasound, CT, or MRI for soft-tissue, joint, or internal injuries",
            "Checking blood flow, sensation, and movement below the injury",
        ]),
        "Treatment": _itemize([
            "First aid using the RICE approach for many soft-tissue injuries: Rest, Ice, Compression, Elevation",
            "Cleaning and dressing wounds, and tetanus cover if needed",
            "Pain relief with paracetamol or anti-inflammatories",
            "Splints, slings, plasters, or braces to protect the part",
            "Stitches, glue, or tape for cuts",
            "Physiotherapy and gradual return to activity",
            "Surgery for severe injuries such as fractures that are out of place or damaged internal organs",
        ]),
        "Prevention": _itemize([
            "Wear seatbelts, helmets, and recommended protective gear",
            "Warm up and cool down when exercising",
            "Keep walkways, stairs, and lighting safe at home",
            "Use the right technique and equipment for sport and work",
            "Take breaks from repetitive tasks",
            "Keep physical fitness and strength well maintained",
        ]),
        "When to Seek Medical Care": (
            "\\textbf{Call 000} for major trauma, heavy bleeding, "
            "suspected broken bones that look out of place, head injury "
            "with confusion or loss of consciousness, or any injury that "
            "affects breathing. Otherwise seek care if:"
            ) + "\n" + _itemize([
            "Pain and swelling are severe or worsening",
            "The limb looks deformed or cannot be used",
            "There is numbness, tingling, coldness, or colour change below the injury",
            "A wound is deep, dirty, or has something embedded in it",
            "Symptoms do not improve after a few days of self-care",
        ]),
    }


def build_womens_health(title):
    return {
        "Overview": (
            f"{title} relates to women's reproductive and sexual health, "
            "including the menstrual cycle, pregnancy, childbirth, and "
            "menopause. Many of these changes are a normal part of life; "
            "others may benefit from advice, monitoring, or treatment. "
            "Care can be provided by a GP, midwife, obstetrician, or "
            "gynaecologist depending on the issue."
        ),
        "Symptoms": _itemize([
            "Changes in the menstrual cycle, such as heavier, lighter, irregular, or missed periods",
            "Painful periods (dysmenorrhoea) or pain during sex",
            "Unusual vaginal bleeding, including bleeding between periods or after menopause",
            "Vaginal discharge that changes in colour, amount, or smell",
            "Pelvic pain or pressure",
            "Hot flushes, night sweats, and mood changes around menopause",
            "Difficulty becoming pregnant",
        ]),
        "Causes": _itemize([
            "Normal hormonal changes across life, including puberty, pregnancy, and menopause",
            "Hormonal conditions such as polycystic ovary syndrome (PCOS)",
            "Structural conditions such as fibroids or endometriosis",
            "Infections of the vagina, cervix, or pelvis",
            "Pelvic floor weakness after childbirth or with age",
            "Stress, weight change, and some medicines",
        ]),
        "Diagnosis": _itemize([
            "Medical history, including menstrual and pregnancy history",
            "Pelvic examination",
            "Swabs and tests for infections",
            "Blood tests for hormones, full blood count, and iron",
            "Pelvic ultrasound and other imaging",
            "Smear or cervical screening tests",
        ]),
        "Treatment": _itemize([
            "Lifestyle measures such as a healthy diet, exercise, and stress management",
            "Hormonal treatments such as the contraceptive pill or hormone replacement therapy",
            "Medicines for pain or to treat infection",
            "Specialist treatments for conditions such as endometriosis or fibroids",
            "Pelvic floor physiotherapy for weakness or prolapse",
            "Surgery when other treatments have not helped",
        ]),
        "Prevention": _itemize([
            "Keep up to date with cervical screening and recommended vaccinations",
            "Maintain a healthy weight and exercise regularly",
            "Use contraception to plan pregnancy and prevent sexually transmitted infections",
            "Take folic acid before and during early pregnancy",
            "Avoid smoking and limit alcohol, especially in pregnancy",
            "Seek pre-pregnancy care if planning a pregnancy",
        ]),
        "When to Seek Medical Care": (
            "See a doctor if menstrual pattern changes, if there is "
            "unusual bleeding, persistent pelvic pain, or unusual "
            "discharge. \\textbf{Call 000} for:"
            ) + "\n" + _itemize([
            "Heavy vaginal bleeding that soaks pads quickly, especially in pregnancy",
            "Severe abdominal or pelvic pain",
            "Fever with pelvic pain or discharge",
            "Bleeding or severe pain after miscarriage, abortion, or childbirth",
            "Possible miscarriage, ectopic pregnancy, or other pregnancy emergency",
        ]),
    }


def build_paediatric(title):
    return {
        "Overview": (
            f"{title} is a health matter that concerns babies, children, "
            "or teenagers. Children are not simply small adults; their "
            "bodies, minds, and needs change as they grow. Many childhood "
            "conditions are mild and improve with simple care, but some "
            "need prompt assessment by a doctor."
        ),
        "Symptoms": _itemize([
            "Fever",
            "Trouble feeding, drinking, or waking as usual",
            "Crying that cannot be settled",
            "Vomiting or diarrhoea",
            "A rash, especially one that does not fade when pressed",
            "Breathing faster than usual, or working harder to breathe",
            "Drowsiness, floppiness, or being less responsive than usual",
            "A fit or seizure",
        ]),
        "Causes": _itemize([
            "Common childhood infections such as colds, ear infections, and gastroenteritis",
            "Normal developmental stages such as teething and tantrums",
            "Allergies or asthma",
            "Minor injuries as children learn to move and explore",
            "Mental and emotional changes during adolescence",
        ]),
        "Diagnosis": _itemize([
            "History from the parent or carer, including how the child is behaving",
            "Observation and examination of the child",
            "Temperature, breathing rate, and other vital signs",
            "Tests such as throat swabs, urine samples, or blood tests if needed",
            "Growth and developmental checks",
        ]),
        "Treatment": _itemize([
            "Simple care such as fluids, rest, and paracetamol or ibuprofen at the right dose for the child's weight",
            "Specific medicines such as antibiotics, asthma inhalers, or allergy treatments",
            "Keeping the child comfortable and watching closely for changes",
            "Treatment plans developed with the family and school where needed",
            "Hospital care for more serious illness or injury",
        ]),
        "Prevention": _itemize([
            "Keep vaccinations up to date on the National Immunisation Program schedule",
            "Encourage regular hand washing and healthy eating",
            "Use car seats, helmets, and safety equipment",
            "Create a safe home and supervise young children",
            "Support emotional and mental wellbeing through family and school",
        ]),
        "When to Seek Medical Care": (
            "Seek urgent medical attention for a baby or child who is "
            "very drowsy, floppy, breathing rapidly or with effort, "
            "very pale, has a non-blanching rash, has a fit, or is "
            "unable to keep fluids down. \\textbf{Call 000} if the child "
            "looks seriously ill or you are worried. Otherwise see a GP "
            "for:"
            ) + "\n" + _itemize([
            "Fever in a baby under three months old",
            "Symptoms that are not improving after a few days",
            "Ongoing concerns about feeding, growth, or development",
        ]),
    }


def build_medication(title):
    return {
        "Overview": (
            f"{title} is a medicine or substance used to prevent or treat "
            "a health condition. Medicines work in many different ways: "
            "they may kill or slow organisms, change how the body's "
            "systems work, replace something missing (such as a hormone "
            "or vitamin), or relieve symptoms. Using medicines safely "
            "means knowing what they are for, how to take them, and what "
            "side effects to watch for."
        ),
        "Symptoms": _itemize([
            "Side effects vary by medicine but may include nausea, drowsiness, headache, or upset stomach",
            "Allergic reactions such as rash, swelling, or difficulty breathing",
            "Symptoms of taking too much, which can range from mild to life-threatening",
            "Withdrawal symptoms if certain medicines are stopped suddenly",
        ]),
        "Causes": _itemize([
            "A medicine is prescribed because a doctor has judged that the benefits outweigh the risks",
            "Side effects arise from the medicine acting on healthy tissues as well as the target problem",
            "Interactions can occur with other medicines, food, alcohol, or health conditions",
            "Harm can result from taking the wrong dose, the wrong medicine, or someone else's prescription",
        ]),
        "Diagnosis": _itemize([
            "A review of all medicines, including prescription, over-the-counter, herbal, and recreational drugs",
            "Questions about dose, timing, and any side effects",
            "Blood tests to check levels or organ function for some medicines",
            "Monitoring for known side effects",
        ]),
        "Treatment": _itemize([
            "Take the medicine exactly as prescribed, at the right dose and time",
            "Read the Consumer Medicines Information (CMI) leaflet for each medicine",
            "Tell the doctor about all other medicines and health problems",
            "Do not stop or change a prescribed medicine without medical advice",
            "Store medicines out of reach of children and dispose of expired medicines safely",
            "Seek advice from a pharmacist or doctor if side effects occur",
        ]),
        "Prevention": _itemize([
            "Keep an up-to-date list of all medicines and bring it to appointments",
            "Use one pharmacy where possible so interactions can be checked",
            "Never share prescription medicines",
            "Avoid alcohol if the medicine warns against it",
            "Ask about alternatives if a medicine causes trouble",
        ]),
        "When to Seek Medical Care": (
            "\\textbf{Call 000} for signs of a severe reaction such as "
            "difficulty breathing, swelling of the face or throat, or "
            "collapse. Otherwise seek urgent advice if:"
            ) + "\n" + _itemize([
            "You think too much medicine has been taken (call the Poisons Information Centre on 13 11 26 in Australia)",
            "You develop a rash, yellowing of the skin or eyes, or unusual bleeding",
            "You are concerned about side effects that are severe or persistent",
            "You are pregnant, breastfeeding, or planning pregnancy and are unsure whether a medicine is safe",
        ]),
    }


def build_test(title):
    return {
        "Overview": (
            f"{title} is a test used to help find out how the body is "
            "working, to look for a particular condition, or to monitor a "
            "known problem. Tests may involve taking a sample (such as "
            "blood, urine, or tissue) or scanning the body from the "
            "outside. Some tests are part of routine screening for "
            "healthy people; others are done when a person has symptoms."
        ),
        "Symptoms": _itemize([
            "Most tests cause little or no discomfort",
            "A small bruise or sting from a needle is common after a blood test",
            "Some scans involve an injection of contrast dye or lying still inside a scanner",
            "Mild anxiety before or during the test is common",
        ]),
        "Causes": _itemize([
            "A doctor may order a test to confirm or rule out a diagnosis",
            "Screening tests are offered to healthy people at certain ages or risk levels",
            "Tests are repeated to follow a known condition or treatment response",
        ]),
        "Diagnosis": _itemize([
            "Test selection is based on the symptom or question to be answered",
            "Some tests need preparation such as fasting or a full bladder",
            "Samples are analysed in a laboratory; scans are read by a radiologist",
            "Results are interpreted together with the person's symptoms and history",
        ]),
        "Treatment": _itemize([
            "A test itself is not a treatment, but results guide treatment decisions",
            "Follow-up may include more tests, referral to a specialist, or starting therapy",
            "Discuss what the results mean and what happens next with the doctor",
        ]),
        "Prevention": _itemize([
            "Take part in screening programs recommended for your age and sex",
            "Ask your doctor what a test involves and how to prepare",
            "Tell the doctor about allergies, pregnancy, or previous problems with a test",
            "Keep a record of results and follow-up plans",
        ]),
        "When to Seek Medical Care": _itemize([
            "If you have symptoms that have not been explained, ask the doctor whether a test is appropriate",
            "If you feel faint, unwell, or have a reaction during a test, tell the staff immediately",
            "If results are abnormal, follow up to discuss the next steps",
        ]),
    }


def build_symptom(title):
    return {
        "Overview": (
            f"{title} is a symptom -- a change you notice in your body -- "
            "rather than a disease in itself. Symptoms can arise from "
            "many different causes, ranging from minor and self-limiting "
            "to serious. The aim of assessment is to work out what is "
            "causing the symptom and whether treatment is needed."
        ),
        "Symptoms": _itemize([
            "The symptom itself, which may be mild, moderate, or severe",
            "Other changes that often go along with it, such as fever, tiredness, or changes in appetite",
            "Triggers or things that make the symptom better or worse",
            "How long the symptom has been present and whether it is getting better or worse",
        ]),
        "Causes": _itemize([
            "Common infections such as colds and throat or urinary infections",
            "Inflammation, allergy, or irritation",
            "Injury or overuse",
            "Side effects of medicines",
            "Stress, anxiety, or mood changes",
            "Long-term conditions such as asthma, diabetes, or arthritis",
            "More serious diseases, sometimes needing prompt treatment",
        ]),
        "Diagnosis": _itemize([
            "A clear description of the symptom: when it started, how it feels, what brings it on, and what helps",
            "Physical examination",
            "Targeted tests such as blood or urine tests, or imaging such as X-ray or ultrasound",
            "Review of medicines and lifestyle",
        ]),
        "Treatment": _itemize([
            "Treating the underlying cause once it is found",
            "Symptom relief such as paracetamol for pain or fluids for fever",
            "Rest, adjusted activity, and self-care measures",
            "Specific medicines when indicated, such as antibiotics for a bacterial infection",
            "Follow-up to check that the symptom has settled",
        ]),
        "Prevention": _itemize([
            "A healthy lifestyle with regular exercise, a balanced diet, and good sleep",
            "Hand washing and recommended vaccinations",
            "Safe lifting, use of protective equipment, and sensible pacing of activity",
            "Not smoking and limiting alcohol",
            "Regular check-ups and managing existing health conditions",
        ]),
        "When to Seek Medical Care": (
            "Seek medical care if the symptom is severe, lasts longer "
            "than a few days, keeps coming back, or is accompanied by "
            "warning signs. \\textbf{Call 000} for:"
            ) + "\n" + _itemize([
            "Chest pain, difficulty breathing, or severe abdominal pain",
            "Sudden weakness, numbness, confusion, or trouble speaking",
            "Heavy bleeding or a major injury",
            "A symptom accompanied by collapse, fitting, or loss of consciousness",
        ]),
    }


def build_lifestyle(title):
    return {
        "Overview": (
            f"{title} is about everyday choices and habits that affect "
            "physical and mental health. Lifestyle factors -- including "
            "diet, physical activity, sleep, smoking, alcohol, and social "
            "connections -- have a powerful influence on long-term "
            "health and on many common conditions."
        ),
        "Symptoms": _itemize([
            "Tiredness, low mood, or reduced concentration when lifestyle is poor",
            "Weight changes that may be unintended",
            "Poor sleep, low energy, or frequent minor illness",
            "Dropping out of enjoyable activities",
            "Reduced fitness or shortness of breath with everyday tasks",
        ]),
        "Causes": _itemize([
            "A diet that is high in processed food, sugar, salt, or alcohol",
            "Physical inactivity",
            "Poor sleep or shift work",
            "Smoking and other substance use",
            "High stress or low social support",
        ]),
        "Diagnosis": _itemize([
            "Talking about daily habits, sleep, diet, activity, and mood",
            "Checking weight, blood pressure, and other measures such as blood sugar or cholesterol",
            "Looking for underlying causes of low mood, fatigue, or weight change",
        ]),
        "Treatment": _itemize([
            "Small, sustainable changes rather than sudden overhaul",
            "A balanced diet with plenty of vegetables, fruit, and whole grains",
            "Regular physical activity, building up to about 150 minutes a week of moderate exercise",
            "Good sleep routines and time for rest and relaxation",
            "Stopping smoking and reducing alcohol",
            "Building connections with family, friends, and community",
        ]),
        "Prevention": _itemize([
            "Make changes one at a time and set realistic goals",
            "Find activities you enjoy so they are easier to keep up",
            "Plan meals and movement into the week",
            "Ask for support from family, friends, a GP, or a community program",
        ]),
        "When to Seek Medical Care": _itemize([
            "Before starting a new program if you have a long-term health condition",
            "If you have symptoms such as chest pain, dizziness, or persistent low mood",
            "If you are concerned about your weight, alcohol use, or smoking",
            "If motivation is low and mood or sleep are affected",
        ]),
    }


def build_body_system(title):
    return {
        "Overview": (
            f"{title} relates to a body system or part of the body. "
            "Understanding the normal structure and function of the body "
            "helps explain how diseases or injuries affect it, and how "
            "treatments work."
        ),
        "Symptoms": _itemize([
            "Pain, swelling, or tenderness in the affected area",
            "Loss of normal movement, strength, or function",
            "Changes such as redness, warmth, lumps, or colour changes",
            "Numbness, tingling, or unusual sensations",
            "Symptoms that depend on the organ or system involved",
        ]),
        "Causes": _itemize([
            "Wear and tear with age",
            "Injury or overuse",
            "Infection or inflammation",
            "Conditions present from birth",
            "Tumours, hormone changes, or problems with blood supply",
        ]),
        "Diagnosis": _itemize([
            "History and physical examination of the relevant area",
            "Blood, urine, or other sample tests",
            "Imaging such as X-ray, ultrasound, CT, or MRI",
            "Specialist tests such as nerve studies,scopes, or function tests",
        ]),
        "Treatment": _itemize([
            "Self-care and lifestyle changes",
            "Medicines such as pain relief, anti-inflammatories, or targeted drugs",
            "Physiotherapy or other rehabilitation",
            "Procedures or surgery when needed",
            "Ongoing monitoring of long-term conditions",
        ]),
        "Prevention": _itemize([
            "Stay active, eat a balanced diet, and keep a healthy weight",
            "Avoid smoking and limit alcohol",
            "Use protective equipment at work and during sport",
            "Keep up to date with screening and check-ups",
        ]),
        "When to Seek Medical Care": (
            "See a doctor if symptoms are new, severe, persistent, or "
            "interfering with daily life. \\textbf{Call 000} for:"
            ) + "\n" + _itemize([
            "Chest pain, difficulty breathing, or sudden weakness",
            "Loss of consciousness, fitting, or sudden severe pain",
            "Heavy bleeding or major injury",
        ]),
    }


def build_service(title):
    return {
        "Overview": (
            f"{title} concerns the way health services, support services, "
            "or community resources are organised and used. Knowing what "
            "is available and how to access it helps people get the right "
            "care at the right time."
        ),
        "Symptoms": _itemize([
            "Confusion about which service to use for a problem",
            "Difficulty getting an appointment, transport, or cost",
            "Feeling that needs are not being met by current care",
        ]),
        "Causes": _itemize([
            "Complex systems and many types of providers",
            "Costs, distance, or limited availability",
            "Language, cultural, or communication barriers",
            "Not knowing what is available or how to ask",
        ]),
        "Diagnosis": _itemize([
            "Identifying what help is needed and roughly which service fits",
            "Checking eligibility for programs and benefits",
            "Writing down current providers, medicines, and needs",
        ]),
        "Treatment": _itemize([
            "Start with a GP, who can guide further care",
            "Use nurse-led, pharmacist, or after-hours services for less urgent needs",
            "Explore community services, peer groups, and carer support",
            "Plan ahead with advance care plans and known contacts",
            "Use emergency services for genuine emergencies",
        ]),
        "Prevention": _itemize([
            "Find and keep a regular GP",
            "Keep a list of medicines, allergies, and contacts",
            "Ask about bulk-billing and concession options early",
            "Build support networks before a crisis",
        ]),
        "When to Seek Medical Care": _itemize([
            "Call 000 for emergencies",
            "Contact the service directly for non-urgent questions",
            "Ask a GP or community worker for help navigating services",
        ]),
    }


def build_general(title):
    return {
        "Overview": (
            f"{title} is a medical topic covered in this reference book. "
            "This chapter gives general information in plain English under "
            "the standard section headings. For advice specific to you or "
            "a family member, speak with a qualified health professional."
        ),
        "Symptoms": _itemize([
            "Changes in the way the body or mind normally works",
            "Pain, discomfort, or reduced function",
            "Tiredness, mood change, or changes in sleep or appetite",
            "Other changes that have appeared recently or that are getting worse",
        ]),
        "Causes": _itemize([
            "Common causes include infections, lifestyle factors, and ageing",
            "Injury or inflammation",
            "Underlying long-term health conditions",
            "Side effects of medicines or treatments",
            "Inherited or genetic factors",
        ]),
        "Diagnosis": _itemize([
            "A medical history and discussion of the symptom",
            "A physical examination",
            "Blood, urine, or other samples",
            "Imaging such as X-ray, ultrasound, CT, or MRI",
            "Specialist referral for further assessment",
        ]),
        "Treatment": _itemize([
            "Self-care and lifestyle change",
            "Medicine to relieve symptoms or treat the cause",
            "Physical therapies, exercise, or rehabilitation",
            "Procedures or surgery when needed",
            "Follow-up to check that the treatment is working",
        ]),
        "Prevention": _itemize([
            "Maintain a healthy lifestyle with regular activity and a balanced diet",
            "Keep up to date with recommended screening and vaccinations",
            "Avoid smoking, limit alcohol, and use protective equipment as needed",
            "Manage existing health problems and follow treatment plans",
        ]),
        "When to Seek Medical Care": (
            "See a doctor if a symptom is new, persistent, severe, or "
            "affecting daily life. \\textbf{Call 000} for:"
            ) + "\n" + _itemize([
            "Chest pain, difficulty breathing, or severe bleeding",
            "Sudden weakness, numbness, confusion, or trouble speaking",
            "Loss of consciousness or a fit",
            "Any sudden, severe symptom that worries you",
        ]),
    }


BUILDERS = {
    "cancer":         build_cancer,
    "mental_health":  build_mental_health,
    "surgery":        build_surgery,
    "infection":      build_infection,
    "injury":         build_injury,
    "womens_health":  build_womens_health,
    "paediatric":     build_paediatric,
    "medication":     build_medication,
    "test":           build_test,
    "symptom":        build_symptom,
    "lifestyle":      build_lifestyle,
    "body_system":    build_body_system,
    "service":        build_service,
    "general":        build_general,
}


# ----------------------------------------------------------------------------
# Rendering
# ----------------------------------------------------------------------------
def render_chapter(title: str) -> str:
    cat = classify(title)
    sections = BUILDERS[cat](title)
    out = []
    out.append(f"\\chapter{{{tex_escape(title)}}}")
    out.append("")
    for name in SECTION_NAMES:
        body = sections.get(name, "")
        out.append(f"\\section*{{{name}}}")
        out.append(body)
        out.append("")
    return "\n".join(out).rstrip() + "\n"


# ----------------------------------------------------------------------------
# File inspection
# ----------------------------------------------------------------------------
def already_real(path: str) -> bool:
    """Return True if the existing file already has a real Overview section
    AND is not Lorem ipsum."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        return False
    if "Lorem ipsum" in content:
        return False
    # Real already-completed chapters in this repo use either
    # \section*{Overview} or \section{Overview} -- and contain visible body.
    has_overview = (
        "\\section*{Overview}" in content or
        "\\section{Overview}" in content
    )
    return has_overview and len(content) > 600


# ----------------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true",
                    help="Report changes that would be made without writing")
    args = ap.parse_args()

    pairs = parse_master(MASTER_TEX)
    print(f"Master file lists {len(pairs)} chapter pairs.")

    written = 0
    skipped_real = 0
    missing_files = 0
    by_category = {}

    for slug, title in pairs:
        path = os.path.join(CHAPTERS_DIR, f"{slug}.tex")
        if os.path.exists(path) and already_real(path):
            skipped_real += 1
            continue
        cat = classify(title)
        by_category[cat] = by_category.get(cat, 0) + 1
        new_text = render_chapter(title)
        if not args.dry_run:
            with open(path, "w", encoding="utf-8") as f:
                f.write(new_text)
        written += 1

    print(f"\nChapters skipped (already had real content): {skipped_real}")
    print(f"Chapters written (or would write): {written}")
    print("\nBy category of newly written chapters:")
    for cat, n in sorted(by_category.items(), key=lambda kv: -kv[1]):
        print(f"  {cat:14s} {n}")

if __name__ == "__main__":
    main()