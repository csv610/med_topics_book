#!/usr/bin/env python3
"""
Generate ALL medical-topic chapter files with plain-English content in the
11-section medical-education structure.

Structure (based on Harrison's / UpToDate / NICE CKS standards):
    1.  Definition and Overview
    2.  Epidemiology
    3.  Aetiology and Pathophysiology
    4.  Clinical Features
    5.  Differential Diagnosis
    6.  When to Seek Medical Care (Red Flags)
    7.  Diagnosis and Investigations
    8.  Management
    9.  Complications
    10. Prognosis and Outcomes
    11. Prevention and Self-Care

- Reads medical_topics.tex for canonical (slug, title) pairs.
- Overwrites ALL chapter files (forces full consistency).
- No citations (per project decision). No Lorem ipsum.
"""

import argparse
import os
import re

HERE         = os.path.dirname(os.path.abspath(__file__))
MASTER_TEX   = os.path.join(HERE, "medical_topics.tex")
CHAPTERS_DIR = os.path.join(HERE, "chapters")

SECTION_NAMES = [
    "Definition and Overview",
    "Epidemiology",
    "Aetiology and Pathophysiology",
    "Clinical Features",
    "Differential Diagnosis",
    "When to Seek Medical Care",
    "Diagnosis and Investigations",
    "Management",
    "Complications",
    "Prognosis and Outcomes",
    "Prevention and Self-Care",
]

def tex_escape(s):
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

PAIR_RE = re.compile(
    r"^\\index\{(?P<title>.+?)\}\s*\n\\include\{chapters/(?P<slug>[^}]+)\}",
    re.MULTILINE,
)

def parse_master(path):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    pairs = []
    seen = set()
    for m in PAIR_RE.finditer(text):
        slug = m.group("slug")
        title = m.group("title")
        if slug in seen:
            continue
        seen.add(slug)
        pairs.append((slug, title))
    return pairs

def classify(title):
    t = title.lower()
    if any(k in t for k in ("cancer","tumour","tumor","carcinoma","leukaemia","leukemia","lymphoma","melanoma","sarcoma","myeloma","mesothelioma","neuroblastoma","glioma","leukoplakia","bowen's disease")):
        return "cancer"
    if any(k in t for k in ("anxiety","depression","depressive","bipolar","schizophren","psychosis","psychotic","obsessive","compulsive","ocd","ptsd","post-traumatic","phobia","phobic","panic","addiction","dependence","withdrawal","substance","eating disorder","anorexia","bulimia","binge eating","dysmorph","personality disorder","mood disorder","mental health","mental illness","behaviour","behavior","aggression","anger","self-harm","suicide","grief","bereavement","stress","burnout","trauma","adolescent mental","child mental","sleep problem","insomn","nightmare","claustrophob","hoarding")):
        return "mental_health"
    if any(k in t for k in ("surgery","surgical","resection","ectomy","oplasty","reconstruction","replacement","arthroscopy","arthrodesis","transplant","graft","repair","fusion","laminectomy","hysterectomy","appendectomy","cesarean","caesarean","c section","c-section","stenting","angioplasty","laparoscop","endoscopy","colonoscopy","colposcopy","biopsy","amputation","incision and drainage","abdominoplasty","blepharoplasty","rhinoplasty","circumcision","vasectomy","ablation","angiogram","delivery","decompression","craniotomy","shunt","stapedectomy","myringotomy","tonsillectomy","adenoidectomy","cholecystectomy","fixation","osteotomy","arthroplasty","fundoplication","bypass")):
        return "surgery"
    if any(k in t for k in ("infection","infectious","virus","viral","bacterial","fungal","parasitic","parasite","sepsis","septic","pneumonia","influenza","flu ","covid","coronavirus","measles","mumps","rubella","chickenpox","shingles","herpes","hpv","hiv","aids","hepatitis","tuberculosis","meningitis","encephalitis","gastroenteritis","dengue","zika","ebola","malaria","typhoid","cholera","rabies","tetanus","botulism","anthrax","plague","leprosy","syphilis","gonorrhea","gonorrhoea","chlamydia","trichomoniasis","thrush","candidiasis","tinea","ringworm","impetigo","cellulitis","boil","abscess","brucellosis","lyme","ricketts","leptospirosis","toxoplasmosis","cryptococcosis","aspergillosis","histoplasmosis","coccidioidomycosis","blastomycosis","gangrene","scarlet fever","diphtheria","pertussis","whooping cough","polio","rsv","croup","bronchiolitis","monkeypox","smallpox","syndrome")):
        return "infection"
    if any(k in t for k in ("injury","injuries","fracture","broken","wound","wounds","sprain","strain","dislocation","dislocated","burn","burns","bite","sting","concussion","contusion","laceration","abrasion","rupture","tear","torn","subluxation","crush","avulsion","blister","bruise","sunburn","chilblain","frostbite","hypothermia","heat stroke","heat exhaustion","electric shock","drowning","fall","falls","accident","animal bite","insect bite")):
        return "injury"
    if any(k in t for k in ("pregnan","antenatal","prenatal","postnatal","postpartum","labour","labor","childbirth","birth","miscarriage","abortion","fertility","conception","in vitro","ivf","endometriosis","adenomyosis","menopause","menstrual","periods","menstruation","amenorrhoea","amenorrhea","pcos","polycystic ovary","ovarian","cervical","vaginal","vulvar","pelvic floor","pms","premenstrual","fibroid","contracept","breastfeed","lactation","engorgement")):
        return "womens_health"
    if any(k in t for k in ("child","children","childhood","baby","babies","infant","toddler","newborn","neonatal","paediatric","pediatric","adolescent","teenager","teenage","youth","juvenile","cradle cap","colic","bedwetting","immunisation","immunization","vaccin")):
        return "paediatric"
    if any(k in t for k in ("medicine","medication","medicines","drug","drugs","antibiotic","antiviral","antifungal","antihistamine","antidepressant","antipsychotic","anti-inflammatory","vaccine","vaccination","inhibitor","blocker","agonist","tablet","capsule","dose","supplement","vitamin","mineral","calcium","iron","magnesium","potassium","zinc","selenium","iodine","folate","folic acid","b12","protein","fibre","fiber","carbohydrate","nutrition","diet","caffeine","alcohol","nicotine","opioid","methadone","buprenorphine","naloxone","codeine","morphine","aspirin","paracetamol","ibuprofen","statin","beta blocker","steroid","corticosteroid","hormone","insulin","metformin","warfarin","heparin","cialis","tadalafil","sildenafil","adrenaline","antacid","laxative")):
        return "medication"
    if any(k in t for k in ("test","tests","scan","x-ray","xray","mri","ct scan","ultrasound","sonogram","biopsy","endoscopy","colonoscopy","screening","ecg","ekg","eeg","echocardiogram","angiogram","mammogram","smear","blood test","blood pressure","blood glucose","monitoring","spirometry","audiogram","vision test","eye test")):
        return "test"
    if any(k in t for k in ("pain","ache","fever","cough","headache","nausea","vomit","dizziness","vertigo","fatigue","tired","weakness","numbness","tingling","rash","itch","bleeding","swelling","lump","bump","redness","discharge","constipation","diarrhoea","diarrhea","bloating","indigestion","heartburn","shortness of breath","breathlessness","wheeze","palpitation","syncope","fainting","seizure","tremor","spasm","cramp","sore throat","blocked nose","runny nose","congestion","sneezing","hiccup","burping","blurred vision","tinnitus","loss of smell","loss of taste","memory","confusion","delirium")):
        return "symptom"
    if any(k in t for k in ("diet","nutrition","exercise","fitness","yoga","tai chi","meditation","mindfulness","sleep","smoking","tobacco","cigarette","healthy","wellbeing","well-being","wellness","lifestyle","weight","obesity","balanced diet","vegetarian","vegan","bmi","detox","hydration","water intake","compassion","kindness","volunteering","relationship","anger management","stress","relaxation")):
        return "lifestyle"
    if any(k in t for k in ("anatomy","physiology","body","system","blood vessel","heart","lung","liver","kidney","brain","spinal","spine","bone","joint","muscle","tendon","ligament","cartilage","nerve","skin","eye","ear","nose","throat","teeth","tooth","dental","mouth","tongue","stomach","intestine","bowel","colon","rectum","anus","bladder","prostate","uterus","ovary","testicle","penis","breast","lymph","spleen","pancreas","gallbladder","thyroid","adrenal","pituitary","endocrine","circulatory","respiratory","digestive","nervous","immune","skeletal","muscular","urinary","reproductive","lymphatic")):
        return "body_system"
    if any(k in t for k in ("health service","healthcare","health care","medicare","bulk billing","hospital","ambulance","after-hours","care plan","caregiver","carer","respite","accommodation","support","services","consumer","rights","advance care","palliative","end of life","hospice","disability","aged care","nursing","allied health","complementary","alternative medicine","homeopathy","acupunct","chiropract","osteopath","physiotherap","occupational therap","speech therap","counselling","counseling","psychology","psychologist","psychiatr","recovery","telehealth","online health","buying medicines")):
        return "service"
    return "general"

def _itemize(items):
    body = "\\begin{itemize}\n"
    for it in items:
        body += f"    \\item {it}\n"
    body += "\\end{itemize}"
    return body

# Import the builder module
exec(open(os.path.join(HERE, "chapter_builders.py")).read())

BUILDERS = {
    "cancer":        build_cancer,
    "mental_health": build_mental_health,
    "surgery":       build_surgery,
    "infection":     build_infection,
    "injury":        build_injury,
    "womens_health": build_womens_health,
    "paediatric":    build_paediatric,
    "medication":    build_medication,
    "test":          build_test,
    "symptom":       build_symptom,
    "lifestyle":     build_lifestyle,
    "body_system":   build_body_system,
    "service":       build_service,
    "general":       build_general,
}

def render_chapter(title):
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

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    pairs = parse_master(MASTER_TEX)
    print(f"Master file lists {len(pairs)} chapter pairs.")
    written = 0
    by_category = {}
    for slug, title in pairs:
        path = os.path.join(CHAPTERS_DIR, f"{slug}.tex")
        cat = classify(title)
        by_category[cat] = by_category.get(cat, 0) + 1
        new_text = render_chapter(title)
        if not args.dry_run:
            with open(path, "w", encoding="utf-8") as f:
                f.write(new_text)
        written += 1
    print(f"\nChapters written: {written}")
    print("\nBy category:")
    for cat, n in sorted(by_category.items(), key=lambda kv: -kv[1]):
        print(f"  {cat:14s} {n}")

if __name__ == "__main__":
    main()
