from datasets import load_dataset

dev_mmlu = load_dataset("CIIRC-NLP/mmlu-cs", split="dev")

def get_topic_shots(test_topic):
    # Filter the dataset for the specific test topic
    dev_set = dev_mmlu.filter(lambda example: example['subject'] == test_topic)
    # Determine the number of shots based on the topic
    #shot_num = 1 if test_topic in ["high_school_european_history", "high_school_us_history", "high_school_world_history", "security_studies"] else 5
    shot_num = 5
    
    # Generate the shots string
    shots = ""
    for i in range(min(shot_num, len(dev_set))):  # Ensure not to exceed the number of examples in dev_set
        shots += f"Otázka:\n{dev_set[i]['question']}\nMožnosti:\n"
        for j in range(4):
            shots += f"{j+1}) {dev_set[i]['choices'][j]}\n"
        shots += f"Odpověď:\n{dev_set[i]['answer']}\n\n"
    
    return shots

def get_prompt(doc):

    shots = get_topic_shots(doc["subject"])

    task = f"""Odpověz na zadanou otázku na téma {topic_translations[doc["subject"]]} výběrem jedné ze čtyř navržených odpovědí.
Zvolenou odpověď neopakuj. Vždy odpovídej pouze číslem odpovídajícím vybrané odpovědi bez dalšího komentáře.
"""

    few_shot = f"""Zde je několik ukázkových příkladů:

{shots}
"""

    request = f"""Odpověz na následující otázku:
Otázka:
{doc["question"]}
Možnosti:
1) {doc['choices'][0]}
2) {doc['choices'][1]}
3) {doc['choices'][2]}
4) {doc['choices'][3]}
Odpověď:
"""
    return task + few_shot + request

topics = {
            "Humanities": [
                "formal_logic",
                "high_school_european_history",
                "high_school_us_history",
                "high_school_world_history",
                "international_law",
                "jurisprudence",
                "logical_fallacies",
                "moral_disputes",
                "moral_scenarios",
                "philosophy",
                "prehistory",
                "professional_law",
                "world_religions",
            ],
            "Social Sciences": [
                "econometrics",
                "high_school_geography",
                "high_school_government_and_politics",
                "high_school_macroeconomics",
                "high_school_microeconomics",
                "high_school_psychology",
                "human_sexuality",
                "professional_psychology",
                "public_relations",
                "security_studies",
                "sociology",
                "us_foreign_policy",
            ],
            "STEM": [
                "abstract_algebra",
                "anatomy",
                "astronomy",
                "college_biology",
                "college_chemistry",
                "college_computer_science",
                "college_mathematics",
                "college_physics",
                "computer_security",
                "conceptual_physics",
                "electrical_engineering",
                "elementary_mathematics",
                "high_school_biology",
                "high_school_chemistry",
                "high_school_computer_science",
                "high_school_mathematics",
                "high_school_physics",
                "high_school_statistics",
                "machine_learning",
            ],
            "Other": [
                "business_ethics",
                "clinical_knowledge",
                "college_medicine",
                "global_facts",
                "human_aging",
                "management",
                "marketing",
                "medical_genetics",
                "miscellaneous",
                "nutrition",
                "professional_accounting",
                "professional_medicine",
                "virology",
            ]
        }

topic_translations = {
    "formal_logic": "formální logika",
    "high_school_european_history": "středoškolské evropské dějiny",
    "high_school_us_history": "středoškolské americké dějiny",
    "high_school_world_history": "středoškolské světové dějiny",
    "international_law": "mezinárodní právo",
    "jurisprudence": "judikatura",
    "logical_fallacies": "logické chyby",
    "moral_disputes": "morální spory",
    "moral_scenarios": "morální scénáře",
    "philosophy": "filozofie",
    "prehistory": "pravěk",
    "professional_law": "profesionální právo",
    "world_religions": "světová náboženství",
    "econometrics": "ekonometrie",
    "high_school_geography": "středoškolská geografie",
    "high_school_government_and_politics": "středoškolská politologie",
    "high_school_macroeconomics": "středoškolská makroekonomie",
    "high_school_microeconomics": "středoškolská mikroekonomie",
    "high_school_psychology": "středoškolská psychologie",
    "human_sexuality": "lidská sexualita",
    "professional_psychology": "profesionální psychologie",
    "public_relations": "vztahy s veřejností",
    "security_studies": "studia bezpečnosti",
    "sociology": "sociologie",
    "us_foreign_policy": "zahraniční politika USA",
    "abstract_algebra": "abstraktní algebra",
    "anatomy": "anatomie",
    "astronomy": "astronomie",
    "college_biology": "vysokoškolská biologie",
    "college_chemistry": "vysokoškolská chemie",
    "college_computer_science": "vysokoškolská informatika",
    "college_mathematics": "vysokoškolská matematika",
    "college_physics": "vysokoškolská fyzika",
    "computer_security": "počítačová bezpečnost",
    "conceptual_physics": "konceptuální fyzika",
    "electrical_engineering": "elektrotechnika",
    "elementary_mathematics": "základní matematika",
    "high_school_biology": "středoškolská biologie",
    "high_school_chemistry": "středoškolská chemie",
    "high_school_computer_science": "středoškolská informatika",
    "high_school_mathematics": "středoškolská matematika",
    "high_school_physics": "středoškolská fyzika",
    "high_school_statistics": "středoškolská statistika",
    "machine_learning": "strojové učení",
    "business_ethics": "firemní etika",
    "clinical_knowledge": "klinické znalosti",
    "college_medicine": "vysokoškolská medicína",
    "global_facts": "globální fakta",
    "human_aging": "stárnutí lidí",
    "management": "management",
    "marketing": "marketing",
    "medical_genetics": "lékařská genetika",
    "miscellaneous": "různé",
    "nutrition": "výživa",
    "professional_accounting": "profesionální účetnictví",
    "professional_medicine": "profesionální medicína",
    "virology": "virologie",
}
