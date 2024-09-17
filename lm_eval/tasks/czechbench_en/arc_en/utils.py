def generate_choices_text(choices):
    return "\n".join(
        f"{choices['label'][i]}) {choices['text'][i]}"
        for i in range(len(choices['label']))
    )

def get_prompt(doc):
    task = """Answer the given question by choosing one of the proposed answers.
Do not repeat the chosen answer. Always answer only with the letter corresponding to the chosen answer without any further comment.
"""

    few_shot = """Here are 5 example questions:
Question:
George wants to warm his hands quickly by rubbing them. Which skin surface will produce the most heat?
Choices:
A) dry palms
B) wet palms
C) palms covered with oil
D) palms covered with lotion
Answer:
A

Question:
Which of the following statements best explains why magnets usually stick to a refrigerator door?
Choices:
A) The refrigerator door is smooth.
B) The refrigerator door contains iron.
C) The refrigerator door is a good conductor.
D) The refrigerator door has electric wires in it.
Answer:
B

Question:
A fold observed in layers of sedimentary rock most likely resulted from the
Choices:
A) cooling of flowing magma.
B) converging of crustal plates.
C) deposition of river sediments.
D) solution of carbonate minerals.
Answer:
B

Question:
As part of an experiment, an astronaut takes a scale to the Moon and weighs himself. The scale reads 31 pounds. If the astronaut has a mass of about 84 kilograms, which are the approximate weight and mass of the astronaut when standing on the Earth?
Choices:
A) 31 pounds and 14 kilograms
B) 31 pounds and 84 kilograms
C) 186 pounds and 14 kilograms
D) 186 pounds and 84 kilograms
Answer:
D

Question:
Which of the following areas is most likely to form metamorphic rocks such as gneiss and schist?
Choices:
A) a sea floor
B) a windblown desert
C) a site deep underground
D) a site covered by a glacier
Answer:
C
"""

    request = f"""Answer the following question:
Question:
{doc["question"]}
Choices:
{generate_choices_text(doc["choices"])}
Answer:
"""

    return task + few_shot + request

def doc_to_target(doc):
    answer_letter = doc["answerKey"]

    return answer_letter
