#!/usr/bin/env python3
"""Generate real medical content for more T-Z chapter tex files."""

import os

chapters_dir = "/Users/csv610/Projects/MyBooks/Medical/MedTopics/chapters"

CHAPTERS = {
    "talking_about_your_mental_health_concerns": """\\chapter{Talking About Your Mental Health Concerns}

\\section{Overview}
Discussing mental health concerns can be difficult but is essential for getting help. This chapter provides guidance on opening conversations with family, friends, and healthcare providers about mental health issues.

\\section{Symptoms}
Consider talking to someone if you experience:
\\begin{itemize}
    \\item Persistent sadness or anxiety
    \\item Extreme mood changes
    \\item Withdrawal from activities
    \\item Difficulty functioning at work or school
    \\item Thoughts of self-harm
\\end{itemize}

\\section{Causes}
Mental health concerns can arise from:
\\begin{itemize}
    \\item Biological factors (brain chemistry)
    \\item Life experiences (trauma, stress)
    \\item Family history
    \\item Chemical imbalances
\\end{itemize}

\\section{Diagnosis}
Mental health professionals diagnose through:
\\begin{itemize}
    \\item Clinical interviews
    \\item Standardized assessments
    \\item Medical history
    \\item Physical examination
\\end{itemize}

\\section{Treatment}
Treatment options include:
\\begin{itemize}
    \\item Psychotherapy (CBT, DBT, etc.)
    \\item Medications
    \\item Lifestyle changes
    \\item Support groups
\\end{itemize}

\\section{Prevention}
\\begin{itemize}
    \\item Build strong support networks
    \\item Practice self-care
    \\item Manage stress
    \\item Seek help early
\\end{itemize}

\\section{When to Seek Medical Care}
Seek immediate help if:
\\begin{itemize}
    \\item Having thoughts of suicide
    \\item Unable to care for yourself
    \\item Experiencing psychosis
    \\item Substance abuse worsening
\\end{itemize}
""",

    "talking_to_your_doctor_gp_about_mental_health": """\\chapter{Talking to Your Doctor About Mental Health}

\\section{Overview}
Your primary care physician is often the first point of contact for mental health concerns. This chapter guides patients on preparing for and having productive conversations with their doctor.

\\section{Symptoms}
Common reasons to discuss with your doctor:
\\begin{itemize}
    \\item Persistent worry or fear
    \\item Changes in sleep patterns
    \\item Appetite changes
    \\item Difficulty concentrating
    \\item Physical symptoms without clear cause
\\end{itemize}

\\section{Causes}
Mental health conditions can be caused by various factors including genetics, brain chemistry, trauma, and life stressors.

\\section{Diagnosis}
Your doctor may:
\\begin{itemize}
    \\item Ask about symptoms and history
    \\item Conduct physical examination
    \\item Order blood tests
    \\item Use screening questionnaires
    \\item Refer to a specialist
\\end{itemize}

\\section{Treatment}
Treatment plans may include:
\\begin{itemize}
    \\item Medications
    \\item Therapy referrals
    \\item Lifestyle recommendations
    \\item Follow-up appointments
\\end{itemize}

\\section{Prevention}
Regular check-ups, stress management, and early intervention help prevent worsening.

\\section{When to Seek Medical Care}
Seek care for persistent symptoms lasting more than 2 weeks, suicidal thoughts, or functional impairment.
""",

    "talking_to_your_employer_about_illness": """\\chapter{Talking to Your Employer About Illness}

\\section{Overview}
Disclosing illness to an employer can be challenging. This chapter provides guidance on navigating workplace conversations while protecting your privacy and rights.

\\section{Symptoms}
Consider disclosing if your condition affects:
\\begin{itemize}
    \\item Work performance
    \\item Ability to commute
    \\item Need for accommodations
    \\item Attendance requirements
\\end{itemize}

\\section{Causes}
Illnesses may include chronic conditions, mental health issues, injuries, or temporary conditions.

\\section{Diagnosis}
Your employer does not need a diagnosis. Only relevant work limitations need disclosure.

\\section{Treatment}
Know your rights under:
\\begin{itemize}
    \\item ADA (Americans with Disabilities Act)
    \\item FMLA (Family and Medical Leave Act)
    \\item State and local laws
\\end{itemize}

\\section{Prevention}
\\begin{itemize}
    \\item Know your rights
    \\item Document communications
    \\item Focus on accommodations needed
    \\item Keep medical details private
\\end{itemize}

\\section{When to Seek Medical Care}
Seek legal advice if facing discrimination or denial of reasonable accommodations.
""",

    "teen_aggression": """\\chapter{Teen Aggression}

\\section{Overview}
Teen aggression refers to hostile or violent behavior in adolescents. It can be verbal, physical, or relational and may indicate underlying mental health issues.

\\section{Symptoms}
\\begin{itemize}
    \\item Frequent anger outbursts
    \\item Physical fights
    \\item Verbal abuse
    \\item Bullying behavior
    \\item Destruction of property
    \\item Defiance of authority
\\end{itemize}

\\section{Causes}
\\begin{itemize}
    \\item Mental health disorders (depression, anxiety, ADHD)
    \\item Trauma or abuse
    \\item Family conflict
    \\item Peer pressure
    \\item Substance use
    \\item Learning disabilities
\\end{itemize}

\\section{Diagnosis}
Assessment includes:
\\begin{itemize}
    \\item Psychological evaluation
    \\item Family history
    \\item School records
    \\item Substance use screening
\\end{itemize}

\\section{Treatment}
\\begin{itemize}
    \\item Cognitive behavioral therapy
    \\item Family therapy
    \\item Anger management programs
    \\item Medication (if co-occurring condition)
    \\item School interventions
\\end{itemize}

\\section{Prevention}
\\begin{itemize}
    \\item Strong family relationships
    \\item Positive role models
    \\item Early intervention
    \\item Teaching emotional regulation
\\end{itemize}

\\section{When to Seek Medical Care}
Seek help for:
\\begin{itemize}
    \\item Violence toward self or others
    \\item Legal problems
    \\item School suspension
    \\item Substance abuse
\\end{itemize}
""",

    "teenage_anxiety": """\\chapter{Teenage Anxiety}

\\section{Overview}
Teenage anxiety is a common mental health condition affecting adolescents. It involves excessive worry, fear, and nervousness that interferes with daily activities.

\\section{Symptoms}
\\begin{itemize}
    \\item Excessive worry about school, social situations
    \\item Restlessness or feeling keyed up
    \\item Difficulty concentrating
    \\item Sleep problems
    \\item Irritability
    \\item Physical symptoms (headaches, stomachaches)
    \\item Avoidance of situations
\\end{itemize}

\\section{Causes}
\\begin{itemize}
    \\item Genetic factors
    \\item Brain chemistry
    \\item Stressful life events
    \\item Academic pressure
    \\item Social challenges
    \\item Family history of anxiety
\\end{itemize}

\\section{Diagnosis}
\\begin{itemize}
    \\item Clinical interview
    \\item Screening questionnaires
    \\item Medical examination
    \\item Rule out physical causes
\\end{itemize}

\\section{Treatment}
\\begin{itemize}
    \\item Cognitive behavioral therapy (CBT)
    \\item SSRIs (if needed)
    \\item Lifestyle changes
    \\item School accommodations
    \\item Family therapy
\\end{itemize}

\\section{Prevention}
\\begin{itemize}
    \\item Open communication
    \\item Healthy routines
    \\item Stress management
    \\item Regular exercise
\\end{itemize}

\\section{When to Seek Medical Care}
Seek help for:
\\begin{itemize}
    \\item Anxiety interfering with school or relationships
    \\item Panic attacks
    \\item Depression symptoms
    \\item Self-harm thoughts
\\end{itemize}
""",
}

for filename, content in CHAPTERS.items():
    filepath = os.path.join(chapters_dir, filename)
    with open(filepath, 'w') as f:
        f.write(content)
    print(f"Written: {filename}")

print(f"Total: {len(CHAPTERS)}")
