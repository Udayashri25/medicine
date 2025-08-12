# backend/medicine_data.py

# =========================
# General Medical
# =========================
general_medical_data = {
    "headache": ["paracetamol", "ibuprofen", "aspirin"],
    "fever": ["acetaminophen", "ibuprofen", "naproxen"],
    "cough": ["dextromethorphan", "guaifenesin", "benzonatate"],
    "sore throat": ["benzocaine lozenges", "chloraseptic spray", "ibuprofen"],
    "common cold": ["pseudoephedrine", "phenylephrine", "diphenhydramine"],
    "allergies": ["loratadine", "cetirizine", "fexofenadine"],
    "sinusitis": ["pseudoephedrine", "oxymetazoline", "amoxicillin"],
    "bronchitis": ["guaifenesin", "dextromethorphan", "azithromycin"],
    "indigestion": ["antacids", "famotidine", "omeprazole"],
    "nausea": ["ondansetron", "promethazine", "metoclopramide"],
    "diarrhea": ["loperamide", "bismuth subsalicylate", "diphenoxylate"],
    "constipation": ["psyllium", "docusate", "polyethylene glycol"],
    "urinary tract infection": ["nitrofurantoin", "trimethoprim-sulfamethoxazole", "ciprofloxacin"],
    "muscle pain": ["ibuprofen", "naproxen", "cyclobenzaprine"],
    "joint pain": ["acetaminophen", "ibuprofen", "naproxen"],
    "minor burns": ["aloe vera gel", "silver sulfadiazine", "bacitracin"],
    "cuts and scrapes": ["hydrogen peroxide", "neomycin", "bacitracin"],
    "eye irritation": ["artificial tears", "ketotifen", "naphazoline"],
    "motion sickness": ["dimenhydrinate", "meclizine", "scopolamine"],
    "athlete's foot": ["terbinafine", "clotrimazole", "miconazole"]
}

# =========================
# Mental Health
# =========================
mental_health_data = {
    "depression": ["fluoxetine", "sertraline", "bupropion"],
    "anxiety": ["alprazolam", "diazepam", "buspirone"],
    "insomnia": ["zolpidem", "eszopiclone", "melatonin"],
    "bipolar disorder": ["lithium", "valproic acid", "quetiapine"],
    "schizophrenia": ["risperidone", "olanzapine", "aripiprazole"],
    "ADHD": ["methylphenidate", "amphetamine/dextroamphetamine", "atomoxetine"],
    "obsessive-compulsive disorder": ["fluoxetine", "sertraline", "clomipramine"],
    "post-traumatic stress disorder": ["sertraline", "paroxetine", "venlafaxine"],
    "generalized anxiety disorder": ["escitalopram", "venlafaxine", "duloxetine"],
    "social anxiety disorder": ["paroxetine", "sertraline", "venlafaxine"],
    "panic disorder": ["sertraline", "paroxetine", "alprazolam"],
    "eating disorders": ["fluoxetine", "olanzapine", "topiramate"],
    "borderline personality disorder": ["fluoxetine", "sertraline", "lamotrigine"],
    "seasonal affective disorder": ["bupropion", "fluoxetine", "light therapy"],
    "premenstrual dysphoric disorder": ["fluoxetine", "sertraline", "oral contraceptives"],
    "trichotillomania": ["n-acetylcysteine", "olanzapine", "clomipramine"],
    "body dysmorphic disorder": ["fluoxetine", "clomipramine", "fluvoxamine"],
    "gambling addiction": ["naltrexone", "nalmefene", "topiramate"],
    "kleptomania": ["fluoxetine", "naltrexone", "escitalopram"],
    "intermittent explosive disorder": ["fluoxetine", "risperidone", "carbamazepine"]
}

# =========================
# Pediatric
# =========================
pediatric_data = {
    "ear infection": ["amoxicillin", "cefdinir", "azithromycin"],
    "diaper rash": ["zinc oxide cream", "petroleum jelly", "hydrocortisone cream"],
    "colic": ["simethicone", "gripe water", "probiotics"],
    "teething": ["acetaminophen", "ibuprofen", "benzocaine gel"],
    "childhood asthma": ["albuterol", "fluticasone", "montelukast"],
    "childhood allergies": ["cetirizine", "loratadine", "fexofenadine"],
    "childhood eczema": ["hydrocortisone cream", "tacrolimus ointment", "pimecrolimus cream"],
    "chickenpox": ["calamine lotion", "diphenhydramine", "acyclovir"],
    "hand, foot, and mouth disease": ["acetaminophen", "ibuprofen", "lidocaine gel"],
    "strep throat": ["amoxicillin", "penicillin", "cephalexin"],
    "pediatric constipation": ["polyethylene glycol", "lactulose", "mineral oil"],
    "childhood obesity": ["lifestyle changes", "metformin", "orlistat"],
    "attention deficit hyperactivity disorder": ["methylphenidate", "amphetamine/dextroamphetamine", "atomoxetine"],
    "juvenile idiopathic arthritis": ["naproxen", "ibuprofen", "methotrexate"],
    "pediatric migraine": ["ibuprofen", "acetaminophen", "sumatriptan"],
    "childhood diabetes": ["insulin", "metformin", "glucagon"],
    "growth hormone deficiency": ["somatropin", "growth hormone injections"],
    "pediatric acne": ["benzoyl peroxide", "tretinoin", "clindamycin"],
    "childhood pneumonia": ["amoxicillin", "azithromycin", "ceftriaxone"],
    "pediatric urinary tract infection": ["trimethoprim-sulfamethoxazole", "nitrofurantoin", "cephalexin"]
}

# =========================
# Geriatric
# =========================
geriatric_data = {
    "osteoporosis": ["alendronate", "risedronate", "teriparatide"],
    "arthritis": ["celecoxib", "naproxen", "meloxicam"],
    "memory loss": ["donepezil", "memantine", "rivastigmine"],
    "hypertension in elderly": ["lisinopril", "amlodipine", "hydrochlorothiazide"],
    "urinary incontinence": ["oxybutynin", "tolterodine", "mirabegron"],
    "age-related macular degeneration": ["ranibizumab", "aflibercept", "bevacizumab"],
    "parkinson's disease": ["levodopa", "carbidopa", "pramipexole"],
    "osteoarthritis": ["acetaminophen", "diclofenac gel", "duloxetine"],
    "benign prostatic hyperplasia": ["tamsulosin", "finasteride", "dutasteride"],
    "glaucoma": ["latanoprost", "timolol", "brimonidine"],
    "elderly depression": ["sertraline", "escitalopram", "mirtazapine"],
    "elderly insomnia": ["temazepam", "zolpidem", "ramelteon"],
    "peripheral artery disease": ["cilostazol", "pentoxifylline", "clopidogrel"],
    "diabetic neuropathy": ["pregabalin", "gabapentin", "duloxetine"],
    "falls prevention": ["vitamin D", "calcium supplements", "balance exercises"],
    "chronic obstructive pulmonary disease": ["tiotropium", "fluticasone/salmeterol", "albuterol"],
    "atrial fibrillation in elderly": ["apixaban", "warfarin", "dabigatran"],
    "elderly malnutrition": ["nutritional supplements", "vitamin B12", "folic acid"],
    "shingles": ["acyclovir", "valacyclovir", "famciclovir"],
    "elder abuse prevention": ["social services intervention", "counseling", "legal assistance"]
}

# =========================
# Dermatological
# =========================
dermatological_data = {
    "acne": ["benzoyl peroxide", "tretinoin", "isotretinoin"],
    "eczema": ["hydrocortisone cream", "tacrolimus ointment", "pimecrolimus cream"],
    "psoriasis": ["topical corticosteroids", "calcipotriene", "methotrexate"],
    "rosacea": ["metronidazole", "azelaic acid", "doxycycline"],
    "atopic dermatitis": ["emollients", "tacrolimus", "dupilumab"],
    "contact dermatitis": ["topical corticosteroids", "oral antihistamines", "topical calcineurin inhibitors"],
    "fungal infections": ["terbinafine", "fluconazole", "itraconazole"],
    "warts": ["salicylic acid", "cryotherapy", "imiquimod"],
    "melasma": ["hydroquinone", "tretinoin", "kojic acid"],
    "seborrheic dermatitis": ["ketoconazole shampoo", "zinc pyrithione", "selenium sulfide"],
    "hives": ["cetirizine", "fexofenadine", "diphenhydramine"],
    "skin cancer": ["surgery", "radiation therapy", "chemotherapy"],
    "vitiligo": ["topical corticosteroids", "tacrolimus", "phototherapy"],
    "alopecia areata": ["topical minoxidil", "intralesional corticosteroids", "topical immunotherapy"],
    "cellulitis": ["cephalexin", "dicloxacillin", "clindamycin"],
    "impetigo": ["mupirocin", "retapamulin", "oral antibiotics"],
    "hidradenitis suppurativa": ["clindamycin", "rifampin", "adalimumab"],
    "keloids": ["intralesional corticosteroids", "silicone sheets", "cryotherapy"],
    "perioral dermatitis": ["metronidazole", "erythromycin", "pimecrolimus"],
    "scabies": ["permethrin cream", "ivermectin", "lindane"]
}

# =========================
# Cardiovascular
# =========================
cardiovascular_data = {
    "hypertension": ["lisinopril", "amlodipine", "hydrochlorothiazide"],
    "hyperlipidemia": ["atorvastatin", "simvastatin", "ezetimibe"],
    "coronary artery disease": ["aspirin", "clopidogrel", "metoprolol"],
    "heart failure": ["lisinopril", "carvedilol", "furosemide"],
    "atrial fibrillation": ["warfarin", "apixaban", "amiodarone"],
    "myocardial infarction": ["aspirin", "ticagrelor", "metoprolol"],
    "deep vein thrombosis": ["enoxaparin", "rivaroxaban", "warfarin"],
    "peripheral artery disease": ["cilostazol", "clopidogrel", "pentoxifylline"],
    "aortic aneurysm": ["metoprolol", "enalapril", "atorvastatin"],
    "pulmonary hypertension": ["sildenafil", "bosentan", "epoprostenol"],
    "cardiac arrhythmias": ["amiodarone", "sotalol", "flecainide"],
    "cardiomyopathy": ["enalapril", "metoprolol", "spironolactone"],
    "pericarditis": ["ibuprofen", "colchicine", "prednisone"],
    "valvular heart disease": ["warfarin", "enalapril", "furosemide"],
    "endocarditis": ["vancomycin", "gentamicin", "ceftriaxone"],
    "hypertrophic cardiomyopathy": ["metoprolol", "verapamil", "disopyramide"],
    "Wolff-Parkinson-White syndrome": ["adenosine", "flecainide", "propafenone"],
    "Brugada syndrome": ["quinidine", "isoproterenol", "cilostazol"],
    "long QT syndrome": ["propranolol", "mexiletine", "potassium supplements"],
    "Marfan syndrome": ["atenolol", "losartan", "enalapril"]
}

# =========================
# Gastrointestinal
# =========================
gastrointestinal_data = {
    "acid reflux": ["omeprazole", "ranitidine", "esomeprazole"],
    "constipation": ["psyllium", "docusate", "polyethylene glycol"],
    "diarrhea": ["loperamide", "bismuth subsalicylate", "diphenoxylate/atropine"],
    "irritable bowel syndrome": ["dicyclomine", "linaclotide", "alosetron"],
    "inflammatory bowel disease": ["mesalamine", "prednisone", "infliximab"],
    "peptic ulcer disease": ["omeprazole", "amoxicillin", "clarithromycin"],
    "gastroenteritis": ["oral rehydration solutions", "loperamide", "ondansetron"],
    "Crohn's disease": ["adalimumab", "azathioprine", "budesonide"],
    "ulcerative colitis": ["mesalamine", "infliximab", "prednisone"],
    "celiac disease": ["gluten-free diet", "nutritional supplements"],
    "diverticulitis": ["ciprofloxacin", "metronidazole", "mesalamine"],
    "gastroesophageal reflux disease": ["esomeprazole", "famotidine", "pantoprazole"],
    "hemorrhoids": ["hydrocortisone cream", "witch hazel pads", "docusate"],
    "hepatitis": ["entecavir", "tenofovir", "interferon alfa"],
    "pancreatitis": ["pancreatic enzyme supplements", "pain management"],
    "gallstones": ["ursodeoxycholic acid", "pain management"],
    "gastroparesis": ["metoclopramide", "domperidone", "erythromycin"],
    "Helicobacter pylori infection": ["amoxicillin", "clarithromycin", "metronidazole"],
    "lactose intolerance": ["lactase enzyme supplements", "calcium supplements"],
    "small intestinal bacterial overgrowth": ["rifaximin", "metronidazole", "probiotics"]
}

# =========================
# Neurological
# =========================
neurological_data = {
    "migraine": ["sumatriptan", "rizatriptan", "topiramate"],
    "epilepsy": ["levetiracetam", "carbamazepine", "valproic acid"],
    "Parkinson's disease": ["levodopa/carbidopa", "pramipexole", "ropinirole"],
    "multiple sclerosis": ["interferon beta-1a", "glatiramer acetate", "fingolimod"],
    "Alzheimer's disease": ["donepezil", "memantine", "rivastigmine"],
    "stroke": ["alteplase", "aspirin", "clopidogrel"],
    "neuropathic pain": ["gabapentin", "pregabalin", "duloxetine"],
    "essential tremor": ["propranolol", "primidone", "topiramate"],
    "amyotrophic lateral sclerosis": ["riluzole", "edaravone", "dextromethorphan/quinidine"],
    "myasthenia gravis": ["pyridostigmine", "prednisone", "azathioprine"],
    "restless legs syndrome": ["ropinirole", "pramipexole", "gabapentin enacarbil"],
    "trigeminal neuralgia": ["carbamazepine", "oxcarbazepine", "baclofen"],
    "Bell's palsy": ["prednisone", "valacyclovir", "eye lubricants"],
    "Huntington's disease": ["tetrabenazine", "deutetrabenazine", "haloperidol"],
    "narcolepsy": ["modafinil", "sodium oxybate", "methylphenidate"],
    "cluster headache": ["sumatriptan", "verapamil", "lithium"],
    "Guillain-Barré syndrome": ["intravenous immunoglobulin", "plasmapheresis"],
    "dystonia": ["botulinum toxin injections", "trihexyphenidyl", "baclofen"],
    "chronic fatigue syndrome": ["cognitive behavioral therapy", "graded exercise therapy"],
    "peripheral neuropathy": ["gabapentin", "amitriptyline", "duloxetine"]
}

# =========================
# Respiratory
# =========================
respiratory_data = {
    "asthma": ["albuterol", "fluticasone", "montelukast"],
    "chronic obstructive pulmonary disease": ["tiotropium", "fluticasone/salmeterol", "roflumilast"],
    "pneumonia": ["amoxicillin", "azithromycin", "levofloxacin"],
    "bronchitis": ["dextromethorphan", "guaifenesin", "codeine"],
    "sinusitis": ["amoxicillin/clavulanate", "fluticasone nasal spray", "pseudoephedrine"],
    "allergic rhinitis": ["cetirizine", "fluticasone nasal spray", "montelukast"],
    "cystic fibrosis": ["tobramycin", "dornase alfa", "ivacaftor"],
    "pulmonary embolism": ["heparin", "warfarin", "rivaroxaban"],
    "tuberculosis": ["isoniazid", "rifampin", "ethambutol"],
    "lung cancer": ["pembrolizumab", "erlotinib", "pemetrexed"],
    "sleep apnea": ["CPAP therapy", "modafinil", "dental appliances"],
    "pulmonary hypertension": ["sildenafil", "bosentan", "epoprostenol"],
    "interstitial lung disease": ["pirfenidone", "nintedanib", "prednisone"],
    "pleural effusion": ["thoracentesis", "pleurodesis", "diuretics"],
    "bronchiectasis": ["azithromycin", "inhaled tobramycin", "airway clearance techniques"],
    "sarcoidosis": ["prednisone", "methotrexate", "hydroxychloroquine"],
    "acute respiratory distress syndrome": ["mechanical ventilation", "prone positioning", "corticosteroids"],
    "pulmonary fibrosis": ["pirfenidone", "nintedanib", "oxygen therapy"],
    "vocal cord dysfunction": ["speech therapy", "breathing exercises", "inhaled ipratropium"],
    "occupational lung diseases": ["corticosteroids", "bronchodilators", "oxygen therapy"]
}

# =========================
# Combined datasets
# =========================
datasets = {
    "General Medical": general_medical_data,
    "Mental Health": mental_health_data,
    "Pediatric": pediatric_data,
    "Geriatric": geriatric_data,
    "Dermatological": dermatological_data,
    "Cardiovascular": cardiovascular_data,
    "Gastrointestinal": gastrointestinal_data,
    "Neurological": neurological_data,
    "Respiratory": respiratory_data,
}

# Default dataset
medical_data = general_medical_data
