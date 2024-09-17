from datasets import load_dataset

def get_topic_shots(test_topic):
    # Filter the dataset for the specific test topic
    dev_set = load_dataset("cais/mmlu", test_topic, split="dev")
    # Determine the number of shots based on the topic
    #shot_num = 1 if test_topic in ["high_school_european_history", "high_school_us_history", "high_school_world_history", "security_studies"] else 5
    shot_num = 5
    
    # Generate the shots string
    shots = ""
    for i in range(min(shot_num, len(dev_set))):  # Ensure not to exceed the number of examples in dev_set
        shots += f"Question:\n{dev_set[i]['question']}\Choices:\n"
        for j in range(4):
            shots += f"{j+1}) {dev_set[i]['choices'][j]}\n"
        shots += f"Answer:\n{dev_set[i]['answer']}\n\n"
    
    return shots

def get_prompt(doc):

    shots = get_topic_shots(doc["subject"])

    task = f"""Answer the given question about {doc["subject"].replace("_", " ")} by choosing one of the four proposed answers.
Do not repeat the chosen answer. Always answer only with the digit corresponding to the chosen answer without any further comment.
"""

    few_shot = f"""Here are some example questions:

{shots}
"""

    request = f"""Answer the following question:
Question:
{doc["question"]}
Choices:
1) {doc['choices'][0]}
2) {doc['choices'][1]}
3) {doc['choices'][2]}
4) {doc['choices'][3]}
Answer:
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

