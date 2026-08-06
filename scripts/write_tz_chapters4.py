#!/usr/bin/env python3
"""Generate real medical content for more T-Z chapter tex files."""

import os

chapters_dir = "/Users/csv610/Projects/MyBooks/Medical/MedTopics/chapters"

CHAPTERS = {
    "teenagers_and_adolescent_s_mental_health": """\\chapter{Teenagers and Adolescent's Mental Health}

\\section{Overview}
Adolescent mental health is a critical component of overall health. Teenagers face unique challenges including hormonal changes, academic pressure, social dynamics, and identity formation.

\\section{Symptoms}
Warning signs include:
\\begin{itemize}
    \\item Extreme mood swings
    \\item Social withdrawal
    \\item Declining academic performance
    \\item Changes in eating or sleeping
    \\item Loss of interest in activities
    \\item Risky behavior
    \\item Talk of death or suicide
\\end{itemize}

\\section{Causes}
\\begin{itemize}
    \\item Biological changes during puberty
    \\item Academic and social pressure
    \\item Family conflict or divorce
    \\item Bullying or trauma
    \\item Mental health disorders
    \\item Substance use
\\end{itemize}

\\section{Diagnosis}
Comprehensive assessment including:
\\begin{itemize}
    \\item Clinical interview
    \\item Mental status examination
    \\item Input from parents and teachers
    \\item Screening for substance use
    \\item Medical evaluation
\\end{itemize}

\\section{Treatment}
\\begin{itemize}
    \\item Psychotherapy (CBT, DBT)
    \\item Family therapy
    \\item Medication (when appropriate)
    \\item School support services
    \\item Crisis intervention
\\end{itemize}

\\section{Prevention}
\\begin{itemize}
    \\item Open communication
    \\item Strong family connections
    \\item Healthy social networks
    \\item Teaching coping skills
    \\item Monitoring substance use
\\end{itemize}

\\section{When to Seek Medical Care}
Seek immediate help for:
\\begin{itemize}
    \\item Suicidal thoughts or behavior
    \\item Self-harm
    \\item Severe anxiety or depression
    \\item Psychotic symptoms
    \\item Substance abuse
\\end{itemize}
""",

    "teenagers_health": """\\chapter{Teenagers Health}

\\section{Overview}
Adolescent health encompasses physical, mental, and social well-being. Regular check-ups, healthy habits, and open communication are essential during this developmental period.

\\section{Symptoms}
Common health concerns:
\\begin{itemize}
    \\item Acne and skin conditions
    \\item Menstrual irregularities
    \\item Growth and development issues
    \\item Mental health concerns
    \\item Sports injuries
    \\item Sexually transmitted infections
\\end{itemize}

\\section{Causes}
Factors affecting teen health:
\\begin{itemize}
    \\item Hormonal changes
    \\item Lifestyle choices
    \\item Peer influence
    \\item Sleep patterns
    \\item Nutrition
    \\item Physical activity
\\end{itemize}

\\section{Diagnosis}
Regular screenings include:
\\begin{itemize}
    \\item Height, weight, BMI
    \\item Blood pressure
    \\item Vision and hearing
    \\item Mental health screening
    \\item Sexual health assessment
    \\item Substance use screening
\\end{itemize}

\\section{Treatment}
\\begin{itemize}
    \\item Preventive care
    \\item Immunizations
    \\item Health education
    \\item Treatment of acute conditions
    \\item Management of chronic conditions
\\end{itemize}

\\section{Prevention}
\\begin{itemize}
    \\item Balanced nutrition
    \\item Regular exercise
    \\item Adequate sleep (8-10 hours)
    \\item Avoid substances
    \\item Practice safe sex
    \\item Mental health self-care
\\end{itemize}

\\section{When to Seek Medical Care}
Seek care for persistent symptoms, mental health concerns, or after injuries.
""",

    "teeth_grinding": """\\chapter{Teeth Grinding (Bruxism)}

\\section{Overview}
Bruxism is the involuntary grinding or clenching of teeth, often during sleep. It can cause tooth damage, jaw pain, and headaches.

\\section{Symptoms}
\\begin{itemize}
    \\item Worn, flattened, or chipped teeth
    \\item Jaw pain or stiffness
    \\item Headaches (especially temporal)
    \\item Earache
    \\item Tooth sensitivity
    \\item Locked jaw
    \\item Disrupted sleep
\\end{itemize}

\\section{Causes}
\\begin{itemize}
    \\item Stress and anxiety
    \\item Sleep disorders
    \\item Misaligned teeth
    \\item Certain medications
    \\item Lifestyle factors (caffeine, alcohol)
    \\item Parafunctional habits
\\end{itemize}

\\section{Diagnosis}
\\begin{itemize}
    \\item Dental examination
    \\item Review of symptoms
    \\item Sleep study (if sleep disorder suspected)
    \\item Dental imaging
\\end{itemize}

\\section{Treatment}
\\begin{itemize}
    \\item Mouth guard or splint
    \\item Stress management
    \\item Dental correction
    \\item Botox injections (severe cases)
    \\item Medication adjustments
\\end{itemize}

\\section{Prevention}
\\begin{itemize}
    \\item Stress reduction
    \\item Limit caffeine and alcohol
    \\item Avoid chewing non-food items
    \\item Practice relaxation techniques
    \\item Maintain good sleep hygiene
\\end{itemize}

\\section{When to Seek Medical Care}
Seek dental care for tooth pain, sensitivity, or visible wear.
""",

    "teeth_keeping_them_clean": """\\chapter{Keeping Teeth Clean}

\\section{Overview}
Proper oral hygiene is essential for preventing dental diseases and maintaining overall health. Good habits include brushing, flossing, and regular dental visits.

\\section{Symptoms}
Signs of poor oral hygiene:
\\begin{itemize}
    \\item Bad breath
    \\item Gum bleeding
    \\item Tooth sensitivity
    \\item Visible plaque
    \\item Discoloration
    \\item Cavities
\\end{itemize}

\\section{Causes}
Dental problems result from:
\\begin{itemize}
    \\item Plaque buildup
    \\item Bacterial accumulation
    \\item Poor hygiene habits
    \\item Sugary diet
    \\item Infrequent dental visits
\\end{itemize}

\\section{Diagnosis}
Regular dental examinations detect:
\\begin{itemize}
    \\item Cavities
    \\item Gum disease
    \\item Oral cancer
    \\item Bite problems
\\end{itemize}

\\section{Treatment}
\\begin{itemize}
    \\item Professional cleanings
    \\item Fillings for cavities
    \\item Root canal therapy
    \\item Gum disease treatment
    \\item Dental restorations
\\end{itemize}

\\section{Prevention}
\\begin{itemize}
    \\item Brush twice daily with fluoride toothpaste
    \\item Floss daily
    \\item Use mouthwash
    \\item Limit sugary foods
    \\item Visit dentist regularly
    \\item Wear mouth guards during sports
\\end{itemize}

\\section{When to Seek Medical Care}
Seek care for persistent bad breath, bleeding gums, tooth pain, or loose teeth.
""",

    "teeth_whitening": """\\chapter{Teeth Whitening}

\\section{Overview}
Teeth whitening is a cosmetic dental procedure that lightens tooth color. Professional treatments are safer and more effective than over-the-counter options.

\\section{Symptoms}
Indications for whitening:
\\begin{itemize}
    \\item Discolored teeth
    \\item Staining from food, drink, or tobacco
    \\item Age-related discoloration
    \\item Tetracycline staining
\\end{itemize}

\\section{Causes}
Tooth discoloration results from:
\\begin{itemize}
    \\item Coffee, tea, red wine
    \\item Tobacco use
    \\item Aging
    \\item Trauma
    \\item Certain medications
    \\item Excessive fluoride
\\end{itemize}

\\section{Diagnosis}
Dentist evaluates:
\\begin{itemize}
    \\item Tooth color
    \\item Type of staining
    \\item Gum health
    \\item Restorations present
\\end{itemize}

\\section{Treatment}
\\begin{itemize}
    \\item Professional in-office bleaching
    \\item Custom take-home trays
    \\item Over-the-counter products
    \\item Whitening strips and toothpaste
    \\item veneers for severe staining
\\end{itemize}

\\section{Prevention}
\\begin{itemize}
    \\item Limit stain-causing foods and drinks
    \\item Maintain good oral hygiene
    \\item Quit tobacco
    \\item Rinse after consuming staining substances
    \\item Regular dental cleanings
\\end{itemize}

\\section{When to Seek Medical Care}
Consult dentist before whitening, especially with sensitive teeth or restorations.
""",
}

for filename, content in CHAPTERS.items():
    filepath = os.path.join(chapters_dir, filename)
    with open(filepath, 'w') as f:
        f.write(content)
    print(f"Written: {filename}")

print(f"Total: {len(CHAPTERS)}")
